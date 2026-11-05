# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **061**
- سجلات الأسطر: **183**
- النطاق: SRC-2C8F288796-L000395 إلى SRC-2C8F288796-L000577
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2C8F288796-L000395](../../web/workspace.html#L395) | 395 | `" toolbar.append(search,filter);panel.append(toolbar);"` | — |
| [SRC-2C8F288796-L000396](../../web/workspace.html#L396) | 396 | `" const list=make(\"div\",\"signal-list\");drawSignalRows(list);panel.append(list);"` | — |
| [SRC-2C8F288796-L000397](../../web/workspace.html#L397) | 397 | `" if(!canWrite())panel.append(make(\"p\",\"disclaimer\",\"دور المستخدم الحالي للقراءة فقط؛ لا يمكنه إضافة إشارات أو تغيير الحالات.\"));"` | — |
| [SRC-2C8F288796-L000398](../../web/workspace.html#L398) | 398 | `" root.append(panel);"` | — |
| [SRC-2C8F288796-L000399](../../web/workspace.html#L399) | 399 | `"}"` | — |
| [SRC-2C8F288796-L000400](../../web/workspace.html#L400) | 400 | `"function drawSignalRows(list){"` | — |
| [SRC-2C8F288796-L000401](../../web/workspace.html#L401) | 401 | `" list.replaceChildren();"` | — |
| [SRC-2C8F288796-L000402](../../web/workspace.html#L402) | 402 | `" const query=state.search.trim().toLocaleLowerCase();"` | — |
| [SRC-2C8F288796-L000403](../../web/workspace.html#L403) | 403 | `" const rows=state.leads.filter(l=>(state.filter===\"all\"\|\|l.status===state.filter)&&(!query\|\|String(l.text\|\|\"\").toLocaleLowerCase().includes(query)));"` | — |
| [SRC-2C8F288796-L000404](../../web/workspace.html#L404) | 404 | `" if(!rows.length)list.append(emptyState(\"لا توجد نتائج مطابقة\",\"غيّر مرشح الحالة أو عبارة البحث، أو أضف إشارة جديدة إن كانت صلاحيتك تسمح.\"));"` | — |
| [SRC-2C8F288796-L000405](../../web/workspace.html#L405) | 405 | `" else rows.forEach(l=>list.append(signalCard(l)));"` | — |
| [SRC-2C8F288796-L000406](../../web/workspace.html#L406) | 406 | `"}"` | — |
| [SRC-2C8F288796-L000407](../../web/workspace.html#L407) | 407 | `"function createSignalForm(){"` | — |
| [SRC-2C8F288796-L000408](../../web/workspace.html#L408) | 408 | `" const wrapper=make(\"section\",\"signal-card\");const head=make(\"div\",\"panel-head\");const title=make(\"div\");title.append(make(\"h2\",\"\",\"إضافة إشارة جديدة\"),make(\"p\",\"\",\"أدخل نصًا منشورًا ورابطه العام. التحليل محلي ولا يشغّل البحث الخارجي.\"));head.append(title);wrapper.append(head);"` | — |
| [SRC-2C8F288796-L000409](../../web/workspace.html#L409) | 409 | `" const text=make(\"textarea\",\"\");text.id=\"newSignalText\";text.placeholder=\"انسخ نص الطلب أو الاحتياج المعلن من المصدر المسموح…\";text.maxLength=20000;text.required=true;"` | — |
| [SRC-2C8F288796-L000410](../../web/workspace.html#L410) | 410 | `" const url=make(\"input\",\"\");url.type=\"url\";url.id=\"newSignalUrl\";url.placeholder=\"https://رابط-المصدر\";url.required=true;"` | — |
| [SRC-2C8F288796-L000411](../../web/workspace.html#L411) | 411 | `" const grid=make(\"div\",\"form-grid\");"` | — |
| [SRC-2C8F288796-L000412](../../web/workspace.html#L412) | 412 | `" const platform=make(\"select\",\"\");platform.id=\"newSignalPlatform\";[\"manual\",\"Facebook\",\"Website\",\"OLX\",\"Other\"].forEach(value=>{const o=make(\"option\",\"\",value===\"manual\"?\"إدخال يدوي\":value);o.value=value;platform.append(o)});"` | — |
| [SRC-2C8F288796-L000413](../../web/workspace.html#L413) | 413 | `" const product=make(\"input\",\"\");product.id=\"newSignalProduct\";product.placeholder=\"مثال: أنظمة إنذار، عقارات\";"` | — |
| [SRC-2C8F288796-L000414](../../web/workspace.html#L414) | 414 | `" const location=make(\"input\",\"\");location.id=\"newSignalLocation\";location.placeholder=\"مثال: القاهرة، التجمع الخامس\";"` | — |
| [SRC-2C8F288796-L000415](../../web/workspace.html#L415) | 415 | `" const note=make(\"input\",\"\");note.id=\"newSignalNote\";note.placeholder=\"ملاحظاتك (اختياري)\";"` | — |
| [SRC-2C8F288796-L000416](../../web/workspace.html#L416) | 416 | `" const fields=[[\"النص\",text],[\"رابط المصدر\",url],[\"المنصة\",platform],[\"مصطلحات المنتج (افصل بفاصلة)\",product],[\"السوق أو المنطقة\",location],[\"ملاحظة\",note]];"` | — |
| [SRC-2C8F288796-L000417](../../web/workspace.html#L417) | 417 | `" fields.forEach(([label,input])=>{const field=make(\"div\",\"field\");field.append(make(\"label\",\"\",label));field.lastChild.htmlFor=input.id;field.append(input);grid.append(field)});"` | — |
| [SRC-2C8F288796-L000418](../../web/workspace.html#L418) | 418 | `" wrapper.append(grid);"` | — |
| [SRC-2C8F288796-L000419](../../web/workspace.html#L419) | 419 | `" const result=make(\"div\",\"\");result.id=\"analysisResult\";"` | — |
| [SRC-2C8F288796-L000420](../../web/workspace.html#L420) | 420 | `" const buttons=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000421](../../web/workspace.html#L421) | 421 | `" const analyze=action(\"١. حلّل الإشارة\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000422](../../web/workspace.html#L422) | 422 | `"  analyze.disabled=true;"` | — |
| [SRC-2C8F288796-L000423](../../web/workspace.html#L423) | 423 | `"  try{"` | — |
| [SRC-2C8F288796-L000424](../../web/workspace.html#L424) | 424 | `"   if(!text.value.trim())throw new Error(\"أدخل نص الإشارة أولًا.\");"` | — |
| [SRC-2C8F288796-L000425](../../web/workspace.html#L425) | 425 | `"   if(!safeHttp(url.value))throw new Error(\"أدخل رابط مصدر عام صالحًا يبدأ بـ HTTP أو HTTPS.\");"` | — |
| [SRC-2C8F288796-L000426](../../web/workspace.html#L426) | 426 | `"   const product_terms=product.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000427](../../web/workspace.html#L427) | 427 | `"   const location_terms=location.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000428](../../web/workspace.html#L428) | 428 | `"   const data=await api(\"/api/analyze\",{method:\"POST\",body:{text:text.value,product_terms:product_terms,location_terms:location_terms}});"` | — |
| [SRC-2C8F288796-L000429](../../web/workspace.html#L429) | 429 | `"   state.analysis={text:text.value,url:url.value,product_terms:product_terms,location_terms:location_terms,assessment:data};"` | — |
| [SRC-2C8F288796-L000430](../../web/workspace.html#L430) | 430 | `"   result.replaceChildren();"` | — |
| [SRC-2C8F288796-L000431](../../web/workspace.html#L431) | 431 | `"   const box=make(\"div\",\"analysis-result\");box.append(make(\"div\",\"analysis-score\",String(data.score??\"—\")+\"/100\"),make(\"div\",\"\",labels[data.label]\|\|data.label\|\|\"غير مصنفة\"),make(\"p\",\"\",data.summary\|\|\"لا يوجد ملخص.\"));"` | — |
| [SRC-2C8F288796-L000432](../../web/workspace.html#L432) | 432 | `"   box.append(make(\"p\",\"disclaimer\",\"هذه درجة قواعد إرشادية لا تمثل احتمال شراء. راجع النص والمصدر قبل اعتماد الإشارة.\"));"` | — |
| [SRC-2C8F288796-L000433](../../web/workspace.html#L433) | 433 | `"   result.append(box);"` | — |
| [SRC-2C8F288796-L000434](../../web/workspace.html#L434) | 434 | `"  }catch(e){result.replaceChildren(make(\"p\",\"auth-error\",escapeMessage(e.message)))}"` | — |
| [SRC-2C8F288796-L000435](../../web/workspace.html#L435) | 435 | `"  finally{analyze.disabled=false}"` | — |
| [SRC-2C8F288796-L000436](../../web/workspace.html#L436) | 436 | `" });"` | — |
| [SRC-2C8F288796-L000437](../../web/workspace.html#L437) | 437 | `" const save=action(\"٢. احفظ الإشارة\",\"\",async()=>{"` | — |
| [SRC-2C8F288796-L000438](../../web/workspace.html#L438) | 438 | `"  save.disabled=true;"` | — |
| [SRC-2C8F288796-L000439](../../web/workspace.html#L439) | 439 | `"  try{"` | — |
| [SRC-2C8F288796-L000440](../../web/workspace.html#L440) | 440 | `"   const item=state.analysis;"` | — |
| [SRC-2C8F288796-L000441](../../web/workspace.html#L441) | 441 | `"   if(!item\|\|item.text!==text.value\|\|item.url!==url.value)throw new Error(\"أعد التحليل بعد أي تغيير في النص أو رابط المصدر.\");"` | — |
| [SRC-2C8F288796-L000442](../../web/workspace.html#L442) | 442 | `"   if(!safeHttp(url.value))throw new Error(\"رابط المصدر غير صالح.\");"` | — |
| [SRC-2C8F288796-L000443](../../web/workspace.html#L443) | 443 | `"   const product_terms=product.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000444](../../web/workspace.html#L444) | 444 | `"   const location_terms=location.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000445](../../web/workspace.html#L445) | 445 | `"   if(JSON.stringify(product_terms)!==JSON.stringify(item.product_terms)\|\|JSON.stringify(location_terms)!==JSON.stringify(item.location_terms))throw new Error(\"تغيرت مصطلحات المنتج أو المنطقة؛ أعد التحليل.\");"` | — |
| [SRC-2C8F288796-L000446](../../web/workspace.html#L446) | 446 | `"   const response=await api(\"/api/leads\",{method:\"POST\",body:{text:text.value,source_url:url.value,platform:platform.value,note:note.value,product_terms:product_terms,location_terms:location_terms}});"` | — |
| [SRC-2C8F288796-L000447](../../web/workspace.html#L447) | 447 | `"   result.replaceChildren(make(\"p\",\"tag teal\",response.created?\"تم حفظ الإشارة.\":\"هذه الإشارة موجودة بالفعل ولم تُكرر.\"));"` | — |
| [SRC-2C8F288796-L000448](../../web/workspace.html#L448) | 448 | `"   state.analysis=null;text.value=\"\";url.value=\"\";note.value=\"\";await loadLeads();renderSignals();"` | — |
| [SRC-2C8F288796-L000449](../../web/workspace.html#L449) | 449 | `"  }catch(e){result.append(make(\"p\",\"auth-error\",escapeMessage(e.message)))}"` | — |
| [SRC-2C8F288796-L000450](../../web/workspace.html#L450) | 450 | `"  finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000451](../../web/workspace.html#L451) | 451 | `" });"` | — |
| [SRC-2C8F288796-L000452](../../web/workspace.html#L452) | 452 | `" buttons.append(analyze,save);wrapper.append(buttons,result);return wrapper;"` | — |
| [SRC-2C8F288796-L000453](../../web/workspace.html#L453) | 453 | `"}"` | — |
| [SRC-2C8F288796-L000454](../../web/workspace.html#L454) | 454 | `"function renderPipeline(){"` | — |
| [SRC-2C8F288796-L000455](../../web/workspace.html#L455) | 455 | `" setPage(\"مسار التأهيل\",\"يعرض المسار الحالات المحفوظة فعليًا، ويمكن تحديث الحالة بعد مراجعة الدليل. لا توجد مراحل CRM غير مدعومة في الخادم.\",\"QUALIFICATION PIPELINE\");"` | — |
| [SRC-2C8F288796-L000456](../../web/workspace.html#L456) | 456 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000457](../../web/workspace.html#L457) | 457 | `" const panel=make(\"section\",\"glass panel\");const head=make(\"div\",\"panel-head\");const title=make(\"div\");title.append(make(\"h2\",\"\",\"حالة كل إشارة\"),make(\"p\",\"\",\"اختر بطاقة لفتح المصدر وتقييم القواعد وتغيير الحالة المسموح بها.\"));head.append(title,action(\"صندوق الإشارات ←\",\"ghost\",()=>navigate(\"signals\")));panel.append(head);"` | — |
| [SRC-2C8F288796-L000458](../../web/workspace.html#L458) | 458 | `" const board=make(\"div\",\"pipeline\");const groups=[[\"نشطة جديدة\",[\"new\",\"needs_review\"]],[\"مؤهلة / متابعة\",[\"qualified\",\"contacted\"]],[\"مغلقة\",[\"converted\",\"rejected\"]]];"` | — |
| [SRC-2C8F288796-L000459](../../web/workspace.html#L459) | 459 | `" groups.forEach(([name,ids])=>{const col=make(\"section\",\"pipeline-col\");const rows=state.leads.filter(l=>ids.includes(l.status));col.append(make(\"h3\",\"\",name+\" · \"+rows.length));if(!rows.length)col.append(make(\"p\",\"subtle\",\"لا توجد سجلات في هذه المجموعة.\"));rows.forEach(l=>{const item=make(\"button\",\"pipeline-item\",String(l.text\|\|\"\").slice(0,115));item.type=\"button\";item.addEventListener(\"click\",()=>openDetails(l));col.append(item)});board.append(col)});"` | — |
| [SRC-2C8F288796-L000460](../../web/workspace.html#L460) | 460 | `" panel.append(board);root.append(panel);"` | — |
| [SRC-2C8F288796-L000461](../../web/workspace.html#L461) | 461 | `"}"` | — |
| [SRC-2C8F288796-L000462](../../web/workspace.html#L462) | 462 | `"async function renderSystem(){"` | — |
| [SRC-2C8F288796-L000463](../../web/workspace.html#L463) | 463 | `" setPage(\"حالات النظام\",\"لقطة إعدادات يقرأها الخادم محليًا. لا تنفذ هذه الشاشة اتصالًا تجريبيًا بالموفرات ولا تستهلك حصص البحث.\",\"SYSTEM CONFIGURATION SNAPSHOT\");"` | — |
| [SRC-2C8F288796-L000464](../../web/workspace.html#L464) | 464 | `" const root=$(\"viewRoot\");root.replaceChildren(emptyState(\"جارٍ قراءة حالة الخادم\",\"GET /api/health — لا يجري اختبار اتصال خارجي.\"));"` | — |
| [SRC-2C8F288796-L000465](../../web/workspace.html#L465) | 465 | `" try{"` | — |
| [SRC-2C8F288796-L000466](../../web/workspace.html#L466) | 466 | `"  const data=await api(\"/api/health\");"` | — |
| [SRC-2C8F288796-L000467](../../web/workspace.html#L467) | 467 | `"  const agent=data.agent\|\|{};const build=data.build\|\|{};"` | — |
| [SRC-2C8F288796-L000468](../../web/workspace.html#L468) | 468 | `"  root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000469](../../web/workspace.html#L469) | 469 | `"  const stats=make(\"div\",\"stats\");"` | — |
| [SRC-2C8F288796-L000470](../../web/workspace.html#L470) | 470 | `"  stats.append("` | — |
| [SRC-2C8F288796-L000471](../../web/workspace.html#L471) | 471 | `"   buildStat(\"استجابة الخادم\",data.ok===true?\"يستجيب\":\"غير مؤكدة\",\"استجابة نقطة /api/health\",\"glow-teal\"),"` | — |
| [SRC-2C8F288796-L000472](../../web/workspace.html#L472) | 472 | `"   buildStat(\"مكتبات البحث\",agent.web_search_ready===true?\"موجودة\":\"غير جاهزة\",\"فحص اعتماديات محلية فقط\",\"glow-blue\"),"` | — |
| [SRC-2C8F288796-L000473](../../web/workspace.html#L473) | 473 | `"   buildStat(\"إعداد النموذج\",agent.language_model_configured===true?\"مهيأ\":\"غير مهيأ\",\"لا يثبت إمكانية الاتصال أو نجاح الاستجابة\",\"glow-violet\"),"` | — |
| [SRC-2C8F288796-L000474](../../web/workspace.html#L474) | 474 | `"   buildStat(\"هوية البناء\",build.sha_status===\"available\"?String(build.sha).slice(0,8):\"غير معروفة\",\"حالة SHA كما أعادها الخادم\",\"glow-amber\")"` | — |
| [SRC-2C8F288796-L000475](../../web/workspace.html#L475) | 475 | `"  );"` | — |
| [SRC-2C8F288796-L000476](../../web/workspace.html#L476) | 476 | `"  root.append(stats);"` | — |
| [SRC-2C8F288796-L000477](../../web/workspace.html#L477) | 477 | `"  const grid=make(\"div\",\"content-grid\");"` | — |
| [SRC-2C8F288796-L000478](../../web/workspace.html#L478) | 478 | `"  const models=make(\"section\",\"glass panel\");const mh=make(\"div\",\"panel-head\");const mt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000479](../../web/workspace.html#L479) | 479 | `"  mt.append(make(\"h2\",\"\",\"موفر النموذج\"));mt.append(make(\"p\",\"\",\"بيانات إعداد يعرضها الخادم؛ لا تعرض مفاتيح أو أسرار.\"));"` | — |
| [SRC-2C8F288796-L000480](../../web/workspace.html#L480) | 480 | `"  mh.append(mt);models.append(mh);"` | — |
| [SRC-2C8F288796-L000481](../../web/workspace.html#L481) | 481 | `"  models.append(make(\"p\",\"\", \"الموفر الأساسي المعلن: \"+String(agent.language_model_provider\|\|\"غير معلوم\")));"` | — |
| [SRC-2C8F288796-L000482](../../web/workspace.html#L482) | 482 | `"  const providers=Array.isArray(agent.model_providers)?agent.model_providers:[];"` | — |
| [SRC-2C8F288796-L000483](../../web/workspace.html#L483) | 483 | `"  if(providers.length){"` | — |
| [SRC-2C8F288796-L000484](../../web/workspace.html#L484) | 484 | `"   const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000485](../../web/workspace.html#L485) | 485 | `"   providers.forEach(p=>{"` | — |
| [SRC-2C8F288796-L000486](../../web/workspace.html#L486) | 486 | `"    const row=make(\"article\",\"signal-card\");"` | — |
| [SRC-2C8F288796-L000487](../../web/workspace.html#L487) | 487 | `"    row.append(make(\"strong\",\"\",String(p.name\|\|\"موفر غير مسمى\")));"` | — |
| [SRC-2C8F288796-L000488](../../web/workspace.html#L488) | 488 | `"    row.append(make(\"span\",\"subtle\",\"النموذج المهيأ: \"+String(p.model\|\|\"غير محدد\")));"` | — |
| [SRC-2C8F288796-L000489](../../web/workspace.html#L489) | 489 | `"    row.append(tag(p.configured===true?\"مهيأ في البيئة\":\"غير مهيأ\",p.configured===true?\"teal\":\"amber\"));"` | — |
| [SRC-2C8F288796-L000490](../../web/workspace.html#L490) | 490 | `"    list.append(row);"` | — |
| [SRC-2C8F288796-L000491](../../web/workspace.html#L491) | 491 | `"   });"` | — |
| [SRC-2C8F288796-L000492](../../web/workspace.html#L492) | 492 | `"   models.append(list);"` | — |
| [SRC-2C8F288796-L000493](../../web/workspace.html#L493) | 493 | `"  }else models.append(emptyState(\"لا توجد موفرات ظاهرة كإعداد\",\"لم يعرض الخادم موفرًا مهيأ ضمن هذه اللقطة.\"));"` | — |
| [SRC-2C8F288796-L000494](../../web/workspace.html#L494) | 494 | `"  const search=make(\"section\",\"glass panel\");const sh=make(\"div\",\"panel-head\");const st=make(\"div\");"` | — |
| [SRC-2C8F288796-L000495](../../web/workspace.html#L495) | 495 | `"  st.append(make(\"h2\",\"\",\"إعدادات البحث الاختيارية\"),make(\"p\",\"\",\"القيم أدناه أعلام إعداد فقط، وليست اختبارات تشغيل.\"));"` | — |
| [SRC-2C8F288796-L000496](../../web/workspace.html#L496) | 496 | `"  sh.append(st);search.append(sh);"` | — |
| [SRC-2C8F288796-L000497](../../web/workspace.html#L497) | 497 | `"  const flags=["` | — |
| [SRC-2C8F288796-L000498](../../web/workspace.html#L498) | 498 | `"   [\"Brave Search API\",agent.brave_search_api_configured],"` | — |
| [SRC-2C8F288796-L000499](../../web/workspace.html#L499) | 499 | `"   [\"Tavily Search API\",agent.tavily_search_api_configured],"` | — |
| [SRC-2C8F288796-L000500](../../web/workspace.html#L500) | 500 | `"   [\"DeepSeek Search API\",agent.deepseek_search_api_configured],"` | — |
| [SRC-2C8F288796-L000501](../../web/workspace.html#L501) | 501 | `"   [\"OpenRouter web search\",agent.openrouter_web_search_enabled]"` | — |
| [SRC-2C8F288796-L000502](../../web/workspace.html#L502) | 502 | `"  ];"` | — |
| [SRC-2C8F288796-L000503](../../web/workspace.html#L503) | 503 | `"  flags.forEach(([name,value])=>{const row=make(\"div\",\"signal-actions\");row.append(make(\"span\",\"\",name),tag(value===true?\"مهيأ/مفعل\":\"غير مهيأ/معطل\",value===true?\"teal\":\"amber\"));search.append(row)});"` | — |
| [SRC-2C8F288796-L000504](../../web/workspace.html#L504) | 504 | `"  search.append(make(\"p\",\"disclaimer\",\"لا تنفذ هذه الشاشة تشخيصًا مباشرًا ولا تختبر صلاحية مفاتيح الموفرات. التشخيص الحي قد يستهلك حصة أو تكلفة، ويظل منفصلًا ويتطلب موافقة المالك.\"));"` | — |
| [SRC-2C8F288796-L000505](../../web/workspace.html#L505) | 505 | `"  grid.append(models,search);root.append(grid);"` | — |
| [SRC-2C8F288796-L000506](../../web/workspace.html#L506) | 506 | `" }catch(e){root.replaceChildren(emptyState(\"تعذرت قراءة الإعدادات\",escapeMessage(e.message)))}"` | — |
| [SRC-2C8F288796-L000507](../../web/workspace.html#L507) | 507 | `"}"` | — |
| [SRC-2C8F288796-L000508](../../web/workspace.html#L508) | 508 | `"function renderPlaceholder(id){"` | — |
| [SRC-2C8F288796-L000509](../../web/workspace.html#L509) | 509 | `" const item=menu.find(x=>x.id===id);const title=item?item.label:\"وحدة\";"` | — |
| [SRC-2C8F288796-L000510](../../web/workspace.html#L510) | 510 | `" setPage(title,\"واجهة الوحدة جزء من تصور Omarai، لكن المستودع عند الرأس الحالي لا يوفّر بعد عقد API موثقًا لهذه الوظيفة. لا نعرض بيانات أو نتائج شكلية على أنها حقيقية.\",\"MODULE NOT ENABLED\");"` | — |
| [SRC-2C8F288796-L000511](../../web/workspace.html#L511) | 511 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000512](../../web/workspace.html#L512) | 512 | `" const card=make(\"section\",\"glass module-placeholder\");"` | — |
| [SRC-2C8F288796-L000513](../../web/workspace.html#L513) | 513 | `" card.append(tag(\"غير مفعلة في الخادم الحالي\",\"amber\"),make(\"h2\",\"\",title));"` | — |
| [SRC-2C8F288796-L000514](../../web/workspace.html#L514) | 514 | `" card.append(make(\"p\",\"\",\"هذه الشاشة لا تستدعي موصلًا خارجيًا ولا تحفظ إعدادات وهمية. يلزم بناء نموذج البيانات وواجهة API واختبارات الصلاحيات والعزل قبل تشغيلها.\"));"` | — |
| [SRC-2C8F288796-L000515](../../web/workspace.html#L515) | 515 | `" const list=make(\"div\",\"module-list\");"` | — |
| [SRC-2C8F288796-L000516](../../web/workspace.html#L516) | 516 | `" [\"تعريف عقد البيانات والحقول ومصدر كل قيمة.\",\"إنشاء API محمي ومربوط بالمستخدم ومساحة العمل المصادق عليها.\",\"إضافة اختبارات نجاح وفشل وعزل بين المستأجرين.\",\"ربط الواجهة بالبيانات الفعلية ثم اختبارها على بيئة معروفة.\"].forEach(x=>list.append(make(\"div\",\"module-step\",x)));"` | — |
| [SRC-2C8F288796-L000517](../../web/workspace.html#L517) | 517 | `" card.append(list,make(\"div\",\"form-actions\"));"` | — |
| [SRC-2C8F288796-L000518](../../web/workspace.html#L518) | 518 | `" const links=card.querySelector(\".form-actions\");links.append(action(\"العودة إلى النظرة العامة\",\"primary\",()=>navigate(\"overview\")),action(\"فتح وكيل البحث الحالي\",\"\",()=>{window.location.href=\"/\"}));"` | — |
| [SRC-2C8F288796-L000519](../../web/workspace.html#L519) | 519 | `" root.append(card);"` | — |
| [SRC-2C8F288796-L000520](../../web/workspace.html#L520) | 520 | `"}"` | — |
| [SRC-2C8F288796-L000521](../../web/workspace.html#L521) | 521 | `"function renderCurrent(){"` | — |
| [SRC-2C8F288796-L000522](../../web/workspace.html#L522) | 522 | `" renderNav();"` | — |
| [SRC-2C8F288796-L000523](../../web/workspace.html#L523) | 523 | `" if(state.activeView===\"overview\")renderOverview();"` | — |
| [SRC-2C8F288796-L000524](../../web/workspace.html#L524) | 524 | `" else if(state.activeView===\"signals\")renderSignals();"` | — |
| [SRC-2C8F288796-L000525](../../web/workspace.html#L525) | 525 | `" else if(state.activeView===\"pipeline\")renderPipeline();"` | — |
| [SRC-2C8F288796-L000526](../../web/workspace.html#L526) | 526 | `" else if(state.activeView===\"system\")renderSystem();"` | — |
| [SRC-2C8F288796-L000527](../../web/workspace.html#L527) | 527 | `" else renderPlaceholder(state.activeView);"` | — |
| [SRC-2C8F288796-L000528](../../web/workspace.html#L528) | 528 | `"}"` | — |
| [SRC-2C8F288796-L000529](../../web/workspace.html#L529) | 529 | `"function navigate(view){"` | — |
| [SRC-2C8F288796-L000530](../../web/workspace.html#L530) | 530 | `" state.activeView=view;renderCurrent();"` | — |
| [SRC-2C8F288796-L000531](../../web/workspace.html#L531) | 531 | `"}"` | — |
| [SRC-2C8F288796-L000532](../../web/workspace.html#L532) | 532 | `"async function loadLeads(){"` | — |
| [SRC-2C8F288796-L000533](../../web/workspace.html#L533) | 533 | `" const data=await api(\"/api/leads?limit=500\");"` | — |
| [SRC-2C8F288796-L000534](../../web/workspace.html#L534) | 534 | `" state.leads=Array.isArray(data.leads)?data.leads:[];"` | — |
| [SRC-2C8F288796-L000535](../../web/workspace.html#L535) | 535 | `"}"` | — |
| [SRC-2C8F288796-L000536](../../web/workspace.html#L536) | 536 | `"async function bootstrap(){"` | — |
| [SRC-2C8F288796-L000537](../../web/workspace.html#L537) | 537 | `" try{"` | — |
| [SRC-2C8F288796-L000538](../../web/workspace.html#L538) | 538 | `"  const session=await api(\"/api/session\");"` | — |
| [SRC-2C8F288796-L000539](../../web/workspace.html#L539) | 539 | `"  state.role=session.role\|\|\"unknown\";"` | — |
| [SRC-2C8F288796-L000540](../../web/workspace.html#L540) | 540 | `"  $(\"rolePill\").textContent=\"صلاحية: \"+state.role;"` | — |
| [SRC-2C8F288796-L000541](../../web/workspace.html#L541) | 541 | `"  $(\"roleSummary\").textContent=\"الدور: \"+state.role+(canWrite()?\" — إضافة وتحديث السجلات متاح.\":\" — قراءة فقط.\");"` | — |
| [SRC-2C8F288796-L000542](../../web/workspace.html#L542) | 542 | `"  hideAuth();"` | — |
| [SRC-2C8F288796-L000543](../../web/workspace.html#L543) | 543 | `"  await loadLeads();"` | — |
| [SRC-2C8F288796-L000544](../../web/workspace.html#L544) | 544 | `"  setConnection(true,\"خادم Omarai متصل\",\"تم تحميل سجل الإشارات. هذا لا يثبت اتصال موفرات البحث الخارجية.\");"` | — |
| [SRC-2C8F288796-L000545](../../web/workspace.html#L545) | 545 | `"  renderCurrent();"` | — |
| [SRC-2C8F288796-L000546](../../web/workspace.html#L546) | 546 | `" }catch(e){"` | — |
| [SRC-2C8F288796-L000547](../../web/workspace.html#L547) | 547 | `"  setConnection(false,\"يلزم تسجيل الدخول\",\"لا يتم تحميل أي سجل قبل التحقق من الجلسة.\");"` | — |
| [SRC-2C8F288796-L000548](../../web/workspace.html#L548) | 548 | `"  showAuth(e.message);"` | — |
| [SRC-2C8F288796-L000549](../../web/workspace.html#L549) | 549 | `"  $(\"viewRoot\").replaceChildren(emptyState(\"مساحة العمل مقفلة\",\"سجّل الدخول لقراءة البيانات المرتبطة بمساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000550](../../web/workspace.html#L550) | 550 | `" }"` | — |
| [SRC-2C8F288796-L000551](../../web/workspace.html#L551) | 551 | `"}"` | — |
| [SRC-2C8F288796-L000552](../../web/workspace.html#L552) | 552 | `"$(\"loginForm\").addEventListener(\"submit\",async event=>{"` | — |
| [SRC-2C8F288796-L000553](../../web/workspace.html#L553) | 553 | `" event.preventDefault();const token=$(\"accessToken\").value.trim();const button=$(\"loginButton\");button.disabled=true;$(\"authError\").textContent=\"\";"` | — |
| [SRC-2C8F288796-L000554](../../web/workspace.html#L554) | 554 | `" try{"` | — |
| [SRC-2C8F288796-L000555](../../web/workspace.html#L555) | 555 | `"  await api(\"/api/session\",{method:\"POST\",body:{access_token:token}});"` | — |
| [SRC-2C8F288796-L000556](../../web/workspace.html#L556) | 556 | `"  $(\"accessToken\").value=\"\";await bootstrap();"` | — |
| [SRC-2C8F288796-L000557](../../web/workspace.html#L557) | 557 | `" }catch(e){$(\"authError\").textContent=escapeMessage(e.message)}"` | — |
| [SRC-2C8F288796-L000558](../../web/workspace.html#L558) | 558 | `" finally{button.disabled=false}"` | — |
| [SRC-2C8F288796-L000559](../../web/workspace.html#L559) | 559 | `"});"` | — |
| [SRC-2C8F288796-L000560](../../web/workspace.html#L560) | 560 | `"$(\"logoutButton\").addEventListener(\"click\",async()=>{"` | — |
| [SRC-2C8F288796-L000561](../../web/workspace.html#L561) | 561 | `" try{"` | — |
| [SRC-2C8F288796-L000562](../../web/workspace.html#L562) | 562 | `"  await api(\"/api/session/logout\",{method:\"POST\",body:{}});"` | — |
| [SRC-2C8F288796-L000563](../../web/workspace.html#L563) | 563 | `" }catch(e){"` | — |
| [SRC-2C8F288796-L000564](../../web/workspace.html#L564) | 564 | `"  alert(\"تعذر تسجيل الخروج من الخادم؛ لم يتم تغيير حالة الجلسة في الواجهة. \"+escapeMessage(e.message));"` | — |
| [SRC-2C8F288796-L000565](../../web/workspace.html#L565) | 565 | `"  return;"` | — |
| [SRC-2C8F288796-L000566](../../web/workspace.html#L566) | 566 | `" }"` | — |
| [SRC-2C8F288796-L000567](../../web/workspace.html#L567) | 567 | `" state.role=null;state.leads=[];state.activeView=\"overview\";showAuth(\"تم تسجيل الخروج. أدخل رمز الوصول للمتابعة.\");setConnection(false,\"غير متصل\",\"سجّل الدخول لعرض السجلات.\");"` | — |
| [SRC-2C8F288796-L000568](../../web/workspace.html#L568) | 568 | `"});"` | — |
| [SRC-2C8F288796-L000569](../../web/workspace.html#L569) | 569 | `"$(\"addSignalTop\").addEventListener(\"click\",()=>navigate(\"signals\"));"` | — |
| [SRC-2C8F288796-L000570](../../web/workspace.html#L570) | 570 | `"$(\"closeDetail\").addEventListener(\"click\",closeDetails);"` | — |
| [SRC-2C8F288796-L000571](../../web/workspace.html#L571) | 571 | `"$(\"detailDrawer\").addEventListener(\"click\",e=>{if(e.target===$(\"detailDrawer\"))closeDetails()});"` | — |
| [SRC-2C8F288796-L000572](../../web/workspace.html#L572) | 572 | `"document.addEventListener(\"keydown\",e=>{if(e.key===\"Escape\")closeDetails()});"` | — |
| [SRC-2C8F288796-L000573](../../web/workspace.html#L573) | 573 | `"renderNav();bootstrap();"` | — |
| [SRC-2C8F288796-L000574](../../web/workspace.html#L574) | 574 | `"})();"` | — |
| [SRC-2C8F288796-L000575](../../web/workspace.html#L575) | 575 | `"</script>"` | — |
| [SRC-2C8F288796-L000576](../../web/workspace.html#L576) | 576 | `"</body>"` | — |
| [SRC-2C8F288796-L000577](../../web/workspace.html#L577) | 577 | `"</html>"` | — |
