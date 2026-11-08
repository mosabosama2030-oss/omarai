# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **065**
- سجلات الأسطر: **493**
- النطاق: SRC-2C8F288796-L000530 إلى SRC-2C8F288796-L001022
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2C8F288796-L000530](../../web/workspace.html#L530) | 530 | `"   result.replaceChildren(make(\"p\",\"tag teal\",response.created?\"تم حفظ الإشارة.\":\"هذه الإشارة موجودة بالفعل ولم تُكرر.\"));"` | — |
| [SRC-2C8F288796-L000531](../../web/workspace.html#L531) | 531 | `"   state.analysis=null;text.value=\"\";url.value=\"\";note.value=\"\";await loadLeads();renderSignals();"` | — |
| [SRC-2C8F288796-L000532](../../web/workspace.html#L532) | 532 | `"  }catch(e){result.append(make(\"p\",\"auth-error\",escapeMessage(e.message)))}"` | — |
| [SRC-2C8F288796-L000533](../../web/workspace.html#L533) | 533 | `"  finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000534](../../web/workspace.html#L534) | 534 | `" });"` | — |
| [SRC-2C8F288796-L000535](../../web/workspace.html#L535) | 535 | `" buttons.append(analyze,save);wrapper.append(buttons,result);return wrapper;"` | — |
| [SRC-2C8F288796-L000536](../../web/workspace.html#L536) | 536 | `"}"` | — |
| [SRC-2C8F288796-L000537](../../web/workspace.html#L537) | 537 | `"function renderPipeline(){"` | — |
| [SRC-2C8F288796-L000538](../../web/workspace.html#L538) | 538 | `" setPage(\"مسار التأهيل\",\"يعرض المسار الحالات المحفوظة فعليًا، ويمكن تحديث الحالة بعد مراجعة الدليل. لا توجد مراحل CRM غير مدعومة في الخادم.\",\"QUALIFICATION PIPELINE\");"` | — |
| [SRC-2C8F288796-L000539](../../web/workspace.html#L539) | 539 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000540](../../web/workspace.html#L540) | 540 | `" const panel=make(\"section\",\"glass panel\");const head=make(\"div\",\"panel-head\");const title=make(\"div\");title.append(make(\"h2\",\"\",\"حالة كل إشارة\"),make(\"p\",\"\",\"اختر بطاقة لفتح المصدر وتقييم القواعد وتغيير الحالة المسموح بها.\"));head.append(title,action(\"صندوق الإشارات ←\",\"ghost\",()=>navigate(\"signals\")));panel.append(head);"` | — |
| [SRC-2C8F288796-L000541](../../web/workspace.html#L541) | 541 | `" const board=make(\"div\",\"pipeline\");const groups=[[\"نشطة جديدة\",[\"new\",\"needs_review\"]],[\"مؤهلة / متابعة\",[\"qualified\",\"contacted\"]],[\"مغلقة\",[\"converted\",\"rejected\"]]];"` | — |
| [SRC-2C8F288796-L000542](../../web/workspace.html#L542) | 542 | `" groups.forEach(([name,ids])=>{const col=make(\"section\",\"pipeline-col\");const rows=state.leads.filter(l=>ids.includes(l.status));col.append(make(\"h3\",\"\",name+\" · \"+rows.length));if(!rows.length)col.append(make(\"p\",\"subtle\",\"لا توجد سجلات في هذه المجموعة.\"));rows.forEach(l=>{const item=make(\"button\",\"pipeline-item\",String(l.text\|\|\"\").slice(0,115));item.type=\"button\";item.addEventListener(\"click\",()=>openDetails(l));col.append(item)});board.append(col)});"` | — |
| [SRC-2C8F288796-L000543](../../web/workspace.html#L543) | 543 | `" panel.append(board);root.append(panel);"` | — |
| [SRC-2C8F288796-L000544](../../web/workspace.html#L544) | 544 | `"}"` | — |
| [SRC-2C8F288796-L000545](../../web/workspace.html#L545) | 545 | `"async function renderSystem(){"` | — |
| [SRC-2C8F288796-L000546](../../web/workspace.html#L546) | 546 | `" setPage(\"حالات النظام\",\"لقطة إعدادات يقرأها الخادم محليًا. لا تنفذ هذه الشاشة اتصالًا تجريبيًا بالموفرات ولا تستهلك حصص البحث.\",\"SYSTEM CONFIGURATION SNAPSHOT\");"` | — |
| [SRC-2C8F288796-L000547](../../web/workspace.html#L547) | 547 | `" const root=$(\"viewRoot\");root.replaceChildren(emptyState(\"جارٍ قراءة حالة الخادم\",\"GET /api/health — لا يجري اختبار اتصال خارجي.\"));"` | — |
| [SRC-2C8F288796-L000548](../../web/workspace.html#L548) | 548 | `" try{"` | — |
| [SRC-2C8F288796-L000549](../../web/workspace.html#L549) | 549 | `"  const data=await api(\"/api/health\");"` | — |
| [SRC-2C8F288796-L000550](../../web/workspace.html#L550) | 550 | `"  const agent=data.agent\|\|{};const build=data.build\|\|{};"` | — |
| [SRC-2C8F288796-L000551](../../web/workspace.html#L551) | 551 | `"  root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000552](../../web/workspace.html#L552) | 552 | `"  const stats=make(\"div\",\"stats\");"` | — |
| [SRC-2C8F288796-L000553](../../web/workspace.html#L553) | 553 | `"  stats.append("` | — |
| [SRC-2C8F288796-L000554](../../web/workspace.html#L554) | 554 | `"   buildStat(\"استجابة الخادم\",data.ok===true?\"يستجيب\":\"غير مؤكدة\",\"استجابة نقطة /api/health\",\"glow-teal\"),"` | — |
| [SRC-2C8F288796-L000555](../../web/workspace.html#L555) | 555 | `"   buildStat(\"مكتبات البحث\",agent.web_search_ready===true?\"موجودة\":\"غير جاهزة\",\"فحص اعتماديات محلية فقط\",\"glow-blue\"),"` | — |
| [SRC-2C8F288796-L000556](../../web/workspace.html#L556) | 556 | `"   buildStat(\"إعداد النموذج\",agent.language_model_configured===true?\"مهيأ\":\"غير مهيأ\",\"لا يثبت إمكانية الاتصال أو نجاح الاستجابة\",\"glow-violet\"),"` | — |
| [SRC-2C8F288796-L000557](../../web/workspace.html#L557) | 557 | `"   buildStat(\"هوية البناء\",build.sha_status===\"available\"?String(build.sha).slice(0,8):\"غير معروفة\",\"حالة SHA كما أعادها الخادم\",\"glow-amber\")"` | — |
| [SRC-2C8F288796-L000558](../../web/workspace.html#L558) | 558 | `"  );"` | — |
| [SRC-2C8F288796-L000559](../../web/workspace.html#L559) | 559 | `"  root.append(stats);"` | — |
| [SRC-2C8F288796-L000560](../../web/workspace.html#L560) | 560 | `"  const grid=make(\"div\",\"content-grid\");"` | — |
| [SRC-2C8F288796-L000561](../../web/workspace.html#L561) | 561 | `"  const models=make(\"section\",\"glass panel\");const mh=make(\"div\",\"panel-head\");const mt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000562](../../web/workspace.html#L562) | 562 | `"  mt.append(make(\"h2\",\"\",\"موفر النموذج\"));mt.append(make(\"p\",\"\",\"بيانات إعداد يعرضها الخادم؛ لا تعرض مفاتيح أو أسرار.\"));"` | — |
| [SRC-2C8F288796-L000563](../../web/workspace.html#L563) | 563 | `"  mh.append(mt);models.append(mh);"` | — |
| [SRC-2C8F288796-L000564](../../web/workspace.html#L564) | 564 | `"  models.append(make(\"p\",\"\", \"الموفر الأساسي المعلن: \"+String(agent.language_model_provider\|\|\"غير معلوم\")));"` | — |
| [SRC-2C8F288796-L000565](../../web/workspace.html#L565) | 565 | `"  const providers=Array.isArray(agent.model_providers)?agent.model_providers:[];"` | — |
| [SRC-2C8F288796-L000566](../../web/workspace.html#L566) | 566 | `"  if(providers.length){"` | — |
| [SRC-2C8F288796-L000567](../../web/workspace.html#L567) | 567 | `"   const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000568](../../web/workspace.html#L568) | 568 | `"   providers.forEach(p=>{"` | — |
| [SRC-2C8F288796-L000569](../../web/workspace.html#L569) | 569 | `"    const row=make(\"article\",\"signal-card\");"` | — |
| [SRC-2C8F288796-L000570](../../web/workspace.html#L570) | 570 | `"    row.append(make(\"strong\",\"\",String(p.name\|\|\"موفر غير مسمى\")));"` | — |
| [SRC-2C8F288796-L000571](../../web/workspace.html#L571) | 571 | `"    row.append(make(\"span\",\"subtle\",\"النموذج المهيأ: \"+String(p.model\|\|\"غير محدد\")));"` | — |
| [SRC-2C8F288796-L000572](../../web/workspace.html#L572) | 572 | `"    row.append(tag(p.configured===true?\"مهيأ في البيئة\":\"غير مهيأ\",p.configured===true?\"teal\":\"amber\"));"` | — |
| [SRC-2C8F288796-L000573](../../web/workspace.html#L573) | 573 | `"    list.append(row);"` | — |
| [SRC-2C8F288796-L000574](../../web/workspace.html#L574) | 574 | `"   });"` | — |
| [SRC-2C8F288796-L000575](../../web/workspace.html#L575) | 575 | `"   models.append(list);"` | — |
| [SRC-2C8F288796-L000576](../../web/workspace.html#L576) | 576 | `"  }else models.append(emptyState(\"لا توجد موفرات ظاهرة كإعداد\",\"لم يعرض الخادم موفرًا مهيأ ضمن هذه اللقطة.\"));"` | — |
| [SRC-2C8F288796-L000577](../../web/workspace.html#L577) | 577 | `"  const search=make(\"section\",\"glass panel\");const sh=make(\"div\",\"panel-head\");const st=make(\"div\");"` | — |
| [SRC-2C8F288796-L000578](../../web/workspace.html#L578) | 578 | `"  st.append(make(\"h2\",\"\",\"إعدادات البحث الاختيارية\"),make(\"p\",\"\",\"القيم أدناه أعلام إعداد فقط، وليست اختبارات تشغيل.\"));"` | — |
| [SRC-2C8F288796-L000579](../../web/workspace.html#L579) | 579 | `"  sh.append(st);search.append(sh);"` | — |
| [SRC-2C8F288796-L000580](../../web/workspace.html#L580) | 580 | `"  const flags=["` | — |
| [SRC-2C8F288796-L000581](../../web/workspace.html#L581) | 581 | `"   [\"Brave Search API\",agent.brave_search_api_configured],"` | — |
| [SRC-2C8F288796-L000582](../../web/workspace.html#L582) | 582 | `"   [\"Tavily Search API\",agent.tavily_search_api_configured],"` | — |
| [SRC-2C8F288796-L000583](../../web/workspace.html#L583) | 583 | `"   [\"DeepSeek Search API\",agent.deepseek_search_api_configured],"` | — |
| [SRC-2C8F288796-L000584](../../web/workspace.html#L584) | 584 | `"   [\"OpenRouter web search\",agent.openrouter_web_search_enabled]"` | — |
| [SRC-2C8F288796-L000585](../../web/workspace.html#L585) | 585 | `"  ];"` | — |
| [SRC-2C8F288796-L000586](../../web/workspace.html#L586) | 586 | `"  flags.forEach(([name,value])=>{const row=make(\"div\",\"signal-actions\");row.append(make(\"span\",\"\",name),tag(value===true?\"مهيأ/مفعل\":\"غير مهيأ/معطل\",value===true?\"teal\":\"amber\"));search.append(row)});"` | — |
| [SRC-2C8F288796-L000587](../../web/workspace.html#L587) | 587 | `"  search.append(make(\"p\",\"disclaimer\",\"لا تنفذ هذه الشاشة تشخيصًا مباشرًا ولا تختبر صلاحية مفاتيح الموفرات. التشخيص الحي قد يستهلك حصة أو تكلفة، ويظل منفصلًا ويتطلب موافقة المالك.\"));"` | — |
| [SRC-2C8F288796-L000588](../../web/workspace.html#L588) | 588 | `"  grid.append(models,search);root.append(grid);"` | — |
| [SRC-2C8F288796-L000589](../../web/workspace.html#L589) | 589 | `" }catch(e){root.replaceChildren(emptyState(\"تعذرت قراءة الإعدادات\",escapeMessage(e.message)))}"` | — |
| [SRC-2C8F288796-L000590](../../web/workspace.html#L590) | 590 | `"}"` | — |
| [SRC-2C8F288796-L000591](../../web/workspace.html#L591) | 591 | `"function renderIndicators(){"` | — |
| [SRC-2C8F288796-L000592](../../web/workspace.html#L592) | 592 | `" setPage(\"مؤشرات الأداء\",\"لوحة وصفية لحالة سجلات مساحة العمل الحالية، وليست توقعًا للمبيعات أو احتمالات الشراء.\",\"WORKSPACE INDICATORS\");"` | — |
| [SRC-2C8F288796-L000593](../../web/workspace.html#L593) | 593 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000594](../../web/workspace.html#L594) | 594 | `" const total=state.leads.length;"` | — |
| [SRC-2C8F288796-L000595](../../web/workspace.html#L595) | 595 | `" const review=state.leads.filter(x=>[\"new\",\"needs_review\"].includes(x.status)).length;"` | — |
| [SRC-2C8F288796-L000596](../../web/workspace.html#L596) | 596 | `" const qualified=state.leads.filter(x=>[\"qualified\",\"contacted\",\"converted\"].includes(x.status)).length;"` | — |
| [SRC-2C8F288796-L000597](../../web/workspace.html#L597) | 597 | `" const converted=total?Math.round(qualified/total*100):0;"` | — |
| [SRC-2C8F288796-L000598](../../web/workspace.html#L598) | 598 | `" const withSource=state.leads.filter(x=>safeHttp(x.source_url)).length;"` | — |
| [SRC-2C8F288796-L000599](../../web/workspace.html#L599) | 599 | `" const hero=make(\"section\",\"glass indicator-hero\");"` | — |
| [SRC-2C8F288796-L000600](../../web/workspace.html#L600) | 600 | `" const ring=make(\"div\",\"indicator-ring\");"` | — |
| [SRC-2C8F288796-L000601](../../web/workspace.html#L601) | 601 | `" ring.style.background=\"conic-gradient(var(--green) 0 \"+converted+\"%, rgba(132,156,190,.16) \"+converted+\"% 100%)\";"` | — |
| [SRC-2C8F288796-L000602](../../web/workspace.html#L602) | 602 | `" ring.setAttribute(\"role\",\"img\");"` | — |
| [SRC-2C8F288796-L000603](../../web/workspace.html#L603) | 603 | `" ring.setAttribute(\"aria-label\",\"نسبة السجلات المؤهلة أو قيد المتابعة: \"+converted+\" بالمئة من السجلات المحمّلة\");"` | — |
| [SRC-2C8F288796-L000604](../../web/workspace.html#L604) | 604 | `" const ringInner=make(\"div\",\"indicator-ring-inner\");"` | — |
| [SRC-2C8F288796-L000605](../../web/workspace.html#L605) | 605 | `" ringInner.append(make(\"strong\",\"indicator-ring-value\",converted+\"%\"),make(\"span\",\"indicator-ring-caption\",\"مؤهل أو متابعة\"));"` | — |
| [SRC-2C8F288796-L000606](../../web/workspace.html#L606) | 606 | `" ring.append(ringInner);"` | — |
| [SRC-2C8F288796-L000607](../../web/workspace.html#L607) | 607 | `" const heroCopy=make(\"div\",\"indicator-hero-copy\");"` | — |
| [SRC-2C8F288796-L000608](../../web/workspace.html#L608) | 608 | `" heroCopy.append(make(\"span\",\"eyebrow\",\"WORKSPACE HEALTH\"),make(\"h2\",\"\",\"مؤشر متابعة السجل\"),make(\"p\",\"\",\"نسبة الإشارات المصنفة مؤهلة أو تم التواصل معها أو تحولت إلى عميل، من إجمالي السجلات المحمّلة حاليًا. هذه نسبة حالة داخلية وليست احتمال شراء.\"));"` | — |
| [SRC-2C8F288796-L000609](../../web/workspace.html#L609) | 609 | `" hero.append(ring,heroCopy);root.append(hero);"` | — |
| [SRC-2C8F288796-L000610](../../web/workspace.html#L610) | 610 | `" const cards=make(\"div\",\"indicator-grid\");"` | — |
| [SRC-2C8F288796-L000611](../../web/workspace.html#L611) | 611 | `" cards.append("` | — |
| [SRC-2C8F288796-L000612](../../web/workspace.html#L612) | 612 | `"  buildStat(\"إجمالي الإشارات\",total,\"السجلات التي أعادها الخادم\",\"glow-teal\"),"` | — |
| [SRC-2C8F288796-L000613](../../web/workspace.html#L613) | 613 | `"  buildStat(\"مؤهلة أو قيد المتابعة\",qualified,\"مؤهل · تم التواصل · تحول\",\"glow-blue\"),"` | — |
| [SRC-2C8F288796-L000614](../../web/workspace.html#L614) | 614 | `"  buildStat(\"تحتاج مراجعة\",review,\"جديد أو بانتظار مراجعة\",\"glow-amber\"),"` | — |
| [SRC-2C8F288796-L000615](../../web/workspace.html#L615) | 615 | `"  buildStat(\"عمليات الاكتشاف\",state.discoveryRuns.length,\"عمليات محفوظة أعادها الخادم\",\"glow-violet\")"` | — |
| [SRC-2C8F288796-L000616](../../web/workspace.html#L616) | 616 | `" );"` | — |
| [SRC-2C8F288796-L000617](../../web/workspace.html#L617) | 617 | `" root.append(cards);"` | — |
| [SRC-2C8F288796-L000618](../../web/workspace.html#L618) | 618 | `" const layout=make(\"div\",\"indicator-layout\");"` | — |
| [SRC-2C8F288796-L000619](../../web/workspace.html#L619) | 619 | `" const statusPanel=make(\"section\",\"glass panel\");"` | — |
| [SRC-2C8F288796-L000620](../../web/workspace.html#L620) | 620 | `" const head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000621](../../web/workspace.html#L621) | 621 | `" title.append(make(\"h2\",\"\",\"توزيع حالات الإشارات\"),make(\"p\",\"\",\"عدد السجلات الفعلي حسب حالة المتابعة الحالية.\"));"` | — |
| [SRC-2C8F288796-L000622](../../web/workspace.html#L622) | 622 | `" head.append(title,action(\"فتح إشارات الطلب ←\",\"ghost\",()=>navigate(\"signals\")));"` | — |
| [SRC-2C8F288796-L000623](../../web/workspace.html#L623) | 623 | `" statusPanel.append(head);"` | — |
| [SRC-2C8F288796-L000624](../../web/workspace.html#L624) | 624 | `" const bars=make(\"div\",\"indicator-list\");"` | — |
| [SRC-2C8F288796-L000625](../../web/workspace.html#L625) | 625 | `" const groups=["` | — |
| [SRC-2C8F288796-L000626](../../web/workspace.html#L626) | 626 | `"  [\"جديد\",\"new\",\"cyan\"],[\"يحتاج مراجعة\",\"needs_review\",\"red\"],[\"مؤهل\",\"qualified\",\"green\"],"` | — |
| [SRC-2C8F288796-L000627](../../web/workspace.html#L627) | 627 | `"  [\"تم التواصل\",\"contacted\",\"green\"],[\"تحول لعميل\",\"converted\",\"green\"],[\"مرفوض\",\"rejected\",\"muted\"]"` | — |
| [SRC-2C8F288796-L000628](../../web/workspace.html#L628) | 628 | `" ];"` | — |
| [SRC-2C8F288796-L000629](../../web/workspace.html#L629) | 629 | `" groups.forEach(([label,id,tone])=>{"` | — |
| [SRC-2C8F288796-L000630](../../web/workspace.html#L630) | 630 | `"  const count=countByStatus(id),row=make(\"div\",\"indicator-row\");"` | — |
| [SRC-2C8F288796-L000631](../../web/workspace.html#L631) | 631 | `"  row.append(make(\"span\",\"\",\"\"+label));"` | — |
| [SRC-2C8F288796-L000632](../../web/workspace.html#L632) | 632 | `"  const track=make(\"div\",\"indicator-track\"),fill=make(\"div\",\"indicator-fill \"+tone);"` | — |
| [SRC-2C8F288796-L000633](../../web/workspace.html#L633) | 633 | `"  fill.style.width=(total?Math.round(count/total*100):0)+\"%\";"` | — |
| [SRC-2C8F288796-L000634](../../web/workspace.html#L634) | 634 | `"  fill.setAttribute(\"aria-hidden\",\"true\");"` | — |
| [SRC-2C8F288796-L000635](../../web/workspace.html#L635) | 635 | `"  track.append(fill);row.append(track,make(\"strong\",\"\",count));bars.append(row);"` | — |
| [SRC-2C8F288796-L000636](../../web/workspace.html#L636) | 636 | `" });"` | — |
| [SRC-2C8F288796-L000637](../../web/workspace.html#L637) | 637 | `" if(!total)bars.append(emptyState(\"لا توجد بيانات بعد\",\"ستظهر المؤشرات تلقائيًا بعد حفظ إشارات فعلية.\"));"` | — |
| [SRC-2C8F288796-L000638](../../web/workspace.html#L638) | 638 | `" statusPanel.append(bars);"` | — |
| [SRC-2C8F288796-L000639](../../web/workspace.html#L639) | 639 | `" const quality=make(\"section\",\"glass panel\");"` | — |
| [SRC-2C8F288796-L000640](../../web/workspace.html#L640) | 640 | `" const qhead=make(\"div\",\"panel-head\"),qtitle=make(\"div\");"` | — |
| [SRC-2C8F288796-L000641](../../web/workspace.html#L641) | 641 | `" qtitle.append(make(\"h2\",\"\",\"اكتمال السجل\"),make(\"p\",\"\",\"معلومات وصفية عن السجلات المحمّلة فقط.\"));"` | — |
| [SRC-2C8F288796-L000642](../../web/workspace.html#L642) | 642 | `" qhead.append(qtitle);quality.append(qhead);"` | — |
| [SRC-2C8F288796-L000643](../../web/workspace.html#L643) | 643 | `" const summary=make(\"div\",\"indicator-summary\");"` | — |
| [SRC-2C8F288796-L000644](../../web/workspace.html#L644) | 644 | `" ["` | — |
| [SRC-2C8F288796-L000645](../../web/workspace.html#L645) | 645 | `"  [\"إشارات لها رابط مصدر\",withSource],"` | — |
| [SRC-2C8F288796-L000646](../../web/workspace.html#L646) | 646 | `"  [\"ملفات المنتجات والأسواق\",state.profiles.length],"` | — |
| [SRC-2C8F288796-L000647](../../web/workspace.html#L647) | 647 | `"  [\"عمليات الاكتشاف المحفوظة\",state.discoveryRuns.length],"` | — |
| [SRC-2C8F288796-L000648](../../web/workspace.html#L648) | 648 | `"  [\"إشارات تحتاج مراجعة\",review]"` | — |
| [SRC-2C8F288796-L000649](../../web/workspace.html#L649) | 649 | `" ].forEach(([label,value])=>{"` | — |
| [SRC-2C8F288796-L000650](../../web/workspace.html#L650) | 650 | `"  const item=make(\"div\",\"indicator-note\");"` | — |
| [SRC-2C8F288796-L000651](../../web/workspace.html#L651) | 651 | `"  item.append(make(\"div\",\"\",label),make(\"strong\",\"indicator-note-value\",value));summary.append(item);"` | — |
| [SRC-2C8F288796-L000652](../../web/workspace.html#L652) | 652 | `" });"` | — |
| [SRC-2C8F288796-L000653](../../web/workspace.html#L653) | 653 | `" quality.append(summary,make(\"p\",\"disclaimer\",\"وجود رابط مصدر لا يعني أن الصفحة قُرئت أو تم التحقق من محتواها. ولا تمثل هذه المؤشرات حجم السوق أو معدل التحويل الفعلي.\"));"` | — |
| [SRC-2C8F288796-L000654](../../web/workspace.html#L654) | 654 | `" layout.append(statusPanel,quality);root.append(layout);"` | — |
| [SRC-2C8F288796-L000655](../../web/workspace.html#L655) | 655 | `" const recent=make(\"section\",\"glass panel\");recent.style.marginTop=\"14px\";"` | — |
| [SRC-2C8F288796-L000656](../../web/workspace.html#L656) | 656 | `" const rh=make(\"div\",\"panel-head\"),rt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000657](../../web/workspace.html#L657) | 657 | `" rt.append(make(\"h2\",\"\",\"أحدث الإشارات\"),make(\"p\",\"\",\"آخر خمسة سجلات بحسب تاريخ التحديث الذي أعاده الخادم.\"));"` | — |
| [SRC-2C8F288796-L000658](../../web/workspace.html#L658) | 658 | `" rh.append(rt,action(\"عرض الكل ←\",\"ghost\",()=>navigate(\"signals\")));recent.append(rh);"` | — |
| [SRC-2C8F288796-L000659](../../web/workspace.html#L659) | 659 | `" const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000660](../../web/workspace.html#L660) | 660 | `" const rows=state.leads.slice().sort((a,b)=>String(b.updated_at\|\|b.observed_at\|\|\"\").localeCompare(String(a.updated_at\|\|a.observed_at\|\|\"\"))).slice(0,5);"` | — |
| [SRC-2C8F288796-L000661](../../web/workspace.html#L661) | 661 | `" if(rows.length)rows.forEach(item=>list.append(signalCard(item)));"` | — |
| [SRC-2C8F288796-L000662](../../web/workspace.html#L662) | 662 | `" else list.append(emptyState(\"لا توجد إشارات لعرضها\",\"أضف إشارة طلب موثقة لتبدأ المؤشرات في الظهور.\"));"` | — |
| [SRC-2C8F288796-L000663](../../web/workspace.html#L663) | 663 | `" recent.append(list);root.append(recent);"` | — |
| [SRC-2C8F288796-L000664](../../web/workspace.html#L664) | 664 | `"}"` | — |
| [SRC-2C8F288796-L000665](../../web/workspace.html#L665) | 665 | `"function renderPlaceholder(id){"` | — |
| [SRC-2C8F288796-L000666](../../web/workspace.html#L666) | 666 | `" const item=menu.find(x=>x.id===id);const title=item?item.label:\"وحدة\";"` | — |
| [SRC-2C8F288796-L000667](../../web/workspace.html#L667) | 667 | `" setPage(title,\"واجهة الوحدة جزء من تصور Omarai، لكن المستودع عند الرأس الحالي لا يوفّر بعد عقد API موثقًا لهذه الوظيفة. لا نعرض بيانات أو نتائج شكلية على أنها حقيقية.\",\"MODULE NOT ENABLED\");"` | — |
| [SRC-2C8F288796-L000668](../../web/workspace.html#L668) | 668 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000669](../../web/workspace.html#L669) | 669 | `" const card=make(\"section\",\"glass module-placeholder\");"` | — |
| [SRC-2C8F288796-L000670](../../web/workspace.html#L670) | 670 | `" card.append(tag(\"غير مفعلة في الخادم الحالي\",\"amber\"),make(\"h2\",\"\",title));"` | — |
| [SRC-2C8F288796-L000671](../../web/workspace.html#L671) | 671 | `" card.append(make(\"p\",\"\",\"هذه الشاشة لا تستدعي موصلًا خارجيًا ولا تحفظ إعدادات وهمية. يلزم بناء نموذج البيانات وواجهة API واختبارات الصلاحيات والعزل قبل تشغيلها.\"));"` | — |
| [SRC-2C8F288796-L000672](../../web/workspace.html#L672) | 672 | `" const list=make(\"div\",\"module-list\");"` | — |
| [SRC-2C8F288796-L000673](../../web/workspace.html#L673) | 673 | `" [\"تعريف عقد البيانات والحقول ومصدر كل قيمة.\",\"إنشاء API محمي ومربوط بالمستخدم ومساحة العمل المصادق عليها.\",\"إضافة اختبارات نجاح وفشل وعزل بين المستأجرين.\",\"ربط الواجهة بالبيانات الفعلية ثم اختبارها على بيئة معروفة.\"].forEach(x=>list.append(make(\"div\",\"module-step\",x)));"` | — |
| [SRC-2C8F288796-L000674](../../web/workspace.html#L674) | 674 | `" card.append(list,make(\"div\",\"form-actions\"));"` | — |
| [SRC-2C8F288796-L000675](../../web/workspace.html#L675) | 675 | `" const links=card.querySelector(\".form-actions\");links.append(action(\"العودة إلى النظرة العامة\",\"primary\",()=>navigate(\"overview\")),action(\"فتح وكيل البحث الحالي\",\"\",()=>{window.location.href=\"/agent\"}));"` | — |
| [SRC-2C8F288796-L000676](../../web/workspace.html#L676) | 676 | `" root.append(card);"` | — |
| [SRC-2C8F288796-L000677](../../web/workspace.html#L677) | 677 | `"}"` | — |
| [SRC-2C8F288796-L000678](../../web/workspace.html#L678) | 678 | `"function csvValues(value){return String(value\|\|\"\").split(\",\").map(x=>x.trim()).filter(Boolean)}"` | — |
| [SRC-2C8F288796-L000679](../../web/workspace.html#L679) | 679 | `"function textField(label,id,placeholder,value,multiline){"` | — |
| [SRC-2C8F288796-L000680](../../web/workspace.html#L680) | 680 | `" const field=make(\"div\",\"field\"),control=make(multiline?\"textarea\":\"input\",\"\");"` | — |
| [SRC-2C8F288796-L000681](../../web/workspace.html#L681) | 681 | `" control.id=id;control.value=value\|\|\"\";control.placeholder=placeholder\|\|\"\";"` | — |
| [SRC-2C8F288796-L000682](../../web/workspace.html#L682) | 682 | `" const caption=make(\"label\",\"\",label);caption.htmlFor=id;field.append(caption,control);"` | — |
| [SRC-2C8F288796-L000683](../../web/workspace.html#L683) | 683 | `" return {field,control};"` | — |
| [SRC-2C8F288796-L000684](../../web/workspace.html#L684) | 684 | `"}"` | — |
| [SRC-2C8F288796-L000685](../../web/workspace.html#L685) | 685 | `"function renderProductProfile(){"` | — |
| [SRC-2C8F288796-L000686](../../web/workspace.html#L686) | 686 | `" setPage(\"ملف المنتج والعرض\",\"عرّف المنتج والسوق قبل تشغيل اكتشاف الطلب. كل ملف محفوظ مرتبط بمساحة العمل المصادق عليها.\",\"PRODUCT & MARKET PROFILE\");"` | — |
| [SRC-2C8F288796-L000687](../../web/workspace.html#L687) | 687 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000688](../../web/workspace.html#L688) | 688 | `" const panel=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000689](../../web/workspace.html#L689) | 689 | `" title.append(make(\"h2\",\"\",\"بيانات المنتج والسوق\"),make(\"p\",\"\",\"أدخل المعلومات المعروفة صراحةً؛ لا يخترع Omarai مواصفات أو عملاء مستهدفين من اسم المنتج وحده.\"));"` | — |
| [SRC-2C8F288796-L000690](../../web/workspace.html#L690) | 690 | `" head.append(title);panel.append(head);"` | — |
| [SRC-2C8F288796-L000691](../../web/workspace.html#L691) | 691 | `" const grid=make(\"div\",\"form-grid\"),controls={};"` | — |
| [SRC-2C8F288796-L000692](../../web/workspace.html#L692) | 692 | `" const fields=["` | — |
| [SRC-2C8F288796-L000693](../../web/workspace.html#L693) | 693 | `"  [\"اسم المنتج أو الخدمة\",\"name\",\"مثال: لوحة إنذار حريق\"],"` | — |
| [SRC-2C8F288796-L000694](../../web/workspace.html#L694) | 694 | `"  [\"الأسماء والمرادفات\",\"aliases\",\"FACP، لوحة إنذار، Fire Alarm Panel\"],"` | — |
| [SRC-2C8F288796-L000695](../../web/workspace.html#L695) | 695 | `"  [\"الفئة أو التصنيف\",\"category\",\"السلامة، أنظمة إنذار\"],"` | — |
| [SRC-2C8F288796-L000696](../../web/workspace.html#L696) | 696 | `"  [\"الاستخدامات\",\"useCases\",\"المصانع، المباني التجارية\"],"` | — |
| [SRC-2C8F288796-L000697](../../web/workspace.html#L697) | 697 | `"  [\"المشكلات التي يحلها\",\"problems\",\"الكشف المبكر، تقليل المخاطر\"],"` | — |
| [SRC-2C8F288796-L000698](../../web/workspace.html#L698) | 698 | `"  [\"المناطق المستهدفة\",\"locations\",\"القاهرة، الجيزة\"],"` | — |
| [SRC-2C8F288796-L000699](../../web/workspace.html#L699) | 699 | `"  [\"القطاعات\",\"industries\",\"المقاولات، التصنيع\"],"` | — |
| [SRC-2C8F288796-L000700](../../web/workspace.html#L700) | 700 | `"  [\"نوع العملاء\",\"customers\",\"مقاولون، ملاك مشروعات\"],"` | — |
| [SRC-2C8F288796-L000701](../../web/workspace.html#L701) | 701 | `"  [\"أدوار الشراء\",\"roles\",\"مدير مشتريات، مدير مشروع\"],"` | — |
| [SRC-2C8F288796-L000702](../../web/workspace.html#L702) | 702 | `"  [\"الاستثناءات\",\"exclusions\",\"القطاعات غير المناسبة\"]"` | — |
| [SRC-2C8F288796-L000703](../../web/workspace.html#L703) | 703 | `" ];"` | — |
| [SRC-2C8F288796-L000704](../../web/workspace.html#L704) | 704 | `" fields.forEach(([label,key,placeholder])=>{"` | — |
| [SRC-2C8F288796-L000705](../../web/workspace.html#L705) | 705 | `"  const item=textField(label,\"profile_\"+key,placeholder,\"\",false);"` | — |
| [SRC-2C8F288796-L000706](../../web/workspace.html#L706) | 706 | `"  controls[key]=item.control;if(!canWrite())item.control.disabled=true;grid.append(item.field);"` | — |
| [SRC-2C8F288796-L000707](../../web/workspace.html#L707) | 707 | `" });"` | — |
| [SRC-2C8F288796-L000708](../../web/workspace.html#L708) | 708 | `" const localeField=make(\"div\",\"field\"),locale=make(\"select\",\"\");"` | — |
| [SRC-2C8F288796-L000709](../../web/workspace.html#L709) | 709 | `" [[\"auto\",\"تلقائي\"],[\"ar\",\"العربية\"],[\"en\",\"الإنجليزية\"],[\"mixed\",\"العربية والإنجليزية\"]].forEach(([v,l])=>{const o=make(\"option\",\"\",l);o.value=v;locale.append(o)});"` | — |
| [SRC-2C8F288796-L000710](../../web/workspace.html#L710) | 710 | `" localeField.append(make(\"label\",\"\",\"لغة البحث\"),locale);controls.locale=locale;if(!canWrite())locale.disabled=true;grid.append(localeField);"` | — |
| [SRC-2C8F288796-L000711](../../web/workspace.html#L711) | 711 | `" panel.append(grid,make(\"p\",\"profile-note\",\"افصل القيم المتعددة بفاصلة. تُستخدم المرادفات والمناطق لصياغة استعلامات مرتبطة بالمنتج؛ تطابق ICP وحده لا يثبت وجود طلب.\"));"` | — |
| [SRC-2C8F288796-L000712](../../web/workspace.html#L712) | 712 | `" const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000713](../../web/workspace.html#L713) | 713 | `" const save=action(\"حفظ ملف المنتج والسوق\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000714](../../web/workspace.html#L714) | 714 | `"  save.disabled=true;"` | — |
| [SRC-2C8F288796-L000715](../../web/workspace.html#L715) | 715 | `"  try{"` | — |
| [SRC-2C8F288796-L000716](../../web/workspace.html#L716) | 716 | `"   const payload={"` | — |
| [SRC-2C8F288796-L000717](../../web/workspace.html#L717) | 717 | `"    product:{name:controls.name.value,aliases:csvValues(controls.aliases.value),category_path:csvValues(controls.category.value),use_cases:csvValues(controls.useCases.value),problems_solved:csvValues(controls.problems.value)},"` | — |
| [SRC-2C8F288796-L000718](../../web/workspace.html#L718) | 718 | `"    market:{locations:csvValues(controls.locations.value),industries:csvValues(controls.industries.value),customer_types:csvValues(controls.customers.value),decision_roles:csvValues(controls.roles.value),exclusions:csvValues(controls.exclusions.value)},"` | — |
| [SRC-2C8F288796-L000719](../../web/workspace.html#L719) | 719 | `"    locale:controls.locale.value"` | — |
| [SRC-2C8F288796-L000720](../../web/workspace.html#L720) | 720 | `"   };"` | — |
| [SRC-2C8F288796-L000721](../../web/workspace.html#L721) | 721 | `"   const result=await api(\"/api/product-profiles\",{method:\"POST\",body:payload});"` | — |
| [SRC-2C8F288796-L000722](../../web/workspace.html#L722) | 722 | `"   state.activeProfileId=result.id;await loadProductProfiles();renderProductProfile();"` | — |
| [SRC-2C8F288796-L000723](../../web/workspace.html#L723) | 723 | `"  }catch(error){panel.append(make(\"p\",\"auth-error\",escapeMessage(error.message)))}"` | — |
| [SRC-2C8F288796-L000724](../../web/workspace.html#L724) | 724 | `"  finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000725](../../web/workspace.html#L725) | 725 | `" });"` | — |
| [SRC-2C8F288796-L000726](../../web/workspace.html#L726) | 726 | `" save.disabled=!canWrite();actions.append(save);panel.append(actions);root.append(panel);"` | — |
| [SRC-2C8F288796-L000727](../../web/workspace.html#L727) | 727 | `" const listPanel=make(\"section\",\"glass panel profile-panel\"),lh=make(\"div\",\"panel-head\"),lt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000728](../../web/workspace.html#L728) | 728 | `" lt.append(make(\"h2\",\"\",\"ملفات المنتجات المحفوظة\"),make(\"p\",\"\",\"اختر ملفًا محفوظًا للانتقال إلى تشغيل الاكتشاف.\"));"` | — |
| [SRC-2C8F288796-L000729](../../web/workspace.html#L729) | 729 | `" lh.append(lt);listPanel.append(lh);"` | — |
| [SRC-2C8F288796-L000730](../../web/workspace.html#L730) | 730 | `" if(!state.profiles.length)listPanel.append(emptyState(\"لا توجد ملفات بعد\",\"أنشئ ملف المنتج والسوق ثم احفظه.\"));"` | — |
| [SRC-2C8F288796-L000731](../../web/workspace.html#L731) | 731 | `" else{"` | — |
| [SRC-2C8F288796-L000732](../../web/workspace.html#L732) | 732 | `"  const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000733](../../web/workspace.html#L733) | 733 | `"  state.profiles.forEach(profile=>{"` | — |
| [SRC-2C8F288796-L000734](../../web/workspace.html#L734) | 734 | `"   const card=make(\"article\",\"signal-card\"),p=profile.profile\|\|{},m=p.market\|\|{};"` | — |
| [SRC-2C8F288796-L000735](../../web/workspace.html#L735) | 735 | `"   card.append(make(\"strong\",\"\",profile.name\|\|\"منتج\"));"` | — |
| [SRC-2C8F288796-L000736](../../web/workspace.html#L736) | 736 | `"   card.append(make(\"p\",\"subtle\",\"المناطق: \"+((m.locations\|\|[]).join(\"، \")\|\|\"غير محددة\")));"` | — |
| [SRC-2C8F288796-L000737](../../web/workspace.html#L737) | 737 | `"   const row=make(\"div\",\"form-actions\");row.append(action(\"استخدام في الاكتشاف\",\"\",()=>{state.activeProfileId=profile.id;navigate(\"campaign\")}));"` | — |
| [SRC-2C8F288796-L000738](../../web/workspace.html#L738) | 738 | `"   card.append(row);list.append(card);"` | — |
| [SRC-2C8F288796-L000739](../../web/workspace.html#L739) | 739 | `"  });listPanel.append(list);"` | — |
| [SRC-2C8F288796-L000740](../../web/workspace.html#L740) | 740 | `" }"` | — |
| [SRC-2C8F288796-L000741](../../web/workspace.html#L741) | 741 | `" root.append(listPanel);"` | — |
| [SRC-2C8F288796-L000742](../../web/workspace.html#L742) | 742 | `"}"` | — |
| [SRC-2C8F288796-L000743](../../web/workspace.html#L743) | 743 | `"function renderDiscoveryRun(run){"` | — |
| [SRC-2C8F288796-L000744](../../web/workspace.html#L744) | 744 | `" const panel=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000745](../../web/workspace.html#L745) | 745 | `" const report=run.search_report\|\|{},leadReport=report.lead_generation\|\|{},sources=Array.isArray(run.sources)?run.sources:[];"` | — |
| [SRC-2C8F288796-L000746](../../web/workspace.html#L746) | 746 | `" title.append(make(\"h2\",\"\",\"نتيجة عملية الاكتشاف\"),make(\"p\",\"\",\"ملف المنتج: \"+String(run.profile_name\|\|\"غير محدد\")+\" · \"+String(run.created_at\|\|\"\")));"` | — |
| [SRC-2C8F288796-L000747](../../web/workspace.html#L747) | 747 | `" head.append(title);panel.append(head);"` | — |
| [SRC-2C8F288796-L000748](../../web/workspace.html#L748) | 748 | `" const stats=make(\"div\",\"stats\"),qualifiedCount=sources.filter(s=>s.lead_qualification===\"public_demand_signal\").length;"` | — |
| [SRC-2C8F288796-L000749](../../web/workspace.html#L749) | 749 | `" stats.append("` | — |
| [SRC-2C8F288796-L000750](../../web/workspace.html#L750) | 750 | `"  buildStat(\"إشارات طلب مؤهلة\",leadReport.candidate_signal_count??qualifiedCount,\"إشارات تحمل عبارة طلب معلنة\",\"glow-teal\"),"` | — |
| [SRC-2C8F288796-L000751](../../web/workspace.html#L751) | 751 | `"  buildStat(\"المصادر التي راجعتها الجولة\",leadReport.related_results_reviewed??sources.length,\"لا يعني ذلك اكتمال السوق\",\"glow-blue\"),"` | — |
| [SRC-2C8F288796-L000752](../../web/workspace.html#L752) | 752 | `"  buildStat(\"حالة تشغيل البحث\",report.pipeline_completion_status\|\|\"غير معلومة\",\"حالة المسار كما أعادها الوكيل\",\"glow-amber\")"` | — |
| [SRC-2C8F288796-L000753](../../web/workspace.html#L753) | 753 | `" );"` | — |
| [SRC-2C8F288796-L000754](../../web/workspace.html#L754) | 754 | `" panel.append(stats,make(\"p\",\"profile-note\",run.answer\|\|\"لا يوجد ملخص لهذه العملية.\"));"` | — |
| [SRC-2C8F288796-L000755](../../web/workspace.html#L755) | 755 | `" if(Array.isArray(run.search_queries)&&run.search_queries.length){const qs=make(\"div\",\"query-list\");run.search_queries.forEach(q=>qs.append(tag(q)));panel.append(qs)}"` | — |
| [SRC-2C8F288796-L000756](../../web/workspace.html#L756) | 756 | `" const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000757](../../web/workspace.html#L757) | 757 | `" if(!sources.length)list.append(emptyState(\"لم تُعد العملية مصادر قابلة للعرض\",\"راجع حالة التشغيل والتحذيرات؛ هذا لا يثبت عدم وجود طلب.\"));"` | — |
| [SRC-2C8F288796-L000758](../../web/workspace.html#L758) | 758 | `" sources.forEach((source,index)=>{"` | — |
| [SRC-2C8F288796-L000759](../../web/workspace.html#L759) | 759 | `"  const qualified=source.lead_qualification===\"public_demand_signal\";"` | — |
| [SRC-2C8F288796-L000760](../../web/workspace.html#L760) | 760 | `"  const card=make(\"article\",\"discovery-source\"+(qualified?\" qualified\":\"\")),meta=make(\"div\",\"discovery-source-meta\");"` | — |
| [SRC-2C8F288796-L000761](../../web/workspace.html#L761) | 761 | `"  meta.append(tag(qualified?\"إشارة طلب معلنة\":\"نتيجة مرتبطة فقط\",qualified?\"teal\":\"\"));"` | — |
| [SRC-2C8F288796-L000762](../../web/workspace.html#L762) | 762 | `"  if(source.platform)meta.append(tag(source.platform));"` | — |
| [SRC-2C8F288796-L000763](../../web/workspace.html#L763) | 763 | `"  meta.append(tag(source.page_fetched?\"تمت قراءة الصفحة\":\"مقتطف/عنوان فقط\"));"` | — |
| [SRC-2C8F288796-L000764](../../web/workspace.html#L764) | 764 | `"  card.append(meta,make(\"h3\",\"\",source.title\|\|\"نتيجة ويب\"));"` | — |
| [SRC-2C8F288796-L000765](../../web/workspace.html#L765) | 765 | `"  if(source.snippet)card.append(make(\"p\",\"\",source.snippet));"` | — |
| [SRC-2C8F288796-L000766](../../web/workspace.html#L766) | 766 | `"  const evidence=source.lead_intent_evidence;"` | — |
| [SRC-2C8F288796-L000767](../../web/workspace.html#L767) | 767 | `"  if(qualified&&evidence){"` | — |
| [SRC-2C8F288796-L000768](../../web/workspace.html#L768) | 768 | `"   card.append(make(\"p\",\"\",\"عبارة الدليل: \"+String(evidence.phrase\|\|\"غير محددة\")));"` | — |
| [SRC-2C8F288796-L000769](../../web/workspace.html#L769) | 769 | `"   card.append(make(\"p\",\"\",\"نوع الإشارة: \"+String(evidence.signal_type\|\|\"غير محدد\")+\" · أساس النص: \"+String(evidence.basis\|\|\"غير محدد\")));"` | — |
| [SRC-2C8F288796-L000770](../../web/workspace.html#L770) | 770 | `"   card.append(make(\"p\",\"discovery-note\",\"ملاءمة المنتج لم تُحسم من العبارة وحدها؛ راجع المصدر قبل اعتماد الفرصة.\"));"` | — |
| [SRC-2C8F288796-L000771](../../web/workspace.html#L771) | 771 | `"  }else card.append(make(\"p\",\"discovery-note\",\"لم يعثر المحرك على عبارة كافية تثبت طلب شراء. لن تُحفظ هذه النتيجة كإشارة طلب من هذه الشاشة.\"));"` | — |
| [SRC-2C8F288796-L000772](../../web/workspace.html#L772) | 772 | `"  card.append(make(\"p\",\"discovery-note\",\"تاريخ النشر: \"+String(source.published_at\|\|\"غير متاح من المصدر\")));"` | — |
| [SRC-2C8F288796-L000773](../../web/workspace.html#L773) | 773 | `"  const url=safeHttp(source.url);if(url){const link=make(\"a\",\"\",url);link.href=url;link.target=\"_blank\";link.rel=\"noopener noreferrer\";card.append(link)}"` | — |
| [SRC-2C8F288796-L000774](../../web/workspace.html#L774) | 774 | `"  if(qualified&&canWrite()){"` | — |
| [SRC-2C8F288796-L000775](../../web/workspace.html#L775) | 775 | `"   const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000776](../../web/workspace.html#L776) | 776 | `"   const save=action(\"حفظ الإشارة في صندوق الطلب\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000777](../../web/workspace.html#L777) | 777 | `"    save.disabled=true;"` | — |
| [SRC-2C8F288796-L000778](../../web/workspace.html#L778) | 778 | `"    try{"` | — |
| [SRC-2C8F288796-L000779](../../web/workspace.html#L779) | 779 | `"     const response=await api(\"/api/discoveries/\"+encodeURIComponent(run.id)+\"/signals/\"+index+\"/save\",{method:\"POST\",body:{}});"` | — |
| [SRC-2C8F288796-L000780](../../web/workspace.html#L780) | 780 | `"     save.textContent=response.created?\"تم الحفظ\":\"الإشارة موجودة بالفعل\";"` | — |
| [SRC-2C8F288796-L000781](../../web/workspace.html#L781) | 781 | `"     await loadLeads();"` | — |
| [SRC-2C8F288796-L000782](../../web/workspace.html#L782) | 782 | `"    }catch(error){card.append(make(\"p\",\"auth-error\",escapeMessage(error.message)))}"` | — |
| [SRC-2C8F288796-L000783](../../web/workspace.html#L783) | 783 | `"    finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000784](../../web/workspace.html#L784) | 784 | `"   });"` | — |
| [SRC-2C8F288796-L000785](../../web/workspace.html#L785) | 785 | `"   actions.append(save);card.append(actions);"` | — |
| [SRC-2C8F288796-L000786](../../web/workspace.html#L786) | 786 | `"  }"` | — |
| [SRC-2C8F288796-L000787](../../web/workspace.html#L787) | 787 | `"  list.append(card);"` | — |
| [SRC-2C8F288796-L000788](../../web/workspace.html#L788) | 788 | `" });"` | — |
| [SRC-2C8F288796-L000789](../../web/workspace.html#L789) | 789 | `" panel.append(list);return panel;"` | — |
| [SRC-2C8F288796-L000790](../../web/workspace.html#L790) | 790 | `"}"` | — |
| [SRC-2C8F288796-L000791](../../web/workspace.html#L791) | 791 | `"function renderDiscovery(){"` | — |
| [SRC-2C8F288796-L000792](../../web/workspace.html#L792) | 792 | `" setPage(\"حملات الاكتشاف\",\"ابحث عن إشارات طلب شراء أو توريد معلنة مرتبطة بملف المنتج والسوق. لا تُعرض النتائج العامة كعملاء محتملين.\",\"BUYER INTENT DISCOVERY\");"` | — |
| [SRC-2C8F288796-L000793](../../web/workspace.html#L793) | 793 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000794](../../web/workspace.html#L794) | 794 | `" const controls=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000795](../../web/workspace.html#L795) | 795 | `" title.append(make(\"h2\",\"\",\"تشغيل اكتشاف جديد\"),make(\"p\",\"\",\"يستخدم محرك البحث الحالي ويولّد الاستعلامات من ملف المنتج المحفوظ.\"));"` | — |
| [SRC-2C8F288796-L000796](../../web/workspace.html#L796) | 796 | `" head.append(title);controls.append(head);"` | — |
| [SRC-2C8F288796-L000797](../../web/workspace.html#L797) | 797 | `" if(!state.profiles.length){"` | — |
| [SRC-2C8F288796-L000798](../../web/workspace.html#L798) | 798 | `"  controls.append(emptyState(\"لا يوجد ملف منتج محفوظ\",\"أنشئ ملف المنتج والسوق قبل تشغيل الاكتشاف.\"));"` | — |
| [SRC-2C8F288796-L000799](../../web/workspace.html#L799) | 799 | `"  controls.append(action(\"إنشاء ملف المنتج ←\",\"primary\",()=>navigate(\"offer\")));"` | — |
| [SRC-2C8F288796-L000800](../../web/workspace.html#L800) | 800 | `" }else{"` | — |
| [SRC-2C8F288796-L000801](../../web/workspace.html#L801) | 801 | `"  const field=make(\"div\",\"field\"),profileSelect=make(\"select\",\"\");"` | — |
| [SRC-2C8F288796-L000802](../../web/workspace.html#L802) | 802 | `"  state.profiles.forEach(profile=>{const option=make(\"option\",\"\",profile.name);option.value=profile.id;option.selected=profile.id===state.activeProfileId;profileSelect.append(option)});"` | — |
| [SRC-2C8F288796-L000803](../../web/workspace.html#L803) | 803 | `"  field.append(make(\"label\",\"\",\"ملف المنتج والسوق\"),profileSelect);controls.append(field);"` | — |
| [SRC-2C8F288796-L000804](../../web/workspace.html#L804) | 804 | `"  const consent=make(\"label\",\"consent-row\"),optional=make(\"input\",\"\");optional.type=\"checkbox\";optional.checked=false;optional.disabled=state.role!==\"owner\";"` | — |
| [SRC-2C8F288796-L000805](../../web/workspace.html#L805) | 805 | `"  consent.append(optional,make(\"span\",\"\",\"السماح بالموصلات الاختيارية (DeepSeek Search وBrave وTavily وبعض واجهات المنصات الرسمية). قد تستهلك حصصًا أو تكلفة؛ تبقى معطلة افتراضيًا ولا يستطيع تفعيلها إلا مالك مساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000806](../../web/workspace.html#L806) | 806 | `"  controls.append(consent);"` | — |
| [SRC-2C8F288796-L000807](../../web/workspace.html#L807) | 807 | `"  const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000808](../../web/workspace.html#L808) | 808 | `"  const status=make(\"p\",\"profile-note\");status.setAttribute(\"role\",\"status\");status.setAttribute(\"aria-live\",\"polite\");"` | — |
| [SRC-2C8F288796-L000809](../../web/workspace.html#L809) | 809 | `"  const run=action(\"بدء اكتشاف الطلب\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000810](../../web/workspace.html#L810) | 810 | `"   run.disabled=true;run.setAttribute(\"aria-busy\",\"true\");state.activeProfileId=profileSelect.value;"` | — |
| [SRC-2C8F288796-L000811](../../web/workspace.html#L811) | 811 | `"   status.className=\"profile-note\";status.textContent=\"جارٍ البحث عن إشارات الطلب؛ ستظل النتائج السابقة متاحة حتى تكتمل الجولة الجديدة.\";"` | — |
| [SRC-2C8F288796-L000812](../../web/workspace.html#L812) | 812 | `"   try{"` | — |
| [SRC-2C8F288796-L000813](../../web/workspace.html#L813) | 813 | `"    const savedRun=await api(\"/api/discoveries\",{method:\"POST\",body:{profile_id:profileSelect.value,allow_optional_providers:optional.checked}});"` | — |
| [SRC-2C8F288796-L000814](../../web/workspace.html#L814) | 814 | `"    state.activeDiscovery=savedRun;"` | — |
| [SRC-2C8F288796-L000815](../../web/workspace.html#L815) | 815 | `"    let refreshWarning=\"\";"` | — |
| [SRC-2C8F288796-L000816](../../web/workspace.html#L816) | 816 | `"    try{await loadDiscoveryRuns()}catch(refreshError){refreshWarning=\" حُفظت نتيجة البحث، لكن تعذر تحديث سجل العمليات: \"+escapeMessage(refreshError.message)}"` | — |
| [SRC-2C8F288796-L000817](../../web/workspace.html#L817) | 817 | `"    renderDiscovery();"` | — |
| [SRC-2C8F288796-L000818](../../web/workspace.html#L818) | 818 | `"    if(refreshWarning){const warning=make(\"p\",\"auth-error\",refreshWarning);warning.setAttribute(\"role\",\"alert\");$(\"viewRoot\").append(warning)}"` | — |
| [SRC-2C8F288796-L000819](../../web/workspace.html#L819) | 819 | `"   }catch(error){"` | — |
| [SRC-2C8F288796-L000820](../../web/workspace.html#L820) | 820 | `"    status.className=\"auth-error\";status.textContent=\"تعذر تشغيل الاكتشاف: \"+escapeMessage(error.message)+\" يمكنك المحاولة مجددًا. لم تُحذف النتائج السابقة.\";"` | — |
| [SRC-2C8F288796-L000821](../../web/workspace.html#L821) | 821 | `"   }finally{"` | — |
| [SRC-2C8F288796-L000822](../../web/workspace.html#L822) | 822 | `"    run.disabled=false;run.removeAttribute(\"aria-busy\");"` | — |
| [SRC-2C8F288796-L000823](../../web/workspace.html#L823) | 823 | `"   }"` | — |
| [SRC-2C8F288796-L000824](../../web/workspace.html#L824) | 824 | `"  });"` | — |
| [SRC-2C8F288796-L000825](../../web/workspace.html#L825) | 825 | `"  run.disabled=!canWrite();actions.append(run);controls.append(actions,status);"` | — |
| [SRC-2C8F288796-L000826](../../web/workspace.html#L826) | 826 | `" }"` | — |
| [SRC-2C8F288796-L000827](../../web/workspace.html#L827) | 827 | `" controls.append(make(\"p\",\"profile-note\",\"تاريخ النشر قد يكون غير متاح. المقتطف لا يعني أن الصفحة قُرئت. فشل الموصل لا يثبت عدم وجود عملاء. لا يتم إرسال أي رسالة من هذه الشاشة.\"));"` | — |
| [SRC-2C8F288796-L000828](../../web/workspace.html#L828) | 828 | `" controls.append(make(\"p\",\"profile-note\",\"تشغيل الاكتشاف يستخدم النموذج اللغوي المهيأ حاليًا في Omarai؛ قد يستهلك حصة أو تكلفة بحسب إعدادات مزود النموذج. لا تدخل بيانات سرية. الموصلات الاختيارية منفصلة وتظل معطلة افتراضيًا حتى موافقة المالك.\"));"` | — |
| [SRC-2C8F288796-L000829](../../web/workspace.html#L829) | 829 | `" root.append(controls);"` | — |
| [SRC-2C8F288796-L000830](../../web/workspace.html#L830) | 830 | `" if(state.discoveryRuns.length){"` | — |
| [SRC-2C8F288796-L000831](../../web/workspace.html#L831) | 831 | `"  const history=make(\"section\",\"glass panel profile-panel\"),hh=make(\"div\",\"panel-head\"),ht=make(\"div\");"` | — |
| [SRC-2C8F288796-L000832](../../web/workspace.html#L832) | 832 | `"  ht.append(make(\"h2\",\"\",\"سجل عمليات الاكتشاف\"),make(\"p\",\"\",\"عمليات محفوظة ضمن مساحة العمل الحالية.\"));"` | — |
| [SRC-2C8F288796-L000833](../../web/workspace.html#L833) | 833 | `"  hh.append(ht);history.append(hh);const list=make(\"div\",\"discovery-history\");"` | — |
| [SRC-2C8F288796-L000834](../../web/workspace.html#L834) | 834 | `"  state.discoveryRuns.forEach(item=>list.append(action("` | — |
| [SRC-2C8F288796-L000835](../../web/workspace.html#L835) | 835 | `"   String(item.profile_name\|\|\"ملف منتج\")+\" · \"+String(item.qualified_signal_count\|\|0)+\" إشارة · \"+String(item.created_at\|\|\"\"),"` | — |
| [SRC-2C8F288796-L000836](../../web/workspace.html#L836) | 836 | `"   \"\","` | — |
| [SRC-2C8F288796-L000837](../../web/workspace.html#L837) | 837 | `"   async()=>{try{state.activeDiscovery=await api(\"/api/discoveries/\"+encodeURIComponent(item.id));renderDiscovery()}catch(error){const message=make(\"p\",\"auth-error\",escapeMessage(error.message));message.setAttribute(\"role\",\"alert\");history.append(message)}}"` | — |
| [SRC-2C8F288796-L000838](../../web/workspace.html#L838) | 838 | `"  )));"` | — |
| [SRC-2C8F288796-L000839](../../web/workspace.html#L839) | 839 | `"  history.append(list);root.append(history);"` | — |
| [SRC-2C8F288796-L000840](../../web/workspace.html#L840) | 840 | `" }"` | — |
| [SRC-2C8F288796-L000841](../../web/workspace.html#L841) | 841 | `" if(state.activeDiscovery)root.append(renderDiscoveryRun(state.activeDiscovery));"` | — |
| [SRC-2C8F288796-L000842](../../web/workspace.html#L842) | 842 | `"}"` | — |
| [SRC-2C8F288796-L000843](../../web/workspace.html#L843) | 843 | `""` | — |
| [SRC-2C8F288796-L000844](../../web/workspace.html#L844) | 844 | `"const chatModes=["` | — |
| [SRC-2C8F288796-L000845](../../web/workspace.html#L845) | 845 | `" {id:\"auto\",label:\"تلقائي\"},"` | — |
| [SRC-2C8F288796-L000846](../../web/workspace.html#L846) | 846 | `" {id:\"deep\",label:\"بحث معمّق\"},"` | — |
| [SRC-2C8F288796-L000847](../../web/workspace.html#L847) | 847 | `" {id:\"latest\",label:\"الأحدث الآن\"},"` | — |
| [SRC-2C8F288796-L000848](../../web/workspace.html#L848) | 848 | `" {id:\"social\",label:\"آراء الناس\"}"` | — |
| [SRC-2C8F288796-L000849](../../web/workspace.html#L849) | 849 | `"];"` | — |
| [SRC-2C8F288796-L000850](../../web/workspace.html#L850) | 850 | `"function chatMessageNode(item){"` | — |
| [SRC-2C8F288796-L000851](../../web/workspace.html#L851) | 851 | `" const row=make(\"div\",\"chat-msg chat-\"+item.role);"` | — |
| [SRC-2C8F288796-L000852](../../web/workspace.html#L852) | 852 | `" row.append(make(\"div\",\"chat-who\",item.role===\"user\"?\"أنت\":\"Omarai\"));"` | — |
| [SRC-2C8F288796-L000853](../../web/workspace.html#L853) | 853 | `" row.append(make(\"div\",\"chat-text\",item.text));"` | — |
| [SRC-2C8F288796-L000854](../../web/workspace.html#L854) | 854 | `" if(item.role===\"assistant\"&&Array.isArray(item.sources)&&item.sources.length){"` | — |
| [SRC-2C8F288796-L000855](../../web/workspace.html#L855) | 855 | `"  const list=make(\"ul\",\"chat-sources\");"` | — |
| [SRC-2C8F288796-L000856](../../web/workspace.html#L856) | 856 | `"  item.sources.slice(0,8).forEach(src=>{"` | — |
| [SRC-2C8F288796-L000857](../../web/workspace.html#L857) | 857 | `"   const href=src&&safeHttp(src.url);if(!href)return;"` | — |
| [SRC-2C8F288796-L000858](../../web/workspace.html#L858) | 858 | `"   const li=make(\"li\");const a=make(\"a\",\"\",String(src.title\|\|href).slice(0,140));"` | — |
| [SRC-2C8F288796-L000859](../../web/workspace.html#L859) | 859 | `"   a.href=href;a.target=\"_blank\";a.rel=\"noopener noreferrer\";li.append(a);list.append(li);"` | — |
| [SRC-2C8F288796-L000860](../../web/workspace.html#L860) | 860 | `"  });"` | — |
| [SRC-2C8F288796-L000861](../../web/workspace.html#L861) | 861 | `"  if(list.childNodes.length){row.append(make(\"div\",\"chat-who\",\"المصادر\"),list)}"` | — |
| [SRC-2C8F288796-L000862](../../web/workspace.html#L862) | 862 | `" }"` | — |
| [SRC-2C8F288796-L000863](../../web/workspace.html#L863) | 863 | `" if(item.role===\"assistant\"&&item.note)row.append(make(\"div\",\"chat-note\",item.note));"` | — |
| [SRC-2C8F288796-L000864](../../web/workspace.html#L864) | 864 | `" return row;"` | — |
| [SRC-2C8F288796-L000865](../../web/workspace.html#L865) | 865 | `"}"` | — |
| [SRC-2C8F288796-L000866](../../web/workspace.html#L866) | 866 | `"function renderChat(){"` | — |
| [SRC-2C8F288796-L000867](../../web/workspace.html#L867) | 867 | `" setPage(\"محادثة Omarai\",\"اسأل باللهجة المصرية أو الفصحى أو الإنجليزية. تُرسل الأسئلة إلى محركات البحث وقد تُرسل مقتطفات المصادر إلى مزود نموذج اللغة المضبوط.\",\"CHAT\");"` | — |
| [SRC-2C8F288796-L000868](../../web/workspace.html#L868) | 868 | `" const chat=state.chat;"` | — |
| [SRC-2C8F288796-L000869](../../web/workspace.html#L869) | 869 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000870](../../web/workspace.html#L870) | 870 | `" const panel=make(\"section\",\"glass panel chat-panel\");"` | — |
| [SRC-2C8F288796-L000871](../../web/workspace.html#L871) | 871 | `" const ph=make(\"div\",\"panel-head\");const pt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000872](../../web/workspace.html#L872) | 872 | `" pt.append(make(\"h2\",\"\",\"المحادثة والبحث\"),make(\"p\",\"\",\"يتذكر آخر ٨ رسائل داخل هذه الجلسة. لا تضع كلمات مرور أو مفاتيح API أو بيانات شخصية سرية في السؤال.\"));"` | — |
| [SRC-2C8F288796-L000873](../../web/workspace.html#L873) | 873 | `" const clear=action(\"محادثة جديدة\",\"ghost\",()=>{if(chat.busy)return;chat.messages=[];chat.history=[];renderChat()});"` | — |
| [SRC-2C8F288796-L000874](../../web/workspace.html#L874) | 874 | `" ph.append(pt,clear);panel.append(ph);"` | — |
| [SRC-2C8F288796-L000875](../../web/workspace.html#L875) | 875 | `""` | — |
| [SRC-2C8F288796-L000876](../../web/workspace.html#L876) | 876 | `" const modeBar=make(\"div\",\"chat-modes\");"` | — |
| [SRC-2C8F288796-L000877](../../web/workspace.html#L877) | 877 | `" chatModes.forEach(m=>{"` | — |
| [SRC-2C8F288796-L000878](../../web/workspace.html#L878) | 878 | `"  const b=make(\"button\",\"button ghost\"+(chat.mode===m.id?\" chat-mode-active\":\"\"),m.label);"` | — |
| [SRC-2C8F288796-L000879](../../web/workspace.html#L879) | 879 | `"  b.type=\"button\";b.setAttribute(\"aria-pressed\",chat.mode===m.id?\"true\":\"false\");b.disabled=chat.busy;"` | — |
| [SRC-2C8F288796-L000880](../../web/workspace.html#L880) | 880 | `"  b.addEventListener(\"click\",()=>{chat.mode=m.id;renderChat()});modeBar.append(b);"` | — |
| [SRC-2C8F288796-L000881](../../web/workspace.html#L881) | 881 | `" });"` | — |
| [SRC-2C8F288796-L000882](../../web/workspace.html#L882) | 882 | `" panel.append(modeBar);"` | — |
| [SRC-2C8F288796-L000883](../../web/workspace.html#L883) | 883 | `""` | — |
| [SRC-2C8F288796-L000884](../../web/workspace.html#L884) | 884 | `" const list=make(\"div\",\"chat-list\");list.id=\"chatList\";list.setAttribute(\"aria-live\",\"polite\");"` | — |
| [SRC-2C8F288796-L000885](../../web/workspace.html#L885) | 885 | `" if(!chat.messages.length){"` | — |
| [SRC-2C8F288796-L000886](../../web/workspace.html#L886) | 886 | `"  list.append(make(\"div\",\"chat-empty\",\"اكتب سؤالك لبدء المحادثة. مثال: «ايه أفضل طريقة أوصل بيها لشركات محتاجة نظام إنذار حريق؟»\"));"` | — |
| [SRC-2C8F288796-L000887](../../web/workspace.html#L887) | 887 | `" }else chat.messages.forEach(item=>list.append(chatMessageNode(item)));"` | — |
| [SRC-2C8F288796-L000888](../../web/workspace.html#L888) | 888 | `" panel.append(list);"` | — |
| [SRC-2C8F288796-L000889](../../web/workspace.html#L889) | 889 | `""` | — |
| [SRC-2C8F288796-L000890](../../web/workspace.html#L890) | 890 | `" const form=make(\"div\",\"chat-form\");"` | — |
| [SRC-2C8F288796-L000891](../../web/workspace.html#L891) | 891 | `" const input=make(\"textarea\");input.id=\"chatInput\";input.rows=2;input.maxLength=4000;input.placeholder=\"اكتب سؤالك هنا… (Enter للإرسال · Shift+Enter لسطر جديد)\";input.disabled=chat.busy;"` | — |
| [SRC-2C8F288796-L000892](../../web/workspace.html#L892) | 892 | `" const send=action(chat.busy?\"يبحث…\":\"أرسل ←\",\"primary\",()=>sendChat());send.id=\"chatSend\";send.disabled=chat.busy;"` | — |
| [SRC-2C8F288796-L000893](../../web/workspace.html#L893) | 893 | `" input.addEventListener(\"keydown\",e=>{if(e.key===\"Enter\"&&!e.shiftKey&&!e.isComposing){e.preventDefault();sendChat()}});"` | — |
| [SRC-2C8F288796-L000894](../../web/workspace.html#L894) | 894 | `" form.append(input,send);panel.append(form);"` | — |
| [SRC-2C8F288796-L000895](../../web/workspace.html#L895) | 895 | `" root.append(panel);"` | — |
| [SRC-2C8F288796-L000896](../../web/workspace.html#L896) | 896 | `" list.scrollTop=list.scrollHeight;"` | — |
| [SRC-2C8F288796-L000897](../../web/workspace.html#L897) | 897 | `" if(!chat.busy)input.focus();"` | — |
| [SRC-2C8F288796-L000898](../../web/workspace.html#L898) | 898 | `"}"` | — |
| [SRC-2C8F288796-L000899](../../web/workspace.html#L899) | 899 | `"async function sendChat(){"` | — |
| [SRC-2C8F288796-L000900](../../web/workspace.html#L900) | 900 | `" const chat=state.chat;if(chat.busy)return;"` | — |
| [SRC-2C8F288796-L000901](../../web/workspace.html#L901) | 901 | `" const requestSessionVersion=chat.sessionVersion;"` | — |
| [SRC-2C8F288796-L000902](../../web/workspace.html#L902) | 902 | `" const input=$(\"chatInput\");const question=input?input.value.trim():\"\";"` | — |
| [SRC-2C8F288796-L000903](../../web/workspace.html#L903) | 903 | `" if(!question)return;"` | — |
| [SRC-2C8F288796-L000904](../../web/workspace.html#L904) | 904 | `" chat.messages.push({role:\"user\",text:question});chat.busy=true;renderChat();"` | — |
| [SRC-2C8F288796-L000905](../../web/workspace.html#L905) | 905 | `" try{"` | — |
| [SRC-2C8F288796-L000906](../../web/workspace.html#L906) | 906 | `"  const data=await api(\"/api/agent\",{method:\"POST\",body:{question:question,history:chat.history.slice(-8),mode:chat.mode}});"` | — |
| [SRC-2C8F288796-L000907](../../web/workspace.html#L907) | 907 | `"  if(state.chat.sessionVersion!==requestSessionVersion)return;"` | — |
| [SRC-2C8F288796-L000908](../../web/workspace.html#L908) | 908 | `"  const answer=String(data.answer\|\|\"لم يرجع الخادم نص إجابة.\");"` | — |
| [SRC-2C8F288796-L000909](../../web/workspace.html#L909) | 909 | `"  const note=data.kind===\"general_answer\"?\"إجابة معرفة عامة دون بحث ويب.\":(data.used_web_search===true?\"\":\"لم يُجرَ بحث ويب لهذه الإجابة.\");"` | — |
| [SRC-2C8F288796-L000910](../../web/workspace.html#L910) | 910 | `"  chat.messages.push({role:\"assistant\",text:answer,sources:Array.isArray(data.sources)?data.sources:[],note:note});"` | — |
| [SRC-2C8F288796-L000911](../../web/workspace.html#L911) | 911 | `"  chat.history.push({role:\"user\",content:question},{role:\"assistant\",content:answer});"` | — |
| [SRC-2C8F288796-L000912](../../web/workspace.html#L912) | 912 | `"  chat.history=chat.history.slice(-16);"` | — |
| [SRC-2C8F288796-L000913](../../web/workspace.html#L913) | 913 | `" }catch(error){"` | — |
| [SRC-2C8F288796-L000914](../../web/workspace.html#L914) | 914 | `"  if(state.chat.sessionVersion===requestSessionVersion){"` | — |
| [SRC-2C8F288796-L000915](../../web/workspace.html#L915) | 915 | `"   chat.messages.push({role:\"assistant\",text:\"تعذر إكمال الطلب: \"+escapeMessage(error&&error.message),sources:[],note:\"\"});"` | — |
| [SRC-2C8F288796-L000916](../../web/workspace.html#L916) | 916 | `"  }"` | — |
| [SRC-2C8F288796-L000917](../../web/workspace.html#L917) | 917 | `" }finally{"` | — |
| [SRC-2C8F288796-L000918](../../web/workspace.html#L918) | 918 | `"  if(state.chat.sessionVersion===requestSessionVersion){"` | — |
| [SRC-2C8F288796-L000919](../../web/workspace.html#L919) | 919 | `"   chat.busy=false;"` | — |
| [SRC-2C8F288796-L000920](../../web/workspace.html#L920) | 920 | `"   if(state.activeView===\"chat\")renderChat();"` | — |
| [SRC-2C8F288796-L000921](../../web/workspace.html#L921) | 921 | `"  }"` | — |
| [SRC-2C8F288796-L000922](../../web/workspace.html#L922) | 922 | `" }"` | — |
| [SRC-2C8F288796-L000923](../../web/workspace.html#L923) | 923 | `"}"` | — |
| [SRC-2C8F288796-L000924](../../web/workspace.html#L924) | 924 | `"function renderCurrent(){"` | — |
| [SRC-2C8F288796-L000925](../../web/workspace.html#L925) | 925 | `" renderNav();"` | — |
| [SRC-2C8F288796-L000926](../../web/workspace.html#L926) | 926 | `" if(state.activeView===\"overview\")renderOverview();"` | — |
| [SRC-2C8F288796-L000927](../../web/workspace.html#L927) | 927 | `" else if(state.activeView===\"indicators\")renderIndicators();"` | — |
| [SRC-2C8F288796-L000928](../../web/workspace.html#L928) | 928 | `" else if(state.activeView===\"offer\")renderProductProfile();"` | — |
| [SRC-2C8F288796-L000929](../../web/workspace.html#L929) | 929 | `" else if(state.activeView===\"campaign\")renderDiscovery();"` | — |
| [SRC-2C8F288796-L000930](../../web/workspace.html#L930) | 930 | `" else if(state.activeView===\"signals\")renderSignals();"` | — |
| [SRC-2C8F288796-L000931](../../web/workspace.html#L931) | 931 | `" else if(state.activeView===\"pipeline\")renderPipeline();"` | — |
| [SRC-2C8F288796-L000932](../../web/workspace.html#L932) | 932 | `" else if(state.activeView===\"chat\")renderChat();"` | — |
| [SRC-2C8F288796-L000933](../../web/workspace.html#L933) | 933 | `" else if(state.activeView===\"system\")renderSystem();"` | — |
| [SRC-2C8F288796-L000934](../../web/workspace.html#L934) | 934 | `" else renderPlaceholder(state.activeView);"` | — |
| [SRC-2C8F288796-L000935](../../web/workspace.html#L935) | 935 | `" if(state.loadWarnings.length){"` | — |
| [SRC-2C8F288796-L000936](../../web/workspace.html#L936) | 936 | `"  $(\"viewRoot\").prepend(make(\"p\",\"auth-error\",\"تم التحقق من الجلسة؛ تعذر تحميل بعض البيانات: \"+state.loadWarnings.join(\"، \")+\". قد تكون بعض القوائم والأرقام غير مكتملة.\"));"` | — |
| [SRC-2C8F288796-L000937](../../web/workspace.html#L937) | 937 | `" }"` | — |
| [SRC-2C8F288796-L000938](../../web/workspace.html#L938) | 938 | `"}"` | — |
| [SRC-2C8F288796-L000939](../../web/workspace.html#L939) | 939 | `"function navigate(view){"` | — |
| [SRC-2C8F288796-L000940](../../web/workspace.html#L940) | 940 | `" state.activeView=view;renderCurrent();"` | — |
| [SRC-2C8F288796-L000941](../../web/workspace.html#L941) | 941 | `"}"` | — |
| [SRC-2C8F288796-L000942](../../web/workspace.html#L942) | 942 | `"async function loadProductProfiles(){"` | — |
| [SRC-2C8F288796-L000943](../../web/workspace.html#L943) | 943 | `" const data=await api(\"/api/product-profiles\");"` | — |
| [SRC-2C8F288796-L000944](../../web/workspace.html#L944) | 944 | `" state.profiles=Array.isArray(data.profiles)?data.profiles:[];"` | — |
| [SRC-2C8F288796-L000945](../../web/workspace.html#L945) | 945 | `" if(!state.profiles.some(item=>item.id===state.activeProfileId))state.activeProfileId=state.profiles[0]?.id\|\|null;"` | — |
| [SRC-2C8F288796-L000946](../../web/workspace.html#L946) | 946 | `"}"` | — |
| [SRC-2C8F288796-L000947](../../web/workspace.html#L947) | 947 | `"async function loadDiscoveryRuns(){"` | — |
| [SRC-2C8F288796-L000948](../../web/workspace.html#L948) | 948 | `" const data=await api(\"/api/discoveries\");"` | — |
| [SRC-2C8F288796-L000949](../../web/workspace.html#L949) | 949 | `" state.discoveryRuns=Array.isArray(data.runs)?data.runs:[];"` | — |
| [SRC-2C8F288796-L000950](../../web/workspace.html#L950) | 950 | `"}"` | — |
| [SRC-2C8F288796-L000951](../../web/workspace.html#L951) | 951 | `"async function loadLeads(){"` | — |
| [SRC-2C8F288796-L000952](../../web/workspace.html#L952) | 952 | `" const data=await api(\"/api/leads?limit=500\");"` | — |
| [SRC-2C8F288796-L000953](../../web/workspace.html#L953) | 953 | `" state.leads=Array.isArray(data.leads)?data.leads:[];"` | — |
| [SRC-2C8F288796-L000954](../../web/workspace.html#L954) | 954 | `"}"` | — |
| [SRC-2C8F288796-L000955](../../web/workspace.html#L955) | 955 | `"async function bootstrap(){"` | — |
| [SRC-2C8F288796-L000956](../../web/workspace.html#L956) | 956 | `" let session;"` | — |
| [SRC-2C8F288796-L000957](../../web/workspace.html#L957) | 957 | `" try{"` | — |
| [SRC-2C8F288796-L000958](../../web/workspace.html#L958) | 958 | `"  session=await api(\"/api/session\");"` | — |
| [SRC-2C8F288796-L000959](../../web/workspace.html#L959) | 959 | `" }catch(e){"` | — |
| [SRC-2C8F288796-L000960](../../web/workspace.html#L960) | 960 | `"  setConnection(false,\"يلزم تسجيل الدخول\",\"تعذر التحقق من جلسة المستخدم.\");"` | — |
| [SRC-2C8F288796-L000961](../../web/workspace.html#L961) | 961 | `"  showAuth(e.message);"` | — |
| [SRC-2C8F288796-L000962](../../web/workspace.html#L962) | 962 | `"  $(\"viewRoot\").replaceChildren(emptyState(\"مساحة العمل مقفلة\",\"سجّل الدخول لقراءة البيانات المرتبطة بمساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000963](../../web/workspace.html#L963) | 963 | `"  return;"` | — |
| [SRC-2C8F288796-L000964](../../web/workspace.html#L964) | 964 | `" }"` | — |
| [SRC-2C8F288796-L000965](../../web/workspace.html#L965) | 965 | `" state.role=session.role\|\|\"unknown\";"` | — |
| [SRC-2C8F288796-L000966](../../web/workspace.html#L966) | 966 | `" $(\"rolePill\").textContent=\"صلاحية: \"+state.role;"` | — |
| [SRC-2C8F288796-L000967](../../web/workspace.html#L967) | 967 | `" $(\"roleSummary\").textContent=\"الدور: \"+state.role+(canWrite()?\" — إضافة وتحديث السجلات متاح.\":\" — قراءة فقط.\");"` | — |
| [SRC-2C8F288796-L000968](../../web/workspace.html#L968) | 968 | `" hideAuth();"` | — |
| [SRC-2C8F288796-L000969](../../web/workspace.html#L969) | 969 | `" const results=await Promise.allSettled(["` | — |
| [SRC-2C8F288796-L000970](../../web/workspace.html#L970) | 970 | `"  loadLeads(),"` | — |
| [SRC-2C8F288796-L000971](../../web/workspace.html#L971) | 971 | `"  loadProductProfiles(),"` | — |
| [SRC-2C8F288796-L000972](../../web/workspace.html#L972) | 972 | `"  loadDiscoveryRuns()"` | — |
| [SRC-2C8F288796-L000973](../../web/workspace.html#L973) | 973 | `" ]);"` | — |
| [SRC-2C8F288796-L000974](../../web/workspace.html#L974) | 974 | `" if($(\"authGate\").classList.contains(\"open\")){"` | — |
| [SRC-2C8F288796-L000975](../../web/workspace.html#L975) | 975 | `"  setConnection(false,\"يلزم تسجيل الدخول\",\"انتهت الجلسة أثناء تحميل البيانات.\");"` | — |
| [SRC-2C8F288796-L000976](../../web/workspace.html#L976) | 976 | `"  $(\"viewRoot\").replaceChildren(emptyState(\"مساحة العمل مقفلة\",\"سجّل الدخول لقراءة البيانات المرتبطة بمساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000977](../../web/workspace.html#L977) | 977 | `"  return;"` | — |
| [SRC-2C8F288796-L000978](../../web/workspace.html#L978) | 978 | `" }"` | — |
| [SRC-2C8F288796-L000979](../../web/workspace.html#L979) | 979 | `" state.loadWarnings=[];"` | — |
| [SRC-2C8F288796-L000980](../../web/workspace.html#L980) | 980 | `" const labels=[\"سجل الإشارات\",\"ملفات المنتجات\",\"سجل الاكتشاف\"];"` | — |
| [SRC-2C8F288796-L000981](../../web/workspace.html#L981) | 981 | `" results.forEach((result,index)=>{"` | — |
| [SRC-2C8F288796-L000982](../../web/workspace.html#L982) | 982 | `"  if(result.status!==\"rejected\")return;"` | — |
| [SRC-2C8F288796-L000983](../../web/workspace.html#L983) | 983 | `"  state.loadWarnings.push(labels[index]);"` | — |
| [SRC-2C8F288796-L000984](../../web/workspace.html#L984) | 984 | `"  if(index===0)state.leads=[];"` | — |
| [SRC-2C8F288796-L000985](../../web/workspace.html#L985) | 985 | `"  else if(index===1)state.profiles=[];"` | — |
| [SRC-2C8F288796-L000986](../../web/workspace.html#L986) | 986 | `"  else state.discoveryRuns=[];"` | — |
| [SRC-2C8F288796-L000987](../../web/workspace.html#L987) | 987 | `" });"` | — |
| [SRC-2C8F288796-L000988](../../web/workspace.html#L988) | 988 | `" const note=state.loadWarnings.length"` | — |
| [SRC-2C8F288796-L000989](../../web/workspace.html#L989) | 989 | `"  ?\"الجلسة مصادق عليها؛ تعذر تحميل بعض البيانات: \"+state.loadWarnings.join(\"، \")+\". حاول تحديث الوحدة لاحقًا.\""` | — |
| [SRC-2C8F288796-L000990](../../web/workspace.html#L990) | 990 | `"  :\"تم تحميل الإشارات وملفات المنتج وسجل الاكتشاف. هذا لا يثبت اتصال جميع الموصلات.\";"` | — |
| [SRC-2C8F288796-L000991](../../web/workspace.html#L991) | 991 | `" setConnection(true,state.loadWarnings.length?\"الجلسة مصادق عليها — بيانات جزئية\":\"الجلسة مصادق عليها\",note);"` | — |
| [SRC-2C8F288796-L000992](../../web/workspace.html#L992) | 992 | `" renderCurrent();"` | — |
| [SRC-2C8F288796-L000993](../../web/workspace.html#L993) | 993 | `"}"` | — |
| [SRC-2C8F288796-L000994](../../web/workspace.html#L994) | 994 | `"$(\"loginForm\").addEventListener(\"submit\",async event=>{"` | — |
| [SRC-2C8F288796-L000995](../../web/workspace.html#L995) | 995 | `" event.preventDefault();const token=$(\"accessToken\").value.trim();const button=$(\"loginButton\");button.disabled=true;$(\"authError\").textContent=\"\";"` | — |
| [SRC-2C8F288796-L000996](../../web/workspace.html#L996) | 996 | `" try{"` | — |
| [SRC-2C8F288796-L000997](../../web/workspace.html#L997) | 997 | `"  await api(\"/api/session\",{method:\"POST\",body:{access_token:token}});"` | — |
| [SRC-2C8F288796-L000998](../../web/workspace.html#L998) | 998 | `"  advanceWorkspaceSessionVersion();clearChatSession();"` | — |
| [SRC-2C8F288796-L000999](../../web/workspace.html#L999) | 999 | `"  $(\"accessToken\").value=\"\";await bootstrap();"` | — |
| [SRC-2C8F288796-L001000](../../web/workspace.html#L1000) | 1000 | `" }catch(e){$(\"authError\").textContent=escapeMessage(e.message)}"` | — |
| [SRC-2C8F288796-L001001](../../web/workspace.html#L1001) | 1001 | `" finally{button.disabled=false}"` | — |
| [SRC-2C8F288796-L001002](../../web/workspace.html#L1002) | 1002 | `"});"` | — |
| [SRC-2C8F288796-L001003](../../web/workspace.html#L1003) | 1003 | `"$(\"logoutButton\").addEventListener(\"click\",async()=>{"` | — |
| [SRC-2C8F288796-L001004](../../web/workspace.html#L1004) | 1004 | `" try{"` | — |
| [SRC-2C8F288796-L001005](../../web/workspace.html#L1005) | 1005 | `"  await api(\"/api/session/logout\",{method:\"POST\",body:{}});"` | — |
| [SRC-2C8F288796-L001006](../../web/workspace.html#L1006) | 1006 | `" }catch(e){"` | — |
| [SRC-2C8F288796-L001007](../../web/workspace.html#L1007) | 1007 | `"  alert(\"تعذر تسجيل الخروج من الخادم؛ لم يتم تغيير حالة الجلسة في الواجهة. \"+escapeMessage(e.message));"` | — |
| [SRC-2C8F288796-L001008](../../web/workspace.html#L1008) | 1008 | `"  return;"` | — |
| [SRC-2C8F288796-L001009](../../web/workspace.html#L1009) | 1009 | `" }"` | — |
| [SRC-2C8F288796-L001010](../../web/workspace.html#L1010) | 1010 | `" state.role=null;state.leads=[];state.profiles=[];state.discoveryRuns=[];state.loadWarnings=[];state.activeDiscovery=null;state.activeProfileId=null;state.activeView=\"overview\";showAuth(\"تم تسجيل الخروج. أدخل رمز الوصول للمتابعة.\");setConnection(false,\"غير متصل\",\"سجّل الدخول لعرض السجلات.\");"` | — |
| [SRC-2C8F288796-L001011](../../web/workspace.html#L1011) | 1011 | `"});"` | — |
| [SRC-2C8F288796-L001012](../../web/workspace.html#L1012) | 1012 | `"$(\"addSignalTop\").addEventListener(\"click\",()=>navigate(\"signals\"));"` | — |
| [SRC-2C8F288796-L001013](../../web/workspace.html#L1013) | 1013 | `"$(\"closeDetail\").addEventListener(\"click\",closeDetails);"` | — |
| [SRC-2C8F288796-L001014](../../web/workspace.html#L1014) | 1014 | `"$(\"chatNav\").addEventListener(\"click\",()=>navigate(\"chat\"));"` | — |
| [SRC-2C8F288796-L001015](../../web/workspace.html#L1015) | 1015 | `"$(\"systemNav\").addEventListener(\"click\",()=>navigate(\"system\"));"` | — |
| [SRC-2C8F288796-L001016](../../web/workspace.html#L1016) | 1016 | `"$(\"detailDrawer\").addEventListener(\"click\",e=>{if(e.target===$(\"detailDrawer\"))closeDetails()});"` | — |
| [SRC-2C8F288796-L001017](../../web/workspace.html#L1017) | 1017 | `"document.addEventListener(\"keydown\",e=>{if(e.key===\"Escape\")closeDetails()});"` | — |
| [SRC-2C8F288796-L001018](../../web/workspace.html#L1018) | 1018 | `"renderNav();bootstrap();"` | — |
| [SRC-2C8F288796-L001019](../../web/workspace.html#L1019) | 1019 | `"})();"` | — |
| [SRC-2C8F288796-L001020](../../web/workspace.html#L1020) | 1020 | `"</script>"` | — |
| [SRC-2C8F288796-L001021](../../web/workspace.html#L1021) | 1021 | `"</body>"` | — |
| [SRC-2C8F288796-L001022](../../web/workspace.html#L1022) | 1022 | `"</html>"` | — |
