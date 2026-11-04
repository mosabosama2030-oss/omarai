# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **061**
- سجلات الأسطر: **56**
- النطاق: SRC-2C8F288796-L000522 إلى SRC-2C8F288796-L000577
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
