# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **061**
- سجلات الأسطر: **101**
- النطاق: SRC-2C8F288796-L000477 إلى SRC-2C8F288796-L000577
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
