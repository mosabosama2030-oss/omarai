# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **068**
- سجلات الأسطر: **800**
- النطاق: SRC-DE7EABE998-L000098 إلى SRC-2C8F288796-L000294
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-DE7EABE998 — [web/agent.html](../../web/agent.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DE7EABE998-L000098](../../web/agent.html#L98) | 98 | `"</div>"` | — |
| [SRC-DE7EABE998-L000099](../../web/agent.html#L99) | 99 | `""` | — |
| [SRC-DE7EABE998-L000100](../../web/agent.html#L100) | 100 | `"<script>"` | — |
| [SRC-DE7EABE998-L000101](../../web/agent.html#L101) | 101 | `"const $=id=>document.getElementById(id);"` | — |
| [SRC-DE7EABE998-L000102](../../web/agent.html#L102) | 102 | `"function apiHeaders(){return {\"Content-Type\":\"application/json\"};}"` | — |
| [SRC-DE7EABE998-L000103](../../web/agent.html#L103) | 103 | `"const history=[];"` | — |
| [SRC-DE7EABE998-L000104](../../web/agent.html#L104) | 104 | `"let busy=false;"` | — |
| [SRC-DE7EABE998-L000105](../../web/agent.html#L105) | 105 | `"let activeMode=\"deep\";"` | — |
| [SRC-DE7EABE998-L000106](../../web/agent.html#L106) | 106 | `"const modeLabels={auto:\"تلقائي\",deep:\"بحث معمّق\",latest:\"الأحدث الآن\",social:\"آراء الناس\"};"` | — |
| [SRC-DE7EABE998-L000107](../../web/agent.html#L107) | 107 | `"function escapeHtml(s){return String(s??\"\").replace(/[&<>\"']/g,c=>({\"&\":\"&amp;\",\"<\":\"&lt;\",\">\":\"&gt;\",'\"':\"&quot;\",\"'\":\"&#39;\"}[c]));}"` | — |
| [SRC-DE7EABE998-L000108](../../web/agent.html#L108) | 108 | `"function answerMarkup(text){"` | — |
| [SRC-DE7EABE998-L000109](../../web/agent.html#L109) | 109 | `"  const escaped=escapeHtml(text);"` | — |
| [SRC-DE7EABE998-L000110](../../web/agent.html#L110) | 110 | `"  return escaped"` | — |
| [SRC-DE7EABE998-L000111](../../web/agent.html#L111) | 111 | `"   .replace(/^###\\s+(.+)$/gm,\"<h3>$1</h3>\")"` | — |
| [SRC-DE7EABE998-L000112](../../web/agent.html#L112) | 112 | `"   .replace(/^##\\s+(.+)$/gm,\"<h3>$1</h3>\")"` | — |
| [SRC-DE7EABE998-L000113](../../web/agent.html#L113) | 113 | `"   .replace(/^#\\s+(.+)$/gm,\"<h3>$1</h3>\")"` | — |
| [SRC-DE7EABE998-L000114](../../web/agent.html#L114) | 114 | `"   .replace(/^\\s*[-*]\\s+(.+)$/gm,\"• $1\")"` | — |
| [SRC-DE7EABE998-L000115](../../web/agent.html#L115) | 115 | `"   .replace(/\\*\\*(.+?)\\*\\*/g,\"<strong>$1</strong>\")"` | — |
| [SRC-DE7EABE998-L000116](../../web/agent.html#L116) | 116 | ``"   .replace(/`([^`]+)`/g,\"<code>$1</code>\")"`` | — |
| [SRC-DE7EABE998-L000117](../../web/agent.html#L117) | 117 | `"   .replace(/\\n/g,\"<br>\");"` | — |
| [SRC-DE7EABE998-L000118](../../web/agent.html#L118) | 118 | `"}"` | — |
| [SRC-DE7EABE998-L000119](../../web/agent.html#L119) | 119 | `"function setStatus(text,kind){$(\"status\").innerHTML='<span class=\"dot '+(kind\|\|\"\")+'\"></span><span>'+escapeHtml(text)+'</span>';}"` | — |
| [SRC-DE7EABE998-L000120](../../web/agent.html#L120) | 120 | `"function modeName(mode){return modeLabels[mode]\|\|modeLabels.auto;}"` | — |
| [SRC-DE7EABE998-L000121](../../web/agent.html#L121) | 121 | `"function safeSourceUrl(value){"` | — |
| [SRC-DE7EABE998-L000122](../../web/agent.html#L122) | 122 | `" try{"` | — |
| [SRC-DE7EABE998-L000123](../../web/agent.html#L123) | 123 | `"  const parsed=new URL(String(value??\"\"));"` | — |
| [SRC-DE7EABE998-L000124](../../web/agent.html#L124) | 124 | `"  if(![\"https:\",\"http:\"].includes(parsed.protocol)\|\|!parsed.hostname\|\|parsed.username\|\|parsed.password)return null;"` | — |
| [SRC-DE7EABE998-L000125](../../web/agent.html#L125) | 125 | `"  return parsed.href;"` | — |
| [SRC-DE7EABE998-L000126](../../web/agent.html#L126) | 126 | `" }catch(_error){return null;}"` | — |
| [SRC-DE7EABE998-L000127](../../web/agent.html#L127) | 127 | `"}"` | — |
| [SRC-DE7EABE998-L000128](../../web/agent.html#L128) | 128 | `"function renderSource(s,index){"` | — |
| [SRC-DE7EABE998-L000129](../../web/agent.html#L129) | 129 | `" if(!s\|\|typeof s!==\"object\")return \"\";"` | — |
| [SRC-DE7EABE998-L000130](../../web/agent.html#L130) | 130 | `" const url=safeSourceUrl(s.url);"` | — |
| [SRC-DE7EABE998-L000131](../../web/agent.html#L131) | 131 | `" const title=escapeHtml(s.title\|\|(\"نتيجة ويب \"+(index+1)));"` | — |
| [SRC-DE7EABE998-L000132](../../web/agent.html#L132) | 132 | `" const tags=[];"` | — |
| [SRC-DE7EABE998-L000133](../../web/agent.html#L133) | 133 | `" tags.push('<span class=\"tag\">'+escapeHtml(s.source_class\|\|\"مصدر عام\")+'</span>');"` | — |
| [SRC-DE7EABE998-L000134](../../web/agent.html#L134) | 134 | `" const fetchStatus=s.page_fetch_status\|\|(s.page_fetched?\"content_extracted\":\"not_attempted\");"` | — |
| [SRC-DE7EABE998-L000135](../../web/agent.html#L135) | 135 | `" if(fetchStatus===\"partial_extraction\")tags.push('<span class=\"tag read\">اُستخرج جزء من النص فقط</span>');"` | — |
| [SRC-DE7EABE998-L000136](../../web/agent.html#L136) | 136 | `" else if(fetchStatus===\"content_extracted\"\|\|s.page_fetched)tags.push('<span class=\"tag read\">قُرئت الصفحة واستُخرج نص</span>');"` | — |
| [SRC-DE7EABE998-L000137](../../web/agent.html#L137) | 137 | `" else if(fetchStatus===\"no_text_extracted\"\|\|fetchStatus===\"empty_content\")tags.push('<span class=\"tag\">لم يُستخرج نص؛ قد تكون الصفحة ديناميكية أو محجوبة</span>');"` | — |
| [SRC-DE7EABE998-L000138](../../web/agent.html#L138) | 138 | `" else if(fetchStatus===\"blocked_or_unresolved_host\"\|\|fetchStatus===\"blocked_connection_target\")tags.push('<span class=\"tag\">حُظر العنوان أو تعذّر التحقق الآمن منه</span>');"` | — |
| [SRC-DE7EABE998-L000139](../../web/agent.html#L139) | 139 | `" else if([\"redirect_failed\",\"redirect_rejected\",\"redirect_limit\"].includes(fetchStatus))tags.push('<span class=\"tag\">تعذّر اتباع تحويل الرابط بأمان</span>');"` | — |
| [SRC-DE7EABE998-L000140](../../web/agent.html#L140) | 140 | `" else if(fetchStatus===\"http_error\")tags.push('<span class=\"tag\">الموقع أعاد خطأ HTTP</span>');"` | — |
| [SRC-DE7EABE998-L000141](../../web/agent.html#L141) | 141 | `" else if(fetchStatus===\"unsupported_content_type\")tags.push('<span class=\"tag\">نوع محتوى الصفحة غير مدعوم</span>');"` | — |
| [SRC-DE7EABE998-L000142](../../web/agent.html#L142) | 142 | `" else if(fetchStatus===\"page_too_large\")tags.push('<span class=\"tag\">الصفحة تجاوزت حد الحجم الآمن</span>');"` | — |
| [SRC-DE7EABE998-L000143](../../web/agent.html#L143) | 143 | `" else if(fetchStatus===\"network_error\")tags.push('<span class=\"tag\">تعذّر الاتصال بالصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000144](../../web/agent.html#L144) | 144 | `" else if(fetchStatus===\"budget_exhausted\")tags.push('<span class=\"tag\">توقفت القراءة بسبب حدود الموارد</span>');"` | — |
| [SRC-DE7EABE998-L000145](../../web/agent.html#L145) | 145 | `" else if(fetchStatus===\"rejected_url\")tags.push('<span class=\"tag\">رُفض الرابط لأسباب أمان</span>');"` | — |
| [SRC-DE7EABE998-L000146](../../web/agent.html#L146) | 146 | `" else if(fetchStatus===\"fetch_failed\")tags.push('<span class=\"tag\">تعذّر جلب الصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000147](../../web/agent.html#L147) | 147 | `" else if(fetchStatus===\"attempted\")tags.push('<span class=\"tag\">محاولة جلب الصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000148](../../web/agent.html#L148) | 148 | `" else tags.push('<span class=\"tag\">مقتطف بحث — لم تُحاول قراءة الصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000149](../../web/agent.html#L149) | 149 | `" if(s.platform&&s.platform!==\"web\")tags.push('<span class=\"tag social\">'+escapeHtml(s.platform)+'</span>');"` | — |
| [SRC-DE7EABE998-L000150](../../web/agent.html#L150) | 150 | `" if(s.published_at)tags.push('<span class=\"tag\">تاريخ ظاهر: '+escapeHtml(s.published_at)+'</span>');"` | — |
| [SRC-DE7EABE998-L000151](../../web/agent.html#L151) | 151 | `" const providers=Array.isArray(s.providers)?s.providers.map(escapeHtml):[];"` | — |
| [SRC-DE7EABE998-L000152](../../web/agent.html#L152) | 152 | `" if(s.publisher_name)tags.push('<span class=\"tag\">الناشر: '+escapeHtml(s.publisher_name)+'</span>');"` | — |
| [SRC-DE7EABE998-L000153](../../web/agent.html#L153) | 153 | `" if(s.publisher_url&&safeSourceUrl(s.publisher_url))tags.push('<a class=\"tag\" href=\"'+escapeHtml(s.publisher_url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">صفحة الناشر ↗</a>');"` | — |
| [SRC-DE7EABE998-L000154](../../web/agent.html#L154) | 154 | `" if(providers.length)tags.push('<span class=\"tag\">'+providers.join(\" · \")+'</span>');"` | — |
| [SRC-DE7EABE998-L000155](../../web/agent.html#L155) | 155 | `" if(s.lead_qualification===\"related_result_not_lead\")tags.push('<span class=\"tag social\">نتيجة مرتبطة وليست عميلًا محتملًا</span>');"` | — |
| [SRC-DE7EABE998-L000156](../../web/agent.html#L156) | 156 | `" if(s.lead_qualification===\"public_demand_signal\"\|\|s.lead_qualification===\"public_buyer_intent_signal\"){"` | — |
| [SRC-DE7EABE998-L000157](../../web/agent.html#L157) | 157 | `"  const demandType=s.lead_intent_evidence&&s.lead_intent_evidence.signal_type;"` | — |
| [SRC-DE7EABE998-L000158](../../web/agent.html#L158) | 158 | `"  const demandLabels={direct_purchase_request:\"طلب شراء مباشر\",request_for_quotation:\"طلب عرض سعر\",tender_or_procurement:\"مناقصة أو توريد\",stated_need:\"احتياج معلن\",indirect_indicator:\"مؤشر احتياج غير مباشر\"};"` | — |
| [SRC-DE7EABE998-L000159](../../web/agent.html#L159) | 159 | `"  const demandLabel=demandLabels[demandType]\|\|\"إشارة طلب غير مكتملة التصنيف\";"` | — |
| [SRC-DE7EABE998-L000160](../../web/agent.html#L160) | 160 | `"  tags.push('<span class=\"tag read\">'+escapeHtml(demandLabel)+' — ملاءمة المنتج والهوية تحتاج إلى تحقق</span>');"` | — |
| [SRC-DE7EABE998-L000161](../../web/agent.html#L161) | 161 | `" }"` | — |
| [SRC-DE7EABE998-L000162](../../web/agent.html#L162) | 162 | `" const heading=url?'<a href=\"'+escapeHtml(url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">['+(index+1)+'] '+title+' ↗</a>':'<strong>['+(index+1)+'] '+title+'</strong><p class=\"warning\">لم يُعرض الرابط لأنه غير صالح.</p>';"` | — |
| [SRC-DE7EABE998-L000163](../../web/agent.html#L163) | 163 | `" return '<article class=\"source\">'+heading+'<p>'+escapeHtml(s.snippet\|\|\"لا يتوفر مقتطف نصي من هذه النتيجة.\")+'</p><div class=\"source-meta\">'+tags.join(\"\")+'</div></article>';"` | — |
| [SRC-DE7EABE998-L000164](../../web/agent.html#L164) | 164 | `"}"` | — |
| [SRC-DE7EABE998-L000165](../../web/agent.html#L165) | 165 | `"function renderReport(result){"` | — |
| [SRC-DE7EABE998-L000166](../../web/agent.html#L166) | 166 | `" const r=result&&result.search_report&&typeof result.search_report===\"object\"?result.search_report:{};"` | — |
| [SRC-DE7EABE998-L000167](../../web/agent.html#L167) | 167 | `" const completion=r.research_completion&&typeof r.research_completion===\"object\"?r.research_completion:"` | — |
| [SRC-DE7EABE998-L000168](../../web/agent.html#L168) | 168 | `"  (result&&result.research_completion&&typeof result.research_completion===\"object\"?result.research_completion:null);"` | — |
| [SRC-DE7EABE998-L000169](../../web/agent.html#L169) | 169 | `" const completionStatusLabels={"` | — |
| [SRC-DE7EABE998-L000170](../../web/agent.html#L170) | 170 | `"  execution_stopped_budget:\"توقفت العملية عند حد الميزانية\","` | — |
| [SRC-DE7EABE998-L000171](../../web/agent.html#L171) | 171 | `"  no_eligible_sources_after_filtering:\"لم يبقَ مصدر مقبول بعد التصفية\","` | — |
| [SRC-DE7EABE998-L000172](../../web/agent.html#L172) | 172 | `"  search_failed_or_incomplete:\"البحث فشل أو لم يكتمل\","` | — |
| [SRC-DE7EABE998-L000173](../../web/agent.html#L173) | 173 | `"  no_results_returned:\"اكتمل البحث دون نتائج\","` | — |
| [SRC-DE7EABE998-L000174](../../web/agent.html#L174) | 174 | `"  search_not_attempted:\"لم تُنفذ محاولة البحث\","` | — |
| [SRC-DE7EABE998-L000175](../../web/agent.html#L175) | 175 | `"  insufficient_evidence:\"الأدلة غير كافية\","` | — |
| [SRC-DE7EABE998-L000176](../../web/agent.html#L176) | 176 | `"  source_snippets_only_generation_not_completed:\"مقتطفات فقط؛ لم تكتمل صياغة الإجابة\","` | — |
| [SRC-DE7EABE998-L000177](../../web/agent.html#L177) | 177 | `"  evidence_collected_generation_not_completed:\"جُمعت أدلة؛ لم تكتمل صياغة الإجابة\","` | — |
| [SRC-DE7EABE998-L000178](../../web/agent.html#L178) | 178 | `"  answer_generation_or_review_failed:\"تعذر توليد الإجابة أو مراجعتها\","` | — |
| [SRC-DE7EABE998-L000179](../../web/agent.html#L179) | 179 | `"  partial_answer_evidence_gaps_detected:\"إجابة جزئية مع فجوات أدلة محتملة\","` | — |
| [SRC-DE7EABE998-L000180](../../web/agent.html#L180) | 180 | `"  answer_generated_citations_range_checked_semantic_support_unverified:\"وُلّدت الإجابة وفُحصت أرقام الإحالات فقط؛ دعم الادعاءات دلاليًا غير متحقق\","` | — |
| [SRC-DE7EABE998-L000181](../../web/agent.html#L181) | 181 | `"  answer_generated_without_valid_citation_markers:\"وُلّدت الإجابة دون علامات إحالة صالحة\""` | — |
| [SRC-DE7EABE998-L000182](../../web/agent.html#L182) | 182 | `" };"` | — |
| [SRC-DE7EABE998-L000183](../../web/agent.html#L183) | 183 | `" const completionPhaseLabels={"` | — |
| [SRC-DE7EABE998-L000184](../../web/agent.html#L184) | 184 | `"  planning:\"التخطيط\",search:\"البحث\",source_filtering:\"تصفية المصادر\","` | — |
| [SRC-DE7EABE998-L000185](../../web/agent.html#L185) | 185 | `"  page_reading:\"قراءة الصفحات\",answer_generation:\"توليد الإجابة\","` | — |
| [SRC-DE7EABE998-L000186](../../web/agent.html#L186) | 186 | `"  citation_validation:\"فحص الإحالات\",semantic_verification:\"التحقق الدلالي\""` | — |
| [SRC-DE7EABE998-L000187](../../web/agent.html#L187) | 187 | `" };"` | — |
| [SRC-DE7EABE998-L000188](../../web/agent.html#L188) | 188 | `" const completionStateLabels={"` | — |
| [SRC-DE7EABE998-L000189](../../web/agent.html#L189) | 189 | `"  completed:\"مكتمل\",unknown:\"غير معلوم\",not_attempted:\"لم يبدأ\","` | — |
| [SRC-DE7EABE998-L000190](../../web/agent.html#L190) | 190 | `"  failed_or_incomplete:\"فشل أو لم يكتمل\",results_received:\"استُلمت نتائج\","` | — |
| [SRC-DE7EABE998-L000191](../../web/agent.html#L191) | 191 | `"  completed_no_results:\"اكتمل دون نتائج\",attempted_no_usable_sources:\"محاولة دون مصادر صالحة\","` | — |
| [SRC-DE7EABE998-L000192](../../web/agent.html#L192) | 192 | `"  not_applicable_no_eligible_sources:\"لا توجد مصادر نهائية\",all_final_sources_read:\"قُرئت كل الصفحات النهائية\","` | — |
| [SRC-DE7EABE998-L000193](../../web/agent.html#L193) | 193 | `"  some_final_sources_read:\"قُرئ بعض الصفحات\",no_final_source_page_read:\"لم تُقرأ صفحات نهائية\","` | — |
| [SRC-DE7EABE998-L000194](../../web/agent.html#L194) | 194 | `"  not_attempted_or_withheld:\"لم تُولد الإجابة أو حُجبت\",answer_generated:\"وُلّدت الإجابة\","` | — |
| [SRC-DE7EABE998-L000195](../../web/agent.html#L195) | 195 | `"  not_completed:\"لم يكتمل\",failed_or_unavailable:\"فشل أو غير متاح\","` | — |
| [SRC-DE7EABE998-L000196](../../web/agent.html#L196) | 196 | `"  not_run:\"لم يُنفذ\",not_performed:\"لم يُنفذ\",sources_retained:\"احتُفظ بمصادر\","` | — |
| [SRC-DE7EABE998-L000197](../../web/agent.html#L197) | 197 | `"  rejected_all_candidates:\"رُفضت كل المرشحات\",no_eligible_sources:\"لا توجد مصادر مقبولة\","` | — |
| [SRC-DE7EABE998-L000198](../../web/agent.html#L198) | 198 | `"  index_range_check_passed:\"فُحص نطاق أرقام الإحالات فقط\","` | — |
| [SRC-DE7EABE998-L000199](../../web/agent.html#L199) | 199 | `"  invalid_index_references_removed:\"حُذفت إحالات خارج النطاق\","` | — |
| [SRC-DE7EABE998-L000200](../../web/agent.html#L200) | 200 | `"  no_citation_markers_present:\"لا توجد علامات إحالة\",diagnostics_not_computed:\"تعذر احتساب التشخيص\""` | — |
| [SRC-DE7EABE998-L000201](../../web/agent.html#L201) | 201 | `" };"` | — |
| [SRC-DE7EABE998-L000202](../../web/agent.html#L202) | 202 | `" const completionSummary=completion&&completion.status"` | — |
| [SRC-DE7EABE998-L000203](../../web/agent.html#L203) | 203 | `"  ?'<p class=\"'+([\"search_failed_or_incomplete\",\"execution_stopped_budget\",\"answer_generation_or_review_failed\",\"no_eligible_sources_after_filtering\",\"partial_answer_evidence_gaps_detected\"].includes(completion.status)?\"warning\":\"report-note\")+'\"><b>حالة إكمال البحث:</b> '+escapeHtml(completionStatusLabels[completion.status]\|\|completion.status)+'. هذه حالة تشغيلية وليست احتمالًا لصحة الإجابة.</p>'"` | — |
| [SRC-DE7EABE998-L000204](../../web/agent.html#L204) | 204 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000205](../../web/agent.html#L205) | 205 | `" const completionPhaseRows=completion&&completion.phases&&typeof completion.phases===\"object\""` | — |
| [SRC-DE7EABE998-L000206](../../web/agent.html#L206) | 206 | `"  ?Object.entries(completion.phases).map(([phase,state])=>'<li>'+escapeHtml(completionPhaseLabels[phase]\|\|phase)+': '+escapeHtml(completionStateLabels[state]\|\|state\|\|\"غير محدد\")+'</li>').join(\"\")"` | — |
| [SRC-DE7EABE998-L000207](../../web/agent.html#L207) | 207 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000208](../../web/agent.html#L208) | 208 | `" const completionCounters=completion&&completion.counters&&typeof completion.counters===\"object\"?completion.counters:{};"` | — |
| [SRC-DE7EABE998-L000209](../../web/agent.html#L209) | 209 | `" const completionCounterRows=["` | — |
| [SRC-DE7EABE998-L000210](../../web/agent.html#L210) | 210 | `"  [completionCounters.queries_planned,\"استعلامًا مخططًا\"],"` | — |
| [SRC-DE7EABE998-L000211](../../web/agent.html#L211) | 211 | `"  [completionCounters.queries_attempted,\"استعلامًا تمت محاولته\"],"` | — |
| [SRC-DE7EABE998-L000212](../../web/agent.html#L212) | 212 | `"  [completionCounters.per_query_result_count_sum,\"مجموع أعداد النتائج المسجلة لكل استعلام، قبل إزالة التكرار\"],"` | — |
| [SRC-DE7EABE998-L000213](../../web/agent.html#L213) | 213 | `"  [completionCounters.final_source_list_count,\"مصدرًا في القائمة النهائية\"],"` | — |
| [SRC-DE7EABE998-L000214](../../web/agent.html#L214) | 214 | `"  [completionCounters.unique_normalized_url_count,\"رابطًا فريدًا بعد التطبيع\"],"` | — |
| [SRC-DE7EABE998-L000215](../../web/agent.html#L215) | 215 | `"  [completionCounters.duplicate_normalized_url_count,\"رابطًا مكررًا وفق التطبيع\"],"` | — |
| [SRC-DE7EABE998-L000216](../../web/agent.html#L216) | 216 | `"  [completionCounters.distinct_registrable_domain_count,\"نطاقًا مسجلًا مختلفًا\"],"` | — |
| [SRC-DE7EABE998-L000217](../../web/agent.html#L217) | 217 | `"  [completionCounters.pages_fetched_flag_count,\"صفحة تحمل علامة جلب\"],"` | — |
| [SRC-DE7EABE998-L000218](../../web/agent.html#L218) | 218 | `"  [completionCounters.pages_read_with_text_count,\"صفحة توفر نصها المقروء\"],"` | — |
| [SRC-DE7EABE998-L000219](../../web/agent.html#L219) | 219 | `"  [completionCounters.snippet_only_source_count,\"مصدرًا بمقتطف دون صفحة مقروءة\"],"` | — |
| [SRC-DE7EABE998-L000220](../../web/agent.html#L220) | 220 | `"  [completionCounters.connector_success_count,\"استجابة موصل ناجحة/مكتملة\"],"` | — |
| [SRC-DE7EABE998-L000221](../../web/agent.html#L221) | 221 | `"  [completionCounters.connector_failure_count,\"حالة إخفاق موصل مسجلة\"],"` | — |
| [SRC-DE7EABE998-L000222](../../web/agent.html#L222) | 222 | `"  [completionCounters.guardrail_rejected_candidate_count,\"مرشحًا مرفوضًا بحواجز الأدلة\"]"` | — |
| [SRC-DE7EABE998-L000223](../../web/agent.html#L223) | 223 | `" ];"` | — |
| [SRC-DE7EABE998-L000224](../../web/agent.html#L224) | 224 | `" const completionCounterHtml=completionCounterRows.map(([value,label])=>'<div class=\"metric\"><strong>'+escapeHtml(value===null\|\|value===undefined?\"غير محدد\":value)+'</strong><span>'+escapeHtml(label)+'</span></div>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000225](../../web/agent.html#L225) | 225 | `" const consistency=completion&&completion.counter_consistency&&typeof completion.counter_consistency===\"object\"?completion.counter_consistency:null;"` | — |
| [SRC-DE7EABE998-L000226](../../web/agent.html#L226) | 226 | `" const consistencyLabels={matched:\"العدادات المتاحة متطابقة\",mismatch_detected:\"اختلاف بين بعض العدادات والقائمة النهائية\",not_computable:\"لا توجد عدادات كافية للمقارنة\"};"` | — |
| [SRC-DE7EABE998-L000227](../../web/agent.html#L227) | 227 | `" const consistencyHtml=consistency?'<p class=\"'+(consistency.status===\"mismatch_detected\"?\"warning\":\"report-note\")+'\">اتساق العدادات: '+escapeHtml(consistencyLabels[consistency.status]\|\|consistency.status\|\|\"غير محدد\")+(Array.isArray(consistency.issues)&&consistency.issues.length?' — '+consistency.issues.map(escapeHtml).join(\"، \"):\"\")+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000228](../../web/agent.html#L228) | 228 | `" const completionDetailsHtml=completion&&completion.status"` | — |
| [SRC-DE7EABE998-L000229](../../web/agent.html#L229) | 229 | `"  ?'<details class=\"details\"><summary>تفاصيل مراحل إكمال البحث والعدادات</summary>'+(completionPhaseRows?'<p class=\"report-note\">مراحل التنفيذ:</p><ul>'+completionPhaseRows+'</ul>':\"\")+'<div class=\"metrics\">'+completionCounterHtml+'</div>'+consistencyHtml+'<p class=\"warning\">التحقق الدلالي من أن كل ادعاء مسنود فعلًا بالمصدر لم يُنفذ في هذا التشخيص. صلاحية رقم الإحالة أو قراءة الصفحة لا تثبت صحة الادعاء.</p></details>'"` | — |
| [SRC-DE7EABE998-L000230](../../web/agent.html#L230) | 230 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000231](../../web/agent.html#L231) | 231 | `" const e=r.evidence_signals&&typeof r.evidence_signals===\"object\"?r.evidence_signals:{};"` | — |
| [SRC-DE7EABE998-L000232](../../web/agent.html#L232) | 232 | `" const sources=Array.isArray(result.sources)?result.sources:[];"` | — |
| [SRC-DE7EABE998-L000233](../../web/agent.html#L233) | 233 | `" const researchErrorOutcome=[\"attempted_research_error\",\"unknown_after_research_error\"].includes(r.search_outcome);"` | — |
| [SRC-DE7EABE998-L000234](../../web/agent.html#L234) | 234 | `" const lead=r.lead_generation&&typeof r.lead_generation===\"object\"?r.lead_generation:null;"` | — |
| [SRC-DE7EABE998-L000235](../../web/agent.html#L235) | 235 | `" const leadResearchIncomplete=!!lead&&lead.status===\"research_incomplete\";"` | — |
| [SRC-DE7EABE998-L000236](../../web/agent.html#L236) | 236 | `" const leadSignalCount=lead&&lead.candidate_signal_count!==null&&lead.candidate_signal_count!==undefined&&Number.isFinite(Number(lead.candidate_signal_count))?Number(lead.candidate_signal_count):null;"` | — |
| [SRC-DE7EABE998-L000237](../../web/agent.html#L237) | 237 | `" const noQualifiedLeads=!!lead&&!leadResearchIncomplete&&leadSignalCount===0;"` | — |
| [SRC-DE7EABE998-L000238](../../web/agent.html#L238) | 238 | `" const scoreLabel=lead?(leadResearchIncomplete?\"تعذر حسم البحث عن العملاء\":noQualifiedLeads?\"لم يُثبت وجود عميل محتمل\":\"إشارات نية شراء مرشحة\"):(researchErrorOutcome?\"تعذر تحديد التغطية\":(e.coverage_level\|\|\"تغطية محدودة\"));"` | — |
| [SRC-DE7EABE998-L000239](../../web/agent.html#L239) | 239 | `" const metrics=lead?["` | — |
| [SRC-DE7EABE998-L000240](../../web/agent.html#L240) | 240 | `"  [leadSignalCount??\"غير محدد\",\"إشارة نصية مرشحة لنية شراء\"],"` | — |
| [SRC-DE7EABE998-L000241](../../web/agent.html#L241) | 241 | `"  [lead.related_results_reviewed??\"غير محدد\",\"نتيجة تمت مراجعتها\"],"` | — |
| [SRC-DE7EABE998-L000242](../../web/agent.html#L242) | 242 | `"  [r.pages_fetched??(leadResearchIncomplete?\"غير محدد\":0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000243](../../web/agent.html#L243) | 243 | `"  [leadResearchIncomplete?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000244](../../web/agent.html#L244) | 244 | `" ]:["` | — |
| [SRC-DE7EABE998-L000245](../../web/agent.html#L245) | 245 | `"  [researchErrorOutcome?(r.unique_sources??\"غير محدد\"):(r.unique_sources??sources.length),\"مصدرًا فريدًا\"],"` | — |
| [SRC-DE7EABE998-L000246](../../web/agent.html#L246) | 246 | `"  [researchErrorOutcome?\"غير محدد\":(e.unique_domains??\"—\"),\"نطاقًا مختلفًا\"],"` | — |
| [SRC-DE7EABE998-L000247](../../web/agent.html#L247) | 247 | `"  [researchErrorOutcome?(r.pages_fetched??\"غير محدد\"):(r.pages_fetched??e.pages_read??0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000248](../../web/agent.html#L248) | 248 | `"  [researchErrorOutcome?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000249](../../web/agent.html#L249) | 249 | `" ];"` | — |
| [SRC-DE7EABE998-L000250](../../web/agent.html#L250) | 250 | `" const metricHtml=metrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000251](../../web/agent.html#L251) | 251 | `" const operationalMetrics=["` | — |
| [SRC-DE7EABE998-L000252](../../web/agent.html#L252) | 252 | `"  [r.provider_candidates_received??\"غير محدد\",\"مرشح أعاده محرك البحث قبل التصفية (قد يتكرر)\"],"` | — |
| [SRC-DE7EABE998-L000253](../../web/agent.html#L253) | 253 | `"  [r.provider_candidates_accepted??\"غير محدد\",\"مرشح اجتاز فحص الموصل قبل الدمج\"],"` | — |
| [SRC-DE7EABE998-L000254](../../web/agent.html#L254) | 254 | `"  [r.provider_candidates_rejected??\"غير محدد\",\"مرشح رُفض بفحص الرابط أو الصلة\"],"` | — |
| [SRC-DE7EABE998-L000255](../../web/agent.html#L255) | 255 | `"  [r.raw_results??\"غير محدد\",\"نتيجة جُمعت قبل دمج التكرارات\"],"` | — |
| [SRC-DE7EABE998-L000256](../../web/agent.html#L256) | 256 | `"  [r.unique_urls??r.unique_sources??sources.length,\"رابط فريد بعد الدمج\"],"` | — |
| [SRC-DE7EABE998-L000257](../../web/agent.html#L257) | 257 | `"  [r.pages_fetch_attempted??\"غير محدد\",\"محاولة جلب صفحة\"],"` | — |
| [SRC-DE7EABE998-L000258](../../web/agent.html#L258) | 258 | `"  [r.pages_content_extracted??r.pages_fetched??\"غير محدد\",\"صفحة استُخرج منها نص\"],"` | — |
| [SRC-DE7EABE998-L000259](../../web/agent.html#L259) | 259 | `"  [r.pages_partial_extracted??\"غير محدد\",\"صفحة استُخرج جزء من نصها\"],"` | — |
| [SRC-DE7EABE998-L000260](../../web/agent.html#L260) | 260 | `"  [r.pages_extract_failed??\"غير محدد\",\"صفحة فشل استخراج نصها\"]"` | — |
| [SRC-DE7EABE998-L000261](../../web/agent.html#L261) | 261 | `" ];"` | — |
| [SRC-DE7EABE998-L000262](../../web/agent.html#L262) | 262 | `" const operationalHtml='<div class=\"metrics\">'+operationalMetrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\")+'</div>';"` | — |
| [SRC-DE7EABE998-L000263](../../web/agent.html#L263) | 263 | `" const connectors=r.connector_summary&&Array.isArray(r.connector_summary.connectors)?r.connector_summary.connectors:[];"` | — |
| [SRC-DE7EABE998-L000264](../../web/agent.html#L264) | 264 | `" const connectorDetails=connectors.length?'<details class=\"details\"><summary>تشخيص الموصلات في هذا الطلب ('+connectors.length+')</summary><div>'+connectors.map(c=>'<article class=\"source\"><strong>'+escapeHtml(c.name\|\|\"موصل\")+' · '+escapeHtml(c.status\|\|\"unknown\")+'</strong><p>الإعداد: '+escapeHtml(c.configuration_status\|\|\"unknown\")+' · تمت المحاولة: '+escapeHtml(c.attempted===true?\"نعم\":c.attempted===false?\"لا\":\"غير محسوم\")+' · متاح في هذا الطلب: '+escapeHtml(c.available_for_this_request===true?\"نعم\":c.available_for_this_request===false?\"لا\":\"غير محسوم\")+' · استجابة المعالجة مؤكدة: '+escapeHtml(c.verified_for_this_request===true?\"نعم\":c.verified_for_this_request===false?\"لا\":\"غير مختبر/غير محسوم\")+' · إخفاق ملاحظ: '+escapeHtml(c.failure_observed===true?\"نعم\":\"لا\")+' · مرشحون أوليون من الموصل: '+escapeHtml(c.result_count??\"غير محدد\")+' · اجتازوا فحص الموصل: '+escapeHtml(c.accepted_count??\"غير محدد\")+' · مصادر نهائية منسوبة إليه: '+escapeHtml(c.useful_result_count??\"غير محدد\")+' · مرفوض: '+escapeHtml(c.rejected_count??\"غير محدد\")+' · توزيع الرفض: '+escapeHtml(c.rejection_counts_observed===true&&c.rejection_counts?('مرشح مشوّه '+(c.rejection_counts.malformed_candidate??0)+'؛ رابط غير صالح/هدف غير آمن '+(c.rejection_counts.invalid_url_or_unsafe_target??0)+'؛ نطاق محظور '+(c.rejection_counts.blocked_domain??0)+'؛ صلة ضعيفة '+(c.rejection_counts.relevance_below_threshold??0)):'غير مسجل في هذه الجولة')+' · كل المرشحين رُفضوا: '+escapeHtml(c.candidate_rejection_observed===true?\"نعم\":c.candidate_rejection_observed===false?\"لا\":\"غير محسوم\")+'</p>'+((Array.isArray(c.queries)&&c.queries.length)?'<p>استعلامات: '+c.queries.map(escapeHtml).join(\" · \")+'</p>':\"\")+((Array.isArray(c.errors)&&c.errors.length)?'<p class=\"warning\">أخطاء: '+c.errors.map(escapeHtml).join(\" · \")+'</p>':\"\")+'</article>').join(\"\")+'</div></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000265](../../web/agent.html#L265) | 265 | `" const integrity=r.answer_integrity&&typeof r.answer_integrity===\"object\"?r.answer_integrity:null;"` | — |
| [SRC-DE7EABE998-L000266](../../web/agent.html#L266) | 266 | `" const integrityNumbers=integrity&&Array.isArray(integrity.potentially_unsupported_numeric_literals)?integrity.potentially_unsupported_numeric_literals:[];"` | — |
| [SRC-DE7EABE998-L000267](../../web/agent.html#L267) | 267 | `" const integrityTargets=integrity&&Array.isArray(integrity.target_coverage)?integrity.target_coverage:[];"` | — |
| [SRC-DE7EABE998-L000268](../../web/agent.html#L268) | 268 | `" const requirementEvidence=integrity&&Array.isArray(integrity.requirement_evidence)?integrity.requirement_evidence:[];"` | — |
| [SRC-DE7EABE998-L000269](../../web/agent.html#L269) | 269 | `" const requirementEvidenceHtml=requirementEvidence.length?'<p class=\"report-note\">سجل الأدلة لكل محور — إشارات لفظية وربط استعلامات، وليست إثباتًا لصحة الادعاءات:</p><ul>'+requirementEvidence.map(item=>{const statusText=({candidate_evidence_found_not_verified:\"وُجد نص مرشح مطابق لفظيًا؛ لم تُتحقق دلالته.\",query_returned_candidates_no_lexical_signal:\"عاد الاستعلام بمصادر، لكن لم يظهر تطابق لفظي كافٍ داخل النص.\",no_candidate_evidence_found:\"لم تُسجل أدلة مرشحة لهذا المحور في النتائج المتاحة.\",query_result_linkage_unavailable:\"تعذر ربط النتائج بالاستعلام المخصص لهذا المحور.\",query_not_available:\"لا يوجد استعلام مخصص مسجل لهذا المحور.\"})[item.status]\|\|\"الحالة غير محسومة.\";const ids=Array.isArray(item.candidate_source_indexes)?item.candidate_source_indexes:[];const qids=Array.isArray(item.query_result_source_indexes)?item.query_result_source_indexes:[];return '<li><strong>'+escapeHtml(item.target\|\|\"محور\")+':</strong> '+escapeHtml(statusText)+(ids.length?' — مرشحو الدليل: '+ids.map(n=>\"المصدر \"+escapeHtml(n)).join(\"، \"):\"\")+(qids.length?' — نتائج الاستعلام: '+qids.map(n=>\"المصدر \"+escapeHtml(n)).join(\"، \"):\"\")+'</li>';}).join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000270](../../web/agent.html#L270) | 270 | `" const citationNumericSupport=integrity&&Array.isArray(integrity.citation_numeric_support)?integrity.citation_numeric_support:[];"` | — |
| [SRC-DE7EABE998-L000271](../../web/agent.html#L271) | 271 | `" const citedNumberIssues=citationNumericSupport.filter(item=>item&&Array.isArray(item.potentially_unsupported_numeric_literals)&&item.potentially_unsupported_numeric_literals.length);"` | — |
| [SRC-DE7EABE998-L000272](../../web/agent.html#L272) | 272 | `" const citedNumberHtml=citedNumberIssues.length?'<p class=\"warning\">وجد الفحص أرقامًا قد لا يسندها المصدر المحدد في الاستشهاد؛ راجع المقتطف أو نص الصفحة الأصلي.</p><ul>'+citedNumberIssues.map(item=>'<li>الجملة '+escapeHtml(item.sentence_number??\"غير محدد\")+' · الرقم: '+item.potentially_unsupported_numeric_literals.map(escapeHtml).join(\"، \")+' · الاستشهادات: '+(Array.isArray(item.cited_source_indexes)?item.cited_source_indexes.map(n=>'المصدر '+escapeHtml(n)).join(\"، \"):\"غير محددة\")+'</li>').join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000273](../../web/agent.html#L273) | 273 | `" const valueDiscrepancies=integrity&&Array.isArray(integrity.potential_value_discrepancies)?integrity.potential_value_discrepancies:[];"` | — |
| [SRC-DE7EABE998-L000274](../../web/agent.html#L274) | 274 | `" const valueDimensionLabels={price_or_cost:\"السعر/التكلفة\",area_or_size:\"المساحة/الحجم\",duration:\"المدة\",percentage_or_rate:\"النسبة\",date_or_year:\"التاريخ/السنة\"};"` | — |
| [SRC-DE7EABE998-L000275](../../web/agent.html#L275) | 275 | `" const valueDiscrepancyHtml=valueDiscrepancies.length?'<p class=\"warning\">رُصدت قيم مختلفة في مصادر متعددة. قد يكون الاختلاف بين منتجات أو فترات أو وحدات مختلفة؛ هذه ليست إثباتًا تلقائيًا لوجود تناقض.</p><ul>'+valueDiscrepancies.map(item=>'<li>'+escapeHtml(valueDimensionLabels[item.dimension]\|\|item.dimension\|\|\"قيمة\")+' — '+(Array.isArray(item.values)?item.values.map(value=>escapeHtml(value.value)+' ('+(Array.isArray(value.source_indexes)?value.source_indexes.map(n=>'المصدر '+escapeHtml(n)).join(\"، \"):\"مصدر غير محدد\")+')').join(' مقابل '):\"قِيَم تحتاج مراجعة\")+'</li>').join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000276](../../web/agent.html#L276) | 276 | `" const citationAlignment=integrity&&Array.isArray(integrity.citation_lexical_alignment)?integrity.citation_lexical_alignment:[];"` | — |
| [SRC-DE7EABE998-L000277](../../web/agent.html#L277) | 277 | `" const weakCitationAlignment=citationAlignment.filter(item=>item&&item.status===\"weak_lexical_overlap\");"` | — |
| [SRC-DE7EABE998-L000278](../../web/agent.html#L278) | 278 | `" const citationAlignmentHtml=citationAlignment.length?'<p class=\"report-note\">'+(weakCitationAlignment.length?'لم يظهر تطابق لفظي كافٍ في '+weakCitationAlignment.length+' جملة/جمل مستشهد بها؛ راجع الاستشهادات يدويًا.':'ظهرت إشارات تطابق لفظي لبعض الجمل المستشهد بها، لكنها لا تثبت أن المصدر يسند الادعاء.')+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000279](../../web/agent.html#L279) | 279 | `" const integrityScope=integrity?({contains_extracted_page_text_and_or_snippets:\"نص صفحات مستخرج مع مقتطفات بحث\",search_snippets_only:\"مقتطفات بحث فقط — لم يؤكد النظام قراءة نص الصفحات\",no_readable_source_text:\"لا يتوفر نص مصدر قابل للفحص\"}[integrity.source_evidence_scope]\|\|integrity.source_evidence_scope\|\|\"غير محدد\"):\"غير محدد\";"` | — |
| [SRC-DE7EABE998-L000280](../../web/agent.html#L280) | 280 | `" const integritySummary=integrity?'<p class=\"report-note\">عدادات الفحص اللفظي: '+escapeHtml(integrity.potentially_unsupported_numeric_count??0)+' رقم لم يظهر نصيًا في الأدلة؛ '+escapeHtml(integrity.potentially_unsupported_numeric_by_citation_count??0)+' رقم لا يسنده المصدر المشار إليه تحديدًا؛ '+escapeHtml(integrity.potential_value_discrepancy_count??0)+' اختلاف قيمة يحتاج مطابقة؛ '+escapeHtml(integrity.potentially_missing_target_count??0)+' محور محتمل النقص؛ '+escapeHtml(integrity.source_evidence_gap_count??0)+' محور بلا إشارة لفظية في المصادر.</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000281](../../web/agent.html#L281) | 281 | `" const taskFulfillmentStatus=r.task_fulfillment_status\|\|result.task_fulfillment_status\|\|\"not_machine_assessed_no_explicit_targets_detected\";"` | — |
| [SRC-DE7EABE998-L000282](../../web/agent.html#L282) | 282 | `" const taskFulfillmentText=({"` | — |
| [SRC-DE7EABE998-L000283](../../web/agent.html#L283) | 283 | `"  possible_gap_detected:\"قد تكون الإجابة أغفلت محورًا من السؤال؛ هذه إشارة لفظية تحتاج مراجعة وليست حكمًا نهائيًا.\","` | — |
| [SRC-DE7EABE998-L000284](../../web/agent.html#L284) | 284 | `"  lexical_signals_found_not_semantically_verified:\"ظهرت إشارات لفظية للمحاور المستخرجة، لكن هذا لا يثبت اكتمال المهمة.\","` | — |
| [SRC-DE7EABE998-L000285](../../web/agent.html#L285) | 285 | `"  candidate_evidence_gaps_or_linkage_unknown:\"لا توجد إشارات نصية كافية لبعض المحاور أو تعذر ربط نتائج البحث بها؛ راجع الاستعلامات والمصادر قبل اعتماد الإجابة.\","` | — |
| [SRC-DE7EABE998-L000286](../../web/agent.html#L286) | 286 | `"  not_assessed_insufficient_evidence:\"الأدلة غير كافية؛ لم يتم التحقق من اكتمال المهمة.\","` | — |
| [SRC-DE7EABE998-L000287](../../web/agent.html#L287) | 287 | `"  not_machine_assessed_no_explicit_targets_detected:\"لم تُستخرج محاور صريحة قابلة للفحص؛ اكتمال المهمة لم يُقيّم آليًا.\""` | — |
| [SRC-DE7EABE998-L000288](../../web/agent.html#L288) | 288 | `" })[taskFulfillmentStatus]\|\|\"حالة اكتمال المهمة غير محسومة آليًا.\";"` | — |
| [SRC-DE7EABE998-L000289](../../web/agent.html#L289) | 289 | `" const taskFulfillmentHtml='<p class=\"'+([\"possible_gap_detected\",\"candidate_evidence_gaps_or_linkage_unknown\"].includes(taskFulfillmentStatus)?\"warning\":\"report-note\")+'\">حالة تنفيذ المطلوب: '+escapeHtml(taskFulfillmentText)+'</p>';"` | — |
| [SRC-DE7EABE998-L000290](../../web/agent.html#L290) | 290 | `" const coverageRepairStatus=r.coverage_repair_status\|\|result.coverage_repair_status\|\|\"\";"` | — |
| [SRC-DE7EABE998-L000291](../../web/agent.html#L291) | 291 | `" const coverageRepairMessages={"` | — |
| [SRC-DE7EABE998-L000292](../../web/agent.html#L292) | 292 | `"  revised_and_reaudited:\"عُدّلت الإجابة بعد رصد محور محتمل النقص ثم خضعت لمراجعة أدلة ثانية؛ تظل المراجعة بمساعدة نموذج وليست تحققًا مستقلًا.\","` | — |
| [SRC-DE7EABE998-L000293](../../web/agent.html#L293) | 293 | `"  revised_and_reaudited_remaining_gaps:\"خضعت الإجابة المعدلة لمراجعة ثانية، لكن بقي محور محتمل النقص؛ لا تعتبر المهمة مكتملة قبل مراجعة الأدلة.\","` | — |
| [SRC-DE7EABE998-L000294](../../web/agent.html#L294) | 294 | `"  reaudit_budget_exhausted:\"انتهت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ عُرضت مقتطفات المصادر بدل اعتبار النص المعدل إجابة مكتملة.\","` | — |
| [SRC-DE7EABE998-L000295](../../web/agent.html#L295) | 295 | `"  reaudit_unavailable:\"تعذرت إعادة تدقيق الإجابة المعدلة؛ عُرضت مقتطفات المصادر بدل اعتبار النص المعدل إجابة مكتملة.\","` | — |
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
| [SRC-DE7EABE998-L000403](../../web/agent.html#L403) | 403 | `" const controller=new AbortController();"` | — |
| [SRC-DE7EABE998-L000404](../../web/agent.html#L404) | 404 | `" let requestTimedOut=false;"` | — |
| [SRC-DE7EABE998-L000405](../../web/agent.html#L405) | 405 | `" const timeoutId=window.setTimeout(()=>{requestTimedOut=true;controller.abort();},135000);"` | — |
| [SRC-DE7EABE998-L000406](../../web/agent.html#L406) | 406 | `" try{"` | — |
| [SRC-DE7EABE998-L000407](../../web/agent.html#L407) | 407 | `"  const response=await fetch(\"/api/agent\",{method:\"POST\",credentials:\"same-origin\",headers:apiHeaders(),signal:controller.signal,body:JSON.stringify({question:q,history:history.slice(-8),mode:activeMode})});"` | — |
| [SRC-DE7EABE998-L000408](../../web/agent.html#L408) | 408 | `"  const data=await response.json().catch(()=>({}));"` | — |
| [SRC-DE7EABE998-L000409](../../web/agent.html#L409) | 409 | `"  pending.remove();"` | — |
| [SRC-DE7EABE998-L000410](../../web/agent.html#L410) | 410 | `"  if(!response.ok){"` | — |
| [SRC-DE7EABE998-L000411](../../web/agent.html#L411) | 411 | `"   if(response.status===401)throw Error(\"رمز الوصول غير صحيح أو غير محفوظ. راجع رمز التطبيق المستضاف.\");"` | — |
| [SRC-DE7EABE998-L000412](../../web/agent.html#L412) | 412 | `"   if(response.status===429)throw Error(\"تجاوز حد الطلبات المؤقت. انتظر قليلًا ثم أعد المحاولة.\");"` | — |
| [SRC-DE7EABE998-L000413](../../web/agent.html#L413) | 413 | `"   throw Error(data.error\|\|\"تعذر إكمال البحث. أعد المحاولة بعد التحقق من الاتصال.\");"` | — |
| [SRC-DE7EABE998-L000414](../../web/agent.html#L414) | 414 | `"  }"` | — |
| [SRC-DE7EABE998-L000415](../../web/agent.html#L415) | 415 | `"  addMessage(\"assistant\",data.answer\|\|\"لم يرجع الخادم نص إجابة.\",data);"` | — |
| [SRC-DE7EABE998-L000416](../../web/agent.html#L416) | 416 | `"  history.push({role:\"user\",content:q},{role:\"assistant\",content:String(data.answer\|\|\"\")});"` | — |
| [SRC-DE7EABE998-L000417](../../web/agent.html#L417) | 417 | `"  const sources=Array.isArray(data.sources)?data.sources.filter(s=>s&&safeSourceUrl(s.url)):[];"` | — |
| [SRC-DE7EABE998-L000418](../../web/agent.html#L418) | 418 | `"  if(data.kind===\"general_answer\"){"` | — |
| [SRC-DE7EABE998-L000419](../../web/agent.html#L419) | 419 | `"   setStatus(\"اكتملت إجابة المعرفة العامة دون بحث ويب\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000420](../../web/agent.html#L420) | 420 | `"  }else if(data.kind===\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000421](../../web/agent.html#L421) | 421 | `"   setStatus(\"إجابة عن قدرات Omarai وحدوده · لم يُجر بحث حي\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000422](../../web/agent.html#L422) | 422 | `"  }else if(data.used_web_search===true&&data.used_language_model===true&&sources.length>0){"` | — |
| [SRC-DE7EABE998-L000423](../../web/agent.html#L423) | 423 | `"   setStatus(\"اكتمل البحث والتحليل · \"+sources.length+\" مصدرًا صالحًا\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000424](../../web/agent.html#L424) | 424 | `"  }else if(data.used_web_search===true&&sources.length>0){"` | — |
| [SRC-DE7EABE998-L000425](../../web/agent.html#L425) | 425 | `"   setStatus(\"البحث أعاد مصادر، لكن التحليل غير مكتمل\",\"warn\");"` | — |
| [SRC-DE7EABE998-L000426](../../web/agent.html#L426) | 426 | `"  }else{"` | — |
| [SRC-DE7EABE998-L000427](../../web/agent.html#L427) | 427 | `"   setStatus(\"نتيجة جزئية: لا يوجد بحث حي مؤكد مع مصادر كافية\",\"bad\");"` | — |
| [SRC-DE7EABE998-L000428](../../web/agent.html#L428) | 428 | `"  }"` | — |
| [SRC-DE7EABE998-L000429](../../web/agent.html#L429) | 429 | `" }catch(error){"` | — |
| [SRC-DE7EABE998-L000430](../../web/agent.html#L430) | 430 | `"  pending.remove();"` | — |
| [SRC-DE7EABE998-L000431](../../web/agent.html#L431) | 431 | `"  const timedOut=requestTimedOut\|\|(error&&error.name===\"AbortError\");"` | — |
| [SRC-DE7EABE998-L000432](../../web/agent.html#L432) | 432 | `"  const safeMessage=timedOut"` | — |
| [SRC-DE7EABE998-L000433](../../web/agent.html#L433) | 433 | `"   ?\"انتهى وقت انتظار الواجهة بعد 135 ثانية. قد يواصل الخادم إنهاء العملية ضمن ميزانية موارده.\""` | — |
| [SRC-DE7EABE998-L000434](../../web/agent.html#L434) | 434 | `"   :(error&&error.message?error.message:\"تعذر إكمال الطلب.\");"` | — |
| [SRC-DE7EABE998-L000435](../../web/agent.html#L435) | 435 | `"  const box=addMessage(\"assistant\",safeMessage,null,{question:q});"` | — |
| [SRC-DE7EABE998-L000436](../../web/agent.html#L436) | 436 | `"  const actions=document.createElement(\"div\");actions.className=\"retry-row\";"` | — |
| [SRC-DE7EABE998-L000437](../../web/agent.html#L437) | 437 | `"  const retry=document.createElement(\"button\");retry.type=\"button\";retry.className=\"retry-button\";"` | — |
| [SRC-DE7EABE998-L000438](../../web/agent.html#L438) | 438 | `"  retry.textContent=\"إعادة محاولة هذا السؤال\";"` | — |
| [SRC-DE7EABE998-L000439](../../web/agent.html#L439) | 439 | `"  retry.addEventListener(\"click\",()=>ask(q));actions.appendChild(retry);box.appendChild(actions);"` | — |
| [SRC-DE7EABE998-L000440](../../web/agent.html#L440) | 440 | `"  setStatus(timedOut?\"انتهى وقت الانتظار؛ يمكنك إعادة محاولة السؤال\":\"لم يكتمل الطلب؛ يمكنك إعادة محاولة السؤال نفسه\",\"bad\");"` | — |
| [SRC-DE7EABE998-L000441](../../web/agent.html#L441) | 441 | `" }finally{"` | — |
| [SRC-DE7EABE998-L000442](../../web/agent.html#L442) | 442 | `"  window.clearTimeout(timeoutId);"` | — |
| [SRC-DE7EABE998-L000443](../../web/agent.html#L443) | 443 | `"  setBusy(false);$(\"question\").focus();"` | — |
| [SRC-DE7EABE998-L000444](../../web/agent.html#L444) | 444 | `" }"` | — |
| [SRC-DE7EABE998-L000445](../../web/agent.html#L445) | 445 | `"}"` | — |
| [SRC-DE7EABE998-L000446](../../web/agent.html#L446) | 446 | `""` | — |
| [SRC-DE7EABE998-L000447](../../web/agent.html#L447) | 447 | `"async function runDiagnostics(){"` | — |
| [SRC-DE7EABE998-L000448](../../web/agent.html#L448) | 448 | `" const button=$(\"runDiagnostics\"),output=$(\"diagnosticsResult\");if(button.disabled)return;"` | — |
| [SRC-DE7EABE998-L000449](../../web/agent.html#L449) | 449 | `" if(!window.confirm(\"سيجري هذا الاختبار اتصالات فعلية بمحركات البحث والنموذج، وقد يستهلك حصص الموفّرين أو يترتب عليه رسوم. هل توافق على تنفيذ هذه الاتصالات الآن؟\"))return;"` | — |
| [SRC-DE7EABE998-L000450](../../web/agent.html#L450) | 450 | `" button.disabled=true;button.textContent=\"جارٍ الاختبار الحقيقي…\";output.textContent=\"تُرسل الآن طلبات فعلية إلى موفّري البحث والنموذج بعد موافقتك.\";"` | — |
| [SRC-DE7EABE998-L000451](../../web/agent.html#L451) | 451 | `" try{"` | — |
| [SRC-DE7EABE998-L000452](../../web/agent.html#L452) | 452 | `"  const response=await fetch(\"/api/diagnostics\",{method:\"POST\",credentials:\"same-origin\",headers:apiHeaders(),body:JSON.stringify({test_model:true,test_social:$(\"diagSocial\").checked,allow_provider_usage:true})});"` | — |
| [SRC-DE7EABE998-L000453](../../web/agent.html#L453) | 453 | `"  const data=await response.json();if(!response.ok)throw Error(data.error\|\|\"فشل طلب الاختبار\");"` | — |
| [SRC-DE7EABE998-L000454](../../web/agent.html#L454) | 454 | `"  const labels={passed:\"نجح فعليًا\",degraded:\"جزئي أو بلا نتائج كافية\",failed:\"فشل\",skipped:\"لم يُختبر\",not_configured:\"غير مضبوط\"};"` | — |
| [SRC-DE7EABE998-L000455](../../web/agent.html#L455) | 455 | `"  const lines=[\"النتيجة: \"+(labels[data.overall_status]\|\|data.overall_status)];"` | — |
| [SRC-DE7EABE998-L000456](../../web/agent.html#L456) | 456 | `"  for(const [key,label] of [[\"web_search\",\"بحث الإنترنت\"],[\"language_model\",\"النموذج اللغوي\"],[\"social_search\",\"المصادر الاجتماعية\"]]){"` | — |
| [SRC-DE7EABE998-L000457](../../web/agent.html#L457) | 457 | `"   const item=(data.checks\|\|{})[key];if(!item)continue;"` | — |
| [SRC-DE7EABE998-L000458](../../web/agent.html#L458) | 458 | `"   lines.push(label+\": \"+(labels[item.status]\|\|item.status)+(item.result_count!==undefined?\" · \"+item.result_count+\" نتيجة\":\"\"));"` | — |
| [SRC-DE7EABE998-L000459](../../web/agent.html#L459) | 459 | `"   if(item.provider_counts&&Object.keys(item.provider_counts).length)lines.push(\"المصادر التي أعادت نتائج: \"+Object.entries(item.provider_counts).map(([p,n])=>p+\" (\"+n+\")\").join(\"، \"));"` | — |
| [SRC-DE7EABE998-L000460](../../web/agent.html#L460) | 460 | `"   if(item.note)lines.push(item.note);"` | — |
| [SRC-DE7EABE998-L000461](../../web/agent.html#L461) | 461 | `"   if(item.warnings&&item.warnings.length)lines.push(item.warnings.join(\"؛ \"));"` | — |
| [SRC-DE7EABE998-L000462](../../web/agent.html#L462) | 462 | `"  }"` | — |
| [SRC-DE7EABE998-L000463](../../web/agent.html#L463) | 463 | `"  if(data.model_usage&&data.model_usage.length)lines.push(\"النموذج المستخدم: \"+data.model_usage.map(x=>x.used_model).join(\"، \"));"` | — |
| [SRC-DE7EABE998-L000464](../../web/agent.html#L464) | 464 | `"  if(data.elapsed_ms!==undefined)lines.push(\"مدة الاختبار: \"+(data.elapsed_ms/1000).toFixed(1)+\" ثانية\");"` | — |
| [SRC-DE7EABE998-L000465](../../web/agent.html#L465) | 465 | `"  output.textContent=lines.join(\"\\n\");setStatus(data.overall_status===\"passed\"?\"نجح الاختبار الحي\":data.overall_status===\"failed\"?\"فشل الاختبار الحي\":\"نتيجة الاختبار جزئية\",data.overall_status===\"passed\"?\"ok\":data.overall_status===\"failed\"?\"bad\":\"warn\");"` | — |
| [SRC-DE7EABE998-L000466](../../web/agent.html#L466) | 466 | `" }catch(e){output.textContent=\"تعذّر الاختبار الحي: \"+(e&&e.message?e.message:\"خطأ غير معروف\");setStatus(\"فشل الاختبار الحي\",\"bad\");}"` | — |
| [SRC-DE7EABE998-L000467](../../web/agent.html#L467) | 467 | `" finally{button.disabled=false;button.textContent=\"إعادة الاختبار الحي\";}"` | — |
| [SRC-DE7EABE998-L000468](../../web/agent.html#L468) | 468 | `"}"` | — |
| [SRC-DE7EABE998-L000469](../../web/agent.html#L469) | 469 | `"async function checkHealth(){"` | — |
| [SRC-DE7EABE998-L000470](../../web/agent.html#L470) | 470 | `" try{"` | — |
| [SRC-DE7EABE998-L000471](../../web/agent.html#L471) | 471 | `"  const r=await fetch(\"/api/health\");const d=await r.json();const a=d.agent\|\|{};"` | — |
| [SRC-DE7EABE998-L000472](../../web/agent.html#L472) | 472 | `"  const configured=[];"` | — |
| [SRC-DE7EABE998-L000473](../../web/agent.html#L473) | 473 | `"  if(a.brave_search_api_configured)configured.push(\"Brave API\");"` | — |
| [SRC-DE7EABE998-L000474](../../web/agent.html#L474) | 474 | `"  if(a.tavily_search_api_configured)configured.push(\"Tavily API\");"` | — |
| [SRC-DE7EABE998-L000475](../../web/agent.html#L475) | 475 | `"  if(a.reddit_oauth_configured)configured.push(\"Reddit OAuth\");"` | — |
| [SRC-DE7EABE998-L000476](../../web/agent.html#L476) | 476 | `"  if(a.facebook_pages_api_configured)configured.push(\"Facebook Pages\");"` | — |
| [SRC-DE7EABE998-L000477](../../web/agent.html#L477) | 477 | `"  if(a.instagram_graph_api_configured)configured.push(\"Instagram Graph\");"` | — |
| [SRC-DE7EABE998-L000478](../../web/agent.html#L478) | 478 | `"  if(a.x_api_configured)configured.push(\"X API\");"` | — |
| [SRC-DE7EABE998-L000479](../../web/agent.html#L479) | 479 | `"  if(a.youtube_api_configured)configured.push(\"YouTube API\");"` | — |
| [SRC-DE7EABE998-L000480](../../web/agent.html#L480) | 480 | `"  const model=!!a.language_model_configured, search=!!a.web_search_ready;"` | — |
| [SRC-DE7EABE998-L000481](../../web/agent.html#L481) | 481 | `"  $(\"setupStatus\").textContent=(search?\"حزم البحث مثبتة. \":\"حزم البحث تحتاج تثبيتًا. \")+(model?\"مفتاح نموذج اللغة موجود في جلسة الخادم. \":\"النموذج التوليدي غير مضبوط بعد. \")+\"لم يتم تأكيد اتصال الإنترنت من هذه الشاشة وحدها؛ شغّل الاختبار الحي. لا تظهر هنا مفاتيح الخدمات أو قيمها.\";"` | — |
| [SRC-DE7EABE998-L000482](../../web/agent.html#L482) | 482 | `"  $(\"providerSetup\").innerHTML=configured.length?'<span class=\"config-label\">موصلات مفاتيحها مضبوطة: '+configured.map(escapeHtml).join(\" · \")+'</span>':'<p>لم تُضبط مفاتيح API البحثية الإضافية؛ يظل Omarai قادرًا على تجربة محركات البحث العامة المتاحة.</p>';"` | — |
| [SRC-DE7EABE998-L000483](../../web/agent.html#L483) | 483 | `"  setStatus(\"الإعداد ظاهر · يلزم اختبار حي\",\"warn\");"` | — |
| [SRC-DE7EABE998-L000484](../../web/agent.html#L484) | 484 | `" }catch(e){setStatus(\"تعذر فحص الإعداد\",\"bad\");$(\"setupStatus\").textContent=\"تعذر الاتصال بخادم Omarai المحلي. تأكد أن الخادم يعمل في Termux.\";}"` | — |
| [SRC-DE7EABE998-L000485](../../web/agent.html#L485) | 485 | `"}"` | — |
| [SRC-DE7EABE998-L000486](../../web/agent.html#L486) | 486 | `"document.querySelectorAll(\".mode-btn\").forEach(button=>button.addEventListener(\"click\",()=>{"` | — |
| [SRC-DE7EABE998-L000487](../../web/agent.html#L487) | 487 | `" activeMode=button.dataset.mode;"` | — |
| [SRC-DE7EABE998-L000488](../../web/agent.html#L488) | 488 | `" document.querySelectorAll(\".mode-btn\").forEach(other=>{const active=other===button;other.classList.toggle(\"active\",active);other.setAttribute(\"aria-pressed\",String(active));});"` | — |
| [SRC-DE7EABE998-L000489](../../web/agent.html#L489) | 489 | `"}));"` | — |
| [SRC-DE7EABE998-L000490](../../web/agent.html#L490) | 490 | `"$(\"send\").addEventListener(\"click\",()=>ask());"` | — |
| [SRC-DE7EABE998-L000491](../../web/agent.html#L491) | 491 | `"$(\"question\").addEventListener(\"keydown\",e=>{if(e.key===\"Enter\"&&!e.shiftKey){e.preventDefault();ask();}});"` | — |
| [SRC-DE7EABE998-L000492](../../web/agent.html#L492) | 492 | `"$(\"clear\").addEventListener(\"click\",()=>{history.length=0;$(\"messages\").innerHTML='<div class=\"welcome\" id=\"welcome\"><div class=\"welcome-icon\">⌕</div><h3>محادثة جديدة</h3><p>اكتب سؤالك واختر نمط البحث المناسب. المصادر والتغطية سيظهران أسفل الإجابة.</p></div>';$(\"question\").focus();});"` | — |
| [SRC-DE7EABE998-L000493](../../web/agent.html#L493) | 493 | `"document.querySelectorAll(\".suggestions button\").forEach(b=>b.addEventListener(\"click\",()=>ask(b.textContent)));"` | — |
| [SRC-DE7EABE998-L000494](../../web/agent.html#L494) | 494 | `"async function loginBrowserSession(){"` | — |
| [SRC-DE7EABE998-L000495](../../web/agent.html#L495) | 495 | `"  const token=$(\"accessToken\").value.trim();"` | — |
| [SRC-DE7EABE998-L000496](../../web/agent.html#L496) | 496 | `"  if(!token){$(\"authStatus\").textContent=\"أدخل رمز الوصول أولًا.\";return;}"` | — |
| [SRC-DE7EABE998-L000497](../../web/agent.html#L497) | 497 | `"  try{"` | — |
| [SRC-DE7EABE998-L000498](../../web/agent.html#L498) | 498 | `"    const response=await fetch(\"/api/session\",{method:\"POST\",credentials:\"same-origin\",headers:{\"Content-Type\":\"application/json\"},body:JSON.stringify({access_token:token})});"` | — |
| [SRC-DE7EABE998-L000499](../../web/agent.html#L499) | 499 | `"    const data=await response.json();"` | — |
| [SRC-DE7EABE998-L000500](../../web/agent.html#L500) | 500 | `"    if(!response.ok)throw new Error(data.error\|\|\"تعذر تسجيل الدخول.\");"` | — |
| [SRC-DE7EABE998-L000501](../../web/agent.html#L501) | 501 | `"    $(\"accessToken\").value=\"\";"` | — |
| [SRC-DE7EABE998-L000502](../../web/agent.html#L502) | 502 | `"    $(\"authStatus\").textContent=\"تم تسجيل الدخول بجلسة HttpOnly تنتهي خلال 8 ساعات أو عند انتهاء/إبطال الرمز.\";"` | — |
| [SRC-DE7EABE998-L000503](../../web/agent.html#L503) | 503 | `"    $(\"saveAccessToken\").textContent=\"متصل\";"` | — |
| [SRC-DE7EABE998-L000504](../../web/agent.html#L504) | 504 | `"  }catch(error){$(\"authStatus\").textContent=error.message;}"` | — |
| [SRC-DE7EABE998-L000505](../../web/agent.html#L505) | 505 | `"}"` | — |
| [SRC-DE7EABE998-L000506](../../web/agent.html#L506) | 506 | `"async function logoutBrowserSession(){"` | — |
| [SRC-DE7EABE998-L000507](../../web/agent.html#L507) | 507 | `"  try{"` | — |
| [SRC-DE7EABE998-L000508](../../web/agent.html#L508) | 508 | `"    const response=await fetch(\"/api/session/logout\",{method:\"POST\",credentials:\"same-origin\",headers:{\"Content-Type\":\"application/json\"},body:\"{}\"});"` | — |
| [SRC-DE7EABE998-L000509](../../web/agent.html#L509) | 509 | `"    const data=await response.json();"` | — |
| [SRC-DE7EABE998-L000510](../../web/agent.html#L510) | 510 | `"    if(!response.ok)throw new Error(data.error\|\|\"تعذر تسجيل الخروج.\");"` | — |
| [SRC-DE7EABE998-L000511](../../web/agent.html#L511) | 511 | `"    $(\"authStatus\").textContent=\"تم تسجيل الخروج.\";"` | — |
| [SRC-DE7EABE998-L000512](../../web/agent.html#L512) | 512 | `"    $(\"saveAccessToken\").textContent=\"تسجيل الدخول\";"` | — |
| [SRC-DE7EABE998-L000513](../../web/agent.html#L513) | 513 | `"  }catch(error){$(\"authStatus\").textContent=error.message;}"` | — |
| [SRC-DE7EABE998-L000514](../../web/agent.html#L514) | 514 | `"}"` | — |
| [SRC-DE7EABE998-L000515](../../web/agent.html#L515) | 515 | `"async function checkBrowserSession(){"` | — |
| [SRC-DE7EABE998-L000516](../../web/agent.html#L516) | 516 | `"  try{"` | — |
| [SRC-DE7EABE998-L000517](../../web/agent.html#L517) | 517 | `"    const response=await fetch(\"/api/session\",{credentials:\"same-origin\"});"` | — |
| [SRC-DE7EABE998-L000518](../../web/agent.html#L518) | 518 | `"    const data=await response.json();"` | — |
| [SRC-DE7EABE998-L000519](../../web/agent.html#L519) | 519 | `"    if(!response.ok)throw new Error(data.error\|\|\"لا توجد جلسة نشطة.\");"` | — |
| [SRC-DE7EABE998-L000520](../../web/agent.html#L520) | 520 | `"    $(\"authStatus\").textContent=\"جلسة نشطة بدور: \"+data.role;"` | — |
| [SRC-DE7EABE998-L000521](../../web/agent.html#L521) | 521 | `"    $(\"saveAccessToken\").textContent=\"متصل\";"` | — |
| [SRC-DE7EABE998-L000522](../../web/agent.html#L522) | 522 | `"  }catch(_error){$(\"authStatus\").textContent=\"أدخل رمز الوصول لبدء جلسة آمنة.\";}"` | — |
| [SRC-DE7EABE998-L000523](../../web/agent.html#L523) | 523 | `"}"` | — |
| [SRC-DE7EABE998-L000524](../../web/agent.html#L524) | 524 | `"$(\"saveAccessToken\").addEventListener(\"click\",loginBrowserSession);"` | — |
| [SRC-DE7EABE998-L000525](../../web/agent.html#L525) | 525 | `"$(\"logoutSession\").addEventListener(\"click\",logoutBrowserSession);"` | — |
| [SRC-DE7EABE998-L000526](../../web/agent.html#L526) | 526 | `"$(\"runDiagnostics\").addEventListener(\"click\",runDiagnostics);checkHealth();checkBrowserSession();"` | — |
| [SRC-DE7EABE998-L000527](../../web/agent.html#L527) | 527 | `"</script>"` | — |
| [SRC-DE7EABE998-L000528](../../web/agent.html#L528) | 528 | `"</body>"` | — |
| [SRC-DE7EABE998-L000529](../../web/agent.html#L529) | 529 | `"</html>"` | — |
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
| [SRC-A16FA6D4B5-L000014](../../web/dashboard.html#L14) | 14 | `"<header class=\"top\"><div class=\"brand\"><div class=\"logo\">O</div><div><h1>Omarai</h1><p>مساعد ذكي لتأهيل إشارات العملاء المحتملين</p></div></div><span class=\"badge\">● تشغيل محلي أو مستضاف حسب إعداد الخادم</span><a class=\"secondary\" href=\"/workspace\">مساحة العمل الجديدة ↗</a></header>"` | — |
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
## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2C8F288796-L000001](../../web/workspace.html#L1) | 1 | `"<!doctype html>"` | — |
| [SRC-2C8F288796-L000002](../../web/workspace.html#L2) | 2 | `"<html lang=\"ar\" dir=\"rtl\">"` | — |
| [SRC-2C8F288796-L000003](../../web/workspace.html#L3) | 3 | `"<head>"` | — |
| [SRC-2C8F288796-L000004](../../web/workspace.html#L4) | 4 | `"<meta charset=\"utf-8\">"` | — |
| [SRC-2C8F288796-L000005](../../web/workspace.html#L5) | 5 | `"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">"` | — |
| [SRC-2C8F288796-L000006](../../web/workspace.html#L6) | 6 | `"<meta name=\"theme-color\" content=\"#09111f\">"` | — |
| [SRC-2C8F288796-L000007](../../web/workspace.html#L7) | 7 | `"<title>Omarai \| مساحة العمل</title>"` | — |
| [SRC-2C8F288796-L000008](../../web/workspace.html#L8) | 8 | `"<style>"` | — |
| [SRC-2C8F288796-L000009](../../web/workspace.html#L9) | 9 | `":root{color-scheme:dark;--bg:#080f1d;--panel:rgba(18,29,48,.78);--panel-2:rgba(15,25,42,.92);--line:rgba(150,178,214,.16);--text:#edf4ff;--muted:#9aaec8;--teal:#69e6d1;--cyan:#79cfff;--violet:#9c91ff;--coral:#ff9c9f;--amber:#f3c77c;--green:#78dfaa;--danger:#ff8794;--radius:20px}"` | — |
| [SRC-2C8F288796-L000010](../../web/workspace.html#L10) | 10 | `"*{box-sizing:border-box}"` | — |
| [SRC-2C8F288796-L000011](../../web/workspace.html#L11) | 11 | `"html{min-height:100%;background:var(--bg)}"` | — |
| [SRC-2C8F288796-L000012](../../web/workspace.html#L12) | 12 | `"body{margin:0;min-height:100vh;color:var(--text);font-family:\"Noto Sans Arabic\",\"IBM Plex Sans Arabic\",\"Segoe UI\",system-ui,sans-serif;background:radial-gradient(ellipse at 85% -10%,rgba(48,91,140,.34),transparent 38%),radial-gradient(ellipse at 8% 36%,rgba(31,91,96,.18),transparent 32%),linear-gradient(145deg,#080f1d,#0b1424 58%,#080f1d)}"` | — |
| [SRC-2C8F288796-L000013](../../web/workspace.html#L13) | 13 | `"button,input,textarea,select{font:inherit}"` | — |
| [SRC-2C8F288796-L000014](../../web/workspace.html#L14) | 14 | `"button{cursor:pointer}"` | — |
| [SRC-2C8F288796-L000015](../../web/workspace.html#L15) | 15 | `"button:focus-visible,a:focus-visible,input:focus-visible,textarea:focus-visible,select:focus-visible{outline:2px solid var(--teal);outline-offset:3px}"` | — |
| [SRC-2C8F288796-L000016](../../web/workspace.html#L16) | 16 | `"a{color:var(--cyan);text-decoration:none}"` | — |
| [SRC-2C8F288796-L000017](../../web/workspace.html#L17) | 17 | `"a:hover{text-decoration:underline}"` | — |
| [SRC-2C8F288796-L000018](../../web/workspace.html#L18) | 18 | `".app{display:grid;grid-template-columns:258px minmax(0,1fr);min-height:100vh;max-width:1680px;margin:auto}"` | — |
| [SRC-2C8F288796-L000019](../../web/workspace.html#L19) | 19 | `".sidebar{position:sticky;top:0;height:100vh;padding:22px 16px;border-left:1px solid var(--line);background:rgba(7,14,25,.72);backdrop-filter:blur(24px);display:flex;flex-direction:column;gap:18px;overflow:auto}"` | — |
| [SRC-2C8F288796-L000020](../../web/workspace.html#L20) | 20 | `".brand{display:flex;align-items:center;gap:12px;padding:4px 8px 16px;border-bottom:1px solid var(--line)}"` | — |
| [SRC-2C8F288796-L000021](../../web/workspace.html#L21) | 21 | `".logo{width:43px;height:43px;display:grid;place-items:center;border-radius:15px;background:linear-gradient(135deg,var(--teal),#7fb7ff 62%,var(--violet));color:#061421;font-weight:950;font-size:24px;box-shadow:0 8px 30px rgba(105,230,209,.19)}"` | — |
| [SRC-2C8F288796-L000022](../../web/workspace.html#L22) | 22 | `".brand-name{font-weight:900;font-size:20px;letter-spacing:.2px}.brand-sub{font-size:10px;color:var(--muted);margin-top:3px}"` | — |
| [SRC-2C8F288796-L000023](../../web/workspace.html#L23) | 23 | `".workspace-label{font-size:10px;color:#758ba8;font-weight:800;letter-spacing:.08em;padding:0 10px}"` | — |
| [SRC-2C8F288796-L000024](../../web/workspace.html#L24) | 24 | `".nav{display:flex;flex-direction:column;gap:5px}"` | — |
| [SRC-2C8F288796-L000025](../../web/workspace.html#L25) | 25 | `".nav button{display:flex;align-items:center;gap:11px;width:100%;padding:11px 12px;border:1px solid transparent;border-radius:13px;background:transparent;color:#c1d0e4;text-align:right;font-size:12px;transition:.16s}"` | — |
| [SRC-2C8F288796-L000026](../../web/workspace.html#L26) | 26 | `".nav button:hover{background:rgba(135,166,203,.08);border-color:var(--line)}"` | — |
| [SRC-2C8F288796-L000027](../../web/workspace.html#L27) | 27 | `".nav button.active{color:#eafffb;background:linear-gradient(100deg,rgba(73,194,181,.17),rgba(105,152,225,.09));border-color:rgba(105,230,209,.22)}"` | — |
| [SRC-2C8F288796-L000028](../../web/workspace.html#L28) | 28 | `".nav-icon{width:22px;text-align:center;font-size:15px;color:var(--teal)}"` | — |
| [SRC-2C8F288796-L000029](../../web/workspace.html#L29) | 29 | `".nav button.disabled{opacity:.56}"` | — |
| [SRC-2C8F288796-L000030](../../web/workspace.html#L30) | 30 | `".nav-status{margin-right:auto;padding:3px 7px;border:1px solid var(--line);border-radius:99px;color:#8297b3;font-size:9px}"` | — |
| [SRC-2C8F288796-L000031](../../web/workspace.html#L31) | 31 | `".side-bottom{margin-top:auto;display:grid;gap:10px}"` | — |
| [SRC-2C8F288796-L000032](../../web/workspace.html#L32) | 32 | `".connection{padding:13px;border:1px solid var(--line);border-radius:15px;background:rgba(18,31,51,.65)}"` | — |
| [SRC-2C8F288796-L000033](../../web/workspace.html#L33) | 33 | `".connection-title{display:flex;align-items:center;gap:8px;font-size:11px;font-weight:800}"` | — |
| [SRC-2C8F288796-L000034](../../web/workspace.html#L34) | 34 | `".dot{width:8px;height:8px;border-radius:50%;background:#8496ad;box-shadow:0 0 0 4px rgba(132,150,173,.10)}"` | — |
| [SRC-2C8F288796-L000035](../../web/workspace.html#L35) | 35 | `".dot.ok{background:var(--green);box-shadow:0 0 0 4px rgba(120,223,170,.10)}"` | — |
| [SRC-2C8F288796-L000036](../../web/workspace.html#L36) | 36 | `".dot.bad{background:var(--danger)}"` | — |
| [SRC-2C8F288796-L000037](../../web/workspace.html#L37) | 37 | `".connection small{display:block;color:var(--muted);line-height:1.7;margin-top:7px;font-size:10px}"` | — |
| [SRC-2C8F288796-L000038](../../web/workspace.html#L38) | 38 | `".side-links{display:flex;gap:8px;flex-wrap:wrap;padding:0 4px}"` | — |
| [SRC-2C8F288796-L000039](../../web/workspace.html#L39) | 39 | `".side-links a{font-size:10px;color:#92a8c4}"` | — |
| [SRC-2C8F288796-L000040](../../web/workspace.html#L40) | 40 | `".main{min-width:0;padding:24px clamp(14px,3vw,38px) 34px}"` | — |
| [SRC-2C8F288796-L000041](../../web/workspace.html#L41) | 41 | `".topbar{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:2px 0 18px;border-bottom:1px solid var(--line)}"` | — |
| [SRC-2C8F288796-L000042](../../web/workspace.html#L42) | 42 | `".breadcrumb{font-size:11px;color:var(--muted)}.breadcrumb strong{color:#e4eefb;font-size:12px}"` | — |
| [SRC-2C8F288796-L000043](../../web/workspace.html#L43) | 43 | `".top-actions{display:flex;align-items:center;gap:9px;flex-wrap:wrap}"` | — |
| [SRC-2C8F288796-L000044](../../web/workspace.html#L44) | 44 | `".role-pill,.status-pill{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);border-radius:99px;padding:7px 11px;color:#bdcbe0;font-size:10px;background:rgba(19,32,52,.6)}"` | — |
| [SRC-2C8F288796-L000045](../../web/workspace.html#L45) | 45 | `".button{display:inline-flex;align-items:center;justify-content:center;gap:8px;border:1px solid var(--line);border-radius:12px;padding:10px 14px;color:#dce8f8;background:rgba(22,37,59,.82);font-size:11px;font-weight:800;transition:.16s}"` | — |
| [SRC-2C8F288796-L000046](../../web/workspace.html#L46) | 46 | `".button:hover{border-color:rgba(105,230,209,.48);transform:translateY(-1px)}"` | — |
| [SRC-2C8F288796-L000047](../../web/workspace.html#L47) | 47 | `".button.primary{background:linear-gradient(105deg,var(--teal),#a4c5ff);color:#071522;border:0}"` | — |
| [SRC-2C8F288796-L000048](../../web/workspace.html#L48) | 48 | `".button.ghost{background:transparent}"` | — |
| [SRC-2C8F288796-L000049](../../web/workspace.html#L49) | 49 | `".button:disabled{opacity:.45;cursor:not-allowed;transform:none}"` | — |
| [SRC-2C8F288796-L000050](../../web/workspace.html#L50) | 50 | `".page-head{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;margin:26px 0 19px}"` | — |
| [SRC-2C8F288796-L000051](../../web/workspace.html#L51) | 51 | `".eyebrow{color:var(--teal);font-size:10px;font-weight:900;letter-spacing:.1em}"` | — |
| [SRC-2C8F288796-L000052](../../web/workspace.html#L52) | 52 | `".page-head h1{font-size:clamp(24px,3vw,34px);line-height:1.35;margin:6px 0 7px;letter-spacing:-.5px}"` | — |
| [SRC-2C8F288796-L000053](../../web/workspace.html#L53) | 53 | `".page-head p{max-width:760px;color:var(--muted);font-size:12px;line-height:1.9;margin:0}"` | — |
| [SRC-2C8F288796-L000054](../../web/workspace.html#L54) | 54 | `".glass{border:1px solid var(--line);border-radius:var(--radius);background:linear-gradient(145deg,rgba(22,35,56,.88),rgba(13,23,40,.87));box-shadow:0 20px 55px rgba(0,0,0,.13);backdrop-filter:blur(18px)}"` | — |
| [SRC-2C8F288796-L000055](../../web/workspace.html#L55) | 55 | `".stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-bottom:14px}"` | — |
| [SRC-2C8F288796-L000056](../../web/workspace.html#L56) | 56 | `".stat{padding:17px 18px;position:relative;overflow:hidden}"` | — |
| [SRC-2C8F288796-L000057](../../web/workspace.html#L57) | 57 | `".stat:after{content:\"\";position:absolute;width:85px;height:85px;border-radius:50%;background:var(--glow,rgba(105,230,209,.1));left:-23px;top:-29px;filter:blur(8px)}.stat.glow-teal:after{background:rgba(105,230,209,.13)}.stat.glow-blue:after{background:rgba(121,207,255,.13)}.stat.glow-amber:after{background:rgba(243,199,124,.13)}.stat.glow-violet:after{background:rgba(156,145,255,.14)}"` | — |
| [SRC-2C8F288796-L000058](../../web/workspace.html#L58) | 58 | `".stat-label{color:var(--muted);font-size:10px;position:relative;z-index:1}"` | — |
| [SRC-2C8F288796-L000059](../../web/workspace.html#L59) | 59 | `".stat-value{font-size:28px;font-weight:900;line-height:1.3;margin:7px 0 3px;position:relative;z-index:1;font-variant-numeric:tabular-nums}"` | — |
| [SRC-2C8F288796-L000060](../../web/workspace.html#L60) | 60 | `".stat-note{color:#7f96b3;font-size:9px;position:relative;z-index:1}"` | — |
| [SRC-2C8F288796-L000061](../../web/workspace.html#L61) | 61 | `".content-grid{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(270px,.8fr);gap:14px}"` | — |
| [SRC-2C8F288796-L000062](../../web/workspace.html#L62) | 62 | `".panel{padding:19px;min-width:0}"` | — |
| [SRC-2C8F288796-L000063](../../web/workspace.html#L63) | 63 | `".panel-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:14px}"` | — |
| [SRC-2C8F288796-L000064](../../web/workspace.html#L64) | 64 | `".panel-head h2{font-size:14px;margin:0}.panel-head p{margin:5px 0 0;color:var(--muted);font-size:10px;line-height:1.7}"` | — |
| [SRC-2C8F288796-L000065](../../web/workspace.html#L65) | 65 | `".subtle{font-size:10px;color:var(--muted)}"` | — |
| [SRC-2C8F288796-L000066](../../web/workspace.html#L66) | 66 | `".signal-list{display:grid;gap:9px}"` | — |
| [SRC-2C8F288796-L000067](../../web/workspace.html#L67) | 67 | `".signal-card{border:1px solid rgba(145,174,211,.14);border-radius:15px;background:rgba(8,17,31,.56);padding:14px;display:grid;gap:9px}"` | — |
| [SRC-2C8F288796-L000068](../../web/workspace.html#L68) | 68 | `".signal-top{display:flex;align-items:flex-start;justify-content:space-between;gap:10px}"` | — |
| [SRC-2C8F288796-L000069](../../web/workspace.html#L69) | 69 | `".signal-text{font-size:12px;line-height:1.8;white-space:pre-wrap;overflow-wrap:anywhere;margin:0;color:#e0eafa}"` | — |
| [SRC-2C8F288796-L000070](../../web/workspace.html#L70) | 70 | `".signal-meta{display:flex;flex-wrap:wrap;gap:6px}"` | — |
| [SRC-2C8F288796-L000071](../../web/workspace.html#L71) | 71 | `".tag{display:inline-flex;align-items:center;border:1px solid var(--line);border-radius:99px;padding:4px 8px;font-size:9px;color:#afc0d6;background:rgba(23,38,61,.55)}"` | — |
| [SRC-2C8F288796-L000072](../../web/workspace.html#L72) | 72 | `".tag.teal{color:#a9f6e8;border-color:rgba(105,230,209,.23);background:rgba(32,112,104,.15)}"` | — |
| [SRC-2C8F288796-L000073](../../web/workspace.html#L73) | 73 | `".tag.amber{color:#f7d99f;border-color:rgba(243,199,124,.22);background:rgba(135,93,32,.12)}"` | — |
| [SRC-2C8F288796-L000074](../../web/workspace.html#L74) | 74 | `".tag.red{color:#ffb0b6;border-color:rgba(255,135,148,.22);background:rgba(130,40,52,.12)}"` | — |
| [SRC-2C8F288796-L000075](../../web/workspace.html#L75) | 75 | `".signal-actions{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap}"` | — |
| [SRC-2C8F288796-L000076](../../web/workspace.html#L76) | 76 | `".small-button{border:1px solid var(--line);border-radius:10px;background:rgba(20,34,54,.8);color:#d6e3f4;padding:7px 10px;font-size:10px;font-weight:800}"` | — |
| [SRC-2C8F288796-L000077](../../web/workspace.html#L77) | 77 | `".small-button:hover{border-color:rgba(105,230,209,.45)}"` | — |
| [SRC-2C8F288796-L000078](../../web/workspace.html#L78) | 78 | `".empty{border:1px dashed rgba(145,174,211,.24);border-radius:15px;padding:27px 16px;text-align:center;color:var(--muted);font-size:11px;line-height:1.9}"` | — |
| [SRC-2C8F288796-L000079](../../web/workspace.html#L79) | 79 | `".empty strong{display:block;color:#dce8f7;font-size:13px;margin-bottom:6px}"` | — |
| [SRC-2C8F288796-L000080](../../web/workspace.html#L80) | 80 | `".mini-bars{display:grid;gap:13px}"` | — |
| [SRC-2C8F288796-L000081](../../web/workspace.html#L81) | 81 | `".bar-row{display:grid;grid-template-columns:82px minmax(0,1fr) 26px;align-items:center;gap:8px;font-size:10px;color:var(--muted)}"` | — |
| [SRC-2C8F288796-L000082](../../web/workspace.html#L82) | 82 | `".bar-track{height:8px;border-radius:99px;background:rgba(132,156,190,.12);overflow:hidden}"` | — |
| [SRC-2C8F288796-L000083](../../web/workspace.html#L83) | 83 | `".bar-fill{height:100%;width:0;border-radius:99px;background:linear-gradient(90deg,var(--teal),var(--cyan))}.bar-fill.w-0{width:0%}.bar-fill.w-5{width:5%}.bar-fill.w-10{width:10%}.bar-fill.w-15{width:15%}.bar-fill.w-20{width:20%}.bar-fill.w-25{width:25%}.bar-fill.w-30{width:30%}.bar-fill.w-35{width:35%}.bar-fill.w-40{width:40%}.bar-fill.w-45{width:45%}.bar-fill.w-50{width:50%}.bar-fill.w-55{width:55%}.bar-fill.w-60{width:60%}.bar-fill.w-65{width:65%}.bar-fill.w-70{width:70%}.bar-fill.w-75{width:75%}.bar-fill.w-80{width:80%}.bar-fill.w-85{width:85%}.bar-fill.w-90{width:90%}.bar-fill.w-95{width:95%}.bar-fill.w-100{width:100%}"` | — |
| [SRC-2C8F288796-L000084](../../web/workspace.html#L84) | 84 | `".notice{padding:13px;border-radius:14px;border:1px solid rgba(243,199,124,.2);background:rgba(116,79,29,.1);color:#efd7a9;font-size:10px;line-height:1.9}"` | — |
| [SRC-2C8F288796-L000085](../../web/workspace.html#L85) | 85 | `".toolbar{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:12px 0 15px}"` | — |
| [SRC-2C8F288796-L000086](../../web/workspace.html#L86) | 86 | `".field{display:grid;gap:6px;margin:11px 0}"` | — |
| [SRC-2C8F288796-L000087](../../web/workspace.html#L87) | 87 | `".field label{font-size:10px;color:#c0d0e5}"` | — |
| [SRC-2C8F288796-L000088](../../web/workspace.html#L88) | 88 | `"input,textarea,select{width:100%;border:1px solid rgba(145,174,211,.22);border-radius:11px;background:rgba(7,16,29,.78);color:var(--text);padding:10px 12px;font-size:11px;min-width:0}"` | — |
| [SRC-2C8F288796-L000089](../../web/workspace.html#L89) | 89 | `"textarea{min-height:104px;resize:vertical;line-height:1.8}"` | — |
| [SRC-2C8F288796-L000090](../../web/workspace.html#L90) | 90 | `"input::placeholder,textarea::placeholder{color:#7085a2}"` | — |
| [SRC-2C8F288796-L000091](../../web/workspace.html#L91) | 91 | `".form-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}"` | — |
| [SRC-2C8F288796-L000092](../../web/workspace.html#L92) | 92 | `".form-actions{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:12px}"` | — |
| [SRC-2C8F288796-L000093](../../web/workspace.html#L93) | 93 | `".analysis-result{border:1px solid rgba(105,230,209,.2);background:rgba(20,88,82,.12);padding:13px;border-radius:14px;margin-top:12px}"` | — |
| [SRC-2C8F288796-L000094](../../web/workspace.html#L94) | 94 | `".analysis-score{font-size:24px;font-weight:900;color:var(--teal)}"` | — |
| [SRC-2C8F288796-L000095](../../web/workspace.html#L95) | 95 | `".disclaimer{font-size:9px;color:#b0bdce;line-height:1.8;margin:7px 0 0}"` | — |
| [SRC-2C8F288796-L000096](../../web/workspace.html#L96) | 96 | `".pipeline{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}"` | — |
| [SRC-2C8F288796-L000097](../../web/workspace.html#L97) | 97 | `".pipeline-col{padding:13px;border:1px solid var(--line);border-radius:15px;background:rgba(9,18,32,.38);min-width:0}"` | — |
| [SRC-2C8F288796-L000098](../../web/workspace.html#L98) | 98 | `".pipeline-col h3{font-size:11px;margin:0 0 10px;display:flex;justify-content:space-between;gap:8px}"` | — |
| [SRC-2C8F288796-L000099](../../web/workspace.html#L99) | 99 | `".pipeline-item{display:block;width:100%;text-align:right;padding:10px;margin-top:8px;border-radius:11px;background:rgba(21,35,55,.75);border:1px solid rgba(145,174,211,.12);color:#e0eafa;font-size:10px;line-height:1.7;cursor:pointer;overflow-wrap:anywhere}"` | — |
| [SRC-2C8F288796-L000100](../../web/workspace.html#L100) | 100 | `".pipeline-item:hover{border-color:rgba(105,230,209,.35)}"` | — |
| [SRC-2C8F288796-L000101](../../web/workspace.html#L101) | 101 | `".detail{position:fixed;z-index:20;inset:0;background:rgba(2,8,16,.7);display:none;justify-content:flex-start}"` | — |
| [SRC-2C8F288796-L000102](../../web/workspace.html#L102) | 102 | `".detail.open{display:flex}"` | — |
| [SRC-2C8F288796-L000103](../../web/workspace.html#L103) | 103 | `".detail-panel{width:min(540px,100%);height:100%;overflow:auto;padding:22px;background:#0b1627;border-left:1px solid var(--line);box-shadow:20px 0 70px rgba(0,0,0,.35)}"` | — |
| [SRC-2C8F288796-L000104](../../web/workspace.html#L104) | 104 | `".detail-head{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:16px}"` | — |
| [SRC-2C8F288796-L000105](../../web/workspace.html#L105) | 105 | `".detail-head h2{font-size:16px;margin:0}"` | — |
| [SRC-2C8F288796-L000106](../../web/workspace.html#L106) | 106 | `".detail-body{font-size:11px;line-height:1.9;color:#d7e4f4;overflow-wrap:anywhere}"` | — |
| [SRC-2C8F288796-L000107](../../web/workspace.html#L107) | 107 | `".detail-body h3{font-size:11px;color:var(--teal);margin:17px 0 7px}"` | — |
| [SRC-2C8F288796-L000108](../../web/workspace.html#L108) | 108 | `".detail-body p{white-space:pre-wrap}"` | — |
| [SRC-2C8F288796-L000109](../../web/workspace.html#L109) | 109 | `".detail-body a{overflow-wrap:anywhere}"` | — |
| [SRC-2C8F288796-L000110](../../web/workspace.html#L110) | 110 | `".module-placeholder{padding:30px;max-width:780px}"` | — |
| [SRC-2C8F288796-L000111](../../web/workspace.html#L111) | 111 | `".module-placeholder h2{font-size:18px;margin:8px 0}"` | — |
| [SRC-2C8F288796-L000112](../../web/workspace.html#L112) | 112 | `".module-placeholder p{font-size:11px;line-height:2;color:var(--muted);max-width:650px}"` | — |
| [SRC-2C8F288796-L000113](../../web/workspace.html#L113) | 113 | `".module-list{display:grid;gap:8px;margin-top:18px}"` | — |
| [SRC-2C8F288796-L000114](../../web/workspace.html#L114) | 114 | `".module-step{padding:11px 13px;border-radius:12px;background:rgba(10,20,36,.7);border:1px solid var(--line);font-size:10px;color:#b9cbe0}"` | — |
| [SRC-2C8F288796-L000115](../../web/workspace.html#L115) | 115 | `".footer{border-top:1px solid var(--line);margin-top:24px;padding:15px 0 0;color:#748aa6;font-size:9px;line-height:1.9}"` | — |
| [SRC-2C8F288796-L000116](../../web/workspace.html#L116) | 116 | `".auth-gate{position:fixed;z-index:50;inset:0;display:none;place-items:center;padding:20px;background:rgba(3,9,17,.88);backdrop-filter:blur(18px)}"` | — |
| [SRC-2C8F288796-L000117](../../web/workspace.html#L117) | 117 | `".auth-gate.open{display:grid}"` | — |
| [SRC-2C8F288796-L000118](../../web/workspace.html#L118) | 118 | `".auth-card{width:min(430px,100%);padding:26px}"` | — |
| [SRC-2C8F288796-L000119](../../web/workspace.html#L119) | 119 | `".auth-card h2{font-size:20px;margin:9px 0}"` | — |
| [SRC-2C8F288796-L000120](../../web/workspace.html#L120) | 120 | `".auth-card p{font-size:11px;color:var(--muted);line-height:1.9}"` | — |
| [SRC-2C8F288796-L000121](../../web/workspace.html#L121) | 121 | `".auth-error{color:var(--danger);font-size:10px;min-height:18px;margin-top:9px}"` | — |
| [SRC-2C8F288796-L000122](../../web/workspace.html#L122) | 122 | `".mobile-brand{display:none}"` | — |
| [SRC-2C8F288796-L000123](../../web/workspace.html#L123) | 123 | `"@media(max-width:1100px){.app{grid-template-columns:220px minmax(0,1fr)}.sidebar{padding-inline:12px}.content-grid{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,minmax(0,1fr))}}"` | — |
| [SRC-2C8F288796-L000124](../../web/workspace.html#L124) | 124 | `"@media(max-width:760px){.app{display:block}.sidebar{position:relative;top:auto;height:auto;padding:12px 14px;border-left:0;border-bottom:1px solid var(--line);gap:10px}.brand{padding:0 3px 10px}.nav{display:flex;flex-direction:row;overflow:auto;padding-bottom:3px}.nav button{width:auto;min-width:max-content;padding:9px 11px}.nav-status,.workspace-label,.side-bottom,.side-links{display:none}.main{padding:13px 13px 26px}.topbar{padding-bottom:12px}.page-head{align-items:flex-start;flex-direction:column;margin:19px 0 14px}.stats{gap:8px}.stat{padding:13px}.stat-value{font-size:23px}.panel{padding:14px}.form-grid{grid-template-columns:1fr}.pipeline{grid-template-columns:1fr}.role-pill{display:none}}"` | — |
| [SRC-2C8F288796-L000125](../../web/workspace.html#L125) | 125 | `"@media(max-width:420px){.stats{grid-template-columns:1fr 1fr}.top-actions{gap:6px}.button{padding:9px 10px}.page-head h1{font-size:24px}.bar-row{grid-template-columns:72px minmax(0,1fr) 22px}}"` | — |
| [SRC-2C8F288796-L000126](../../web/workspace.html#L126) | 126 | `""` | — |
| [SRC-2C8F288796-L000127](../../web/workspace.html#L127) | 127 | `"/* Approved direction: Neon Command — production workspace adaptation */"` | — |
| [SRC-2C8F288796-L000128](../../web/workspace.html#L128) | 128 | `":root{--bg:#070d16;--panel:rgba(12,25,38,.88);--panel-2:rgba(9,20,32,.96);--line:rgba(74,216,255,.17);--text:#e7f7ff;--muted:#86a5b8;--teal:#52dfff;--cyan:#71eaff;--violet:#8d9bff;--coral:#ff9caa;--amber:#f4cc83;--green:#78e4b0;--danger:#ff899b;--radius:16px}"` | — |
| [SRC-2C8F288796-L000129](../../web/workspace.html#L129) | 129 | `"body{background:radial-gradient(ellipse at 50% -20%,rgba(21,54,77,.8),transparent 55%),radial-gradient(ellipse at 100% 25%,rgba(34,39,92,.18),transparent 35%),#070d16}"` | — |
| [SRC-2C8F288796-L000130](../../web/workspace.html#L130) | 130 | `".sidebar{background:rgba(5,13,22,.86);border-left-color:rgba(74,216,255,.18);backdrop-filter:blur(26px)}"` | — |
| [SRC-2C8F288796-L000131](../../web/workspace.html#L131) | 131 | `".logo{background:linear-gradient(135deg,#52dfff,#8d9bff);box-shadow:0 0 28px rgba(82,223,255,.18)}"` | — |
| [SRC-2C8F288796-L000132](../../web/workspace.html#L132) | 132 | `".brand-name{letter-spacing:.04em}"` | — |
| [SRC-2C8F288796-L000133](../../web/workspace.html#L133) | 133 | `".nav button{border-radius:10px}"` | — |
| [SRC-2C8F288796-L000134](../../web/workspace.html#L134) | 134 | `".nav button.active{background:linear-gradient(100deg,rgba(67,223,255,.13),rgba(91,113,255,.10));border-color:rgba(67,223,255,.28);box-shadow:inset 0 1px rgba(255,255,255,.035)}"` | — |
| [SRC-2C8F288796-L000135](../../web/workspace.html#L135) | 135 | `".nav-icon{color:#71eaff}"` | — |
| [SRC-2C8F288796-L000136](../../web/workspace.html#L136) | 136 | `".connection,.role-pill,.status-pill,.button,.small-button{border-color:rgba(57,207,255,.18);background:rgba(10,27,40,.78)}"` | — |
| [SRC-2C8F288796-L000137](../../web/workspace.html#L137) | 137 | `".button.primary{background:linear-gradient(105deg,#52dfff,#a1b4ff);color:#061421;box-shadow:0 6px 24px rgba(82,223,255,.12)}"` | — |
| [SRC-2C8F288796-L000138](../../web/workspace.html#L138) | 138 | `".glass{background:linear-gradient(145deg,rgba(16,35,52,.94),rgba(8,20,32,.92));border-color:rgba(74,216,255,.18);box-shadow:inset 0 1px rgba(255,255,255,.035),0 16px 42px rgba(0,0,0,.32);backdrop-filter:blur(22px)}"` | — |
| [SRC-2C8F288796-L000139](../../web/workspace.html#L139) | 139 | `".stat{border-radius:15px;background:linear-gradient(145deg,rgba(16,35,52,.96),rgba(9,21,33,.94))}"` | — |
| [SRC-2C8F288796-L000140](../../web/workspace.html#L140) | 140 | `".stat:after{background:rgba(82,223,255,.13)}"` | — |
| [SRC-2C8F288796-L000141](../../web/workspace.html#L141) | 141 | `".stat.glow-teal:after{background:rgba(82,223,255,.15)}"` | — |
| [SRC-2C8F288796-L000142](../../web/workspace.html#L142) | 142 | `".stat.glow-blue:after{background:rgba(113,234,255,.13)}"` | — |
| [SRC-2C8F288796-L000143](../../web/workspace.html#L143) | 143 | `".stat.glow-amber:after{background:rgba(244,204,131,.13)}"` | — |
| [SRC-2C8F288796-L000144](../../web/workspace.html#L144) | 144 | `".stat.glow-violet:after{background:rgba(141,155,255,.15)}"` | — |
| [SRC-2C8F288796-L000145](../../web/workspace.html#L145) | 145 | `".stat-value{color:#71eaff;text-shadow:0 0 20px rgba(82,223,255,.10)}"` | — |
| [SRC-2C8F288796-L000146](../../web/workspace.html#L146) | 146 | `".signal-card,.pipeline-col{background:rgba(5,16,27,.68);border-color:rgba(57,207,255,.14);border-radius:12px}"` | — |
| [SRC-2C8F288796-L000147](../../web/workspace.html#L147) | 147 | `".signal-card{box-shadow:inset 0 1px rgba(255,255,255,.025)}"` | — |
| [SRC-2C8F288796-L000148](../../web/workspace.html#L148) | 148 | `".tag{border-radius:8px;border-color:rgba(57,207,255,.19);background:rgba(10,29,43,.65)}"` | — |
| [SRC-2C8F288796-L000149](../../web/workspace.html#L149) | 149 | `".tag.teal{color:#91f0ff;border-color:rgba(82,223,255,.28);background:rgba(28,113,143,.14)}"` | — |
| [SRC-2C8F288796-L000150](../../web/workspace.html#L150) | 150 | `".bar-fill{background:linear-gradient(90deg,#52dfff,#8d9bff);box-shadow:0 0 12px rgba(82,223,255,.2)}"` | — |
| [SRC-2C8F288796-L000151](../../web/workspace.html#L151) | 151 | `"input,textarea,select{background:rgba(5,15,25,.88);border-color:rgba(57,207,255,.2)}"` | — |
| [SRC-2C8F288796-L000152](../../web/workspace.html#L152) | 152 | `".analysis-result{border-color:rgba(82,223,255,.22);background:rgba(22,100,124,.13)}"` | — |
| [SRC-2C8F288796-L000153](../../web/workspace.html#L153) | 153 | `".pipeline-item{background:rgba(8,23,35,.9);border-color:rgba(57,207,255,.14);border-radius:10px}"` | — |
| [SRC-2C8F288796-L000154](../../web/workspace.html#L154) | 154 | `".detail-panel{background:#081522;border-left-color:rgba(57,207,255,.2)}"` | — |
| [SRC-2C8F288796-L000155](../../web/workspace.html#L155) | 155 | `".auth-gate{background:rgba(2,8,15,.9)}"` | — |
| [SRC-2C8F288796-L000156](../../web/workspace.html#L156) | 156 | `".auth-card{background:linear-gradient(145deg,rgba(16,35,52,.98),rgba(8,20,32,.98));border-color:rgba(74,216,255,.22)}"` | — |
| [SRC-2C8F288796-L000157](../../web/workspace.html#L157) | 157 | `".profile-panel{margin-bottom:14px}"` | — |
| [SRC-2C8F288796-L000158](../../web/workspace.html#L158) | 158 | `".profile-note,.discovery-note{font-size:11px;line-height:1.9;color:var(--muted)}"` | — |
| [SRC-2C8F288796-L000159](../../web/workspace.html#L159) | 159 | `".discovery-history,.query-list,.discovery-source-meta{display:flex;flex-wrap:wrap;gap:7px;margin:10px 0}"` | — |
| [SRC-2C8F288796-L000160](../../web/workspace.html#L160) | 160 | `".discovery-source{border:1px solid var(--line);border-radius:12px;background:rgba(5,16,27,.68);padding:14px;display:grid;gap:9px}"` | — |
| [SRC-2C8F288796-L000161](../../web/workspace.html#L161) | 161 | `".discovery-source.qualified{border-color:rgba(82,223,255,.35);box-shadow:inset 0 0 25px rgba(82,223,255,.035)}"` | — |
| [SRC-2C8F288796-L000162](../../web/workspace.html#L162) | 162 | `".discovery-source h3{font-size:14px;line-height:1.7;margin:0;color:var(--text)}"` | — |
| [SRC-2C8F288796-L000163](../../web/workspace.html#L163) | 163 | `".discovery-source p{font-size:12px;line-height:1.9;margin:0;color:#c5d5e7;white-space:pre-wrap;overflow-wrap:anywhere}"` | — |
| [SRC-2C8F288796-L000164](../../web/workspace.html#L164) | 164 | `".discovery-source a{font-size:11px;color:var(--cyan);overflow-wrap:anywhere}"` | — |
| [SRC-2C8F288796-L000165](../../web/workspace.html#L165) | 165 | `".query-list .tag{max-width:100%;white-space:normal;overflow-wrap:anywhere;line-height:1.7}"` | — |
| [SRC-2C8F288796-L000166](../../web/workspace.html#L166) | 166 | `".consent-row{display:flex;align-items:flex-start;gap:10px;padding:12px;border:1px solid var(--line);border-radius:10px;background:rgba(5,16,27,.5);font-size:11px;line-height:1.8}"` | — |
| [SRC-2C8F288796-L000167](../../web/workspace.html#L167) | 167 | `".consent-row input{width:18px;min-width:18px;height:18px;margin:2px 0 0;accent-color:#52dfff}"` | — |
| [SRC-2C8F288796-L000168](../../web/workspace.html#L168) | 168 | `"@media(max-width:760px){"` | — |
| [SRC-2C8F288796-L000169](../../web/workspace.html#L169) | 169 | `" .sidebar{background:rgba(5,13,22,.94);border-bottom-color:rgba(57,207,255,.18)}"` | — |
| [SRC-2C8F288796-L000170](../../web/workspace.html#L170) | 170 | `" .nav{scrollbar-width:thin;scrollbar-color:rgba(82,223,255,.28) transparent}"` | — |
| [SRC-2C8F288796-L000171](../../web/workspace.html#L171) | 171 | `" .nav button{min-height:42px}"` | — |
| [SRC-2C8F288796-L000172](../../web/workspace.html#L172) | 172 | `" .main{padding-inline:12px}"` | — |
| [SRC-2C8F288796-L000173](../../web/workspace.html#L173) | 173 | `" .topbar{align-items:flex-start}"` | — |
| [SRC-2C8F288796-L000174](../../web/workspace.html#L174) | 174 | `" .top-actions{max-width:100%}"` | — |
| [SRC-2C8F288796-L000175](../../web/workspace.html#L175) | 175 | `" .button,.small-button{min-height:40px}"` | — |
| [SRC-2C8F288796-L000176](../../web/workspace.html#L176) | 176 | `" .glass{backdrop-filter:blur(16px)}"` | — |
| [SRC-2C8F288796-L000177](../../web/workspace.html#L177) | 177 | `"}"` | — |
| [SRC-2C8F288796-L000178](../../web/workspace.html#L178) | 178 | `"@media(max-width:420px){"` | — |
| [SRC-2C8F288796-L000179](../../web/workspace.html#L179) | 179 | `" .stat{min-height:100px}"` | — |
| [SRC-2C8F288796-L000180](../../web/workspace.html#L180) | 180 | `" .stat-value{font-size:22px}"` | — |
| [SRC-2C8F288796-L000181](../../web/workspace.html#L181) | 181 | `" .signal-top{flex-direction:column}"` | — |
| [SRC-2C8F288796-L000182](../../web/workspace.html#L182) | 182 | `" .signal-actions{align-items:stretch}"` | — |
| [SRC-2C8F288796-L000183](../../web/workspace.html#L183) | 183 | `" .signal-actions .small-button{flex:1}"` | — |
| [SRC-2C8F288796-L000184](../../web/workspace.html#L184) | 184 | `"}"` | — |
| [SRC-2C8F288796-L000185](../../web/workspace.html#L185) | 185 | `"@media(prefers-reduced-motion:reduce){"` | — |
| [SRC-2C8F288796-L000186](../../web/workspace.html#L186) | 186 | `" *,*::before,*::after{scroll-behavior:auto!important;animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}"` | — |
| [SRC-2C8F288796-L000187](../../web/workspace.html#L187) | 187 | `"}"` | — |
| [SRC-2C8F288796-L000188](../../web/workspace.html#L188) | 188 | `"@media(forced-colors:active){"` | — |
| [SRC-2C8F288796-L000189](../../web/workspace.html#L189) | 189 | `" .glass,.stat,.signal-card,.pipeline-col,.button,.small-button{border:1px solid CanvasText;backdrop-filter:none}"` | — |
| [SRC-2C8F288796-L000190](../../web/workspace.html#L190) | 190 | `" .nav button.active{outline:2px solid Highlight}"` | — |
| [SRC-2C8F288796-L000191](../../web/workspace.html#L191) | 191 | `"}"` | — |
| [SRC-2C8F288796-L000192](../../web/workspace.html#L192) | 192 | `""` | — |
| [SRC-2C8F288796-L000193](../../web/workspace.html#L193) | 193 | `"/* Responsive glass performance indicators */"` | — |
| [SRC-2C8F288796-L000194](../../web/workspace.html#L194) | 194 | `".side-links{display:flex;gap:8px;flex-wrap:wrap;padding:0 4px;align-items:center}"` | — |
| [SRC-2C8F288796-L000195](../../web/workspace.html#L195) | 195 | `".side-links a,.side-link-button{font-size:10px;color:#92a8c4}"` | — |
| [SRC-2C8F288796-L000196](../../web/workspace.html#L196) | 196 | `".side-link-button{border:0;background:transparent;padding:4px;cursor:pointer;font:inherit}"` | — |
| [SRC-2C8F288796-L000197](../../web/workspace.html#L197) | 197 | `".side-link-button:hover,.side-links a:hover{color:var(--teal);text-decoration:underline}"` | — |
| [SRC-2C8F288796-L000198](../../web/workspace.html#L198) | 198 | `".indicator-hero{display:flex;align-items:center;gap:24px;padding:22px;margin-bottom:14px;min-width:0}"` | — |
| [SRC-2C8F288796-L000199](../../web/workspace.html#L199) | 199 | `".indicator-ring{width:154px;height:154px;flex:0 0 154px;border-radius:50%;display:grid;place-items:center;padding:10px;box-shadow:0 0 32px rgba(82,223,255,.08)}"` | — |
| [SRC-2C8F288796-L000200](../../web/workspace.html#L200) | 200 | `".indicator-ring-inner{width:100%;height:100%;border:1px solid var(--line);border-radius:50%;background:linear-gradient(145deg,#102438,#091522);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}"` | — |
| [SRC-2C8F288796-L000201](../../web/workspace.html#L201) | 201 | `".indicator-ring-value{font-size:31px;font-weight:900;color:var(--green);font-variant-numeric:tabular-nums}"` | — |
| [SRC-2C8F288796-L000202](../../web/workspace.html#L202) | 202 | `".indicator-ring-caption{font-size:10px;color:var(--muted)}"` | — |
| [SRC-2C8F288796-L000203](../../web/workspace.html#L203) | 203 | `".indicator-hero-copy{min-width:0}"` | — |
| [SRC-2C8F288796-L000204](../../web/workspace.html#L204) | 204 | `".indicator-hero-copy h2{font-size:19px;margin:8px 0}"` | — |
| [SRC-2C8F288796-L000205](../../web/workspace.html#L205) | 205 | `".indicator-hero-copy p{font-size:11px;line-height:1.9;color:var(--muted);max-width:700px;margin:0}"` | — |
| [SRC-2C8F288796-L000206](../../web/workspace.html#L206) | 206 | `".indicator-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-bottom:14px}"` | — |
| [SRC-2C8F288796-L000207](../../web/workspace.html#L207) | 207 | `".indicator-layout{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(260px,.8fr);gap:14px}"` | — |
| [SRC-2C8F288796-L000208](../../web/workspace.html#L208) | 208 | `".indicator-list{display:grid;gap:13px}"` | — |
| [SRC-2C8F288796-L000209](../../web/workspace.html#L209) | 209 | `".indicator-row{display:grid;grid-template-columns:112px minmax(0,1fr) 34px;gap:10px;align-items:center;font-size:11px;color:var(--muted)}"` | — |
| [SRC-2C8F288796-L000210](../../web/workspace.html#L210) | 210 | `".indicator-track{height:10px;border-radius:99px;background:rgba(132,156,190,.12);overflow:hidden}"` | — |
| [SRC-2C8F288796-L000211](../../web/workspace.html#L211) | 211 | `".indicator-fill{height:100%;min-width:0;border-radius:99px}"` | — |
| [SRC-2C8F288796-L000212](../../web/workspace.html#L212) | 212 | `".indicator-fill.cyan{background:linear-gradient(90deg,#45cfe9,#77dff0)}"` | — |
| [SRC-2C8F288796-L000213](../../web/workspace.html#L213) | 213 | `".indicator-fill.green{background:linear-gradient(90deg,#3bbd91,#80e3b5)}"` | — |
| [SRC-2C8F288796-L000214](../../web/workspace.html#L214) | 214 | `".indicator-fill.red{background:linear-gradient(90deg,#d95d77,#ff91a2)}"` | — |
| [SRC-2C8F288796-L000215](../../web/workspace.html#L215) | 215 | `".indicator-fill.muted{background:linear-gradient(90deg,#647b92,#9aabba)}"` | — |
| [SRC-2C8F288796-L000216](../../web/workspace.html#L216) | 216 | `".indicator-summary{display:grid;grid-template-columns:1fr 1fr;gap:9px}"` | — |
| [SRC-2C8F288796-L000217](../../web/workspace.html#L217) | 217 | `".indicator-note{padding:12px;border:1px solid var(--line);border-radius:12px;background:rgba(5,16,27,.5);font-size:10px;line-height:1.8;color:var(--muted)}"` | — |
| [SRC-2C8F288796-L000218](../../web/workspace.html#L218) | 218 | `".indicator-note-value{display:block;margin-top:5px;color:var(--text);font-size:21px;font-weight:850;font-variant-numeric:tabular-nums}"` | — |
| [SRC-2C8F288796-L000219](../../web/workspace.html#L219) | 219 | `"@media(max-width:1100px){.indicator-layout{grid-template-columns:1fr}.indicator-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}"` | — |
| [SRC-2C8F288796-L000220](../../web/workspace.html#L220) | 220 | `"@media(max-width:760px){"` | — |
| [SRC-2C8F288796-L000221](../../web/workspace.html#L221) | 221 | `" .side-bottom{display:block;margin-top:0}"` | — |
| [SRC-2C8F288796-L000222](../../web/workspace.html#L222) | 222 | `" .side-bottom .connection{display:none}"` | — |
| [SRC-2C8F288796-L000223](../../web/workspace.html#L223) | 223 | `" .side-links{display:flex}"` | — |
| [SRC-2C8F288796-L000224](../../web/workspace.html#L224) | 224 | `" .indicator-hero{gap:15px;padding:16px}"` | — |
| [SRC-2C8F288796-L000225](../../web/workspace.html#L225) | 225 | `" .indicator-ring{width:126px;height:126px;flex-basis:126px}"` | — |
| [SRC-2C8F288796-L000226](../../web/workspace.html#L226) | 226 | `" .indicator-ring-value{font-size:26px}"` | — |
| [SRC-2C8F288796-L000227](../../web/workspace.html#L227) | 227 | `" .indicator-hero-copy h2{font-size:16px}"` | — |
| [SRC-2C8F288796-L000228](../../web/workspace.html#L228) | 228 | `"}"` | — |
| [SRC-2C8F288796-L000229](../../web/workspace.html#L229) | 229 | `"@media(max-width:520px){"` | — |
| [SRC-2C8F288796-L000230](../../web/workspace.html#L230) | 230 | `" .indicator-hero{align-items:flex-start;flex-direction:column}"` | — |
| [SRC-2C8F288796-L000231](../../web/workspace.html#L231) | 231 | `" .indicator-ring{width:112px;height:112px;flex-basis:112px;align-self:center}"` | — |
| [SRC-2C8F288796-L000232](../../web/workspace.html#L232) | 232 | `" .indicator-ring-value{font-size:24px}"` | — |
| [SRC-2C8F288796-L000233](../../web/workspace.html#L233) | 233 | `" .indicator-grid{gap:8px}"` | — |
| [SRC-2C8F288796-L000234](../../web/workspace.html#L234) | 234 | `" .indicator-grid .stat{min-height:94px;padding:12px}"` | — |
| [SRC-2C8F288796-L000235](../../web/workspace.html#L235) | 235 | `" .indicator-row{grid-template-columns:86px minmax(0,1fr) 26px;gap:7px;font-size:10px}"` | — |
| [SRC-2C8F288796-L000236](../../web/workspace.html#L236) | 236 | `" .indicator-summary{grid-template-columns:1fr 1fr}"` | — |
| [SRC-2C8F288796-L000237](../../web/workspace.html#L237) | 237 | `"}"` | — |
| [SRC-2C8F288796-L000238](../../web/workspace.html#L238) | 238 | `"@media(max-width:360px){.indicator-summary{grid-template-columns:1fr}.indicator-row{grid-template-columns:76px minmax(0,1fr) 24px}}"` | — |
| [SRC-2C8F288796-L000239](../../web/workspace.html#L239) | 239 | `""` | — |
| [SRC-2C8F288796-L000240](../../web/workspace.html#L240) | 240 | `".chat-panel{display:flex;flex-direction:column;gap:12px}.chat-modes{display:flex;gap:8px;flex-wrap:wrap}.chat-mode-active{border-color:var(--teal);color:#fff}"` | — |
| [SRC-2C8F288796-L000241](../../web/workspace.html#L241) | 241 | `".chat-list{display:flex;flex-direction:column;gap:12px;min-height:320px;max-height:calc(100vh - 430px);overflow:auto;padding:4px}"` | — |
| [SRC-2C8F288796-L000242](../../web/workspace.html#L242) | 242 | `".chat-empty{color:var(--muted);font-size:12px;line-height:1.9;text-align:center;margin:auto;padding:24px;border:1px dashed rgba(145,174,211,.28);border-radius:14px}"` | — |
| [SRC-2C8F288796-L000243](../../web/workspace.html#L243) | 243 | `".chat-msg{max-width:88%;padding:12px 14px;border-radius:14px;border:1px solid rgba(145,174,211,.22);background:rgba(7,16,29,.62)}.chat-user{align-self:flex-start;border-color:rgba(57,207,255,.35)}.chat-assistant{align-self:flex-end}"` | — |
| [SRC-2C8F288796-L000244](../../web/workspace.html#L244) | 244 | `".chat-who{font-size:10px;color:var(--muted);margin-bottom:6px}.chat-text{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px;line-height:1.9}"` | — |
| [SRC-2C8F288796-L000245](../../web/workspace.html#L245) | 245 | `".chat-sources{margin:6px 0 0;padding:0 18px;font-size:11px;line-height:1.9}.chat-sources a{color:var(--teal)}.chat-citation{color:var(--teal);text-decoration:underline;text-underline-offset:2px}.chat-note{margin-top:8px;font-size:10px;color:var(--muted)}"` | — |
| [SRC-2C8F288796-L000246](../../web/workspace.html#L246) | 246 | `".chat-form{display:flex;gap:9px;align-items:flex-end}.chat-form textarea{flex:1;min-height:52px;max-height:160px}"` | — |
| [SRC-2C8F288796-L000247](../../web/workspace.html#L247) | 247 | `"@media(max-width:740px){.chat-msg{max-width:100%}.chat-list{max-height:none}}"` | — |
| [SRC-2C8F288796-L000248](../../web/workspace.html#L248) | 248 | `"</style>"` | — |
| [SRC-2C8F288796-L000249](../../web/workspace.html#L249) | 249 | `"</head>"` | — |
| [SRC-2C8F288796-L000250](../../web/workspace.html#L250) | 250 | `"<body>"` | — |
| [SRC-2C8F288796-L000251](../../web/workspace.html#L251) | 251 | `"<div class=\"app\">"` | — |
| [SRC-2C8F288796-L000252](../../web/workspace.html#L252) | 252 | `"<aside class=\"sidebar\">"` | — |
| [SRC-2C8F288796-L000253](../../web/workspace.html#L253) | 253 | `"  <div class=\"brand\"><div class=\"logo\">O</div><div><div class=\"brand-name\">Omarai</div><div class=\"brand-sub\">ذكاء المبيعات واكتساب العملاء</div></div></div>"` | — |
| [SRC-2C8F288796-L000254](../../web/workspace.html#L254) | 254 | `"  <div class=\"workspace-label\">مساحة العمل</div>"` | — |
| [SRC-2C8F288796-L000255](../../web/workspace.html#L255) | 255 | `"  <nav class=\"nav\" id=\"mainNav\" aria-label=\"التنقل الرئيسي\"></nav>"` | — |
| [SRC-2C8F288796-L000256](../../web/workspace.html#L256) | 256 | `"  <div class=\"side-bottom\">"` | — |
| [SRC-2C8F288796-L000257](../../web/workspace.html#L257) | 257 | `"    <div class=\"connection\"><div class=\"connection-title\"><span class=\"dot\" id=\"apiDot\"></span><span id=\"apiStatus\">التحقق من الخادم</span></div><small id=\"apiStatusNote\">حالة الخادم لا تعني أن موصلات البحث الخارجية تعمل.</small></div>"` | — |
| [SRC-2C8F288796-L000258](../../web/workspace.html#L258) | 258 | `"    <div class=\"connection\"><div class=\"connection-title\">الهوية والصلاحيات</div><small id=\"roleSummary\">لم يتم التحقق من جلسة المستخدم بعد.</small></div>"` | — |
| [SRC-2C8F288796-L000259](../../web/workspace.html#L259) | 259 | `"    <div class=\"side-links\"><button class=\"side-link-button\" id=\"chatNav\" type=\"button\">محادثة Omarai</button><button class=\"side-link-button\" id=\"systemNav\" type=\"button\">حالة النظام</button><a href=\"/agent\">وكيل البحث</a></div>"` | — |
| [SRC-2C8F288796-L000260](../../web/workspace.html#L260) | 260 | `"  </div>"` | — |
| [SRC-2C8F288796-L000261](../../web/workspace.html#L261) | 261 | `"</aside>"` | — |
| [SRC-2C8F288796-L000262](../../web/workspace.html#L262) | 262 | `"<main class=\"main\">"` | — |
| [SRC-2C8F288796-L000263](../../web/workspace.html#L263) | 263 | `"  <header class=\"topbar\">"` | — |
| [SRC-2C8F288796-L000264](../../web/workspace.html#L264) | 264 | `"    <div class=\"breadcrumb\">Omarai <span aria-hidden=\"true\">/</span> <strong id=\"crumb\">نظرة عامة</strong></div>"` | — |
| [SRC-2C8F288796-L000265](../../web/workspace.html#L265) | 265 | `"    <div class=\"top-actions\"><span class=\"role-pill\" id=\"rolePill\">التحقق من الجلسة…</span><button class=\"button ghost\" id=\"logoutButton\" type=\"button\">تسجيل الخروج</button><button class=\"button primary\" id=\"addSignalTop\" type=\"button\">＋ إشارة جديدة</button></div>"` | — |
| [SRC-2C8F288796-L000266](../../web/workspace.html#L266) | 266 | `"  </header>"` | — |
| [SRC-2C8F288796-L000267](../../web/workspace.html#L267) | 267 | `"  <section class=\"page-head\"><div><div class=\"eyebrow\" id=\"pageEyebrow\">SALES INTELLIGENCE WORKSPACE</div><h1 id=\"pageTitle\">حوّل إشارات الطلب إلى فرص قابلة للمراجعة</h1><p id=\"pageDescription\">مساحة عمل عربية لإدارة إشارات الطلب والأدلة والمتابعة. الأرقام هنا تُقرأ من سجل Omarai الفعلي، ولا تُعرض بيانات تجريبية على أنها فرص حقيقية.</p></div></section>"` | — |
| [SRC-2C8F288796-L000268](../../web/workspace.html#L268) | 268 | `"  <div id=\"viewRoot\" aria-live=\"polite\"><div class=\"glass panel empty\"><strong>جارٍ تحميل مساحة العمل</strong>يتم التحقق من الجلسة ثم قراءة بياناتك المصرح بها.</div></div>"` | — |
| [SRC-2C8F288796-L000269](../../web/workspace.html#L269) | 269 | `"  <footer class=\"footer\">Omarai · تُعرض الإشارات من السجل المرتبط بمساحة العمل المصادق عليها. درجات القواعد ليست احتمالات شراء. البحث الخارجي واستهلاك حصص الموصلات لا يبدأان تلقائيًا من هذه الشاشة.</footer>"` | — |
| [SRC-2C8F288796-L000270](../../web/workspace.html#L270) | 270 | `"</main>"` | — |
| [SRC-2C8F288796-L000271](../../web/workspace.html#L271) | 271 | `"</div>"` | — |
| [SRC-2C8F288796-L000272](../../web/workspace.html#L272) | 272 | `""` | — |
| [SRC-2C8F288796-L000273](../../web/workspace.html#L273) | 273 | `"<div class=\"detail\" id=\"detailDrawer\" role=\"dialog\" aria-modal=\"true\" aria-labelledby=\"detailTitle\">"` | — |
| [SRC-2C8F288796-L000274](../../web/workspace.html#L274) | 274 | `"  <section class=\"detail-panel\"><div class=\"detail-head\"><h2 id=\"detailTitle\">تفاصيل الإشارة</h2><button class=\"button ghost\" id=\"closeDetail\" type=\"button\">إغلاق ✕</button></div><div class=\"detail-body\" id=\"detailBody\"></div></section>"` | — |
| [SRC-2C8F288796-L000275](../../web/workspace.html#L275) | 275 | `"</div>"` | — |
| [SRC-2C8F288796-L000276](../../web/workspace.html#L276) | 276 | `"<div class=\"auth-gate open\" id=\"authGate\">"` | — |
| [SRC-2C8F288796-L000277](../../web/workspace.html#L277) | 277 | `"  <section class=\"auth-card glass\">"` | — |
| [SRC-2C8F288796-L000278](../../web/workspace.html#L278) | 278 | `"    <div class=\"eyebrow\">OMARAI SECURE WORKSPACE</div>"` | — |
| [SRC-2C8F288796-L000279](../../web/workspace.html#L279) | 279 | `"    <h2>تسجيل الدخول إلى مساحة العمل</h2>"` | — |
| [SRC-2C8F288796-L000280](../../web/workspace.html#L280) | 280 | `"    <p>تستخدم هذه الصفحة جلسة الخادم الآمنة HttpOnly. رمز الوصول لا يُحفظ في Local Storage أو Session Storage، ويُمسح من حقل الإدخال بعد نجاح الدخول.</p>"` | — |
| [SRC-2C8F288796-L000281](../../web/workspace.html#L281) | 281 | `"    <form id=\"loginForm\">"` | — |
| [SRC-2C8F288796-L000282](../../web/workspace.html#L282) | 282 | `"      <div class=\"field\"><label for=\"accessToken\">رمز الوصول الخاص بالتطبيق</label><input id=\"accessToken\" type=\"password\" autocomplete=\"current-password\" required minlength=\"32\" placeholder=\"أدخل رمز الوصول\"></div>"` | — |
| [SRC-2C8F288796-L000283](../../web/workspace.html#L283) | 283 | `"      <button class=\"button primary\" type=\"submit\" id=\"loginButton\">تسجيل الدخول</button>"` | — |
| [SRC-2C8F288796-L000284](../../web/workspace.html#L284) | 284 | `"      <div class=\"auth-error\" id=\"authError\" role=\"alert\"></div>"` | — |
| [SRC-2C8F288796-L000285](../../web/workspace.html#L285) | 285 | `"    </form>"` | — |
| [SRC-2C8F288796-L000286](../../web/workspace.html#L286) | 286 | `"    <p>لا تدخل مفاتيح موفر البحث أو كلمات مرور خارجية في هذا الحقل.</p>"` | — |
| [SRC-2C8F288796-L000287](../../web/workspace.html#L287) | 287 | `"  </section>"` | — |
| [SRC-2C8F288796-L000288](../../web/workspace.html#L288) | 288 | `"</div>"` | — |
| [SRC-2C8F288796-L000289](../../web/workspace.html#L289) | 289 | `""` | — |
| [SRC-2C8F288796-L000290](../../web/workspace.html#L290) | 290 | `"<script>"` | — |
| [SRC-2C8F288796-L000291](../../web/workspace.html#L291) | 291 | `"(function(){"` | — |
| [SRC-2C8F288796-L000292](../../web/workspace.html#L292) | 292 | `"\"use strict\";"` | — |
| [SRC-2C8F288796-L000293](../../web/workspace.html#L293) | 293 | `"const $=id=>document.getElementById(id);"` | — |
| [SRC-2C8F288796-L000294](../../web/workspace.html#L294) | 294 | `"const state={authSessionVersion:0,role:null,leads:[],profiles:[],discoveryRuns:[],loadWarnings:[],activeDiscovery:null,activeProfileId:null,activeView:\"overview\",chat:{messages:[],history:[],busy:false,mode:\"deep\",sessionVersion:0},analysis:null,filtered:[],search:\"\",filter:\"all\"};"` | — |
