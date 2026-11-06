# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **063**
- سجلات الأسطر: **285**
- النطاق: SRC-2C8F288796-L000498 إلى SRC-2C8F288796-L000782
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2C8F288796-L000498](../../web/workspace.html#L498) | 498 | `"    row.append(make(\"strong\",\"\",String(p.name\|\|\"موفر غير مسمى\")));"` | — |
| [SRC-2C8F288796-L000499](../../web/workspace.html#L499) | 499 | `"    row.append(make(\"span\",\"subtle\",\"النموذج المهيأ: \"+String(p.model\|\|\"غير محدد\")));"` | — |
| [SRC-2C8F288796-L000500](../../web/workspace.html#L500) | 500 | `"    row.append(tag(p.configured===true?\"مهيأ في البيئة\":\"غير مهيأ\",p.configured===true?\"teal\":\"amber\"));"` | — |
| [SRC-2C8F288796-L000501](../../web/workspace.html#L501) | 501 | `"    list.append(row);"` | — |
| [SRC-2C8F288796-L000502](../../web/workspace.html#L502) | 502 | `"   });"` | — |
| [SRC-2C8F288796-L000503](../../web/workspace.html#L503) | 503 | `"   models.append(list);"` | — |
| [SRC-2C8F288796-L000504](../../web/workspace.html#L504) | 504 | `"  }else models.append(emptyState(\"لا توجد موفرات ظاهرة كإعداد\",\"لم يعرض الخادم موفرًا مهيأ ضمن هذه اللقطة.\"));"` | — |
| [SRC-2C8F288796-L000505](../../web/workspace.html#L505) | 505 | `"  const search=make(\"section\",\"glass panel\");const sh=make(\"div\",\"panel-head\");const st=make(\"div\");"` | — |
| [SRC-2C8F288796-L000506](../../web/workspace.html#L506) | 506 | `"  st.append(make(\"h2\",\"\",\"إعدادات البحث الاختيارية\"),make(\"p\",\"\",\"القيم أدناه أعلام إعداد فقط، وليست اختبارات تشغيل.\"));"` | — |
| [SRC-2C8F288796-L000507](../../web/workspace.html#L507) | 507 | `"  sh.append(st);search.append(sh);"` | — |
| [SRC-2C8F288796-L000508](../../web/workspace.html#L508) | 508 | `"  const flags=["` | — |
| [SRC-2C8F288796-L000509](../../web/workspace.html#L509) | 509 | `"   [\"Brave Search API\",agent.brave_search_api_configured],"` | — |
| [SRC-2C8F288796-L000510](../../web/workspace.html#L510) | 510 | `"   [\"Tavily Search API\",agent.tavily_search_api_configured],"` | — |
| [SRC-2C8F288796-L000511](../../web/workspace.html#L511) | 511 | `"   [\"DeepSeek Search API\",agent.deepseek_search_api_configured],"` | — |
| [SRC-2C8F288796-L000512](../../web/workspace.html#L512) | 512 | `"   [\"OpenRouter web search\",agent.openrouter_web_search_enabled]"` | — |
| [SRC-2C8F288796-L000513](../../web/workspace.html#L513) | 513 | `"  ];"` | — |
| [SRC-2C8F288796-L000514](../../web/workspace.html#L514) | 514 | `"  flags.forEach(([name,value])=>{const row=make(\"div\",\"signal-actions\");row.append(make(\"span\",\"\",name),tag(value===true?\"مهيأ/مفعل\":\"غير مهيأ/معطل\",value===true?\"teal\":\"amber\"));search.append(row)});"` | — |
| [SRC-2C8F288796-L000515](../../web/workspace.html#L515) | 515 | `"  search.append(make(\"p\",\"disclaimer\",\"لا تنفذ هذه الشاشة تشخيصًا مباشرًا ولا تختبر صلاحية مفاتيح الموفرات. التشخيص الحي قد يستهلك حصة أو تكلفة، ويظل منفصلًا ويتطلب موافقة المالك.\"));"` | — |
| [SRC-2C8F288796-L000516](../../web/workspace.html#L516) | 516 | `"  grid.append(models,search);root.append(grid);"` | — |
| [SRC-2C8F288796-L000517](../../web/workspace.html#L517) | 517 | `" }catch(e){root.replaceChildren(emptyState(\"تعذرت قراءة الإعدادات\",escapeMessage(e.message)))}"` | — |
| [SRC-2C8F288796-L000518](../../web/workspace.html#L518) | 518 | `"}"` | — |
| [SRC-2C8F288796-L000519](../../web/workspace.html#L519) | 519 | `"function renderPlaceholder(id){"` | — |
| [SRC-2C8F288796-L000520](../../web/workspace.html#L520) | 520 | `" const item=menu.find(x=>x.id===id);const title=item?item.label:\"وحدة\";"` | — |
| [SRC-2C8F288796-L000521](../../web/workspace.html#L521) | 521 | `" setPage(title,\"واجهة الوحدة جزء من تصور Omarai، لكن المستودع عند الرأس الحالي لا يوفّر بعد عقد API موثقًا لهذه الوظيفة. لا نعرض بيانات أو نتائج شكلية على أنها حقيقية.\",\"MODULE NOT ENABLED\");"` | — |
| [SRC-2C8F288796-L000522](../../web/workspace.html#L522) | 522 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000523](../../web/workspace.html#L523) | 523 | `" const card=make(\"section\",\"glass module-placeholder\");"` | — |
| [SRC-2C8F288796-L000524](../../web/workspace.html#L524) | 524 | `" card.append(tag(\"غير مفعلة في الخادم الحالي\",\"amber\"),make(\"h2\",\"\",title));"` | — |
| [SRC-2C8F288796-L000525](../../web/workspace.html#L525) | 525 | `" card.append(make(\"p\",\"\",\"هذه الشاشة لا تستدعي موصلًا خارجيًا ولا تحفظ إعدادات وهمية. يلزم بناء نموذج البيانات وواجهة API واختبارات الصلاحيات والعزل قبل تشغيلها.\"));"` | — |
| [SRC-2C8F288796-L000526](../../web/workspace.html#L526) | 526 | `" const list=make(\"div\",\"module-list\");"` | — |
| [SRC-2C8F288796-L000527](../../web/workspace.html#L527) | 527 | `" [\"تعريف عقد البيانات والحقول ومصدر كل قيمة.\",\"إنشاء API محمي ومربوط بالمستخدم ومساحة العمل المصادق عليها.\",\"إضافة اختبارات نجاح وفشل وعزل بين المستأجرين.\",\"ربط الواجهة بالبيانات الفعلية ثم اختبارها على بيئة معروفة.\"].forEach(x=>list.append(make(\"div\",\"module-step\",x)));"` | — |
| [SRC-2C8F288796-L000528](../../web/workspace.html#L528) | 528 | `" card.append(list,make(\"div\",\"form-actions\"));"` | — |
| [SRC-2C8F288796-L000529](../../web/workspace.html#L529) | 529 | `" const links=card.querySelector(\".form-actions\");links.append(action(\"العودة إلى النظرة العامة\",\"primary\",()=>navigate(\"overview\")),action(\"فتح وكيل البحث الحالي\",\"\",()=>{window.location.href=\"/agent\"}));"` | — |
| [SRC-2C8F288796-L000530](../../web/workspace.html#L530) | 530 | `" root.append(card);"` | — |
| [SRC-2C8F288796-L000531](../../web/workspace.html#L531) | 531 | `"}"` | — |
| [SRC-2C8F288796-L000532](../../web/workspace.html#L532) | 532 | `"function csvValues(value){return String(value\|\|\"\").split(\",\").map(x=>x.trim()).filter(Boolean)}"` | — |
| [SRC-2C8F288796-L000533](../../web/workspace.html#L533) | 533 | `"function textField(label,id,placeholder,value,multiline){"` | — |
| [SRC-2C8F288796-L000534](../../web/workspace.html#L534) | 534 | `" const field=make(\"div\",\"field\"),control=make(multiline?\"textarea\":\"input\",\"\");"` | — |
| [SRC-2C8F288796-L000535](../../web/workspace.html#L535) | 535 | `" control.id=id;control.value=value\|\|\"\";control.placeholder=placeholder\|\|\"\";"` | — |
| [SRC-2C8F288796-L000536](../../web/workspace.html#L536) | 536 | `" const caption=make(\"label\",\"\",label);caption.htmlFor=id;field.append(caption,control);"` | — |
| [SRC-2C8F288796-L000537](../../web/workspace.html#L537) | 537 | `" return {field,control};"` | — |
| [SRC-2C8F288796-L000538](../../web/workspace.html#L538) | 538 | `"}"` | — |
| [SRC-2C8F288796-L000539](../../web/workspace.html#L539) | 539 | `"function renderProductProfile(){"` | — |
| [SRC-2C8F288796-L000540](../../web/workspace.html#L540) | 540 | `" setPage(\"ملف المنتج والعرض\",\"عرّف المنتج والسوق قبل تشغيل اكتشاف الطلب. كل ملف محفوظ مرتبط بمساحة العمل المصادق عليها.\",\"PRODUCT & MARKET PROFILE\");"` | — |
| [SRC-2C8F288796-L000541](../../web/workspace.html#L541) | 541 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000542](../../web/workspace.html#L542) | 542 | `" const panel=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000543](../../web/workspace.html#L543) | 543 | `" title.append(make(\"h2\",\"\",\"بيانات المنتج والسوق\"),make(\"p\",\"\",\"أدخل المعلومات المعروفة صراحةً؛ لا يخترع Omarai مواصفات أو عملاء مستهدفين من اسم المنتج وحده.\"));"` | — |
| [SRC-2C8F288796-L000544](../../web/workspace.html#L544) | 544 | `" head.append(title);panel.append(head);"` | — |
| [SRC-2C8F288796-L000545](../../web/workspace.html#L545) | 545 | `" const grid=make(\"div\",\"form-grid\"),controls={};"` | — |
| [SRC-2C8F288796-L000546](../../web/workspace.html#L546) | 546 | `" const fields=["` | — |
| [SRC-2C8F288796-L000547](../../web/workspace.html#L547) | 547 | `"  [\"اسم المنتج أو الخدمة\",\"name\",\"مثال: لوحة إنذار حريق\"],"` | — |
| [SRC-2C8F288796-L000548](../../web/workspace.html#L548) | 548 | `"  [\"الأسماء والمرادفات\",\"aliases\",\"FACP، لوحة إنذار، Fire Alarm Panel\"],"` | — |
| [SRC-2C8F288796-L000549](../../web/workspace.html#L549) | 549 | `"  [\"الفئة أو التصنيف\",\"category\",\"السلامة، أنظمة إنذار\"],"` | — |
| [SRC-2C8F288796-L000550](../../web/workspace.html#L550) | 550 | `"  [\"الاستخدامات\",\"useCases\",\"المصانع، المباني التجارية\"],"` | — |
| [SRC-2C8F288796-L000551](../../web/workspace.html#L551) | 551 | `"  [\"المشكلات التي يحلها\",\"problems\",\"الكشف المبكر، تقليل المخاطر\"],"` | — |
| [SRC-2C8F288796-L000552](../../web/workspace.html#L552) | 552 | `"  [\"المناطق المستهدفة\",\"locations\",\"القاهرة، الجيزة\"],"` | — |
| [SRC-2C8F288796-L000553](../../web/workspace.html#L553) | 553 | `"  [\"القطاعات\",\"industries\",\"المقاولات، التصنيع\"],"` | — |
| [SRC-2C8F288796-L000554](../../web/workspace.html#L554) | 554 | `"  [\"نوع العملاء\",\"customers\",\"مقاولون، ملاك مشروعات\"],"` | — |
| [SRC-2C8F288796-L000555](../../web/workspace.html#L555) | 555 | `"  [\"أدوار الشراء\",\"roles\",\"مدير مشتريات، مدير مشروع\"],"` | — |
| [SRC-2C8F288796-L000556](../../web/workspace.html#L556) | 556 | `"  [\"الاستثناءات\",\"exclusions\",\"القطاعات غير المناسبة\"]"` | — |
| [SRC-2C8F288796-L000557](../../web/workspace.html#L557) | 557 | `" ];"` | — |
| [SRC-2C8F288796-L000558](../../web/workspace.html#L558) | 558 | `" fields.forEach(([label,key,placeholder])=>{"` | — |
| [SRC-2C8F288796-L000559](../../web/workspace.html#L559) | 559 | `"  const item=textField(label,\"profile_\"+key,placeholder,\"\",false);"` | — |
| [SRC-2C8F288796-L000560](../../web/workspace.html#L560) | 560 | `"  controls[key]=item.control;if(!canWrite())item.control.disabled=true;grid.append(item.field);"` | — |
| [SRC-2C8F288796-L000561](../../web/workspace.html#L561) | 561 | `" });"` | — |
| [SRC-2C8F288796-L000562](../../web/workspace.html#L562) | 562 | `" const localeField=make(\"div\",\"field\"),locale=make(\"select\",\"\");"` | — |
| [SRC-2C8F288796-L000563](../../web/workspace.html#L563) | 563 | `" [[\"auto\",\"تلقائي\"],[\"ar\",\"العربية\"],[\"en\",\"الإنجليزية\"],[\"mixed\",\"العربية والإنجليزية\"]].forEach(([v,l])=>{const o=make(\"option\",\"\",l);o.value=v;locale.append(o)});"` | — |
| [SRC-2C8F288796-L000564](../../web/workspace.html#L564) | 564 | `" localeField.append(make(\"label\",\"\",\"لغة البحث\"),locale);controls.locale=locale;if(!canWrite())locale.disabled=true;grid.append(localeField);"` | — |
| [SRC-2C8F288796-L000565](../../web/workspace.html#L565) | 565 | `" panel.append(grid,make(\"p\",\"profile-note\",\"افصل القيم المتعددة بفاصلة. تُستخدم المرادفات والمناطق لصياغة استعلامات مرتبطة بالمنتج؛ تطابق ICP وحده لا يثبت وجود طلب.\"));"` | — |
| [SRC-2C8F288796-L000566](../../web/workspace.html#L566) | 566 | `" const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000567](../../web/workspace.html#L567) | 567 | `" const save=action(\"حفظ ملف المنتج والسوق\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000568](../../web/workspace.html#L568) | 568 | `"  save.disabled=true;"` | — |
| [SRC-2C8F288796-L000569](../../web/workspace.html#L569) | 569 | `"  try{"` | — |
| [SRC-2C8F288796-L000570](../../web/workspace.html#L570) | 570 | `"   const payload={"` | — |
| [SRC-2C8F288796-L000571](../../web/workspace.html#L571) | 571 | `"    product:{name:controls.name.value,aliases:csvValues(controls.aliases.value),category_path:csvValues(controls.category.value),use_cases:csvValues(controls.useCases.value),problems_solved:csvValues(controls.problems.value)},"` | — |
| [SRC-2C8F288796-L000572](../../web/workspace.html#L572) | 572 | `"    market:{locations:csvValues(controls.locations.value),industries:csvValues(controls.industries.value),customer_types:csvValues(controls.customers.value),decision_roles:csvValues(controls.roles.value),exclusions:csvValues(controls.exclusions.value)},"` | — |
| [SRC-2C8F288796-L000573](../../web/workspace.html#L573) | 573 | `"    locale:controls.locale.value"` | — |
| [SRC-2C8F288796-L000574](../../web/workspace.html#L574) | 574 | `"   };"` | — |
| [SRC-2C8F288796-L000575](../../web/workspace.html#L575) | 575 | `"   const result=await api(\"/api/product-profiles\",{method:\"POST\",body:payload});"` | — |
| [SRC-2C8F288796-L000576](../../web/workspace.html#L576) | 576 | `"   state.activeProfileId=result.id;await loadProductProfiles();renderProductProfile();"` | — |
| [SRC-2C8F288796-L000577](../../web/workspace.html#L577) | 577 | `"  }catch(error){panel.append(make(\"p\",\"auth-error\",escapeMessage(error.message)))}"` | — |
| [SRC-2C8F288796-L000578](../../web/workspace.html#L578) | 578 | `"  finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000579](../../web/workspace.html#L579) | 579 | `" });"` | — |
| [SRC-2C8F288796-L000580](../../web/workspace.html#L580) | 580 | `" save.disabled=!canWrite();actions.append(save);panel.append(actions);root.append(panel);"` | — |
| [SRC-2C8F288796-L000581](../../web/workspace.html#L581) | 581 | `" const listPanel=make(\"section\",\"glass panel profile-panel\"),lh=make(\"div\",\"panel-head\"),lt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000582](../../web/workspace.html#L582) | 582 | `" lt.append(make(\"h2\",\"\",\"ملفات المنتجات المحفوظة\"),make(\"p\",\"\",\"اختر ملفًا محفوظًا للانتقال إلى تشغيل الاكتشاف.\"));"` | — |
| [SRC-2C8F288796-L000583](../../web/workspace.html#L583) | 583 | `" lh.append(lt);listPanel.append(lh);"` | — |
| [SRC-2C8F288796-L000584](../../web/workspace.html#L584) | 584 | `" if(!state.profiles.length)listPanel.append(emptyState(\"لا توجد ملفات بعد\",\"أنشئ ملف المنتج والسوق ثم احفظه.\"));"` | — |
| [SRC-2C8F288796-L000585](../../web/workspace.html#L585) | 585 | `" else{"` | — |
| [SRC-2C8F288796-L000586](../../web/workspace.html#L586) | 586 | `"  const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000587](../../web/workspace.html#L587) | 587 | `"  state.profiles.forEach(profile=>{"` | — |
| [SRC-2C8F288796-L000588](../../web/workspace.html#L588) | 588 | `"   const card=make(\"article\",\"signal-card\"),p=profile.profile\|\|{},m=p.market\|\|{};"` | — |
| [SRC-2C8F288796-L000589](../../web/workspace.html#L589) | 589 | `"   card.append(make(\"strong\",\"\",profile.name\|\|\"منتج\"));"` | — |
| [SRC-2C8F288796-L000590](../../web/workspace.html#L590) | 590 | `"   card.append(make(\"p\",\"subtle\",\"المناطق: \"+((m.locations\|\|[]).join(\"، \")\|\|\"غير محددة\")));"` | — |
| [SRC-2C8F288796-L000591](../../web/workspace.html#L591) | 591 | `"   const row=make(\"div\",\"form-actions\");row.append(action(\"استخدام في الاكتشاف\",\"\",()=>{state.activeProfileId=profile.id;navigate(\"campaign\")}));"` | — |
| [SRC-2C8F288796-L000592](../../web/workspace.html#L592) | 592 | `"   card.append(row);list.append(card);"` | — |
| [SRC-2C8F288796-L000593](../../web/workspace.html#L593) | 593 | `"  });listPanel.append(list);"` | — |
| [SRC-2C8F288796-L000594](../../web/workspace.html#L594) | 594 | `" }"` | — |
| [SRC-2C8F288796-L000595](../../web/workspace.html#L595) | 595 | `" root.append(listPanel);"` | — |
| [SRC-2C8F288796-L000596](../../web/workspace.html#L596) | 596 | `"}"` | — |
| [SRC-2C8F288796-L000597](../../web/workspace.html#L597) | 597 | `"function renderDiscoveryRun(run){"` | — |
| [SRC-2C8F288796-L000598](../../web/workspace.html#L598) | 598 | `" const panel=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000599](../../web/workspace.html#L599) | 599 | `" const report=run.search_report\|\|{},leadReport=report.lead_generation\|\|{},sources=Array.isArray(run.sources)?run.sources:[];"` | — |
| [SRC-2C8F288796-L000600](../../web/workspace.html#L600) | 600 | `" title.append(make(\"h2\",\"\",\"نتيجة عملية الاكتشاف\"),make(\"p\",\"\",\"ملف المنتج: \"+String(run.profile_name\|\|\"غير محدد\")+\" · \"+String(run.created_at\|\|\"\")));"` | — |
| [SRC-2C8F288796-L000601](../../web/workspace.html#L601) | 601 | `" head.append(title);panel.append(head);"` | — |
| [SRC-2C8F288796-L000602](../../web/workspace.html#L602) | 602 | `" const stats=make(\"div\",\"stats\"),qualifiedCount=sources.filter(s=>s.lead_qualification===\"public_demand_signal\").length;"` | — |
| [SRC-2C8F288796-L000603](../../web/workspace.html#L603) | 603 | `" stats.append("` | — |
| [SRC-2C8F288796-L000604](../../web/workspace.html#L604) | 604 | `"  buildStat(\"إشارات طلب مؤهلة\",leadReport.candidate_signal_count??qualifiedCount,\"إشارات تحمل عبارة طلب معلنة\",\"glow-teal\"),"` | — |
| [SRC-2C8F288796-L000605](../../web/workspace.html#L605) | 605 | `"  buildStat(\"المصادر التي راجعتها الجولة\",leadReport.related_results_reviewed??sources.length,\"لا يعني ذلك اكتمال السوق\",\"glow-blue\"),"` | — |
| [SRC-2C8F288796-L000606](../../web/workspace.html#L606) | 606 | `"  buildStat(\"حالة تشغيل البحث\",report.pipeline_completion_status\|\|\"غير معلومة\",\"حالة المسار كما أعادها الوكيل\",\"glow-amber\")"` | — |
| [SRC-2C8F288796-L000607](../../web/workspace.html#L607) | 607 | `" );"` | — |
| [SRC-2C8F288796-L000608](../../web/workspace.html#L608) | 608 | `" panel.append(stats,make(\"p\",\"profile-note\",run.answer\|\|\"لا يوجد ملخص لهذه العملية.\"));"` | — |
| [SRC-2C8F288796-L000609](../../web/workspace.html#L609) | 609 | `" if(Array.isArray(run.search_queries)&&run.search_queries.length){const qs=make(\"div\",\"query-list\");run.search_queries.forEach(q=>qs.append(tag(q)));panel.append(qs)}"` | — |
| [SRC-2C8F288796-L000610](../../web/workspace.html#L610) | 610 | `" const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000611](../../web/workspace.html#L611) | 611 | `" if(!sources.length)list.append(emptyState(\"لم تُعد العملية مصادر قابلة للعرض\",\"راجع حالة التشغيل والتحذيرات؛ هذا لا يثبت عدم وجود طلب.\"));"` | — |
| [SRC-2C8F288796-L000612](../../web/workspace.html#L612) | 612 | `" sources.forEach((source,index)=>{"` | — |
| [SRC-2C8F288796-L000613](../../web/workspace.html#L613) | 613 | `"  const qualified=source.lead_qualification===\"public_demand_signal\";"` | — |
| [SRC-2C8F288796-L000614](../../web/workspace.html#L614) | 614 | `"  const card=make(\"article\",\"discovery-source\"+(qualified?\" qualified\":\"\")),meta=make(\"div\",\"discovery-source-meta\");"` | — |
| [SRC-2C8F288796-L000615](../../web/workspace.html#L615) | 615 | `"  meta.append(tag(qualified?\"إشارة طلب معلنة\":\"نتيجة مرتبطة فقط\",qualified?\"teal\":\"\"));"` | — |
| [SRC-2C8F288796-L000616](../../web/workspace.html#L616) | 616 | `"  if(source.platform)meta.append(tag(source.platform));"` | — |
| [SRC-2C8F288796-L000617](../../web/workspace.html#L617) | 617 | `"  meta.append(tag(source.page_fetched?\"تمت قراءة الصفحة\":\"مقتطف/عنوان فقط\"));"` | — |
| [SRC-2C8F288796-L000618](../../web/workspace.html#L618) | 618 | `"  card.append(meta,make(\"h3\",\"\",source.title\|\|\"نتيجة ويب\"));"` | — |
| [SRC-2C8F288796-L000619](../../web/workspace.html#L619) | 619 | `"  if(source.snippet)card.append(make(\"p\",\"\",source.snippet));"` | — |
| [SRC-2C8F288796-L000620](../../web/workspace.html#L620) | 620 | `"  const evidence=source.lead_intent_evidence;"` | — |
| [SRC-2C8F288796-L000621](../../web/workspace.html#L621) | 621 | `"  if(qualified&&evidence){"` | — |
| [SRC-2C8F288796-L000622](../../web/workspace.html#L622) | 622 | `"   card.append(make(\"p\",\"\",\"عبارة الدليل: \"+String(evidence.phrase\|\|\"غير محددة\")));"` | — |
| [SRC-2C8F288796-L000623](../../web/workspace.html#L623) | 623 | `"   card.append(make(\"p\",\"\",\"نوع الإشارة: \"+String(evidence.signal_type\|\|\"غير محدد\")+\" · أساس النص: \"+String(evidence.basis\|\|\"غير محدد\")));"` | — |
| [SRC-2C8F288796-L000624](../../web/workspace.html#L624) | 624 | `"   card.append(make(\"p\",\"discovery-note\",\"ملاءمة المنتج لم تُحسم من العبارة وحدها؛ راجع المصدر قبل اعتماد الفرصة.\"));"` | — |
| [SRC-2C8F288796-L000625](../../web/workspace.html#L625) | 625 | `"  }else card.append(make(\"p\",\"discovery-note\",\"لم يعثر المحرك على عبارة كافية تثبت طلب شراء. لن تُحفظ هذه النتيجة كإشارة طلب من هذه الشاشة.\"));"` | — |
| [SRC-2C8F288796-L000626](../../web/workspace.html#L626) | 626 | `"  card.append(make(\"p\",\"discovery-note\",\"تاريخ النشر: \"+String(source.published_at\|\|\"غير متاح من المصدر\")));"` | — |
| [SRC-2C8F288796-L000627](../../web/workspace.html#L627) | 627 | `"  const url=safeHttp(source.url);if(url){const link=make(\"a\",\"\",url);link.href=url;link.target=\"_blank\";link.rel=\"noopener noreferrer\";card.append(link)}"` | — |
| [SRC-2C8F288796-L000628](../../web/workspace.html#L628) | 628 | `"  if(qualified&&canWrite()){"` | — |
| [SRC-2C8F288796-L000629](../../web/workspace.html#L629) | 629 | `"   const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000630](../../web/workspace.html#L630) | 630 | `"   const save=action(\"حفظ الإشارة في صندوق الطلب\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000631](../../web/workspace.html#L631) | 631 | `"    save.disabled=true;"` | — |
| [SRC-2C8F288796-L000632](../../web/workspace.html#L632) | 632 | `"    try{"` | — |
| [SRC-2C8F288796-L000633](../../web/workspace.html#L633) | 633 | `"     const response=await api(\"/api/discoveries/\"+encodeURIComponent(run.id)+\"/signals/\"+index+\"/save\",{method:\"POST\",body:{}});"` | — |
| [SRC-2C8F288796-L000634](../../web/workspace.html#L634) | 634 | `"     save.textContent=response.created?\"تم الحفظ\":\"الإشارة موجودة بالفعل\";"` | — |
| [SRC-2C8F288796-L000635](../../web/workspace.html#L635) | 635 | `"     await loadLeads();"` | — |
| [SRC-2C8F288796-L000636](../../web/workspace.html#L636) | 636 | `"    }catch(error){card.append(make(\"p\",\"auth-error\",escapeMessage(error.message)))}"` | — |
| [SRC-2C8F288796-L000637](../../web/workspace.html#L637) | 637 | `"    finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000638](../../web/workspace.html#L638) | 638 | `"   });"` | — |
| [SRC-2C8F288796-L000639](../../web/workspace.html#L639) | 639 | `"   actions.append(save);card.append(actions);"` | — |
| [SRC-2C8F288796-L000640](../../web/workspace.html#L640) | 640 | `"  }"` | — |
| [SRC-2C8F288796-L000641](../../web/workspace.html#L641) | 641 | `"  list.append(card);"` | — |
| [SRC-2C8F288796-L000642](../../web/workspace.html#L642) | 642 | `" });"` | — |
| [SRC-2C8F288796-L000643](../../web/workspace.html#L643) | 643 | `" panel.append(list);return panel;"` | — |
| [SRC-2C8F288796-L000644](../../web/workspace.html#L644) | 644 | `"}"` | — |
| [SRC-2C8F288796-L000645](../../web/workspace.html#L645) | 645 | `"function renderDiscovery(){"` | — |
| [SRC-2C8F288796-L000646](../../web/workspace.html#L646) | 646 | `" setPage(\"حملات الاكتشاف\",\"ابحث عن إشارات طلب شراء أو توريد معلنة مرتبطة بملف المنتج والسوق. لا تُعرض النتائج العامة كعملاء محتملين.\",\"BUYER INTENT DISCOVERY\");"` | — |
| [SRC-2C8F288796-L000647](../../web/workspace.html#L647) | 647 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000648](../../web/workspace.html#L648) | 648 | `" const controls=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000649](../../web/workspace.html#L649) | 649 | `" title.append(make(\"h2\",\"\",\"تشغيل اكتشاف جديد\"),make(\"p\",\"\",\"يستخدم محرك البحث الحالي ويولّد الاستعلامات من ملف المنتج المحفوظ.\"));"` | — |
| [SRC-2C8F288796-L000650](../../web/workspace.html#L650) | 650 | `" head.append(title);controls.append(head);"` | — |
| [SRC-2C8F288796-L000651](../../web/workspace.html#L651) | 651 | `" if(!state.profiles.length){"` | — |
| [SRC-2C8F288796-L000652](../../web/workspace.html#L652) | 652 | `"  controls.append(emptyState(\"لا يوجد ملف منتج محفوظ\",\"أنشئ ملف المنتج والسوق قبل تشغيل الاكتشاف.\"));"` | — |
| [SRC-2C8F288796-L000653](../../web/workspace.html#L653) | 653 | `"  controls.append(action(\"إنشاء ملف المنتج ←\",\"primary\",()=>navigate(\"offer\")));"` | — |
| [SRC-2C8F288796-L000654](../../web/workspace.html#L654) | 654 | `" }else{"` | — |
| [SRC-2C8F288796-L000655](../../web/workspace.html#L655) | 655 | `"  const field=make(\"div\",\"field\"),profileSelect=make(\"select\",\"\");"` | — |
| [SRC-2C8F288796-L000656](../../web/workspace.html#L656) | 656 | `"  state.profiles.forEach(profile=>{const option=make(\"option\",\"\",profile.name);option.value=profile.id;option.selected=profile.id===state.activeProfileId;profileSelect.append(option)});"` | — |
| [SRC-2C8F288796-L000657](../../web/workspace.html#L657) | 657 | `"  field.append(make(\"label\",\"\",\"ملف المنتج والسوق\"),profileSelect);controls.append(field);"` | — |
| [SRC-2C8F288796-L000658](../../web/workspace.html#L658) | 658 | `"  const consent=make(\"label\",\"consent-row\"),optional=make(\"input\",\"\");optional.type=\"checkbox\";optional.checked=false;optional.disabled=state.role!==\"owner\";"` | — |
| [SRC-2C8F288796-L000659](../../web/workspace.html#L659) | 659 | `"  consent.append(optional,make(\"span\",\"\",\"السماح بالموصلات الاختيارية (DeepSeek Search وBrave وTavily وبعض واجهات المنصات الرسمية). قد تستهلك حصصًا أو تكلفة؛ تبقى معطلة افتراضيًا ولا يستطيع تفعيلها إلا مالك مساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000660](../../web/workspace.html#L660) | 660 | `"  controls.append(consent);"` | — |
| [SRC-2C8F288796-L000661](../../web/workspace.html#L661) | 661 | `"  const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000662](../../web/workspace.html#L662) | 662 | `"  const run=action(\"بدء اكتشاف الطلب\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000663](../../web/workspace.html#L663) | 663 | `"   run.disabled=true;state.activeProfileId=profileSelect.value;"` | — |
| [SRC-2C8F288796-L000664](../../web/workspace.html#L664) | 664 | `"   root.append(emptyState(\"جارٍ البحث عن إشارات الطلب\",\"قد تستغرق الجولة وقتًا حسب استجابة الموصلات.\"));"` | — |
| [SRC-2C8F288796-L000665](../../web/workspace.html#L665) | 665 | `"   try{"` | — |
| [SRC-2C8F288796-L000666](../../web/workspace.html#L666) | 666 | `"    state.activeDiscovery=await api(\"/api/discoveries\",{method:\"POST\",body:{profile_id:profileSelect.value,allow_optional_providers:optional.checked}});"` | — |
| [SRC-2C8F288796-L000667](../../web/workspace.html#L667) | 667 | `"    await loadDiscoveryRuns();renderDiscovery();"` | — |
| [SRC-2C8F288796-L000668](../../web/workspace.html#L668) | 668 | `"   }catch(error){root.append(make(\"p\",\"auth-error\",escapeMessage(error.message)))}"` | — |
| [SRC-2C8F288796-L000669](../../web/workspace.html#L669) | 669 | `"   finally{run.disabled=false}"` | — |
| [SRC-2C8F288796-L000670](../../web/workspace.html#L670) | 670 | `"  });"` | — |
| [SRC-2C8F288796-L000671](../../web/workspace.html#L671) | 671 | `"  run.disabled=!canWrite();actions.append(run);controls.append(actions);"` | — |
| [SRC-2C8F288796-L000672](../../web/workspace.html#L672) | 672 | `" }"` | — |
| [SRC-2C8F288796-L000673](../../web/workspace.html#L673) | 673 | `" controls.append(make(\"p\",\"profile-note\",\"تاريخ النشر قد يكون غير متاح. المقتطف لا يعني أن الصفحة قُرئت. فشل الموصل لا يثبت عدم وجود عملاء. لا يتم إرسال أي رسالة من هذه الشاشة.\"));"` | — |
| [SRC-2C8F288796-L000674](../../web/workspace.html#L674) | 674 | `" controls.append(make(\"p\",\"profile-note\",\"تشغيل الاكتشاف يستخدم النموذج اللغوي المهيأ حاليًا في Omarai؛ قد يستهلك حصة أو تكلفة بحسب إعدادات مزود النموذج. لا تدخل بيانات سرية. الموصلات الاختيارية منفصلة وتظل معطلة افتراضيًا حتى موافقة المالك.\"));"` | — |
| [SRC-2C8F288796-L000675](../../web/workspace.html#L675) | 675 | `" root.append(controls);"` | — |
| [SRC-2C8F288796-L000676](../../web/workspace.html#L676) | 676 | `" if(state.discoveryRuns.length){"` | — |
| [SRC-2C8F288796-L000677](../../web/workspace.html#L677) | 677 | `"  const history=make(\"section\",\"glass panel profile-panel\"),hh=make(\"div\",\"panel-head\"),ht=make(\"div\");"` | — |
| [SRC-2C8F288796-L000678](../../web/workspace.html#L678) | 678 | `"  ht.append(make(\"h2\",\"\",\"سجل عمليات الاكتشاف\"),make(\"p\",\"\",\"عمليات محفوظة ضمن مساحة العمل الحالية.\"));"` | — |
| [SRC-2C8F288796-L000679](../../web/workspace.html#L679) | 679 | `"  hh.append(ht);history.append(hh);const list=make(\"div\",\"discovery-history\");"` | — |
| [SRC-2C8F288796-L000680](../../web/workspace.html#L680) | 680 | `"  state.discoveryRuns.forEach(item=>list.append(action("` | — |
| [SRC-2C8F288796-L000681](../../web/workspace.html#L681) | 681 | `"   String(item.profile_name\|\|\"ملف منتج\")+\" · \"+String(item.qualified_signal_count\|\|0)+\" إشارة · \"+String(item.created_at\|\|\"\"),"` | — |
| [SRC-2C8F288796-L000682](../../web/workspace.html#L682) | 682 | `"   \"\","` | — |
| [SRC-2C8F288796-L000683](../../web/workspace.html#L683) | 683 | `"   async()=>{try{state.activeDiscovery=await api(\"/api/discoveries/\"+encodeURIComponent(item.id));renderDiscovery()}catch(error){history.append(make(\"p\",\"auth-error\",escapeMessage(error.message)))}}"` | — |
| [SRC-2C8F288796-L000684](../../web/workspace.html#L684) | 684 | `"  )));"` | — |
| [SRC-2C8F288796-L000685](../../web/workspace.html#L685) | 685 | `"  history.append(list);root.append(history);"` | — |
| [SRC-2C8F288796-L000686](../../web/workspace.html#L686) | 686 | `" }"` | — |
| [SRC-2C8F288796-L000687](../../web/workspace.html#L687) | 687 | `" if(state.activeDiscovery)root.append(renderDiscoveryRun(state.activeDiscovery));"` | — |
| [SRC-2C8F288796-L000688](../../web/workspace.html#L688) | 688 | `"}"` | — |
| [SRC-2C8F288796-L000689](../../web/workspace.html#L689) | 689 | `"function renderCurrent(){"` | — |
| [SRC-2C8F288796-L000690](../../web/workspace.html#L690) | 690 | `" renderNav();"` | — |
| [SRC-2C8F288796-L000691](../../web/workspace.html#L691) | 691 | `" if(state.activeView===\"overview\")renderOverview();"` | — |
| [SRC-2C8F288796-L000692](../../web/workspace.html#L692) | 692 | `" else if(state.activeView===\"offer\")renderProductProfile();"` | — |
| [SRC-2C8F288796-L000693](../../web/workspace.html#L693) | 693 | `" else if(state.activeView===\"campaign\")renderDiscovery();"` | — |
| [SRC-2C8F288796-L000694](../../web/workspace.html#L694) | 694 | `" else if(state.activeView===\"signals\")renderSignals();"` | — |
| [SRC-2C8F288796-L000695](../../web/workspace.html#L695) | 695 | `" else if(state.activeView===\"pipeline\")renderPipeline();"` | — |
| [SRC-2C8F288796-L000696](../../web/workspace.html#L696) | 696 | `" else if(state.activeView===\"system\")renderSystem();"` | — |
| [SRC-2C8F288796-L000697](../../web/workspace.html#L697) | 697 | `" else renderPlaceholder(state.activeView);"` | — |
| [SRC-2C8F288796-L000698](../../web/workspace.html#L698) | 698 | `" if(state.loadWarnings.length){"` | — |
| [SRC-2C8F288796-L000699](../../web/workspace.html#L699) | 699 | `"  $(\"viewRoot\").prepend(make(\"p\",\"auth-error\",\"تم التحقق من الجلسة؛ تعذر تحميل بعض البيانات: \"+state.loadWarnings.join(\"، \")+\". قد تكون بعض القوائم والأرقام غير مكتملة.\"));"` | — |
| [SRC-2C8F288796-L000700](../../web/workspace.html#L700) | 700 | `" }"` | — |
| [SRC-2C8F288796-L000701](../../web/workspace.html#L701) | 701 | `"}"` | — |
| [SRC-2C8F288796-L000702](../../web/workspace.html#L702) | 702 | `"function navigate(view){"` | — |
| [SRC-2C8F288796-L000703](../../web/workspace.html#L703) | 703 | `" state.activeView=view;renderCurrent();"` | — |
| [SRC-2C8F288796-L000704](../../web/workspace.html#L704) | 704 | `"}"` | — |
| [SRC-2C8F288796-L000705](../../web/workspace.html#L705) | 705 | `"async function loadProductProfiles(){"` | — |
| [SRC-2C8F288796-L000706](../../web/workspace.html#L706) | 706 | `" const data=await api(\"/api/product-profiles\");"` | — |
| [SRC-2C8F288796-L000707](../../web/workspace.html#L707) | 707 | `" state.profiles=Array.isArray(data.profiles)?data.profiles:[];"` | — |
| [SRC-2C8F288796-L000708](../../web/workspace.html#L708) | 708 | `" if(!state.profiles.some(item=>item.id===state.activeProfileId))state.activeProfileId=state.profiles[0]?.id\|\|null;"` | — |
| [SRC-2C8F288796-L000709](../../web/workspace.html#L709) | 709 | `"}"` | — |
| [SRC-2C8F288796-L000710](../../web/workspace.html#L710) | 710 | `"async function loadDiscoveryRuns(){"` | — |
| [SRC-2C8F288796-L000711](../../web/workspace.html#L711) | 711 | `" const data=await api(\"/api/discoveries\");"` | — |
| [SRC-2C8F288796-L000712](../../web/workspace.html#L712) | 712 | `" state.discoveryRuns=Array.isArray(data.runs)?data.runs:[];"` | — |
| [SRC-2C8F288796-L000713](../../web/workspace.html#L713) | 713 | `"}"` | — |
| [SRC-2C8F288796-L000714](../../web/workspace.html#L714) | 714 | `"async function loadLeads(){"` | — |
| [SRC-2C8F288796-L000715](../../web/workspace.html#L715) | 715 | `" const data=await api(\"/api/leads?limit=500\");"` | — |
| [SRC-2C8F288796-L000716](../../web/workspace.html#L716) | 716 | `" state.leads=Array.isArray(data.leads)?data.leads:[];"` | — |
| [SRC-2C8F288796-L000717](../../web/workspace.html#L717) | 717 | `"}"` | — |
| [SRC-2C8F288796-L000718](../../web/workspace.html#L718) | 718 | `"async function bootstrap(){"` | — |
| [SRC-2C8F288796-L000719](../../web/workspace.html#L719) | 719 | `" let session;"` | — |
| [SRC-2C8F288796-L000720](../../web/workspace.html#L720) | 720 | `" try{"` | — |
| [SRC-2C8F288796-L000721](../../web/workspace.html#L721) | 721 | `"  session=await api(\"/api/session\");"` | — |
| [SRC-2C8F288796-L000722](../../web/workspace.html#L722) | 722 | `" }catch(e){"` | — |
| [SRC-2C8F288796-L000723](../../web/workspace.html#L723) | 723 | `"  setConnection(false,\"يلزم تسجيل الدخول\",\"تعذر التحقق من جلسة المستخدم.\");"` | — |
| [SRC-2C8F288796-L000724](../../web/workspace.html#L724) | 724 | `"  showAuth(e.message);"` | — |
| [SRC-2C8F288796-L000725](../../web/workspace.html#L725) | 725 | `"  $(\"viewRoot\").replaceChildren(emptyState(\"مساحة العمل مقفلة\",\"سجّل الدخول لقراءة البيانات المرتبطة بمساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000726](../../web/workspace.html#L726) | 726 | `"  return;"` | — |
| [SRC-2C8F288796-L000727](../../web/workspace.html#L727) | 727 | `" }"` | — |
| [SRC-2C8F288796-L000728](../../web/workspace.html#L728) | 728 | `" state.role=session.role\|\|\"unknown\";"` | — |
| [SRC-2C8F288796-L000729](../../web/workspace.html#L729) | 729 | `" $(\"rolePill\").textContent=\"صلاحية: \"+state.role;"` | — |
| [SRC-2C8F288796-L000730](../../web/workspace.html#L730) | 730 | `" $(\"roleSummary\").textContent=\"الدور: \"+state.role+(canWrite()?\" — إضافة وتحديث السجلات متاح.\":\" — قراءة فقط.\");"` | — |
| [SRC-2C8F288796-L000731](../../web/workspace.html#L731) | 731 | `" hideAuth();"` | — |
| [SRC-2C8F288796-L000732](../../web/workspace.html#L732) | 732 | `" const results=await Promise.allSettled(["` | — |
| [SRC-2C8F288796-L000733](../../web/workspace.html#L733) | 733 | `"  loadLeads(),"` | — |
| [SRC-2C8F288796-L000734](../../web/workspace.html#L734) | 734 | `"  loadProductProfiles(),"` | — |
| [SRC-2C8F288796-L000735](../../web/workspace.html#L735) | 735 | `"  loadDiscoveryRuns()"` | — |
| [SRC-2C8F288796-L000736](../../web/workspace.html#L736) | 736 | `" ]);"` | — |
| [SRC-2C8F288796-L000737](../../web/workspace.html#L737) | 737 | `" if($(\"authGate\").classList.contains(\"open\")){"` | — |
| [SRC-2C8F288796-L000738](../../web/workspace.html#L738) | 738 | `"  setConnection(false,\"يلزم تسجيل الدخول\",\"انتهت الجلسة أثناء تحميل البيانات.\");"` | — |
| [SRC-2C8F288796-L000739](../../web/workspace.html#L739) | 739 | `"  $(\"viewRoot\").replaceChildren(emptyState(\"مساحة العمل مقفلة\",\"سجّل الدخول لقراءة البيانات المرتبطة بمساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000740](../../web/workspace.html#L740) | 740 | `"  return;"` | — |
| [SRC-2C8F288796-L000741](../../web/workspace.html#L741) | 741 | `" }"` | — |
| [SRC-2C8F288796-L000742](../../web/workspace.html#L742) | 742 | `" state.loadWarnings=[];"` | — |
| [SRC-2C8F288796-L000743](../../web/workspace.html#L743) | 743 | `" const labels=[\"سجل الإشارات\",\"ملفات المنتجات\",\"سجل الاكتشاف\"];"` | — |
| [SRC-2C8F288796-L000744](../../web/workspace.html#L744) | 744 | `" results.forEach((result,index)=>{"` | — |
| [SRC-2C8F288796-L000745](../../web/workspace.html#L745) | 745 | `"  if(result.status!==\"rejected\")return;"` | — |
| [SRC-2C8F288796-L000746](../../web/workspace.html#L746) | 746 | `"  state.loadWarnings.push(labels[index]);"` | — |
| [SRC-2C8F288796-L000747](../../web/workspace.html#L747) | 747 | `"  if(index===0)state.leads=[];"` | — |
| [SRC-2C8F288796-L000748](../../web/workspace.html#L748) | 748 | `"  else if(index===1)state.profiles=[];"` | — |
| [SRC-2C8F288796-L000749](../../web/workspace.html#L749) | 749 | `"  else state.discoveryRuns=[];"` | — |
| [SRC-2C8F288796-L000750](../../web/workspace.html#L750) | 750 | `" });"` | — |
| [SRC-2C8F288796-L000751](../../web/workspace.html#L751) | 751 | `" const note=state.loadWarnings.length"` | — |
| [SRC-2C8F288796-L000752](../../web/workspace.html#L752) | 752 | `"  ?\"الجلسة مصادق عليها؛ تعذر تحميل بعض البيانات: \"+state.loadWarnings.join(\"، \")+\". حاول تحديث الوحدة لاحقًا.\""` | — |
| [SRC-2C8F288796-L000753](../../web/workspace.html#L753) | 753 | `"  :\"تم تحميل الإشارات وملفات المنتج وسجل الاكتشاف. هذا لا يثبت اتصال جميع الموصلات.\";"` | — |
| [SRC-2C8F288796-L000754](../../web/workspace.html#L754) | 754 | `" setConnection(true,state.loadWarnings.length?\"الجلسة مصادق عليها — بيانات جزئية\":\"الجلسة مصادق عليها\",note);"` | — |
| [SRC-2C8F288796-L000755](../../web/workspace.html#L755) | 755 | `" renderCurrent();"` | — |
| [SRC-2C8F288796-L000756](../../web/workspace.html#L756) | 756 | `"}"` | — |
| [SRC-2C8F288796-L000757](../../web/workspace.html#L757) | 757 | `"$(\"loginForm\").addEventListener(\"submit\",async event=>{"` | — |
| [SRC-2C8F288796-L000758](../../web/workspace.html#L758) | 758 | `" event.preventDefault();const token=$(\"accessToken\").value.trim();const button=$(\"loginButton\");button.disabled=true;$(\"authError\").textContent=\"\";"` | — |
| [SRC-2C8F288796-L000759](../../web/workspace.html#L759) | 759 | `" try{"` | — |
| [SRC-2C8F288796-L000760](../../web/workspace.html#L760) | 760 | `"  await api(\"/api/session\",{method:\"POST\",body:{access_token:token}});"` | — |
| [SRC-2C8F288796-L000761](../../web/workspace.html#L761) | 761 | `"  $(\"accessToken\").value=\"\";await bootstrap();"` | — |
| [SRC-2C8F288796-L000762](../../web/workspace.html#L762) | 762 | `" }catch(e){$(\"authError\").textContent=escapeMessage(e.message)}"` | — |
| [SRC-2C8F288796-L000763](../../web/workspace.html#L763) | 763 | `" finally{button.disabled=false}"` | — |
| [SRC-2C8F288796-L000764](../../web/workspace.html#L764) | 764 | `"});"` | — |
| [SRC-2C8F288796-L000765](../../web/workspace.html#L765) | 765 | `"$(\"logoutButton\").addEventListener(\"click\",async()=>{"` | — |
| [SRC-2C8F288796-L000766](../../web/workspace.html#L766) | 766 | `" try{"` | — |
| [SRC-2C8F288796-L000767](../../web/workspace.html#L767) | 767 | `"  await api(\"/api/session/logout\",{method:\"POST\",body:{}});"` | — |
| [SRC-2C8F288796-L000768](../../web/workspace.html#L768) | 768 | `" }catch(e){"` | — |
| [SRC-2C8F288796-L000769](../../web/workspace.html#L769) | 769 | `"  alert(\"تعذر تسجيل الخروج من الخادم؛ لم يتم تغيير حالة الجلسة في الواجهة. \"+escapeMessage(e.message));"` | — |
| [SRC-2C8F288796-L000770](../../web/workspace.html#L770) | 770 | `"  return;"` | — |
| [SRC-2C8F288796-L000771](../../web/workspace.html#L771) | 771 | `" }"` | — |
| [SRC-2C8F288796-L000772](../../web/workspace.html#L772) | 772 | `" state.role=null;state.leads=[];state.profiles=[];state.discoveryRuns=[];state.loadWarnings=[];state.activeDiscovery=null;state.activeProfileId=null;state.activeView=\"overview\";showAuth(\"تم تسجيل الخروج. أدخل رمز الوصول للمتابعة.\");setConnection(false,\"غير متصل\",\"سجّل الدخول لعرض السجلات.\");"` | — |
| [SRC-2C8F288796-L000773](../../web/workspace.html#L773) | 773 | `"});"` | — |
| [SRC-2C8F288796-L000774](../../web/workspace.html#L774) | 774 | `"$(\"addSignalTop\").addEventListener(\"click\",()=>navigate(\"signals\"));"` | — |
| [SRC-2C8F288796-L000775](../../web/workspace.html#L775) | 775 | `"$(\"closeDetail\").addEventListener(\"click\",closeDetails);"` | — |
| [SRC-2C8F288796-L000776](../../web/workspace.html#L776) | 776 | `"$(\"detailDrawer\").addEventListener(\"click\",e=>{if(e.target===$(\"detailDrawer\"))closeDetails()});"` | — |
| [SRC-2C8F288796-L000777](../../web/workspace.html#L777) | 777 | `"document.addEventListener(\"keydown\",e=>{if(e.key===\"Escape\")closeDetails()});"` | — |
| [SRC-2C8F288796-L000778](../../web/workspace.html#L778) | 778 | `"renderNav();bootstrap();"` | — |
| [SRC-2C8F288796-L000779](../../web/workspace.html#L779) | 779 | `"})();"` | — |
| [SRC-2C8F288796-L000780](../../web/workspace.html#L780) | 780 | `"</script>"` | — |
| [SRC-2C8F288796-L000781](../../web/workspace.html#L781) | 781 | `"</body>"` | — |
| [SRC-2C8F288796-L000782](../../web/workspace.html#L782) | 782 | `"</html>"` | — |
