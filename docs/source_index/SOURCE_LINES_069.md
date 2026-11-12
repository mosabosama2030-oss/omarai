# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **069**
- سجلات الأسطر: **799**
- النطاق: SRC-2C8F288796-L000295 إلى SRC-2C8F288796-L001093
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2C8F288796-L000295](../../web/workspace.html#L295) | 295 | `"const statuses=["` | — |
| [SRC-2C8F288796-L000296](../../web/workspace.html#L296) | 296 | `" {id:\"new\",label:\"جديد\"},"` | — |
| [SRC-2C8F288796-L000297](../../web/workspace.html#L297) | 297 | `" {id:\"needs_review\",label:\"يحتاج مراجعة\"},"` | — |
| [SRC-2C8F288796-L000298](../../web/workspace.html#L298) | 298 | `" {id:\"qualified\",label:\"مؤهل\"},"` | — |
| [SRC-2C8F288796-L000299](../../web/workspace.html#L299) | 299 | `" {id:\"contacted\",label:\"تم التواصل\"},"` | — |
| [SRC-2C8F288796-L000300](../../web/workspace.html#L300) | 300 | `" {id:\"converted\",label:\"تحول لعميل\"},"` | — |
| [SRC-2C8F288796-L000301](../../web/workspace.html#L301) | 301 | `" {id:\"rejected\",label:\"مرفوض\"}"` | — |
| [SRC-2C8F288796-L000302](../../web/workspace.html#L302) | 302 | `"];"` | — |
| [SRC-2C8F288796-L000303](../../web/workspace.html#L303) | 303 | `"const labels={high_intent:\"إشارة قوية نسبيًا\",medium_intent:\"إشارة متوسطة\",early_research:\"استكشاف مبكر\",unclear:\"غير واضحة\",not_buyer_signal:\"ليست إشارة شراء مباشرة\"};"` | — |
| [SRC-2C8F288796-L000304](../../web/workspace.html#L304) | 304 | `"const menu=["` | — |
| [SRC-2C8F288796-L000305](../../web/workspace.html#L305) | 305 | `" {id:\"overview\",label:\"نظرة عامة\",icon:\"⌂\",enabled:true},"` | — |
| [SRC-2C8F288796-L000306](../../web/workspace.html#L306) | 306 | `" {id:\"offer\",label:\"ملف المنتج\",icon:\"◇\",enabled:true},"` | — |
| [SRC-2C8F288796-L000307](../../web/workspace.html#L307) | 307 | `" {id:\"campaign\",label:\"حملات الاكتشاف\",icon:\"⌕\",enabled:true},"` | — |
| [SRC-2C8F288796-L000308](../../web/workspace.html#L308) | 308 | `" {id:\"signals\",label:\"إشارات الطلب\",icon:\"▤\",enabled:true},"` | — |
| [SRC-2C8F288796-L000309](../../web/workspace.html#L309) | 309 | `" {id:\"pipeline\",label:\"مسار التأهيل\",icon:\"⇢\",enabled:true},"` | — |
| [SRC-2C8F288796-L000310](../../web/workspace.html#L310) | 310 | `" {id:\"indicators\",label:\"مؤشرات الأداء\",icon:\"▥\",enabled:true}"` | — |
| [SRC-2C8F288796-L000311](../../web/workspace.html#L311) | 311 | `"];"` | — |
| [SRC-2C8F288796-L000312](../../web/workspace.html#L312) | 312 | `"function make(tag,cls,text){"` | — |
| [SRC-2C8F288796-L000313](../../web/workspace.html#L313) | 313 | `" const node=document.createElement(tag);"` | — |
| [SRC-2C8F288796-L000314](../../web/workspace.html#L314) | 314 | `" if(cls)node.className=cls;"` | — |
| [SRC-2C8F288796-L000315](../../web/workspace.html#L315) | 315 | `" if(text!==undefined&&text!==null)node.textContent=String(text);"` | — |
| [SRC-2C8F288796-L000316](../../web/workspace.html#L316) | 316 | `" return node;"` | — |
| [SRC-2C8F288796-L000317](../../web/workspace.html#L317) | 317 | `"}"` | — |
| [SRC-2C8F288796-L000318](../../web/workspace.html#L318) | 318 | `"function action(label,cls,handler){"` | — |
| [SRC-2C8F288796-L000319](../../web/workspace.html#L319) | 319 | `" const b=make(\"button\",\"button \"+(cls\|\|\"\"),label);"` | — |
| [SRC-2C8F288796-L000320](../../web/workspace.html#L320) | 320 | `" b.type=\"button\";b.addEventListener(\"click\",handler);return b;"` | — |
| [SRC-2C8F288796-L000321](../../web/workspace.html#L321) | 321 | `"}"` | — |
| [SRC-2C8F288796-L000322](../../web/workspace.html#L322) | 322 | `"function safeHttp(value){"` | — |
| [SRC-2C8F288796-L000323](../../web/workspace.html#L323) | 323 | `" try{const u=new URL(String(value\|\|\"\"));if((u.protocol!==\"http:\"&&u.protocol!==\"https:\")\|\|!u.hostname\|\|u.username\|\|u.password)return null;return u.href}catch(_e){return null}"` | — |
| [SRC-2C8F288796-L000324](../../web/workspace.html#L324) | 324 | `"}"` | — |
| [SRC-2C8F288796-L000325](../../web/workspace.html#L325) | 325 | `"function escapeMessage(message){return String(message\|\|\"حدث خطأ غير متوقع\").slice(0,500)}"` | — |
| [SRC-2C8F288796-L000326](../../web/workspace.html#L326) | 326 | `"async function api(path,options){"` | — |
| [SRC-2C8F288796-L000327](../../web/workspace.html#L327) | 327 | `" const opts=options\|\|{};"` | — |
| [SRC-2C8F288796-L000328](../../web/workspace.html#L328) | 328 | `" const requestSessionVersion=state.authSessionVersion;"` | — |
| [SRC-2C8F288796-L000329](../../web/workspace.html#L329) | 329 | `" const headers={};"` | — |
| [SRC-2C8F288796-L000330](../../web/workspace.html#L330) | 330 | `" if(opts.body!==undefined)headers[\"Content-Type\"]=\"application/json\";"` | — |
| [SRC-2C8F288796-L000331](../../web/workspace.html#L331) | 331 | `" const response=await fetch(path,{method:opts.method\|\|\"GET\",credentials:\"same-origin\",headers:headers,signal:opts.signal,body:opts.body===undefined?undefined:JSON.stringify(opts.body)});"` | — |
| [SRC-2C8F288796-L000332](../../web/workspace.html#L332) | 332 | `" let data={};"` | — |
| [SRC-2C8F288796-L000333](../../web/workspace.html#L333) | 333 | `" try{data=await response.json()}catch(_e){data={error:\"تعذر قراءة استجابة الخادم\"}}"` | — |
| [SRC-2C8F288796-L000334](../../web/workspace.html#L334) | 334 | `" if(response.status===401){showAuth(\"انتهت الجلسة أو لم يتم تسجيل الدخول. أدخل رمز الوصول للمتابعة.\");throw new Error(\"يلزم تسجيل الدخول مجددًا.\")}"` | — |
| [SRC-2C8F288796-L000335](../../web/workspace.html#L335) | 335 | `" if(state.authSessionVersion!==requestSessionVersion)throw new Error(\"انتهت الجلسة أثناء الطلب؛ أعد تسجيل الدخول.\");"` | — |
| [SRC-2C8F288796-L000336](../../web/workspace.html#L336) | 336 | `" if(!response.ok)throw new Error(data.error\|\|(\"فشل الطلب (\"+response.status+\")\"));"` | — |
| [SRC-2C8F288796-L000337](../../web/workspace.html#L337) | 337 | `" return data;"` | — |
| [SRC-2C8F288796-L000338](../../web/workspace.html#L338) | 338 | `"}"` | — |
| [SRC-2C8F288796-L000339](../../web/workspace.html#L339) | 339 | `"function clearChatSession(){"` | — |
| [SRC-2C8F288796-L000340](../../web/workspace.html#L340) | 340 | `" const chat=state.chat;"` | — |
| [SRC-2C8F288796-L000341](../../web/workspace.html#L341) | 341 | `" chat.messages=[];chat.history=[];chat.busy=false;chat.mode=\"deep\";"` | — |
| [SRC-2C8F288796-L000342](../../web/workspace.html#L342) | 342 | `" chat.sessionVersion=(chat.sessionVersion\|\|0)+1;"` | — |
| [SRC-2C8F288796-L000343](../../web/workspace.html#L343) | 343 | `"}"` | — |
| [SRC-2C8F288796-L000344](../../web/workspace.html#L344) | 344 | `"function advanceWorkspaceSessionVersion(){"` | — |
| [SRC-2C8F288796-L000345](../../web/workspace.html#L345) | 345 | `" state.authSessionVersion=(state.authSessionVersion\|\|0)+1;"` | — |
| [SRC-2C8F288796-L000346](../../web/workspace.html#L346) | 346 | `"}"` | — |
| [SRC-2C8F288796-L000347](../../web/workspace.html#L347) | 347 | `"function clearWorkspaceSession(){"` | — |
| [SRC-2C8F288796-L000348](../../web/workspace.html#L348) | 348 | `" advanceWorkspaceSessionVersion();"` | — |
| [SRC-2C8F288796-L000349](../../web/workspace.html#L349) | 349 | `" state.role=null;state.leads=[];state.profiles=[];state.discoveryRuns=[];state.loadWarnings=[];"` | — |
| [SRC-2C8F288796-L000350](../../web/workspace.html#L350) | 350 | `" state.activeDiscovery=null;state.activeProfileId=null;state.activeView=\"overview\";"` | — |
| [SRC-2C8F288796-L000351](../../web/workspace.html#L351) | 351 | `" state.analysis=null;state.filtered=[];state.search=\"\";state.filter=\"all\";"` | — |
| [SRC-2C8F288796-L000352](../../web/workspace.html#L352) | 352 | `" clearChatSession();"` | — |
| [SRC-2C8F288796-L000353](../../web/workspace.html#L353) | 353 | `" closeDetails();$(\"detailBody\").replaceChildren();"` | — |
| [SRC-2C8F288796-L000354](../../web/workspace.html#L354) | 354 | `" $(\"viewRoot\").replaceChildren(emptyState(\"مساحة العمل مقفلة\",\"سجّل الدخول لقراءة البيانات المرتبطة بمساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000355](../../web/workspace.html#L355) | 355 | `" $(\"rolePill\").textContent=\"غير مسجل\";"` | — |
| [SRC-2C8F288796-L000356](../../web/workspace.html#L356) | 356 | `" $(\"roleSummary\").textContent=\"لم يتم التحقق من جلسة مستخدم.\";"` | — |
| [SRC-2C8F288796-L000357](../../web/workspace.html#L357) | 357 | `" renderNav();"` | — |
| [SRC-2C8F288796-L000358](../../web/workspace.html#L358) | 358 | `"}"` | — |
| [SRC-2C8F288796-L000359](../../web/workspace.html#L359) | 359 | `"function showAuth(message){"` | — |
| [SRC-2C8F288796-L000360](../../web/workspace.html#L360) | 360 | `" clearWorkspaceSession();"` | — |
| [SRC-2C8F288796-L000361](../../web/workspace.html#L361) | 361 | `" $(\"authGate\").classList.add(\"open\");"` | — |
| [SRC-2C8F288796-L000362](../../web/workspace.html#L362) | 362 | `" $(\"authError\").textContent=message\|\|\"\";"` | — |
| [SRC-2C8F288796-L000363](../../web/workspace.html#L363) | 363 | `" $(\"accessToken\").value=\"\";"` | — |
| [SRC-2C8F288796-L000364](../../web/workspace.html#L364) | 364 | `"}"` | — |
| [SRC-2C8F288796-L000365](../../web/workspace.html#L365) | 365 | `"function hideAuth(){ $(\"authGate\").classList.remove(\"open\"); $(\"authError\").textContent=\"\"; }"` | — |
| [SRC-2C8F288796-L000366](../../web/workspace.html#L366) | 366 | `"function statusLabel(id){const item=statuses.find(x=>x.id===id);return item?item.label:id\|\|\"غير محدد\"}"` | — |
| [SRC-2C8F288796-L000367](../../web/workspace.html#L367) | 367 | `"function tag(text,cls){return make(\"span\",\"tag \"+(cls\|\|\"\"),text)}"` | — |
| [SRC-2C8F288796-L000368](../../web/workspace.html#L368) | 368 | `"function setPage(title,description,eyebrow){"` | — |
| [SRC-2C8F288796-L000369](../../web/workspace.html#L369) | 369 | `" $(\"crumb\").textContent=title;$(\"pageTitle\").textContent=title;$(\"pageDescription\").textContent=description\|\|\"\";"` | — |
| [SRC-2C8F288796-L000370](../../web/workspace.html#L370) | 370 | `" $(\"pageEyebrow\").textContent=eyebrow\|\|\"OMARAI WORKSPACE\";"` | — |
| [SRC-2C8F288796-L000371](../../web/workspace.html#L371) | 371 | `"}"` | — |
| [SRC-2C8F288796-L000372](../../web/workspace.html#L372) | 372 | `"function renderNav(){"` | — |
| [SRC-2C8F288796-L000373](../../web/workspace.html#L373) | 373 | `" const nav=$(\"mainNav\");nav.replaceChildren();"` | — |
| [SRC-2C8F288796-L000374](../../web/workspace.html#L374) | 374 | `" menu.forEach(item=>{"` | — |
| [SRC-2C8F288796-L000375](../../web/workspace.html#L375) | 375 | `"  const b=make(\"button\",state.activeView===item.id?\"active\":\"\",null);"` | — |
| [SRC-2C8F288796-L000376](../../web/workspace.html#L376) | 376 | `"  b.type=\"button\";b.setAttribute(\"aria-current\",state.activeView===item.id?\"page\":\"false\");"` | — |
| [SRC-2C8F288796-L000377](../../web/workspace.html#L377) | 377 | `"  const icon=make(\"span\",\"nav-icon\",item.icon);const name=make(\"span\",\"\",item.label);b.append(icon,name);"` | — |
| [SRC-2C8F288796-L000378](../../web/workspace.html#L378) | 378 | `"  if(!item.enabled)b.append(make(\"span\",\"nav-status\",\"قريبًا\"));"` | — |
| [SRC-2C8F288796-L000379](../../web/workspace.html#L379) | 379 | `"  if(item.enabled)b.addEventListener(\"click\",()=>navigate(item.id));"` | — |
| [SRC-2C8F288796-L000380](../../web/workspace.html#L380) | 380 | `"  else b.addEventListener(\"click\",()=>navigate(item.id));"` | — |
| [SRC-2C8F288796-L000381](../../web/workspace.html#L381) | 381 | `"  if(!item.enabled)b.classList.add(\"disabled\");"` | — |
| [SRC-2C8F288796-L000382](../../web/workspace.html#L382) | 382 | `"  nav.append(b);"` | — |
| [SRC-2C8F288796-L000383](../../web/workspace.html#L383) | 383 | `" });"` | — |
| [SRC-2C8F288796-L000384](../../web/workspace.html#L384) | 384 | `"}"` | — |
| [SRC-2C8F288796-L000385](../../web/workspace.html#L385) | 385 | `"function setConnection(ok,label,note){"` | — |
| [SRC-2C8F288796-L000386](../../web/workspace.html#L386) | 386 | `" $(\"apiDot\").className=\"dot \"+(ok?\"ok\":\"bad\");$(\"apiStatus\").textContent=label;$(\"apiStatusNote\").textContent=note\|\|\"\";"` | — |
| [SRC-2C8F288796-L000387](../../web/workspace.html#L387) | 387 | `"}"` | — |
| [SRC-2C8F288796-L000388](../../web/workspace.html#L388) | 388 | `"const WRITE_ROLES = [\"owner\",\"admin\",\"manager\",\"sales_agent\"];"` | — |
| [SRC-2C8F288796-L000389](../../web/workspace.html#L389) | 389 | `"function canWrite(){return WRITE_ROLES.includes(state.role)}"` | — |
| [SRC-2C8F288796-L000390](../../web/workspace.html#L390) | 390 | `"function countByStatus(id){return state.leads.filter(x=>x.status===id).length}"` | — |
| [SRC-2C8F288796-L000391](../../web/workspace.html#L391) | 391 | `"function buildStat(label,value,note,glow){"` | — |
| [SRC-2C8F288796-L000392](../../web/workspace.html#L392) | 392 | `" const card=make(\"article\",\"glass stat \"+(glow\|\|\"glow-teal\"));"` | — |
| [SRC-2C8F288796-L000393](../../web/workspace.html#L393) | 393 | `" card.append(make(\"div\",\"stat-label\",label),make(\"div\",\"stat-value\",value),make(\"div\",\"stat-note\",note));return card;"` | — |
| [SRC-2C8F288796-L000394](../../web/workspace.html#L394) | 394 | `"}"` | — |
| [SRC-2C8F288796-L000395](../../web/workspace.html#L395) | 395 | `"function renderOverview(){"` | — |
| [SRC-2C8F288796-L000396](../../web/workspace.html#L396) | 396 | `" setPage(\"نظرة عامة\",\"كل ما تحتاجه لمراجعة إشارات الطلب ومتابعتها من مكان واحد.\",\"مساحة العمل\");"` | — |
| [SRC-2C8F288796-L000397](../../web/workspace.html#L397) | 397 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000398](../../web/workspace.html#L398) | 398 | `" const qualified=state.leads.filter(x=>[\"qualified\",\"contacted\",\"converted\"].includes(x.status)).length;"` | — |
| [SRC-2C8F288796-L000399](../../web/workspace.html#L399) | 399 | `" const review=state.leads.filter(x=>[\"new\",\"needs_review\"].includes(x.status)).length;"` | — |
| [SRC-2C8F288796-L000400](../../web/workspace.html#L400) | 400 | `" const stats=make(\"div\",\"stats\");"` | — |
| [SRC-2C8F288796-L000401](../../web/workspace.html#L401) | 401 | `" stats.append("` | — |
| [SRC-2C8F288796-L000402](../../web/workspace.html#L402) | 402 | `"  buildStat(\"إجمالي الإشارات\",state.leads.length,\"السجلات المحمّلة من الخادم\",\"glow-teal\"),"` | — |
| [SRC-2C8F288796-L000403](../../web/workspace.html#L403) | 403 | `"  buildStat(\"تحتاج مراجعة\",review,\"تنتظر قرارك\",\"glow-amber\"),"` | — |
| [SRC-2C8F288796-L000404](../../web/workspace.html#L404) | 404 | `"  buildStat(\"مؤهلة أو قيد المتابعة\",qualified,\"مؤهل · تم التواصل · تحوّل\",\"glow-blue\")"` | — |
| [SRC-2C8F288796-L000405](../../web/workspace.html#L405) | 405 | `" );"` | — |
| [SRC-2C8F288796-L000406](../../web/workspace.html#L406) | 406 | `" root.append(stats);"` | — |
| [SRC-2C8F288796-L000407](../../web/workspace.html#L407) | 407 | `" const grid=make(\"div\",\"content-grid\");"` | — |
| [SRC-2C8F288796-L000408](../../web/workspace.html#L408) | 408 | `" const recent=make(\"section\",\"glass panel\");const h=make(\"div\",\"panel-head\");const head=make(\"div\");"` | — |
| [SRC-2C8F288796-L000409](../../web/workspace.html#L409) | 409 | `" head.append(make(\"h2\",\"\",\"أحدث إشارات الطلب\"),make(\"p\",\"\",\"راجع المصدر وتاريخ الرصد قبل اتخاذ أي خطوة.\"));"` | — |
| [SRC-2C8F288796-L000410](../../web/workspace.html#L410) | 410 | `" h.append(head,action(\"عرض كل الإشارات ←\",\"ghost\",()=>navigate(\"signals\")));recent.append(h);"` | — |
| [SRC-2C8F288796-L000411](../../web/workspace.html#L411) | 411 | `" const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000412](../../web/workspace.html#L412) | 412 | `" const rows=state.leads.slice().sort((a,b)=>String(b.updated_at\|\|b.observed_at\|\|\"\").localeCompare(String(a.updated_at\|\|a.observed_at\|\|\"\"))).slice(0,4);"` | — |
| [SRC-2C8F288796-L000413](../../web/workspace.html#L413) | 413 | `" if(!rows.length)list.append(emptyState(\"لا توجد إشارات محفوظة بعد\",\"ابدأ بتعريف منتجك ثم أنشئ حملة اكتشاف، أو أضف إشارة يدويًا.\"));"` | — |
| [SRC-2C8F288796-L000414](../../web/workspace.html#L414) | 414 | `" else rows.forEach(item=>list.append(signalCard(item)));"` | — |
| [SRC-2C8F288796-L000415](../../web/workspace.html#L415) | 415 | `" recent.append(list);"` | — |
| [SRC-2C8F288796-L000416](../../web/workspace.html#L416) | 416 | `" const startPanel=make(\"section\",\"glass panel\");const sh=make(\"div\",\"panel-head\");const st=make(\"div\");"` | — |
| [SRC-2C8F288796-L000417](../../web/workspace.html#L417) | 417 | `" st.append(make(\"h2\",\"\",\"ابدأ من هنا\"),make(\"p\",\"\",\"خطوتان بسيطتان للانطلاق.\"));"` | — |
| [SRC-2C8F288796-L000418](../../web/workspace.html#L418) | 418 | `" sh.append(st);startPanel.append(sh);"` | — |
| [SRC-2C8F288796-L000419](../../web/workspace.html#L419) | 419 | `" startPanel.append(action(\"١. إعداد ملف المنتج\",\"primary\",()=>navigate(\"offer\")));"` | — |
| [SRC-2C8F288796-L000420](../../web/workspace.html#L420) | 420 | `" startPanel.append(action(\"٢. إنشاء حملة اكتشاف\",\"\",()=>navigate(\"campaign\")));"` | — |
| [SRC-2C8F288796-L000421](../../web/workspace.html#L421) | 421 | `" startPanel.append(make(\"p\",\"disclaimer\",\"تظهر الإشارة مع مصدرها وتاريخ رصدها. التصنيف القواعدي إرشادي، وليس احتمالًا للشراء.\"));"` | — |
| [SRC-2C8F288796-L000422](../../web/workspace.html#L422) | 422 | `" grid.append(recent,startPanel);root.append(grid);"` | — |
| [SRC-2C8F288796-L000423](../../web/workspace.html#L423) | 423 | `"}"` | — |
| [SRC-2C8F288796-L000424](../../web/workspace.html#L424) | 424 | `"function emptyState(title,description){"` | — |
| [SRC-2C8F288796-L000425](../../web/workspace.html#L425) | 425 | `" const box=make(\"div\",\"empty\");box.append(make(\"strong\",\"\",title),make(\"span\",\"\",description));return box;"` | — |
| [SRC-2C8F288796-L000426](../../web/workspace.html#L426) | 426 | `"}"` | — |
| [SRC-2C8F288796-L000427](../../web/workspace.html#L427) | 427 | `"function signalCard(lead){"` | — |
| [SRC-2C8F288796-L000428](../../web/workspace.html#L428) | 428 | `" const card=make(\"article\",\"signal-card\");"` | — |
| [SRC-2C8F288796-L000429](../../web/workspace.html#L429) | 429 | `" const top=make(\"div\",\"signal-top\");const left=make(\"div\",\"signal-meta\");"` | — |
| [SRC-2C8F288796-L000430](../../web/workspace.html#L430) | 430 | `" const assessment=lead.assessment\|\|{};left.append(tag(labels[assessment.label]\|\|assessment.label\|\|\"غير مصنفة\",assessment.label===\"high_intent\"?\"teal\":\"\"));"` | — |
| [SRC-2C8F288796-L000431](../../web/workspace.html#L431) | 431 | `" left.append(tag(statusLabel(lead.status),lead.status===\"rejected\"?\"red\":\"\"));"` | — |
| [SRC-2C8F288796-L000432](../../web/workspace.html#L432) | 432 | `" top.append(left,make(\"span\",\"subtle\",lead.observed_at\|\|\"تاريخ الرصد غير متاح\"));card.append(top);"` | — |
| [SRC-2C8F288796-L000433](../../web/workspace.html#L433) | 433 | `" const text=String(lead.text\|\|\"\");card.append(make(\"p\",\"signal-text\",text.length>250?text.slice(0,247)+\"…\":text));"` | — |
| [SRC-2C8F288796-L000434](../../web/workspace.html#L434) | 434 | `" const meta=make(\"div\",\"signal-meta\");"` | — |
| [SRC-2C8F288796-L000435](../../web/workspace.html#L435) | 435 | `" meta.append(tag(\"الدرجة \"+String(assessment.score??\"—\")+\"/100\"),tag(String(lead.platform\|\|\"مصدر غير محدد\")));"` | — |
| [SRC-2C8F288796-L000436](../../web/workspace.html#L436) | 436 | `" const source=safeHttp(lead.source_url);if(source)meta.append(tag(\"رابط مرفق — لم تُفحص الصفحة\"));"` | — |
| [SRC-2C8F288796-L000437](../../web/workspace.html#L437) | 437 | `" card.append(meta);"` | — |
| [SRC-2C8F288796-L000438](../../web/workspace.html#L438) | 438 | `" const actions=make(\"div\",\"signal-actions\");actions.append(make(\"span\",\"subtle\",\"المعرّف: \"+String(lead.id\|\|\"\").slice(0,8)));"` | — |
| [SRC-2C8F288796-L000439](../../web/workspace.html#L439) | 439 | `" actions.append(action(\"التفاصيل\",\"\",()=>openDetails(lead)));"` | — |
| [SRC-2C8F288796-L000440](../../web/workspace.html#L440) | 440 | `" if(canWrite())actions.append(action(\"تغيير الحالة\",\"\",()=>openDetails(lead)));"` | — |
| [SRC-2C8F288796-L000441](../../web/workspace.html#L441) | 441 | `" card.append(actions);return card;"` | — |
| [SRC-2C8F288796-L000442](../../web/workspace.html#L442) | 442 | `"}"` | — |
| [SRC-2C8F288796-L000443](../../web/workspace.html#L443) | 443 | `"function openDetails(lead){"` | — |
| [SRC-2C8F288796-L000444](../../web/workspace.html#L444) | 444 | `" const body=$(\"detailBody\");body.replaceChildren();"` | — |
| [SRC-2C8F288796-L000445](../../web/workspace.html#L445) | 445 | `" const a=lead.assessment\|\|{};"` | — |
| [SRC-2C8F288796-L000446](../../web/workspace.html#L446) | 446 | `" body.append(make(\"h3\",\"\",\"نص الإشارة\"),make(\"p\",\"\",lead.text\|\|\"لا يوجد نص محفوظ.\"));"` | — |
| [SRC-2C8F288796-L000447](../../web/workspace.html#L447) | 447 | `" body.append(make(\"h3\",\"\",\"المصدر والدليل\"));"` | — |
| [SRC-2C8F288796-L000448](../../web/workspace.html#L448) | 448 | `" const url=safeHttp(lead.source_url);"` | — |
| [SRC-2C8F288796-L000449](../../web/workspace.html#L449) | 449 | `" if(url){const link=make(\"a\",\"\",url);link.href=url;link.target=\"_blank\";link.rel=\"noopener noreferrer\";body.append(link);body.append(make(\"p\",\"disclaimer\",\"وجود الرابط لا يثبت أن الصفحة متاحة أو أن محتواها يطابق نص الإشارة؛ لم تُجرَ قراءة آلية للمصدر في هذه الشاشة.\"))}"` | — |
| [SRC-2C8F288796-L000450](../../web/workspace.html#L450) | 450 | `" else body.append(make(\"p\",\"\",\"لا يوجد رابط HTTP(S) صالح محفوظ لهذا السجل.\"));"` | — |
| [SRC-2C8F288796-L000451](../../web/workspace.html#L451) | 451 | `" body.append(make(\"h3\",\"\",\"التصنيف والتقييم\"));"` | — |
| [SRC-2C8F288796-L000452](../../web/workspace.html#L452) | 452 | `" body.append(make(\"p\",\"\", (labels[a.label]\|\|a.label\|\|\"غير مصنف\")+\" · \"+String(a.score??\"—\")+\"/100\"));"` | — |
| [SRC-2C8F288796-L000453](../../web/workspace.html#L453) | 453 | `" if(a.summary)body.append(make(\"p\",\"\",a.summary));"` | — |
| [SRC-2C8F288796-L000454](../../web/workspace.html#L454) | 454 | `" if(Array.isArray(a.matched_signals)&&a.matched_signals.length){"` | — |
| [SRC-2C8F288796-L000455](../../web/workspace.html#L455) | 455 | `"  const ul=make(\"ul\",\"\");a.matched_signals.forEach(s=>ul.append(make(\"li\",\"\",String(s.phrase\|\|\"إشارة\")+(s.points!==undefined?\" · +\"+s.points:\"\"))));body.append(ul);"` | — |
| [SRC-2C8F288796-L000456](../../web/workspace.html#L456) | 456 | `" }"` | — |
| [SRC-2C8F288796-L000457](../../web/workspace.html#L457) | 457 | `" body.append(make(\"p\",\"disclaimer\",\"درجة القواعد تفسير أولي، وليست احتمالًا إحصائيًا للشراء ولا تثبت نية الكاتب أو استمرار الطلب.\"));"` | — |
| [SRC-2C8F288796-L000458](../../web/workspace.html#L458) | 458 | `" body.append(make(\"h3\",\"\",\"حالة المتابعة\"),make(\"p\",\"\",statusLabel(lead.status)));"` | — |
| [SRC-2C8F288796-L000459](../../web/workspace.html#L459) | 459 | `" if(canWrite()){"` | — |
| [SRC-2C8F288796-L000460](../../web/workspace.html#L460) | 460 | `"  const select=make(\"select\",\"\");select.setAttribute(\"aria-label\",\"تغيير حالة الإشارة\");"` | — |
| [SRC-2C8F288796-L000461](../../web/workspace.html#L461) | 461 | `"  statuses.forEach(s=>{const o=make(\"option\",\"\",s.label);o.value=s.id;o.selected=s.id===lead.status;select.append(o)});"` | — |
| [SRC-2C8F288796-L000462](../../web/workspace.html#L462) | 462 | `"  const save=action(\"حفظ الحالة\",\"primary\",async()=>{save.disabled=true;try{await api(\"/api/leads/\"+encodeURIComponent(lead.id)+\"/status\",{method:\"POST\",body:{status:select.value}});closeDetails();await loadLeads();renderCurrent()}catch(e){body.append(make(\"p\",\"auth-error\",escapeMessage(e.message)))}finally{save.disabled=false}});"` | — |
| [SRC-2C8F288796-L000463](../../web/workspace.html#L463) | 463 | `"  body.append(make(\"h3\",\"\",\"تحديث الحالة\"),select,save);"` | — |
| [SRC-2C8F288796-L000464](../../web/workspace.html#L464) | 464 | `" }"` | — |
| [SRC-2C8F288796-L000465](../../web/workspace.html#L465) | 465 | `" $(\"detailDrawer\").classList.add(\"open\");"` | — |
| [SRC-2C8F288796-L000466](../../web/workspace.html#L466) | 466 | `"}"` | — |
| [SRC-2C8F288796-L000467](../../web/workspace.html#L467) | 467 | `"function closeDetails(){$(\"detailDrawer\").classList.remove(\"open\")}"` | — |
| [SRC-2C8F288796-L000468](../../web/workspace.html#L468) | 468 | `"function renderSignals(){"` | — |
| [SRC-2C8F288796-L000469](../../web/workspace.html#L469) | 469 | `" setPage(\"صندوق إشارات الطلب\",\"راجع النص الأصلي والمصدر والتصنيف. لا تعرض هذه الشاشة شركات أو أشخاصًا غير موجودين في السجل الفعلي.\",\"DEMAND SIGNAL INBOX\");"` | — |
| [SRC-2C8F288796-L000470](../../web/workspace.html#L470) | 470 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000471](../../web/workspace.html#L471) | 471 | `" const panel=make(\"section\",\"glass panel\");const ph=make(\"div\",\"panel-head\");const ptitle=make(\"div\");ptitle.append(make(\"h2\",\"\",\"الإشارات المحفوظة\"),make(\"p\",\"\",\"بيانات من GET /api/leads، محمية بجلسة المستخدم وعزل مساحة العمل.\"));const refresh=action(\"تحديث ↻\",\"ghost\",async()=>{"` | — |
| [SRC-2C8F288796-L000472](../../web/workspace.html#L472) | 472 | `"  refresh.disabled=true;"` | — |
| [SRC-2C8F288796-L000473](../../web/workspace.html#L473) | 473 | `"  try{"` | — |
| [SRC-2C8F288796-L000474](../../web/workspace.html#L474) | 474 | `"   await loadLeads();"` | — |
| [SRC-2C8F288796-L000475](../../web/workspace.html#L475) | 475 | `"   renderSignals();"` | — |
| [SRC-2C8F288796-L000476](../../web/workspace.html#L476) | 476 | `"  }catch(error){"` | — |
| [SRC-2C8F288796-L000477](../../web/workspace.html#L477) | 477 | `"   panel.prepend(make(\"p\",\"auth-error\",\"تعذر تحديث إشارات الطلب. البيانات المعروضة هي آخر نسخة تم تحميلها. \"+escapeMessage(error.message)));"` | — |
| [SRC-2C8F288796-L000478](../../web/workspace.html#L478) | 478 | `"  }finally{"` | — |
| [SRC-2C8F288796-L000479](../../web/workspace.html#L479) | 479 | `"   refresh.disabled=false;"` | — |
| [SRC-2C8F288796-L000480](../../web/workspace.html#L480) | 480 | `"  }"` | — |
| [SRC-2C8F288796-L000481](../../web/workspace.html#L481) | 481 | `" });"` | — |
| [SRC-2C8F288796-L000482](../../web/workspace.html#L482) | 482 | `" ph.append(ptitle,refresh);panel.append(ph);"` | — |
| [SRC-2C8F288796-L000483](../../web/workspace.html#L483) | 483 | `" if(canWrite())panel.append(createSignalForm());"` | — |
| [SRC-2C8F288796-L000484](../../web/workspace.html#L484) | 484 | `" const toolbar=make(\"div\",\"toolbar\");const search=make(\"input\",\"\");search.type=\"search\";search.placeholder=\"ابحث داخل نصوص الإشارات…\";search.value=state.search;search.setAttribute(\"aria-label\",\"البحث في الإشارات\");"` | — |
| [SRC-2C8F288796-L000485](../../web/workspace.html#L485) | 485 | `" search.addEventListener(\"input\",()=>{state.search=search.value;drawSignalRows(list)});"` | — |
| [SRC-2C8F288796-L000486](../../web/workspace.html#L486) | 486 | `" const filter=make(\"select\",\"\");filter.setAttribute(\"aria-label\",\"تصفية حسب الحالة\");const all=make(\"option\",\"\",\"كل الحالات\");all.value=\"all\";filter.append(all);"` | — |
| [SRC-2C8F288796-L000487](../../web/workspace.html#L487) | 487 | `" statuses.forEach(s=>{const o=make(\"option\",\"\",s.label);o.value=s.id;filter.append(o)});filter.value=state.filter;"` | — |
| [SRC-2C8F288796-L000488](../../web/workspace.html#L488) | 488 | `" filter.addEventListener(\"change\",()=>{state.filter=filter.value;drawSignalRows(list)});"` | — |
| [SRC-2C8F288796-L000489](../../web/workspace.html#L489) | 489 | `" toolbar.append(search,filter);panel.append(toolbar);"` | — |
| [SRC-2C8F288796-L000490](../../web/workspace.html#L490) | 490 | `" const list=make(\"div\",\"signal-list\");drawSignalRows(list);panel.append(list);"` | — |
| [SRC-2C8F288796-L000491](../../web/workspace.html#L491) | 491 | `" if(!canWrite())panel.append(make(\"p\",\"disclaimer\",\"دور المستخدم الحالي للقراءة فقط؛ لا يمكنه إضافة إشارات أو تغيير الحالات.\"));"` | — |
| [SRC-2C8F288796-L000492](../../web/workspace.html#L492) | 492 | `" root.append(panel);"` | — |
| [SRC-2C8F288796-L000493](../../web/workspace.html#L493) | 493 | `"}"` | — |
| [SRC-2C8F288796-L000494](../../web/workspace.html#L494) | 494 | `"function drawSignalRows(list){"` | — |
| [SRC-2C8F288796-L000495](../../web/workspace.html#L495) | 495 | `" list.replaceChildren();"` | — |
| [SRC-2C8F288796-L000496](../../web/workspace.html#L496) | 496 | `" const query=state.search.trim().toLocaleLowerCase();"` | — |
| [SRC-2C8F288796-L000497](../../web/workspace.html#L497) | 497 | `" const rows=state.leads.filter(l=>(state.filter===\"all\"\|\|l.status===state.filter)&&(!query\|\|String(l.text\|\|\"\").toLocaleLowerCase().includes(query)));"` | — |
| [SRC-2C8F288796-L000498](../../web/workspace.html#L498) | 498 | `" if(!rows.length)list.append(emptyState(\"لا توجد نتائج مطابقة\",\"غيّر مرشح الحالة أو عبارة البحث، أو أضف إشارة جديدة إن كانت صلاحيتك تسمح.\"));"` | — |
| [SRC-2C8F288796-L000499](../../web/workspace.html#L499) | 499 | `" else rows.forEach(l=>list.append(signalCard(l)));"` | — |
| [SRC-2C8F288796-L000500](../../web/workspace.html#L500) | 500 | `"}"` | — |
| [SRC-2C8F288796-L000501](../../web/workspace.html#L501) | 501 | `"function createSignalForm(){"` | — |
| [SRC-2C8F288796-L000502](../../web/workspace.html#L502) | 502 | `" const wrapper=make(\"section\",\"signal-card\");const head=make(\"div\",\"panel-head\");const title=make(\"div\");title.append(make(\"h2\",\"\",\"إضافة إشارة جديدة\"),make(\"p\",\"\",\"أدخل نصًا منشورًا ورابطه العام. التحليل محلي ولا يشغّل البحث الخارجي.\"));head.append(title);wrapper.append(head);"` | — |
| [SRC-2C8F288796-L000503](../../web/workspace.html#L503) | 503 | `" const text=make(\"textarea\",\"\");text.id=\"newSignalText\";text.placeholder=\"انسخ نص الطلب أو الاحتياج المعلن من المصدر المسموح…\";text.maxLength=20000;text.required=true;"` | — |
| [SRC-2C8F288796-L000504](../../web/workspace.html#L504) | 504 | `" const url=make(\"input\",\"\");url.type=\"url\";url.id=\"newSignalUrl\";url.placeholder=\"https://رابط-المصدر\";url.required=true;"` | — |
| [SRC-2C8F288796-L000505](../../web/workspace.html#L505) | 505 | `" const grid=make(\"div\",\"form-grid\");"` | — |
| [SRC-2C8F288796-L000506](../../web/workspace.html#L506) | 506 | `" const platform=make(\"select\",\"\");platform.id=\"newSignalPlatform\";[\"manual\",\"Facebook\",\"Website\",\"OLX\",\"Other\"].forEach(value=>{const o=make(\"option\",\"\",value===\"manual\"?\"إدخال يدوي\":value);o.value=value;platform.append(o)});"` | — |
| [SRC-2C8F288796-L000507](../../web/workspace.html#L507) | 507 | `" const product=make(\"input\",\"\");product.id=\"newSignalProduct\";product.placeholder=\"مثال: أنظمة إنذار، عقارات\";"` | — |
| [SRC-2C8F288796-L000508](../../web/workspace.html#L508) | 508 | `" const location=make(\"input\",\"\");location.id=\"newSignalLocation\";location.placeholder=\"مثال: القاهرة، التجمع الخامس\";"` | — |
| [SRC-2C8F288796-L000509](../../web/workspace.html#L509) | 509 | `" const note=make(\"input\",\"\");note.id=\"newSignalNote\";note.placeholder=\"ملاحظاتك (اختياري)\";"` | — |
| [SRC-2C8F288796-L000510](../../web/workspace.html#L510) | 510 | `" const fields=[[\"النص\",text],[\"رابط المصدر\",url],[\"المنصة\",platform],[\"مصطلحات المنتج (افصل بفاصلة)\",product],[\"السوق أو المنطقة\",location],[\"ملاحظة\",note]];"` | — |
| [SRC-2C8F288796-L000511](../../web/workspace.html#L511) | 511 | `" fields.forEach(([label,input])=>{const field=make(\"div\",\"field\");field.append(make(\"label\",\"\",label));field.lastChild.htmlFor=input.id;field.append(input);grid.append(field)});"` | — |
| [SRC-2C8F288796-L000512](../../web/workspace.html#L512) | 512 | `" wrapper.append(grid);"` | — |
| [SRC-2C8F288796-L000513](../../web/workspace.html#L513) | 513 | `" const result=make(\"div\",\"\");result.id=\"analysisResult\";"` | — |
| [SRC-2C8F288796-L000514](../../web/workspace.html#L514) | 514 | `" const buttons=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000515](../../web/workspace.html#L515) | 515 | `" const analyze=action(\"١. حلّل الإشارة\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000516](../../web/workspace.html#L516) | 516 | `"  analyze.disabled=true;"` | — |
| [SRC-2C8F288796-L000517](../../web/workspace.html#L517) | 517 | `"  try{"` | — |
| [SRC-2C8F288796-L000518](../../web/workspace.html#L518) | 518 | `"   if(!text.value.trim())throw new Error(\"أدخل نص الإشارة أولًا.\");"` | — |
| [SRC-2C8F288796-L000519](../../web/workspace.html#L519) | 519 | `"   if(!safeHttp(url.value))throw new Error(\"أدخل رابط مصدر عام صالحًا يبدأ بـ HTTP أو HTTPS.\");"` | — |
| [SRC-2C8F288796-L000520](../../web/workspace.html#L520) | 520 | `"   const product_terms=product.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000521](../../web/workspace.html#L521) | 521 | `"   const location_terms=location.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000522](../../web/workspace.html#L522) | 522 | `"   const data=await api(\"/api/analyze\",{method:\"POST\",body:{text:text.value,product_terms:product_terms,location_terms:location_terms}});"` | — |
| [SRC-2C8F288796-L000523](../../web/workspace.html#L523) | 523 | `"   state.analysis={text:text.value,url:url.value,product_terms:product_terms,location_terms:location_terms,assessment:data};"` | — |
| [SRC-2C8F288796-L000524](../../web/workspace.html#L524) | 524 | `"   result.replaceChildren();"` | — |
| [SRC-2C8F288796-L000525](../../web/workspace.html#L525) | 525 | `"   const box=make(\"div\",\"analysis-result\");box.append(make(\"div\",\"analysis-score\",String(data.score??\"—\")+\"/100\"),make(\"div\",\"\",labels[data.label]\|\|data.label\|\|\"غير مصنفة\"),make(\"p\",\"\",data.summary\|\|\"لا يوجد ملخص.\"));"` | — |
| [SRC-2C8F288796-L000526](../../web/workspace.html#L526) | 526 | `"   box.append(make(\"p\",\"disclaimer\",\"هذه درجة قواعد إرشادية لا تمثل احتمال شراء. راجع النص والمصدر قبل اعتماد الإشارة.\"));"` | — |
| [SRC-2C8F288796-L000527](../../web/workspace.html#L527) | 527 | `"   result.append(box);"` | — |
| [SRC-2C8F288796-L000528](../../web/workspace.html#L528) | 528 | `"  }catch(e){result.replaceChildren(make(\"p\",\"auth-error\",escapeMessage(e.message)))}"` | — |
| [SRC-2C8F288796-L000529](../../web/workspace.html#L529) | 529 | `"  finally{analyze.disabled=false}"` | — |
| [SRC-2C8F288796-L000530](../../web/workspace.html#L530) | 530 | `" });"` | — |
| [SRC-2C8F288796-L000531](../../web/workspace.html#L531) | 531 | `" const save=action(\"٢. احفظ الإشارة\",\"\",async()=>{"` | — |
| [SRC-2C8F288796-L000532](../../web/workspace.html#L532) | 532 | `"  save.disabled=true;"` | — |
| [SRC-2C8F288796-L000533](../../web/workspace.html#L533) | 533 | `"  try{"` | — |
| [SRC-2C8F288796-L000534](../../web/workspace.html#L534) | 534 | `"   const item=state.analysis;"` | — |
| [SRC-2C8F288796-L000535](../../web/workspace.html#L535) | 535 | `"   if(!item\|\|item.text!==text.value\|\|item.url!==url.value)throw new Error(\"أعد التحليل بعد أي تغيير في النص أو رابط المصدر.\");"` | — |
| [SRC-2C8F288796-L000536](../../web/workspace.html#L536) | 536 | `"   if(!safeHttp(url.value))throw new Error(\"رابط المصدر غير صالح.\");"` | — |
| [SRC-2C8F288796-L000537](../../web/workspace.html#L537) | 537 | `"   const product_terms=product.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000538](../../web/workspace.html#L538) | 538 | `"   const location_terms=location.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000539](../../web/workspace.html#L539) | 539 | `"   if(JSON.stringify(product_terms)!==JSON.stringify(item.product_terms)\|\|JSON.stringify(location_terms)!==JSON.stringify(item.location_terms))throw new Error(\"تغيرت مصطلحات المنتج أو المنطقة؛ أعد التحليل.\");"` | — |
| [SRC-2C8F288796-L000540](../../web/workspace.html#L540) | 540 | `"   const response=await api(\"/api/leads\",{method:\"POST\",body:{text:text.value,source_url:url.value,platform:platform.value,note:note.value,product_terms:product_terms,location_terms:location_terms}});"` | — |
| [SRC-2C8F288796-L000541](../../web/workspace.html#L541) | 541 | `"   result.replaceChildren(make(\"p\",\"tag teal\",response.created?\"تم حفظ الإشارة.\":\"هذه الإشارة موجودة بالفعل ولم تُكرر.\"));"` | — |
| [SRC-2C8F288796-L000542](../../web/workspace.html#L542) | 542 | `"   state.analysis=null;text.value=\"\";url.value=\"\";note.value=\"\";"` | — |
| [SRC-2C8F288796-L000543](../../web/workspace.html#L543) | 543 | `"   let refreshWarning=\"\";"` | — |
| [SRC-2C8F288796-L000544](../../web/workspace.html#L544) | 544 | `"   try{"` | — |
| [SRC-2C8F288796-L000545](../../web/workspace.html#L545) | 545 | `"    await loadLeads();"` | — |
| [SRC-2C8F288796-L000546](../../web/workspace.html#L546) | 546 | `"   }catch(refreshError){"` | — |
| [SRC-2C8F288796-L000547](../../web/workspace.html#L547) | 547 | `"    refreshWarning=escapeMessage(refreshError.message);"` | — |
| [SRC-2C8F288796-L000548](../../web/workspace.html#L548) | 548 | `"   }"` | — |
| [SRC-2C8F288796-L000549](../../web/workspace.html#L549) | 549 | `"   if(refreshWarning){"` | — |
| [SRC-2C8F288796-L000550](../../web/workspace.html#L550) | 550 | `"    result.append(make(\"p\",\"auth-error\",\"تم حفظ الإشارة، لكن تعذر تحديث صندوق الإشارات. افتح الصندوق وحدّثه لاحقًا. \"+refreshWarning));"` | — |
| [SRC-2C8F288796-L000551](../../web/workspace.html#L551) | 551 | `"   }else{"` | — |
| [SRC-2C8F288796-L000552](../../web/workspace.html#L552) | 552 | `"    renderSignals();"` | — |
| [SRC-2C8F288796-L000553](../../web/workspace.html#L553) | 553 | `"   }"` | — |
| [SRC-2C8F288796-L000554](../../web/workspace.html#L554) | 554 | `"  }catch(e){result.append(make(\"p\",\"auth-error\",escapeMessage(e.message)))}"` | — |
| [SRC-2C8F288796-L000555](../../web/workspace.html#L555) | 555 | `"  finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000556](../../web/workspace.html#L556) | 556 | `" });"` | — |
| [SRC-2C8F288796-L000557](../../web/workspace.html#L557) | 557 | `" buttons.append(analyze,save);wrapper.append(buttons,result);return wrapper;"` | — |
| [SRC-2C8F288796-L000558](../../web/workspace.html#L558) | 558 | `"}"` | — |
| [SRC-2C8F288796-L000559](../../web/workspace.html#L559) | 559 | `"function renderPipeline(){"` | — |
| [SRC-2C8F288796-L000560](../../web/workspace.html#L560) | 560 | `" setPage(\"مسار التأهيل\",\"يعرض المسار الحالات المحفوظة فعليًا، ويمكن تحديث الحالة بعد مراجعة الدليل. لا توجد مراحل CRM غير مدعومة في الخادم.\",\"QUALIFICATION PIPELINE\");"` | — |
| [SRC-2C8F288796-L000561](../../web/workspace.html#L561) | 561 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000562](../../web/workspace.html#L562) | 562 | `" const panel=make(\"section\",\"glass panel\");const head=make(\"div\",\"panel-head\");const title=make(\"div\");title.append(make(\"h2\",\"\",\"حالة كل إشارة\"),make(\"p\",\"\",\"اختر بطاقة لفتح المصدر وتقييم القواعد وتغيير الحالة المسموح بها.\"));head.append(title,action(\"صندوق الإشارات ←\",\"ghost\",()=>navigate(\"signals\")));panel.append(head);"` | — |
| [SRC-2C8F288796-L000563](../../web/workspace.html#L563) | 563 | `" const board=make(\"div\",\"pipeline\");const groups=[[\"نشطة جديدة\",[\"new\",\"needs_review\"]],[\"مؤهلة / متابعة\",[\"qualified\",\"contacted\"]],[\"مغلقة\",[\"converted\",\"rejected\"]]];"` | — |
| [SRC-2C8F288796-L000564](../../web/workspace.html#L564) | 564 | `" groups.forEach(([name,ids])=>{const col=make(\"section\",\"pipeline-col\");const rows=state.leads.filter(l=>ids.includes(l.status));col.append(make(\"h3\",\"\",name+\" · \"+rows.length));if(!rows.length)col.append(make(\"p\",\"subtle\",\"لا توجد سجلات في هذه المجموعة.\"));rows.forEach(l=>{const item=make(\"button\",\"pipeline-item\",String(l.text\|\|\"\").slice(0,115));item.type=\"button\";item.addEventListener(\"click\",()=>openDetails(l));col.append(item)});board.append(col)});"` | — |
| [SRC-2C8F288796-L000565](../../web/workspace.html#L565) | 565 | `" panel.append(board);root.append(panel);"` | — |
| [SRC-2C8F288796-L000566](../../web/workspace.html#L566) | 566 | `"}"` | — |
| [SRC-2C8F288796-L000567](../../web/workspace.html#L567) | 567 | `"async function renderSystem(){"` | — |
| [SRC-2C8F288796-L000568](../../web/workspace.html#L568) | 568 | `" setPage(\"حالات النظام\",\"لقطة إعدادات يقرأها الخادم محليًا. لا تنفذ هذه الشاشة اتصالًا تجريبيًا بالموفرات ولا تستهلك حصص البحث.\",\"SYSTEM CONFIGURATION SNAPSHOT\");"` | — |
| [SRC-2C8F288796-L000569](../../web/workspace.html#L569) | 569 | `" const root=$(\"viewRoot\");root.replaceChildren(emptyState(\"جارٍ قراءة حالة الخادم\",\"GET /api/health — لا يجري اختبار اتصال خارجي.\"));"` | — |
| [SRC-2C8F288796-L000570](../../web/workspace.html#L570) | 570 | `" try{"` | — |
| [SRC-2C8F288796-L000571](../../web/workspace.html#L571) | 571 | `"  const data=await api(\"/api/health\");"` | — |
| [SRC-2C8F288796-L000572](../../web/workspace.html#L572) | 572 | `"  const agent=data.agent\|\|{};const build=data.build\|\|{};"` | — |
| [SRC-2C8F288796-L000573](../../web/workspace.html#L573) | 573 | `"  root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000574](../../web/workspace.html#L574) | 574 | `"  const stats=make(\"div\",\"stats\");"` | — |
| [SRC-2C8F288796-L000575](../../web/workspace.html#L575) | 575 | `"  stats.append("` | — |
| [SRC-2C8F288796-L000576](../../web/workspace.html#L576) | 576 | `"   buildStat(\"استجابة الخادم\",data.ok===true?\"يستجيب\":\"غير مؤكدة\",\"استجابة نقطة /api/health\",\"glow-teal\"),"` | — |
| [SRC-2C8F288796-L000577](../../web/workspace.html#L577) | 577 | `"   buildStat(\"مكتبات البحث\",agent.web_search_ready===true?\"موجودة\":\"غير جاهزة\",\"فحص اعتماديات محلية فقط\",\"glow-blue\"),"` | — |
| [SRC-2C8F288796-L000578](../../web/workspace.html#L578) | 578 | `"   buildStat(\"إعداد النموذج\",agent.language_model_configured===true?\"مهيأ\":\"غير مهيأ\",\"لا يثبت إمكانية الاتصال أو نجاح الاستجابة\",\"glow-violet\"),"` | — |
| [SRC-2C8F288796-L000579](../../web/workspace.html#L579) | 579 | `"   buildStat(\"هوية البناء\",build.sha_status===\"available\"?String(build.sha).slice(0,8):\"غير معروفة\",\"حالة SHA كما أعادها الخادم\",\"glow-amber\")"` | — |
| [SRC-2C8F288796-L000580](../../web/workspace.html#L580) | 580 | `"  );"` | — |
| [SRC-2C8F288796-L000581](../../web/workspace.html#L581) | 581 | `"  root.append(stats);"` | — |
| [SRC-2C8F288796-L000582](../../web/workspace.html#L582) | 582 | `"  const grid=make(\"div\",\"content-grid\");"` | — |
| [SRC-2C8F288796-L000583](../../web/workspace.html#L583) | 583 | `"  const models=make(\"section\",\"glass panel\");const mh=make(\"div\",\"panel-head\");const mt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000584](../../web/workspace.html#L584) | 584 | `"  mt.append(make(\"h2\",\"\",\"موفر النموذج\"));mt.append(make(\"p\",\"\",\"بيانات إعداد يعرضها الخادم؛ لا تعرض مفاتيح أو أسرار.\"));"` | — |
| [SRC-2C8F288796-L000585](../../web/workspace.html#L585) | 585 | `"  mh.append(mt);models.append(mh);"` | — |
| [SRC-2C8F288796-L000586](../../web/workspace.html#L586) | 586 | `"  models.append(make(\"p\",\"\", \"الموفر الأساسي المعلن: \"+String(agent.language_model_provider\|\|\"غير معلوم\")));"` | — |
| [SRC-2C8F288796-L000587](../../web/workspace.html#L587) | 587 | `"  const providers=Array.isArray(agent.model_providers)?agent.model_providers:[];"` | — |
| [SRC-2C8F288796-L000588](../../web/workspace.html#L588) | 588 | `"  if(providers.length){"` | — |
| [SRC-2C8F288796-L000589](../../web/workspace.html#L589) | 589 | `"   const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000590](../../web/workspace.html#L590) | 590 | `"   providers.forEach(p=>{"` | — |
| [SRC-2C8F288796-L000591](../../web/workspace.html#L591) | 591 | `"    const row=make(\"article\",\"signal-card\");"` | — |
| [SRC-2C8F288796-L000592](../../web/workspace.html#L592) | 592 | `"    row.append(make(\"strong\",\"\",String(p.name\|\|\"موفر غير مسمى\")));"` | — |
| [SRC-2C8F288796-L000593](../../web/workspace.html#L593) | 593 | `"    row.append(make(\"span\",\"subtle\",\"النموذج المهيأ: \"+String(p.model\|\|\"غير محدد\")));"` | — |
| [SRC-2C8F288796-L000594](../../web/workspace.html#L594) | 594 | `"    row.append(tag(p.configured===true?\"مهيأ في البيئة\":\"غير مهيأ\",p.configured===true?\"teal\":\"amber\"));"` | — |
| [SRC-2C8F288796-L000595](../../web/workspace.html#L595) | 595 | `"    list.append(row);"` | — |
| [SRC-2C8F288796-L000596](../../web/workspace.html#L596) | 596 | `"   });"` | — |
| [SRC-2C8F288796-L000597](../../web/workspace.html#L597) | 597 | `"   models.append(list);"` | — |
| [SRC-2C8F288796-L000598](../../web/workspace.html#L598) | 598 | `"  }else models.append(emptyState(\"لا توجد موفرات ظاهرة كإعداد\",\"لم يعرض الخادم موفرًا مهيأ ضمن هذه اللقطة.\"));"` | — |
| [SRC-2C8F288796-L000599](../../web/workspace.html#L599) | 599 | `"  const search=make(\"section\",\"glass panel\");const sh=make(\"div\",\"panel-head\");const st=make(\"div\");"` | — |
| [SRC-2C8F288796-L000600](../../web/workspace.html#L600) | 600 | `"  st.append(make(\"h2\",\"\",\"إعدادات البحث الاختيارية\"),make(\"p\",\"\",\"القيم أدناه أعلام إعداد فقط، وليست اختبارات تشغيل.\"));"` | — |
| [SRC-2C8F288796-L000601](../../web/workspace.html#L601) | 601 | `"  sh.append(st);search.append(sh);"` | — |
| [SRC-2C8F288796-L000602](../../web/workspace.html#L602) | 602 | `"  const flags=["` | — |
| [SRC-2C8F288796-L000603](../../web/workspace.html#L603) | 603 | `"   [\"Brave Search API\",agent.brave_search_api_configured],"` | — |
| [SRC-2C8F288796-L000604](../../web/workspace.html#L604) | 604 | `"   [\"Tavily Search API\",agent.tavily_search_api_configured],"` | — |
| [SRC-2C8F288796-L000605](../../web/workspace.html#L605) | 605 | `"   [\"DeepSeek Search API\",agent.deepseek_search_api_configured],"` | — |
| [SRC-2C8F288796-L000606](../../web/workspace.html#L606) | 606 | `"   [\"OpenRouter web search\",agent.openrouter_web_search_enabled]"` | — |
| [SRC-2C8F288796-L000607](../../web/workspace.html#L607) | 607 | `"  ];"` | — |
| [SRC-2C8F288796-L000608](../../web/workspace.html#L608) | 608 | `"  flags.forEach(([name,value])=>{const row=make(\"div\",\"signal-actions\");row.append(make(\"span\",\"\",name),tag(value===true?\"مهيأ/مفعل\":\"غير مهيأ/معطل\",value===true?\"teal\":\"amber\"));search.append(row)});"` | — |
| [SRC-2C8F288796-L000609](../../web/workspace.html#L609) | 609 | `"  search.append(make(\"p\",\"disclaimer\",\"لا تنفذ هذه الشاشة تشخيصًا مباشرًا ولا تختبر صلاحية مفاتيح الموفرات. التشخيص الحي قد يستهلك حصة أو تكلفة، ويظل منفصلًا ويتطلب موافقة المالك.\"));"` | — |
| [SRC-2C8F288796-L000610](../../web/workspace.html#L610) | 610 | `"  grid.append(models,search);root.append(grid);"` | — |
| [SRC-2C8F288796-L000611](../../web/workspace.html#L611) | 611 | `" }catch(e){root.replaceChildren(emptyState(\"تعذرت قراءة الإعدادات\",escapeMessage(e.message)))}"` | — |
| [SRC-2C8F288796-L000612](../../web/workspace.html#L612) | 612 | `"}"` | — |
| [SRC-2C8F288796-L000613](../../web/workspace.html#L613) | 613 | `"function renderIndicators(){"` | — |
| [SRC-2C8F288796-L000614](../../web/workspace.html#L614) | 614 | `" setPage(\"مؤشرات الأداء\",\"لوحة وصفية لحالة سجلات مساحة العمل الحالية، وليست توقعًا للمبيعات أو احتمالات الشراء.\",\"WORKSPACE INDICATORS\");"` | — |
| [SRC-2C8F288796-L000615](../../web/workspace.html#L615) | 615 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000616](../../web/workspace.html#L616) | 616 | `" const total=state.leads.length;"` | — |
| [SRC-2C8F288796-L000617](../../web/workspace.html#L617) | 617 | `" const review=state.leads.filter(x=>[\"new\",\"needs_review\"].includes(x.status)).length;"` | — |
| [SRC-2C8F288796-L000618](../../web/workspace.html#L618) | 618 | `" const qualified=state.leads.filter(x=>[\"qualified\",\"contacted\",\"converted\"].includes(x.status)).length;"` | — |
| [SRC-2C8F288796-L000619](../../web/workspace.html#L619) | 619 | `" const converted=total?Math.round(qualified/total*100):0;"` | — |
| [SRC-2C8F288796-L000620](../../web/workspace.html#L620) | 620 | `" const withSource=state.leads.filter(x=>safeHttp(x.source_url)).length;"` | — |
| [SRC-2C8F288796-L000621](../../web/workspace.html#L621) | 621 | `" const hero=make(\"section\",\"glass indicator-hero\");"` | — |
| [SRC-2C8F288796-L000622](../../web/workspace.html#L622) | 622 | `" const ring=make(\"div\",\"indicator-ring\");"` | — |
| [SRC-2C8F288796-L000623](../../web/workspace.html#L623) | 623 | `" ring.style.background=\"conic-gradient(var(--green) 0 \"+converted+\"%, rgba(132,156,190,.16) \"+converted+\"% 100%)\";"` | — |
| [SRC-2C8F288796-L000624](../../web/workspace.html#L624) | 624 | `" ring.setAttribute(\"role\",\"img\");"` | — |
| [SRC-2C8F288796-L000625](../../web/workspace.html#L625) | 625 | `" ring.setAttribute(\"aria-label\",\"نسبة السجلات المؤهلة أو قيد المتابعة: \"+converted+\" بالمئة من السجلات المحمّلة\");"` | — |
| [SRC-2C8F288796-L000626](../../web/workspace.html#L626) | 626 | `" const ringInner=make(\"div\",\"indicator-ring-inner\");"` | — |
| [SRC-2C8F288796-L000627](../../web/workspace.html#L627) | 627 | `" ringInner.append(make(\"strong\",\"indicator-ring-value\",converted+\"%\"),make(\"span\",\"indicator-ring-caption\",\"مؤهل أو متابعة\"));"` | — |
| [SRC-2C8F288796-L000628](../../web/workspace.html#L628) | 628 | `" ring.append(ringInner);"` | — |
| [SRC-2C8F288796-L000629](../../web/workspace.html#L629) | 629 | `" const heroCopy=make(\"div\",\"indicator-hero-copy\");"` | — |
| [SRC-2C8F288796-L000630](../../web/workspace.html#L630) | 630 | `" heroCopy.append(make(\"span\",\"eyebrow\",\"WORKSPACE HEALTH\"),make(\"h2\",\"\",\"مؤشر متابعة السجل\"),make(\"p\",\"\",\"نسبة الإشارات المصنفة مؤهلة أو تم التواصل معها أو تحولت إلى عميل، من إجمالي السجلات المحمّلة حاليًا. هذه نسبة حالة داخلية وليست احتمال شراء.\"));"` | — |
| [SRC-2C8F288796-L000631](../../web/workspace.html#L631) | 631 | `" hero.append(ring,heroCopy);root.append(hero);"` | — |
| [SRC-2C8F288796-L000632](../../web/workspace.html#L632) | 632 | `" const cards=make(\"div\",\"indicator-grid\");"` | — |
| [SRC-2C8F288796-L000633](../../web/workspace.html#L633) | 633 | `" cards.append("` | — |
| [SRC-2C8F288796-L000634](../../web/workspace.html#L634) | 634 | `"  buildStat(\"إجمالي الإشارات\",total,\"السجلات التي أعادها الخادم\",\"glow-teal\"),"` | — |
| [SRC-2C8F288796-L000635](../../web/workspace.html#L635) | 635 | `"  buildStat(\"مؤهلة أو قيد المتابعة\",qualified,\"مؤهل · تم التواصل · تحول\",\"glow-blue\"),"` | — |
| [SRC-2C8F288796-L000636](../../web/workspace.html#L636) | 636 | `"  buildStat(\"تحتاج مراجعة\",review,\"جديد أو بانتظار مراجعة\",\"glow-amber\"),"` | — |
| [SRC-2C8F288796-L000637](../../web/workspace.html#L637) | 637 | `"  buildStat(\"عمليات الاكتشاف\",state.discoveryRuns.length,\"عمليات محفوظة أعادها الخادم\",\"glow-violet\")"` | — |
| [SRC-2C8F288796-L000638](../../web/workspace.html#L638) | 638 | `" );"` | — |
| [SRC-2C8F288796-L000639](../../web/workspace.html#L639) | 639 | `" root.append(cards);"` | — |
| [SRC-2C8F288796-L000640](../../web/workspace.html#L640) | 640 | `" const layout=make(\"div\",\"indicator-layout\");"` | — |
| [SRC-2C8F288796-L000641](../../web/workspace.html#L641) | 641 | `" const statusPanel=make(\"section\",\"glass panel\");"` | — |
| [SRC-2C8F288796-L000642](../../web/workspace.html#L642) | 642 | `" const head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000643](../../web/workspace.html#L643) | 643 | `" title.append(make(\"h2\",\"\",\"توزيع حالات الإشارات\"),make(\"p\",\"\",\"عدد السجلات الفعلي حسب حالة المتابعة الحالية.\"));"` | — |
| [SRC-2C8F288796-L000644](../../web/workspace.html#L644) | 644 | `" head.append(title,action(\"فتح إشارات الطلب ←\",\"ghost\",()=>navigate(\"signals\")));"` | — |
| [SRC-2C8F288796-L000645](../../web/workspace.html#L645) | 645 | `" statusPanel.append(head);"` | — |
| [SRC-2C8F288796-L000646](../../web/workspace.html#L646) | 646 | `" const bars=make(\"div\",\"indicator-list\");"` | — |
| [SRC-2C8F288796-L000647](../../web/workspace.html#L647) | 647 | `" const groups=["` | — |
| [SRC-2C8F288796-L000648](../../web/workspace.html#L648) | 648 | `"  [\"جديد\",\"new\",\"cyan\"],[\"يحتاج مراجعة\",\"needs_review\",\"red\"],[\"مؤهل\",\"qualified\",\"green\"],"` | — |
| [SRC-2C8F288796-L000649](../../web/workspace.html#L649) | 649 | `"  [\"تم التواصل\",\"contacted\",\"green\"],[\"تحول لعميل\",\"converted\",\"green\"],[\"مرفوض\",\"rejected\",\"muted\"]"` | — |
| [SRC-2C8F288796-L000650](../../web/workspace.html#L650) | 650 | `" ];"` | — |
| [SRC-2C8F288796-L000651](../../web/workspace.html#L651) | 651 | `" groups.forEach(([label,id,tone])=>{"` | — |
| [SRC-2C8F288796-L000652](../../web/workspace.html#L652) | 652 | `"  const count=countByStatus(id),row=make(\"div\",\"indicator-row\");"` | — |
| [SRC-2C8F288796-L000653](../../web/workspace.html#L653) | 653 | `"  row.append(make(\"span\",\"\",\"\"+label));"` | — |
| [SRC-2C8F288796-L000654](../../web/workspace.html#L654) | 654 | `"  const track=make(\"div\",\"indicator-track\"),fill=make(\"div\",\"indicator-fill \"+tone);"` | — |
| [SRC-2C8F288796-L000655](../../web/workspace.html#L655) | 655 | `"  fill.style.width=(total?Math.round(count/total*100):0)+\"%\";"` | — |
| [SRC-2C8F288796-L000656](../../web/workspace.html#L656) | 656 | `"  fill.setAttribute(\"aria-hidden\",\"true\");"` | — |
| [SRC-2C8F288796-L000657](../../web/workspace.html#L657) | 657 | `"  track.append(fill);row.append(track,make(\"strong\",\"\",count));bars.append(row);"` | — |
| [SRC-2C8F288796-L000658](../../web/workspace.html#L658) | 658 | `" });"` | — |
| [SRC-2C8F288796-L000659](../../web/workspace.html#L659) | 659 | `" if(!total)bars.append(emptyState(\"لا توجد بيانات بعد\",\"ستظهر المؤشرات تلقائيًا بعد حفظ إشارات فعلية.\"));"` | — |
| [SRC-2C8F288796-L000660](../../web/workspace.html#L660) | 660 | `" statusPanel.append(bars);"` | — |
| [SRC-2C8F288796-L000661](../../web/workspace.html#L661) | 661 | `" const quality=make(\"section\",\"glass panel\");"` | — |
| [SRC-2C8F288796-L000662](../../web/workspace.html#L662) | 662 | `" const qhead=make(\"div\",\"panel-head\"),qtitle=make(\"div\");"` | — |
| [SRC-2C8F288796-L000663](../../web/workspace.html#L663) | 663 | `" qtitle.append(make(\"h2\",\"\",\"اكتمال السجل\"),make(\"p\",\"\",\"معلومات وصفية عن السجلات المحمّلة فقط.\"));"` | — |
| [SRC-2C8F288796-L000664](../../web/workspace.html#L664) | 664 | `" qhead.append(qtitle);quality.append(qhead);"` | — |
| [SRC-2C8F288796-L000665](../../web/workspace.html#L665) | 665 | `" const summary=make(\"div\",\"indicator-summary\");"` | — |
| [SRC-2C8F288796-L000666](../../web/workspace.html#L666) | 666 | `" ["` | — |
| [SRC-2C8F288796-L000667](../../web/workspace.html#L667) | 667 | `"  [\"إشارات لها رابط مصدر\",withSource],"` | — |
| [SRC-2C8F288796-L000668](../../web/workspace.html#L668) | 668 | `"  [\"ملفات المنتجات والأسواق\",state.profiles.length],"` | — |
| [SRC-2C8F288796-L000669](../../web/workspace.html#L669) | 669 | `"  [\"عمليات الاكتشاف المحفوظة\",state.discoveryRuns.length],"` | — |
| [SRC-2C8F288796-L000670](../../web/workspace.html#L670) | 670 | `"  [\"إشارات تحتاج مراجعة\",review]"` | — |
| [SRC-2C8F288796-L000671](../../web/workspace.html#L671) | 671 | `" ].forEach(([label,value])=>{"` | — |
| [SRC-2C8F288796-L000672](../../web/workspace.html#L672) | 672 | `"  const item=make(\"div\",\"indicator-note\");"` | — |
| [SRC-2C8F288796-L000673](../../web/workspace.html#L673) | 673 | `"  item.append(make(\"div\",\"\",label),make(\"strong\",\"indicator-note-value\",value));summary.append(item);"` | — |
| [SRC-2C8F288796-L000674](../../web/workspace.html#L674) | 674 | `" });"` | — |
| [SRC-2C8F288796-L000675](../../web/workspace.html#L675) | 675 | `" quality.append(summary,make(\"p\",\"disclaimer\",\"وجود رابط مصدر لا يعني أن الصفحة قُرئت أو تم التحقق من محتواها. ولا تمثل هذه المؤشرات حجم السوق أو معدل التحويل الفعلي.\"));"` | — |
| [SRC-2C8F288796-L000676](../../web/workspace.html#L676) | 676 | `" layout.append(statusPanel,quality);root.append(layout);"` | — |
| [SRC-2C8F288796-L000677](../../web/workspace.html#L677) | 677 | `" const recent=make(\"section\",\"glass panel\");recent.style.marginTop=\"14px\";"` | — |
| [SRC-2C8F288796-L000678](../../web/workspace.html#L678) | 678 | `" const rh=make(\"div\",\"panel-head\"),rt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000679](../../web/workspace.html#L679) | 679 | `" rt.append(make(\"h2\",\"\",\"أحدث الإشارات\"),make(\"p\",\"\",\"آخر خمسة سجلات بحسب تاريخ التحديث الذي أعاده الخادم.\"));"` | — |
| [SRC-2C8F288796-L000680](../../web/workspace.html#L680) | 680 | `" rh.append(rt,action(\"عرض الكل ←\",\"ghost\",()=>navigate(\"signals\")));recent.append(rh);"` | — |
| [SRC-2C8F288796-L000681](../../web/workspace.html#L681) | 681 | `" const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000682](../../web/workspace.html#L682) | 682 | `" const rows=state.leads.slice().sort((a,b)=>String(b.updated_at\|\|b.observed_at\|\|\"\").localeCompare(String(a.updated_at\|\|a.observed_at\|\|\"\"))).slice(0,5);"` | — |
| [SRC-2C8F288796-L000683](../../web/workspace.html#L683) | 683 | `" if(rows.length)rows.forEach(item=>list.append(signalCard(item)));"` | — |
| [SRC-2C8F288796-L000684](../../web/workspace.html#L684) | 684 | `" else list.append(emptyState(\"لا توجد إشارات لعرضها\",\"أضف إشارة طلب موثقة لتبدأ المؤشرات في الظهور.\"));"` | — |
| [SRC-2C8F288796-L000685](../../web/workspace.html#L685) | 685 | `" recent.append(list);root.append(recent);"` | — |
| [SRC-2C8F288796-L000686](../../web/workspace.html#L686) | 686 | `"}"` | — |
| [SRC-2C8F288796-L000687](../../web/workspace.html#L687) | 687 | `"function renderPlaceholder(id){"` | — |
| [SRC-2C8F288796-L000688](../../web/workspace.html#L688) | 688 | `" const item=menu.find(x=>x.id===id);const title=item?item.label:\"وحدة\";"` | — |
| [SRC-2C8F288796-L000689](../../web/workspace.html#L689) | 689 | `" setPage(title,\"واجهة الوحدة جزء من تصور Omarai، لكن المستودع عند الرأس الحالي لا يوفّر بعد عقد API موثقًا لهذه الوظيفة. لا نعرض بيانات أو نتائج شكلية على أنها حقيقية.\",\"MODULE NOT ENABLED\");"` | — |
| [SRC-2C8F288796-L000690](../../web/workspace.html#L690) | 690 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000691](../../web/workspace.html#L691) | 691 | `" const card=make(\"section\",\"glass module-placeholder\");"` | — |
| [SRC-2C8F288796-L000692](../../web/workspace.html#L692) | 692 | `" card.append(tag(\"غير مفعلة في الخادم الحالي\",\"amber\"),make(\"h2\",\"\",title));"` | — |
| [SRC-2C8F288796-L000693](../../web/workspace.html#L693) | 693 | `" card.append(make(\"p\",\"\",\"هذه الشاشة لا تستدعي موصلًا خارجيًا ولا تحفظ إعدادات وهمية. يلزم بناء نموذج البيانات وواجهة API واختبارات الصلاحيات والعزل قبل تشغيلها.\"));"` | — |
| [SRC-2C8F288796-L000694](../../web/workspace.html#L694) | 694 | `" const list=make(\"div\",\"module-list\");"` | — |
| [SRC-2C8F288796-L000695](../../web/workspace.html#L695) | 695 | `" [\"تعريف عقد البيانات والحقول ومصدر كل قيمة.\",\"إنشاء API محمي ومربوط بالمستخدم ومساحة العمل المصادق عليها.\",\"إضافة اختبارات نجاح وفشل وعزل بين المستأجرين.\",\"ربط الواجهة بالبيانات الفعلية ثم اختبارها على بيئة معروفة.\"].forEach(x=>list.append(make(\"div\",\"module-step\",x)));"` | — |
| [SRC-2C8F288796-L000696](../../web/workspace.html#L696) | 696 | `" card.append(list,make(\"div\",\"form-actions\"));"` | — |
| [SRC-2C8F288796-L000697](../../web/workspace.html#L697) | 697 | `" const links=card.querySelector(\".form-actions\");links.append(action(\"العودة إلى النظرة العامة\",\"primary\",()=>navigate(\"overview\")),action(\"فتح وكيل البحث الحالي\",\"\",()=>{window.location.href=\"/agent\"}));"` | — |
| [SRC-2C8F288796-L000698](../../web/workspace.html#L698) | 698 | `" root.append(card);"` | — |
| [SRC-2C8F288796-L000699](../../web/workspace.html#L699) | 699 | `"}"` | — |
| [SRC-2C8F288796-L000700](../../web/workspace.html#L700) | 700 | `"function csvValues(value){return String(value\|\|\"\").split(\",\").map(x=>x.trim()).filter(Boolean)}"` | — |
| [SRC-2C8F288796-L000701](../../web/workspace.html#L701) | 701 | `"function textField(label,id,placeholder,value,multiline){"` | — |
| [SRC-2C8F288796-L000702](../../web/workspace.html#L702) | 702 | `" const field=make(\"div\",\"field\"),control=make(multiline?\"textarea\":\"input\",\"\");"` | — |
| [SRC-2C8F288796-L000703](../../web/workspace.html#L703) | 703 | `" control.id=id;control.value=value\|\|\"\";control.placeholder=placeholder\|\|\"\";"` | — |
| [SRC-2C8F288796-L000704](../../web/workspace.html#L704) | 704 | `" const caption=make(\"label\",\"\",label);caption.htmlFor=id;field.append(caption,control);"` | — |
| [SRC-2C8F288796-L000705](../../web/workspace.html#L705) | 705 | `" return {field,control};"` | — |
| [SRC-2C8F288796-L000706](../../web/workspace.html#L706) | 706 | `"}"` | — |
| [SRC-2C8F288796-L000707](../../web/workspace.html#L707) | 707 | `"function renderProductProfile(){"` | — |
| [SRC-2C8F288796-L000708](../../web/workspace.html#L708) | 708 | `" setPage(\"ملف المنتج والعرض\",\"عرّف المنتج والسوق قبل تشغيل اكتشاف الطلب. كل ملف محفوظ مرتبط بمساحة العمل المصادق عليها.\",\"PRODUCT & MARKET PROFILE\");"` | — |
| [SRC-2C8F288796-L000709](../../web/workspace.html#L709) | 709 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000710](../../web/workspace.html#L710) | 710 | `" const panel=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000711](../../web/workspace.html#L711) | 711 | `" title.append(make(\"h2\",\"\",\"بيانات المنتج والسوق\"),make(\"p\",\"\",\"أدخل المعلومات المعروفة صراحةً؛ لا يخترع Omarai مواصفات أو عملاء مستهدفين من اسم المنتج وحده.\"));"` | — |
| [SRC-2C8F288796-L000712](../../web/workspace.html#L712) | 712 | `" head.append(title);panel.append(head);"` | — |
| [SRC-2C8F288796-L000713](../../web/workspace.html#L713) | 713 | `" const grid=make(\"div\",\"form-grid\"),controls={};"` | — |
| [SRC-2C8F288796-L000714](../../web/workspace.html#L714) | 714 | `" const fields=["` | — |
| [SRC-2C8F288796-L000715](../../web/workspace.html#L715) | 715 | `"  [\"اسم المنتج أو الخدمة\",\"name\",\"مثال: لوحة إنذار حريق\"],"` | — |
| [SRC-2C8F288796-L000716](../../web/workspace.html#L716) | 716 | `"  [\"الأسماء والمرادفات\",\"aliases\",\"FACP، لوحة إنذار، Fire Alarm Panel\"],"` | — |
| [SRC-2C8F288796-L000717](../../web/workspace.html#L717) | 717 | `"  [\"الفئة أو التصنيف\",\"category\",\"السلامة، أنظمة إنذار\"],"` | — |
| [SRC-2C8F288796-L000718](../../web/workspace.html#L718) | 718 | `"  [\"الاستخدامات\",\"useCases\",\"المصانع، المباني التجارية\"],"` | — |
| [SRC-2C8F288796-L000719](../../web/workspace.html#L719) | 719 | `"  [\"المشكلات التي يحلها\",\"problems\",\"الكشف المبكر، تقليل المخاطر\"],"` | — |
| [SRC-2C8F288796-L000720](../../web/workspace.html#L720) | 720 | `"  [\"المناطق المستهدفة\",\"locations\",\"القاهرة، الجيزة\"],"` | — |
| [SRC-2C8F288796-L000721](../../web/workspace.html#L721) | 721 | `"  [\"القطاعات\",\"industries\",\"المقاولات، التصنيع\"],"` | — |
| [SRC-2C8F288796-L000722](../../web/workspace.html#L722) | 722 | `"  [\"نوع العملاء\",\"customers\",\"مقاولون، ملاك مشروعات\"],"` | — |
| [SRC-2C8F288796-L000723](../../web/workspace.html#L723) | 723 | `"  [\"أدوار الشراء\",\"roles\",\"مدير مشتريات، مدير مشروع\"],"` | — |
| [SRC-2C8F288796-L000724](../../web/workspace.html#L724) | 724 | `"  [\"الاستثناءات\",\"exclusions\",\"القطاعات غير المناسبة\"]"` | — |
| [SRC-2C8F288796-L000725](../../web/workspace.html#L725) | 725 | `" ];"` | — |
| [SRC-2C8F288796-L000726](../../web/workspace.html#L726) | 726 | `" fields.forEach(([label,key,placeholder])=>{"` | — |
| [SRC-2C8F288796-L000727](../../web/workspace.html#L727) | 727 | `"  const item=textField(label,\"profile_\"+key,placeholder,\"\",false);"` | — |
| [SRC-2C8F288796-L000728](../../web/workspace.html#L728) | 728 | `"  controls[key]=item.control;if(!canWrite())item.control.disabled=true;grid.append(item.field);"` | — |
| [SRC-2C8F288796-L000729](../../web/workspace.html#L729) | 729 | `" });"` | — |
| [SRC-2C8F288796-L000730](../../web/workspace.html#L730) | 730 | `" const localeField=make(\"div\",\"field\"),locale=make(\"select\",\"\");"` | — |
| [SRC-2C8F288796-L000731](../../web/workspace.html#L731) | 731 | `" [[\"auto\",\"تلقائي\"],[\"ar\",\"العربية\"],[\"en\",\"الإنجليزية\"],[\"mixed\",\"العربية والإنجليزية\"]].forEach(([v,l])=>{const o=make(\"option\",\"\",l);o.value=v;locale.append(o)});"` | — |
| [SRC-2C8F288796-L000732](../../web/workspace.html#L732) | 732 | `" localeField.append(make(\"label\",\"\",\"لغة البحث\"),locale);controls.locale=locale;if(!canWrite())locale.disabled=true;grid.append(localeField);"` | — |
| [SRC-2C8F288796-L000733](../../web/workspace.html#L733) | 733 | `" panel.append(grid,make(\"p\",\"profile-note\",\"افصل القيم المتعددة بفاصلة. تُستخدم المرادفات والمناطق لصياغة استعلامات مرتبطة بالمنتج؛ تطابق ICP وحده لا يثبت وجود طلب.\"));"` | — |
| [SRC-2C8F288796-L000734](../../web/workspace.html#L734) | 734 | `" const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000735](../../web/workspace.html#L735) | 735 | `" const save=action(\"حفظ ملف المنتج والسوق\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000736](../../web/workspace.html#L736) | 736 | `"  save.disabled=true;"` | — |
| [SRC-2C8F288796-L000737](../../web/workspace.html#L737) | 737 | `"  try{"` | — |
| [SRC-2C8F288796-L000738](../../web/workspace.html#L738) | 738 | `"   const payload={"` | — |
| [SRC-2C8F288796-L000739](../../web/workspace.html#L739) | 739 | `"    product:{name:controls.name.value,aliases:csvValues(controls.aliases.value),category_path:csvValues(controls.category.value),use_cases:csvValues(controls.useCases.value),problems_solved:csvValues(controls.problems.value)},"` | — |
| [SRC-2C8F288796-L000740](../../web/workspace.html#L740) | 740 | `"    market:{locations:csvValues(controls.locations.value),industries:csvValues(controls.industries.value),customer_types:csvValues(controls.customers.value),decision_roles:csvValues(controls.roles.value),exclusions:csvValues(controls.exclusions.value)},"` | — |
| [SRC-2C8F288796-L000741](../../web/workspace.html#L741) | 741 | `"    locale:controls.locale.value"` | — |
| [SRC-2C8F288796-L000742](../../web/workspace.html#L742) | 742 | `"   };"` | — |
| [SRC-2C8F288796-L000743](../../web/workspace.html#L743) | 743 | `"   const result=await api(\"/api/product-profiles\",{method:\"POST\",body:payload});"` | — |
| [SRC-2C8F288796-L000744](../../web/workspace.html#L744) | 744 | `"   state.activeProfileId=result.id;"` | — |
| [SRC-2C8F288796-L000745](../../web/workspace.html#L745) | 745 | `"   let refreshWarning=\"\";"` | — |
| [SRC-2C8F288796-L000746](../../web/workspace.html#L746) | 746 | `"   try{"` | — |
| [SRC-2C8F288796-L000747](../../web/workspace.html#L747) | 747 | `"    await loadProductProfiles();"` | — |
| [SRC-2C8F288796-L000748](../../web/workspace.html#L748) | 748 | `"   }catch(refreshError){"` | — |
| [SRC-2C8F288796-L000749](../../web/workspace.html#L749) | 749 | `"    refreshWarning=escapeMessage(refreshError.message);"` | — |
| [SRC-2C8F288796-L000750](../../web/workspace.html#L750) | 750 | `"   }"` | — |
| [SRC-2C8F288796-L000751](../../web/workspace.html#L751) | 751 | `"   if(refreshWarning){"` | — |
| [SRC-2C8F288796-L000752](../../web/workspace.html#L752) | 752 | `"    panel.append(make(\"p\",\"auth-error\",\"تم حفظ ملف المنتج والسوق، لكن تعذر تحديث قائمة الملفات المحفوظة. \"+refreshWarning));"` | — |
| [SRC-2C8F288796-L000753](../../web/workspace.html#L753) | 753 | `"   }else{"` | — |
| [SRC-2C8F288796-L000754](../../web/workspace.html#L754) | 754 | `"    renderProductProfile();"` | — |
| [SRC-2C8F288796-L000755](../../web/workspace.html#L755) | 755 | `"   }"` | — |
| [SRC-2C8F288796-L000756](../../web/workspace.html#L756) | 756 | `"  }catch(error){panel.append(make(\"p\",\"auth-error\",escapeMessage(error.message)))}"` | — |
| [SRC-2C8F288796-L000757](../../web/workspace.html#L757) | 757 | `"  finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000758](../../web/workspace.html#L758) | 758 | `" });"` | — |
| [SRC-2C8F288796-L000759](../../web/workspace.html#L759) | 759 | `" save.disabled=!canWrite();actions.append(save);panel.append(actions);root.append(panel);"` | — |
| [SRC-2C8F288796-L000760](../../web/workspace.html#L760) | 760 | `" const listPanel=make(\"section\",\"glass panel profile-panel\"),lh=make(\"div\",\"panel-head\"),lt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000761](../../web/workspace.html#L761) | 761 | `" lt.append(make(\"h2\",\"\",\"ملفات المنتجات المحفوظة\"),make(\"p\",\"\",\"اختر ملفًا محفوظًا للانتقال إلى تشغيل الاكتشاف.\"));"` | — |
| [SRC-2C8F288796-L000762](../../web/workspace.html#L762) | 762 | `" lh.append(lt);listPanel.append(lh);"` | — |
| [SRC-2C8F288796-L000763](../../web/workspace.html#L763) | 763 | `" if(!state.profiles.length)listPanel.append(emptyState(\"لا توجد ملفات بعد\",\"أنشئ ملف المنتج والسوق ثم احفظه.\"));"` | — |
| [SRC-2C8F288796-L000764](../../web/workspace.html#L764) | 764 | `" else{"` | — |
| [SRC-2C8F288796-L000765](../../web/workspace.html#L765) | 765 | `"  const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000766](../../web/workspace.html#L766) | 766 | `"  state.profiles.forEach(profile=>{"` | — |
| [SRC-2C8F288796-L000767](../../web/workspace.html#L767) | 767 | `"   const card=make(\"article\",\"signal-card\"),p=profile.profile\|\|{},m=p.market\|\|{};"` | — |
| [SRC-2C8F288796-L000768](../../web/workspace.html#L768) | 768 | `"   card.append(make(\"strong\",\"\",profile.name\|\|\"منتج\"));"` | — |
| [SRC-2C8F288796-L000769](../../web/workspace.html#L769) | 769 | `"   card.append(make(\"p\",\"subtle\",\"المناطق: \"+((m.locations\|\|[]).join(\"، \")\|\|\"غير محددة\")));"` | — |
| [SRC-2C8F288796-L000770](../../web/workspace.html#L770) | 770 | `"   const row=make(\"div\",\"form-actions\");row.append(action(\"استخدام في الاكتشاف\",\"\",()=>{state.activeProfileId=profile.id;navigate(\"campaign\")}));"` | — |
| [SRC-2C8F288796-L000771](../../web/workspace.html#L771) | 771 | `"   card.append(row);list.append(card);"` | — |
| [SRC-2C8F288796-L000772](../../web/workspace.html#L772) | 772 | `"  });listPanel.append(list);"` | — |
| [SRC-2C8F288796-L000773](../../web/workspace.html#L773) | 773 | `" }"` | — |
| [SRC-2C8F288796-L000774](../../web/workspace.html#L774) | 774 | `" root.append(listPanel);"` | — |
| [SRC-2C8F288796-L000775](../../web/workspace.html#L775) | 775 | `"}"` | — |
| [SRC-2C8F288796-L000776](../../web/workspace.html#L776) | 776 | `"function renderDiscoveryRun(run){"` | — |
| [SRC-2C8F288796-L000777](../../web/workspace.html#L777) | 777 | `" const panel=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000778](../../web/workspace.html#L778) | 778 | `" const report=run.search_report\|\|{},leadReport=report.lead_generation\|\|{},sources=Array.isArray(run.sources)?run.sources:[];"` | — |
| [SRC-2C8F288796-L000779](../../web/workspace.html#L779) | 779 | `" title.append(make(\"h2\",\"\",\"نتيجة عملية الاكتشاف\"),make(\"p\",\"\",\"ملف المنتج: \"+String(run.profile_name\|\|\"غير محدد\")+\" · \"+String(run.created_at\|\|\"\")));"` | — |
| [SRC-2C8F288796-L000780](../../web/workspace.html#L780) | 780 | `" head.append(title);panel.append(head);"` | — |
| [SRC-2C8F288796-L000781](../../web/workspace.html#L781) | 781 | `" const stats=make(\"div\",\"stats\"),qualifiedCount=sources.filter(s=>s.lead_qualification===\"public_demand_signal\").length;"` | — |
| [SRC-2C8F288796-L000782](../../web/workspace.html#L782) | 782 | `" stats.append("` | — |
| [SRC-2C8F288796-L000783](../../web/workspace.html#L783) | 783 | `"  buildStat(\"إشارات طلب مؤهلة\",leadReport.candidate_signal_count??qualifiedCount,\"إشارات تحمل عبارة طلب معلنة\",\"glow-teal\"),"` | — |
| [SRC-2C8F288796-L000784](../../web/workspace.html#L784) | 784 | `"  buildStat(\"المصادر التي راجعتها الجولة\",leadReport.related_results_reviewed??sources.length,\"لا يعني ذلك اكتمال السوق\",\"glow-blue\"),"` | — |
| [SRC-2C8F288796-L000785](../../web/workspace.html#L785) | 785 | `"  buildStat(\"حالة تشغيل البحث\",report.pipeline_completion_status\|\|\"غير معلومة\",\"حالة المسار كما أعادها الوكيل\",\"glow-amber\")"` | — |
| [SRC-2C8F288796-L000786](../../web/workspace.html#L786) | 786 | `" );"` | — |
| [SRC-2C8F288796-L000787](../../web/workspace.html#L787) | 787 | `" panel.append(stats,make(\"p\",\"profile-note\",run.answer\|\|\"لا يوجد ملخص لهذه العملية.\"));"` | — |
| [SRC-2C8F288796-L000788](../../web/workspace.html#L788) | 788 | `" if(Array.isArray(run.search_queries)&&run.search_queries.length){const qs=make(\"div\",\"query-list\");run.search_queries.forEach(q=>qs.append(tag(q)));panel.append(qs)}"` | — |
| [SRC-2C8F288796-L000789](../../web/workspace.html#L789) | 789 | `" const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000790](../../web/workspace.html#L790) | 790 | `" if(!sources.length)list.append(emptyState(\"لم تُعد العملية مصادر قابلة للعرض\",\"راجع حالة التشغيل والتحذيرات؛ هذا لا يثبت عدم وجود طلب.\"));"` | — |
| [SRC-2C8F288796-L000791](../../web/workspace.html#L791) | 791 | `" sources.forEach((source,index)=>{"` | — |
| [SRC-2C8F288796-L000792](../../web/workspace.html#L792) | 792 | `"  const qualified=source.lead_qualification===\"public_demand_signal\";"` | — |
| [SRC-2C8F288796-L000793](../../web/workspace.html#L793) | 793 | `"  const card=make(\"article\",\"discovery-source\"+(qualified?\" qualified\":\"\")),meta=make(\"div\",\"discovery-source-meta\");"` | — |
| [SRC-2C8F288796-L000794](../../web/workspace.html#L794) | 794 | `"  meta.append(tag(qualified?\"إشارة طلب معلنة\":\"نتيجة مرتبطة فقط\",qualified?\"teal\":\"\"));"` | — |
| [SRC-2C8F288796-L000795](../../web/workspace.html#L795) | 795 | `"  if(source.platform)meta.append(tag(source.platform));"` | — |
| [SRC-2C8F288796-L000796](../../web/workspace.html#L796) | 796 | `"  meta.append(tag(source.page_fetched?\"تمت قراءة الصفحة\":\"مقتطف/عنوان فقط\"));"` | — |
| [SRC-2C8F288796-L000797](../../web/workspace.html#L797) | 797 | `"  card.append(meta,make(\"h3\",\"\",source.title\|\|\"نتيجة ويب\"));"` | — |
| [SRC-2C8F288796-L000798](../../web/workspace.html#L798) | 798 | `"  if(source.snippet)card.append(make(\"p\",\"\",source.snippet));"` | — |
| [SRC-2C8F288796-L000799](../../web/workspace.html#L799) | 799 | `"  const evidence=source.lead_intent_evidence;"` | — |
| [SRC-2C8F288796-L000800](../../web/workspace.html#L800) | 800 | `"  if(qualified&&evidence){"` | — |
| [SRC-2C8F288796-L000801](../../web/workspace.html#L801) | 801 | `"   card.append(make(\"p\",\"\",\"عبارة الدليل: \"+String(evidence.phrase\|\|\"غير محددة\")));"` | — |
| [SRC-2C8F288796-L000802](../../web/workspace.html#L802) | 802 | `"   card.append(make(\"p\",\"\",\"نوع الإشارة: \"+String(evidence.signal_type\|\|\"غير محدد\")+\" · أساس النص: \"+String(evidence.basis\|\|\"غير محدد\")));"` | — |
| [SRC-2C8F288796-L000803](../../web/workspace.html#L803) | 803 | `"   card.append(make(\"p\",\"discovery-note\",\"ملاءمة المنتج لم تُحسم من العبارة وحدها؛ راجع المصدر قبل اعتماد الفرصة.\"));"` | — |
| [SRC-2C8F288796-L000804](../../web/workspace.html#L804) | 804 | `"  }else card.append(make(\"p\",\"discovery-note\",\"لم يعثر المحرك على عبارة كافية تثبت طلب شراء. لن تُحفظ هذه النتيجة كإشارة طلب من هذه الشاشة.\"));"` | — |
| [SRC-2C8F288796-L000805](../../web/workspace.html#L805) | 805 | `"  card.append(make(\"p\",\"discovery-note\",\"تاريخ النشر: \"+String(source.published_at\|\|\"غير متاح من المصدر\")));"` | — |
| [SRC-2C8F288796-L000806](../../web/workspace.html#L806) | 806 | `"  const url=safeHttp(source.url);if(url){const link=make(\"a\",\"\",url);link.href=url;link.target=\"_blank\";link.rel=\"noopener noreferrer\";card.append(link)}"` | — |
| [SRC-2C8F288796-L000807](../../web/workspace.html#L807) | 807 | `"  if(qualified&&canWrite()){"` | — |
| [SRC-2C8F288796-L000808](../../web/workspace.html#L808) | 808 | `"   const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000809](../../web/workspace.html#L809) | 809 | `"   const save=action(\"حفظ الإشارة في صندوق الطلب\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000810](../../web/workspace.html#L810) | 810 | `"    save.disabled=true;"` | — |
| [SRC-2C8F288796-L000811](../../web/workspace.html#L811) | 811 | `"    try{"` | — |
| [SRC-2C8F288796-L000812](../../web/workspace.html#L812) | 812 | `"     const response=await api(\"/api/discoveries/\"+encodeURIComponent(run.id)+\"/signals/\"+index+\"/save\",{method:\"POST\",body:{}});"` | — |
| [SRC-2C8F288796-L000813](../../web/workspace.html#L813) | 813 | `"     save.textContent=response.created?\"تم الحفظ\":\"الإشارة موجودة بالفعل\";"` | — |
| [SRC-2C8F288796-L000814](../../web/workspace.html#L814) | 814 | `"     let refreshWarning=\"\";"` | — |
| [SRC-2C8F288796-L000815](../../web/workspace.html#L815) | 815 | `"     try{"` | — |
| [SRC-2C8F288796-L000816](../../web/workspace.html#L816) | 816 | `"      await loadLeads();"` | — |
| [SRC-2C8F288796-L000817](../../web/workspace.html#L817) | 817 | `"     }catch(refreshError){"` | — |
| [SRC-2C8F288796-L000818](../../web/workspace.html#L818) | 818 | `"      refreshWarning=escapeMessage(refreshError.message);"` | — |
| [SRC-2C8F288796-L000819](../../web/workspace.html#L819) | 819 | `"     }"` | — |
| [SRC-2C8F288796-L000820](../../web/workspace.html#L820) | 820 | `"     if(refreshWarning)card.append(make(\"p\",\"auth-error\",\"تم حفظ الإشارة، لكن تعذر تحديث صندوق الإشارات. أعد فتح الصندوق أو حدّثه لاحقًا. \"+refreshWarning));"` | — |
| [SRC-2C8F288796-L000821](../../web/workspace.html#L821) | 821 | `"    }catch(error){card.append(make(\"p\",\"auth-error\",escapeMessage(error.message)))}"` | — |
| [SRC-2C8F288796-L000822](../../web/workspace.html#L822) | 822 | `"    finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000823](../../web/workspace.html#L823) | 823 | `"   });"` | — |
| [SRC-2C8F288796-L000824](../../web/workspace.html#L824) | 824 | `"   actions.append(save);card.append(actions);"` | — |
| [SRC-2C8F288796-L000825](../../web/workspace.html#L825) | 825 | `"  }"` | — |
| [SRC-2C8F288796-L000826](../../web/workspace.html#L826) | 826 | `"  list.append(card);"` | — |
| [SRC-2C8F288796-L000827](../../web/workspace.html#L827) | 827 | `" });"` | — |
| [SRC-2C8F288796-L000828](../../web/workspace.html#L828) | 828 | `" panel.append(list);return panel;"` | — |
| [SRC-2C8F288796-L000829](../../web/workspace.html#L829) | 829 | `"}"` | — |
| [SRC-2C8F288796-L000830](../../web/workspace.html#L830) | 830 | `"function renderDiscovery(){"` | — |
| [SRC-2C8F288796-L000831](../../web/workspace.html#L831) | 831 | `" setPage(\"حملات الاكتشاف\",\"ابحث عن إشارات طلب شراء أو توريد معلنة مرتبطة بملف المنتج والسوق. لا تُعرض النتائج العامة كعملاء محتملين.\",\"BUYER INTENT DISCOVERY\");"` | — |
| [SRC-2C8F288796-L000832](../../web/workspace.html#L832) | 832 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000833](../../web/workspace.html#L833) | 833 | `" const controls=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000834](../../web/workspace.html#L834) | 834 | `" title.append(make(\"h2\",\"\",\"تشغيل اكتشاف جديد\"),make(\"p\",\"\",\"يستخدم محرك البحث الحالي ويولّد الاستعلامات من ملف المنتج المحفوظ.\"));"` | — |
| [SRC-2C8F288796-L000835](../../web/workspace.html#L835) | 835 | `" head.append(title);controls.append(head);"` | — |
| [SRC-2C8F288796-L000836](../../web/workspace.html#L836) | 836 | `" if(!state.profiles.length){"` | — |
| [SRC-2C8F288796-L000837](../../web/workspace.html#L837) | 837 | `"  controls.append(emptyState(\"لا يوجد ملف منتج محفوظ\",\"أنشئ ملف المنتج والسوق قبل تشغيل الاكتشاف.\"));"` | — |
| [SRC-2C8F288796-L000838](../../web/workspace.html#L838) | 838 | `"  controls.append(action(\"إنشاء ملف المنتج ←\",\"primary\",()=>navigate(\"offer\")));"` | — |
| [SRC-2C8F288796-L000839](../../web/workspace.html#L839) | 839 | `" }else{"` | — |
| [SRC-2C8F288796-L000840](../../web/workspace.html#L840) | 840 | `"  const field=make(\"div\",\"field\"),profileSelect=make(\"select\",\"\");"` | — |
| [SRC-2C8F288796-L000841](../../web/workspace.html#L841) | 841 | `"  state.profiles.forEach(profile=>{const option=make(\"option\",\"\",profile.name);option.value=profile.id;option.selected=profile.id===state.activeProfileId;profileSelect.append(option)});"` | — |
| [SRC-2C8F288796-L000842](../../web/workspace.html#L842) | 842 | `"  field.append(make(\"label\",\"\",\"ملف المنتج والسوق\"),profileSelect);controls.append(field);"` | — |
| [SRC-2C8F288796-L000843](../../web/workspace.html#L843) | 843 | `"  const consent=make(\"label\",\"consent-row\"),optional=make(\"input\",\"\");optional.type=\"checkbox\";optional.checked=false;optional.disabled=state.role!==\"owner\";"` | — |
| [SRC-2C8F288796-L000844](../../web/workspace.html#L844) | 844 | `"  consent.append(optional,make(\"span\",\"\",\"السماح بالموصلات الاختيارية (DeepSeek Search وBrave وTavily وبعض واجهات المنصات الرسمية). قد تستهلك حصصًا أو تكلفة؛ تبقى معطلة افتراضيًا ولا يستطيع تفعيلها إلا مالك مساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000845](../../web/workspace.html#L845) | 845 | `"  controls.append(consent);"` | — |
| [SRC-2C8F288796-L000846](../../web/workspace.html#L846) | 846 | `"  const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000847](../../web/workspace.html#L847) | 847 | `"  const status=make(\"p\",\"profile-note\");status.setAttribute(\"role\",\"status\");status.setAttribute(\"aria-live\",\"polite\");"` | — |
| [SRC-2C8F288796-L000848](../../web/workspace.html#L848) | 848 | `"  const run=action(\"بدء اكتشاف الطلب\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000849](../../web/workspace.html#L849) | 849 | `"   run.disabled=true;run.setAttribute(\"aria-busy\",\"true\");state.activeProfileId=profileSelect.value;"` | — |
| [SRC-2C8F288796-L000850](../../web/workspace.html#L850) | 850 | `"   status.setAttribute(\"role\",\"status\");status.setAttribute(\"aria-live\",\"polite\");status.className=\"profile-note\";status.textContent=\"جارٍ البحث عن إشارات الطلب؛ ستظل النتائج السابقة متاحة حتى تكتمل الجولة الجديدة.\";"` | — |
| [SRC-2C8F288796-L000851](../../web/workspace.html#L851) | 851 | `"   try{"` | — |
| [SRC-2C8F288796-L000852](../../web/workspace.html#L852) | 852 | `"    const savedRun=await api(\"/api/discoveries\",{method:\"POST\",body:{profile_id:profileSelect.value,allow_optional_providers:optional.checked}});"` | — |
| [SRC-2C8F288796-L000853](../../web/workspace.html#L853) | 853 | `"    state.activeDiscovery=savedRun;"` | — |
| [SRC-2C8F288796-L000854](../../web/workspace.html#L854) | 854 | `"    let refreshWarning=\"\";"` | — |
| [SRC-2C8F288796-L000855](../../web/workspace.html#L855) | 855 | `"    try{await loadDiscoveryRuns()}catch(refreshError){refreshWarning=\" حُفظت نتيجة البحث، لكن تعذر تحديث سجل العمليات: \"+escapeMessage(refreshError.message)}"` | — |
| [SRC-2C8F288796-L000856](../../web/workspace.html#L856) | 856 | `"    renderDiscovery();"` | — |
| [SRC-2C8F288796-L000857](../../web/workspace.html#L857) | 857 | `"    if(refreshWarning){const warning=make(\"p\",\"auth-error\",refreshWarning);warning.setAttribute(\"role\",\"alert\");$(\"viewRoot\").append(warning)}"` | — |
| [SRC-2C8F288796-L000858](../../web/workspace.html#L858) | 858 | `"   }catch(error){"` | — |
| [SRC-2C8F288796-L000859](../../web/workspace.html#L859) | 859 | `"    status.setAttribute(\"role\",\"alert\");status.setAttribute(\"aria-live\",\"assertive\");status.className=\"auth-error\";status.textContent=\"تعذر تشغيل الاكتشاف: \"+escapeMessage(error.message)+\" يمكنك المحاولة مجددًا. لم تُحذف النتائج السابقة.\";"` | — |
| [SRC-2C8F288796-L000860](../../web/workspace.html#L860) | 860 | `"   }finally{"` | — |
| [SRC-2C8F288796-L000861](../../web/workspace.html#L861) | 861 | `"    run.disabled=false;run.removeAttribute(\"aria-busy\");"` | — |
| [SRC-2C8F288796-L000862](../../web/workspace.html#L862) | 862 | `"   }"` | — |
| [SRC-2C8F288796-L000863](../../web/workspace.html#L863) | 863 | `"  });"` | — |
| [SRC-2C8F288796-L000864](../../web/workspace.html#L864) | 864 | `"  run.disabled=!canWrite();actions.append(run);controls.append(actions,status);"` | — |
| [SRC-2C8F288796-L000865](../../web/workspace.html#L865) | 865 | `" }"` | — |
| [SRC-2C8F288796-L000866](../../web/workspace.html#L866) | 866 | `" controls.append(make(\"p\",\"profile-note\",\"تاريخ النشر قد يكون غير متاح. المقتطف لا يعني أن الصفحة قُرئت. فشل الموصل لا يثبت عدم وجود عملاء. لا يتم إرسال أي رسالة من هذه الشاشة.\"));"` | — |
| [SRC-2C8F288796-L000867](../../web/workspace.html#L867) | 867 | `" controls.append(make(\"p\",\"profile-note\",\"تشغيل الاكتشاف يستخدم النموذج اللغوي المهيأ حاليًا في Omarai؛ قد يستهلك حصة أو تكلفة بحسب إعدادات مزود النموذج. لا تدخل بيانات سرية. الموصلات الاختيارية منفصلة وتظل معطلة افتراضيًا حتى موافقة المالك.\"));"` | — |
| [SRC-2C8F288796-L000868](../../web/workspace.html#L868) | 868 | `" root.append(controls);"` | — |
| [SRC-2C8F288796-L000869](../../web/workspace.html#L869) | 869 | `" if(state.discoveryRuns.length){"` | — |
| [SRC-2C8F288796-L000870](../../web/workspace.html#L870) | 870 | `"  const history=make(\"section\",\"glass panel profile-panel\"),hh=make(\"div\",\"panel-head\"),ht=make(\"div\");"` | — |
| [SRC-2C8F288796-L000871](../../web/workspace.html#L871) | 871 | `"  ht.append(make(\"h2\",\"\",\"سجل عمليات الاكتشاف\"),make(\"p\",\"\",\"عمليات محفوظة ضمن مساحة العمل الحالية.\"));"` | — |
| [SRC-2C8F288796-L000872](../../web/workspace.html#L872) | 872 | `"  hh.append(ht);history.append(hh);const list=make(\"div\",\"discovery-history\");"` | — |
| [SRC-2C8F288796-L000873](../../web/workspace.html#L873) | 873 | `"  state.discoveryRuns.forEach(item=>list.append(action("` | — |
| [SRC-2C8F288796-L000874](../../web/workspace.html#L874) | 874 | `"   String(item.profile_name\|\|\"ملف منتج\")+\" · \"+String(item.qualified_signal_count\|\|0)+\" إشارة · \"+String(item.created_at\|\|\"\"),"` | — |
| [SRC-2C8F288796-L000875](../../web/workspace.html#L875) | 875 | `"   \"\","` | — |
| [SRC-2C8F288796-L000876](../../web/workspace.html#L876) | 876 | `"   async()=>{try{state.activeDiscovery=await api(\"/api/discoveries/\"+encodeURIComponent(item.id));renderDiscovery()}catch(error){const message=make(\"p\",\"auth-error\",escapeMessage(error.message));message.setAttribute(\"role\",\"alert\");history.append(message)}}"` | — |
| [SRC-2C8F288796-L000877](../../web/workspace.html#L877) | 877 | `"  )));"` | — |
| [SRC-2C8F288796-L000878](../../web/workspace.html#L878) | 878 | `"  history.append(list);root.append(history);"` | — |
| [SRC-2C8F288796-L000879](../../web/workspace.html#L879) | 879 | `" }"` | — |
| [SRC-2C8F288796-L000880](../../web/workspace.html#L880) | 880 | `" if(state.activeDiscovery)root.append(renderDiscoveryRun(state.activeDiscovery));"` | — |
| [SRC-2C8F288796-L000881](../../web/workspace.html#L881) | 881 | `"}"` | — |
| [SRC-2C8F288796-L000882](../../web/workspace.html#L882) | 882 | `""` | — |
| [SRC-2C8F288796-L000883](../../web/workspace.html#L883) | 883 | `"const chatModes=["` | — |
| [SRC-2C8F288796-L000884](../../web/workspace.html#L884) | 884 | `" {id:\"auto\",label:\"تلقائي\"},"` | — |
| [SRC-2C8F288796-L000885](../../web/workspace.html#L885) | 885 | `" {id:\"deep\",label:\"بحث معمّق\"},"` | — |
| [SRC-2C8F288796-L000886](../../web/workspace.html#L886) | 886 | `" {id:\"latest\",label:\"الأحدث الآن\"},"` | — |
| [SRC-2C8F288796-L000887](../../web/workspace.html#L887) | 887 | `" {id:\"social\",label:\"آراء الناس\"}"` | — |
| [SRC-2C8F288796-L000888](../../web/workspace.html#L888) | 888 | `"];"` | — |
| [SRC-2C8F288796-L000889](../../web/workspace.html#L889) | 889 | `"function appendCitedAnswer(container,text,sources){"` | — |
| [SRC-2C8F288796-L000890](../../web/workspace.html#L890) | 890 | `" const value=String(text\|\|\"\");"` | — |
| [SRC-2C8F288796-L000891](../../web/workspace.html#L891) | 891 | `" const marker=/\\[(?:المصدر\|source)\\s+(\\d+)\\]/gi;"` | — |
| [SRC-2C8F288796-L000892](../../web/workspace.html#L892) | 892 | `" let cursor=0,match;"` | — |
| [SRC-2C8F288796-L000893](../../web/workspace.html#L893) | 893 | `" while((match=marker.exec(value))){"` | — |
| [SRC-2C8F288796-L000894](../../web/workspace.html#L894) | 894 | `"  container.append(document.createTextNode(value.slice(cursor,match.index)));"` | — |
| [SRC-2C8F288796-L000895](../../web/workspace.html#L895) | 895 | `"  const index=Number(match[1]);"` | — |
| [SRC-2C8F288796-L000896](../../web/workspace.html#L896) | 896 | `"  const source=Number.isSafeInteger(index)&&index>0&&Array.isArray(sources)?sources[index-1]:null;"` | — |
| [SRC-2C8F288796-L000897](../../web/workspace.html#L897) | 897 | `"  const href=source&&safeHttp(source.url);"` | — |
| [SRC-2C8F288796-L000898](../../web/workspace.html#L898) | 898 | `"  if(href){"` | — |
| [SRC-2C8F288796-L000899](../../web/workspace.html#L899) | 899 | `"   const link=document.createElement(\"a\");"` | — |
| [SRC-2C8F288796-L000900](../../web/workspace.html#L900) | 900 | `"   link.className=\"chat-citation\";link.href=href;link.target=\"_blank\";"` | — |
| [SRC-2C8F288796-L000901](../../web/workspace.html#L901) | 901 | `"   link.rel=\"noopener noreferrer\";link.textContent=match[0];"` | — |
| [SRC-2C8F288796-L000902](../../web/workspace.html#L902) | 902 | `"   link.title=String(source.title\|\|(\"المصدر \"+index)).slice(0,180);"` | — |
| [SRC-2C8F288796-L000903](../../web/workspace.html#L903) | 903 | `"   link.setAttribute(\"aria-label\",\"فتح المصدر \"+index+\": \"+String(source.title\|\|\"دون عنوان\").slice(0,140));"` | — |
| [SRC-2C8F288796-L000904](../../web/workspace.html#L904) | 904 | `"   container.append(link);"` | — |
| [SRC-2C8F288796-L000905](../../web/workspace.html#L905) | 905 | `"  }else{"` | — |
| [SRC-2C8F288796-L000906](../../web/workspace.html#L906) | 906 | `"   container.append(document.createTextNode(match[0]));"` | — |
| [SRC-2C8F288796-L000907](../../web/workspace.html#L907) | 907 | `"  }"` | — |
| [SRC-2C8F288796-L000908](../../web/workspace.html#L908) | 908 | `"  cursor=marker.lastIndex;"` | — |
| [SRC-2C8F288796-L000909](../../web/workspace.html#L909) | 909 | `" }"` | — |
| [SRC-2C8F288796-L000910](../../web/workspace.html#L910) | 910 | `" container.append(document.createTextNode(value.slice(cursor)));"` | — |
| [SRC-2C8F288796-L000911](../../web/workspace.html#L911) | 911 | `"}"` | — |
| [SRC-2C8F288796-L000912](../../web/workspace.html#L912) | 912 | `"function chatMessageNode(item){"` | — |
| [SRC-2C8F288796-L000913](../../web/workspace.html#L913) | 913 | `" const row=make(\"div\",\"chat-msg chat-\"+item.role);"` | — |
| [SRC-2C8F288796-L000914](../../web/workspace.html#L914) | 914 | `" row.append(make(\"div\",\"chat-who\",item.role===\"user\"?\"أنت\":\"Omarai\"));"` | — |
| [SRC-2C8F288796-L000915](../../web/workspace.html#L915) | 915 | `" const answer=make(\"div\",\"chat-text\");appendCitedAnswer(answer,item.text,item.sources);row.append(answer);"` | — |
| [SRC-2C8F288796-L000916](../../web/workspace.html#L916) | 916 | `" if(item.role===\"assistant\"&&Array.isArray(item.sources)&&item.sources.length){"` | — |
| [SRC-2C8F288796-L000917](../../web/workspace.html#L917) | 917 | `"  const list=make(\"ul\",\"chat-sources\");"` | — |
| [SRC-2C8F288796-L000918](../../web/workspace.html#L918) | 918 | `"  item.sources.slice(0,8).forEach(src=>{"` | — |
| [SRC-2C8F288796-L000919](../../web/workspace.html#L919) | 919 | `"   const href=src&&safeHttp(src.url);if(!href)return;"` | — |
| [SRC-2C8F288796-L000920](../../web/workspace.html#L920) | 920 | `"   const li=make(\"li\");const a=make(\"a\",\"\",String(src.title\|\|href).slice(0,140));"` | — |
| [SRC-2C8F288796-L000921](../../web/workspace.html#L921) | 921 | `"   a.href=href;a.target=\"_blank\";a.rel=\"noopener noreferrer\";li.append(a);list.append(li);"` | — |
| [SRC-2C8F288796-L000922](../../web/workspace.html#L922) | 922 | `"  });"` | — |
| [SRC-2C8F288796-L000923](../../web/workspace.html#L923) | 923 | `"  if(list.childNodes.length){row.append(make(\"div\",\"chat-who\",\"المصادر\"),list)}"` | — |
| [SRC-2C8F288796-L000924](../../web/workspace.html#L924) | 924 | `" }"` | — |
| [SRC-2C8F288796-L000925](../../web/workspace.html#L925) | 925 | `" if(item.role===\"assistant\"&&item.note)row.append(make(\"div\",\"chat-note\",item.note));"` | — |
| [SRC-2C8F288796-L000926](../../web/workspace.html#L926) | 926 | `" return row;"` | — |
| [SRC-2C8F288796-L000927](../../web/workspace.html#L927) | 927 | `"}"` | — |
| [SRC-2C8F288796-L000928](../../web/workspace.html#L928) | 928 | `"function renderChat(){"` | — |
| [SRC-2C8F288796-L000929](../../web/workspace.html#L929) | 929 | `" setPage(\"محادثة Omarai\",\"اسأل باللهجة المصرية أو الفصحى أو الإنجليزية. تُرسل الأسئلة إلى محركات البحث وقد تُرسل مقتطفات المصادر إلى مزود نموذج اللغة المضبوط.\",\"CHAT\");"` | — |
| [SRC-2C8F288796-L000930](../../web/workspace.html#L930) | 930 | `" const chat=state.chat;"` | — |
| [SRC-2C8F288796-L000931](../../web/workspace.html#L931) | 931 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000932](../../web/workspace.html#L932) | 932 | `" const panel=make(\"section\",\"glass panel chat-panel\");"` | — |
| [SRC-2C8F288796-L000933](../../web/workspace.html#L933) | 933 | `" const ph=make(\"div\",\"panel-head\");const pt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000934](../../web/workspace.html#L934) | 934 | `" pt.append(make(\"h2\",\"\",\"المحادثة والبحث\"),make(\"p\",\"\",\"يتذكر آخر ٨ رسائل داخل هذه الجلسة. لا تضع كلمات مرور أو مفاتيح API أو بيانات شخصية سرية في السؤال.\"));"` | — |
| [SRC-2C8F288796-L000935](../../web/workspace.html#L935) | 935 | `" const clear=action(\"محادثة جديدة\",\"ghost\",()=>{if(chat.busy)return;chat.messages=[];chat.history=[];renderChat()});"` | — |
| [SRC-2C8F288796-L000936](../../web/workspace.html#L936) | 936 | `" ph.append(pt,clear);panel.append(ph);"` | — |
| [SRC-2C8F288796-L000937](../../web/workspace.html#L937) | 937 | `""` | — |
| [SRC-2C8F288796-L000938](../../web/workspace.html#L938) | 938 | `" const modeBar=make(\"div\",\"chat-modes\");"` | — |
| [SRC-2C8F288796-L000939](../../web/workspace.html#L939) | 939 | `" chatModes.forEach(m=>{"` | — |
| [SRC-2C8F288796-L000940](../../web/workspace.html#L940) | 940 | `"  const b=make(\"button\",\"button ghost\"+(chat.mode===m.id?\" chat-mode-active\":\"\"),m.label);"` | — |
| [SRC-2C8F288796-L000941](../../web/workspace.html#L941) | 941 | `"  b.type=\"button\";b.setAttribute(\"aria-pressed\",chat.mode===m.id?\"true\":\"false\");b.disabled=chat.busy;"` | — |
| [SRC-2C8F288796-L000942](../../web/workspace.html#L942) | 942 | `"  b.addEventListener(\"click\",()=>{chat.mode=m.id;renderChat()});modeBar.append(b);"` | — |
| [SRC-2C8F288796-L000943](../../web/workspace.html#L943) | 943 | `" });"` | — |
| [SRC-2C8F288796-L000944](../../web/workspace.html#L944) | 944 | `" panel.append(modeBar);"` | — |
| [SRC-2C8F288796-L000945](../../web/workspace.html#L945) | 945 | `""` | — |
| [SRC-2C8F288796-L000946](../../web/workspace.html#L946) | 946 | `" const list=make(\"div\",\"chat-list\");list.id=\"chatList\";list.setAttribute(\"aria-live\",\"polite\");"` | — |
| [SRC-2C8F288796-L000947](../../web/workspace.html#L947) | 947 | `" if(!chat.messages.length){"` | — |
| [SRC-2C8F288796-L000948](../../web/workspace.html#L948) | 948 | `"  list.append(make(\"div\",\"chat-empty\",\"اكتب سؤالك لبدء المحادثة. مثال: «ايه أفضل طريقة أوصل بيها لشركات محتاجة نظام إنذار حريق؟»\"));"` | — |
| [SRC-2C8F288796-L000949](../../web/workspace.html#L949) | 949 | `" }else chat.messages.forEach(item=>list.append(chatMessageNode(item)));"` | — |
| [SRC-2C8F288796-L000950](../../web/workspace.html#L950) | 950 | `" panel.append(list);"` | — |
| [SRC-2C8F288796-L000951](../../web/workspace.html#L951) | 951 | `""` | — |
| [SRC-2C8F288796-L000952](../../web/workspace.html#L952) | 952 | `" const form=make(\"div\",\"chat-form\");"` | — |
| [SRC-2C8F288796-L000953](../../web/workspace.html#L953) | 953 | `" const input=make(\"textarea\");input.id=\"chatInput\";input.rows=2;input.maxLength=4000;input.placeholder=\"اكتب سؤالك هنا… (Enter للإرسال · Shift+Enter لسطر جديد)\";input.disabled=chat.busy;"` | — |
| [SRC-2C8F288796-L000954](../../web/workspace.html#L954) | 954 | `" const send=action(chat.busy?\"يبحث…\":\"أرسل ←\",\"primary\",()=>sendChat());send.id=\"chatSend\";send.disabled=chat.busy;"` | — |
| [SRC-2C8F288796-L000955](../../web/workspace.html#L955) | 955 | `" input.addEventListener(\"keydown\",e=>{if(e.key===\"Enter\"&&!e.shiftKey&&!e.isComposing){e.preventDefault();sendChat()}});"` | — |
| [SRC-2C8F288796-L000956](../../web/workspace.html#L956) | 956 | `" form.append(input,send);panel.append(form);"` | — |
| [SRC-2C8F288796-L000957](../../web/workspace.html#L957) | 957 | `" root.append(panel);"` | — |
| [SRC-2C8F288796-L000958](../../web/workspace.html#L958) | 958 | `" list.scrollTop=list.scrollHeight;"` | — |
| [SRC-2C8F288796-L000959](../../web/workspace.html#L959) | 959 | `" if(!chat.busy)input.focus();"` | — |
| [SRC-2C8F288796-L000960](../../web/workspace.html#L960) | 960 | `"}"` | — |
| [SRC-2C8F288796-L000961](../../web/workspace.html#L961) | 961 | `"async function sendChat(){"` | — |
| [SRC-2C8F288796-L000962](../../web/workspace.html#L962) | 962 | `" const chat=state.chat;if(chat.busy)return;"` | — |
| [SRC-2C8F288796-L000963](../../web/workspace.html#L963) | 963 | `" const requestSessionVersion=chat.sessionVersion;"` | — |
| [SRC-2C8F288796-L000964](../../web/workspace.html#L964) | 964 | `" const input=$(\"chatInput\");const question=input?input.value.trim():\"\";"` | — |
| [SRC-2C8F288796-L000965](../../web/workspace.html#L965) | 965 | `" if(!question)return;"` | — |
| [SRC-2C8F288796-L000966](../../web/workspace.html#L966) | 966 | `" chat.messages.push({role:\"user\",text:question});chat.busy=true;renderChat();"` | — |
| [SRC-2C8F288796-L000967](../../web/workspace.html#L967) | 967 | `" const controller=new AbortController();"` | — |
| [SRC-2C8F288796-L000968](../../web/workspace.html#L968) | 968 | `" let requestTimedOut=false;"` | — |
| [SRC-2C8F288796-L000969](../../web/workspace.html#L969) | 969 | `" const timeoutId=window.setTimeout(()=>{requestTimedOut=true;controller.abort();},135000);"` | — |
| [SRC-2C8F288796-L000970](../../web/workspace.html#L970) | 970 | `" try{"` | — |
| [SRC-2C8F288796-L000971](../../web/workspace.html#L971) | 971 | `"  const data=await api(\"/api/agent\",{method:\"POST\",signal:controller.signal,body:{question:question,history:chat.history.slice(-8),mode:chat.mode}});"` | — |
| [SRC-2C8F288796-L000972](../../web/workspace.html#L972) | 972 | `"  if(state.chat.sessionVersion!==requestSessionVersion)return;"` | — |
| [SRC-2C8F288796-L000973](../../web/workspace.html#L973) | 973 | `"  const answer=String(data.answer\|\|\"لم يرجع الخادم نص إجابة.\");"` | — |
| [SRC-2C8F288796-L000974](../../web/workspace.html#L974) | 974 | `"  const note=data.kind===\"general_answer\"?\"إجابة معرفة عامة دون بحث ويب.\":(data.used_web_search===true?\"\":\"لم يُجرَ بحث ويب لهذه الإجابة.\");"` | — |
| [SRC-2C8F288796-L000975](../../web/workspace.html#L975) | 975 | `"  chat.messages.push({role:\"assistant\",text:answer,sources:Array.isArray(data.sources)?data.sources:[],note:note});"` | — |
| [SRC-2C8F288796-L000976](../../web/workspace.html#L976) | 976 | `"  chat.history.push({role:\"user\",content:question},{role:\"assistant\",content:answer});"` | — |
| [SRC-2C8F288796-L000977](../../web/workspace.html#L977) | 977 | `"  chat.history=chat.history.slice(-16);"` | — |
| [SRC-2C8F288796-L000978](../../web/workspace.html#L978) | 978 | `" }catch(error){"` | — |
| [SRC-2C8F288796-L000979](../../web/workspace.html#L979) | 979 | `"  if(state.chat.sessionVersion===requestSessionVersion){"` | — |
| [SRC-2C8F288796-L000980](../../web/workspace.html#L980) | 980 | `"   const timedOut=requestTimedOut\|\|(error&&error.name===\"AbortError\");"` | — |
| [SRC-2C8F288796-L000981](../../web/workspace.html#L981) | 981 | `"   const message=timedOut"` | — |
| [SRC-2C8F288796-L000982](../../web/workspace.html#L982) | 982 | `"    ?\"انتهى وقت انتظار الواجهة بعد 135 ثانية. قد يواصل الخادم إنهاء العملية ضمن ميزانية موارده.\""` | — |
| [SRC-2C8F288796-L000983](../../web/workspace.html#L983) | 983 | `"    :\"تعذر إكمال الطلب: \"+escapeMessage(error&&error.message);"` | — |
| [SRC-2C8F288796-L000984](../../web/workspace.html#L984) | 984 | `"   chat.messages.push({role:\"assistant\",text:message,sources:[],note:\"\"});"` | — |
| [SRC-2C8F288796-L000985](../../web/workspace.html#L985) | 985 | `"  }"` | — |
| [SRC-2C8F288796-L000986](../../web/workspace.html#L986) | 986 | `" }finally{"` | — |
| [SRC-2C8F288796-L000987](../../web/workspace.html#L987) | 987 | `"  window.clearTimeout(timeoutId);"` | — |
| [SRC-2C8F288796-L000988](../../web/workspace.html#L988) | 988 | `"  if(state.chat.sessionVersion===requestSessionVersion){"` | — |
| [SRC-2C8F288796-L000989](../../web/workspace.html#L989) | 989 | `"   chat.busy=false;"` | — |
| [SRC-2C8F288796-L000990](../../web/workspace.html#L990) | 990 | `"   if(state.activeView===\"chat\")renderChat();"` | — |
| [SRC-2C8F288796-L000991](../../web/workspace.html#L991) | 991 | `"  }"` | — |
| [SRC-2C8F288796-L000992](../../web/workspace.html#L992) | 992 | `" }"` | — |
| [SRC-2C8F288796-L000993](../../web/workspace.html#L993) | 993 | `"}"` | — |
| [SRC-2C8F288796-L000994](../../web/workspace.html#L994) | 994 | `""` | — |
| [SRC-2C8F288796-L000995](../../web/workspace.html#L995) | 995 | `"function renderCurrent(){"` | — |
| [SRC-2C8F288796-L000996](../../web/workspace.html#L996) | 996 | `" renderNav();"` | — |
| [SRC-2C8F288796-L000997](../../web/workspace.html#L997) | 997 | `" if(state.activeView===\"overview\")renderOverview();"` | — |
| [SRC-2C8F288796-L000998](../../web/workspace.html#L998) | 998 | `" else if(state.activeView===\"indicators\")renderIndicators();"` | — |
| [SRC-2C8F288796-L000999](../../web/workspace.html#L999) | 999 | `" else if(state.activeView===\"offer\")renderProductProfile();"` | — |
| [SRC-2C8F288796-L001000](../../web/workspace.html#L1000) | 1000 | `" else if(state.activeView===\"campaign\")renderDiscovery();"` | — |
| [SRC-2C8F288796-L001001](../../web/workspace.html#L1001) | 1001 | `" else if(state.activeView===\"signals\")renderSignals();"` | — |
| [SRC-2C8F288796-L001002](../../web/workspace.html#L1002) | 1002 | `" else if(state.activeView===\"pipeline\")renderPipeline();"` | — |
| [SRC-2C8F288796-L001003](../../web/workspace.html#L1003) | 1003 | `" else if(state.activeView===\"chat\")renderChat();"` | — |
| [SRC-2C8F288796-L001004](../../web/workspace.html#L1004) | 1004 | `" else if(state.activeView===\"system\")renderSystem();"` | — |
| [SRC-2C8F288796-L001005](../../web/workspace.html#L1005) | 1005 | `" else renderPlaceholder(state.activeView);"` | — |
| [SRC-2C8F288796-L001006](../../web/workspace.html#L1006) | 1006 | `" if(state.loadWarnings.length){"` | — |
| [SRC-2C8F288796-L001007](../../web/workspace.html#L1007) | 1007 | `"  $(\"viewRoot\").prepend(make(\"p\",\"auth-error\",\"تم التحقق من الجلسة؛ تعذر تحميل بعض البيانات: \"+state.loadWarnings.join(\"، \")+\". قد تكون بعض القوائم والأرقام غير مكتملة.\"));"` | — |
| [SRC-2C8F288796-L001008](../../web/workspace.html#L1008) | 1008 | `" }"` | — |
| [SRC-2C8F288796-L001009](../../web/workspace.html#L1009) | 1009 | `"}"` | — |
| [SRC-2C8F288796-L001010](../../web/workspace.html#L1010) | 1010 | `"function navigate(view){"` | — |
| [SRC-2C8F288796-L001011](../../web/workspace.html#L1011) | 1011 | `" state.activeView=view;renderCurrent();"` | — |
| [SRC-2C8F288796-L001012](../../web/workspace.html#L1012) | 1012 | `"}"` | — |
| [SRC-2C8F288796-L001013](../../web/workspace.html#L1013) | 1013 | `"async function loadProductProfiles(){"` | — |
| [SRC-2C8F288796-L001014](../../web/workspace.html#L1014) | 1014 | `" const data=await api(\"/api/product-profiles\");"` | — |
| [SRC-2C8F288796-L001015](../../web/workspace.html#L1015) | 1015 | `" state.profiles=Array.isArray(data.profiles)?data.profiles:[];"` | — |
| [SRC-2C8F288796-L001016](../../web/workspace.html#L1016) | 1016 | `" if(!state.profiles.some(item=>item.id===state.activeProfileId))state.activeProfileId=state.profiles[0]?.id\|\|null;"` | — |
| [SRC-2C8F288796-L001017](../../web/workspace.html#L1017) | 1017 | `"}"` | — |
| [SRC-2C8F288796-L001018](../../web/workspace.html#L1018) | 1018 | `"async function loadDiscoveryRuns(){"` | — |
| [SRC-2C8F288796-L001019](../../web/workspace.html#L1019) | 1019 | `" const data=await api(\"/api/discoveries\");"` | — |
| [SRC-2C8F288796-L001020](../../web/workspace.html#L1020) | 1020 | `" state.discoveryRuns=Array.isArray(data.runs)?data.runs:[];"` | — |
| [SRC-2C8F288796-L001021](../../web/workspace.html#L1021) | 1021 | `"}"` | — |
| [SRC-2C8F288796-L001022](../../web/workspace.html#L1022) | 1022 | `"async function loadLeads(){"` | — |
| [SRC-2C8F288796-L001023](../../web/workspace.html#L1023) | 1023 | `" const data=await api(\"/api/leads?limit=500\");"` | — |
| [SRC-2C8F288796-L001024](../../web/workspace.html#L1024) | 1024 | `" state.leads=Array.isArray(data.leads)?data.leads:[];"` | — |
| [SRC-2C8F288796-L001025](../../web/workspace.html#L1025) | 1025 | `"}"` | — |
| [SRC-2C8F288796-L001026](../../web/workspace.html#L1026) | 1026 | `"async function bootstrap(){"` | — |
| [SRC-2C8F288796-L001027](../../web/workspace.html#L1027) | 1027 | `" let session;"` | — |
| [SRC-2C8F288796-L001028](../../web/workspace.html#L1028) | 1028 | `" try{"` | — |
| [SRC-2C8F288796-L001029](../../web/workspace.html#L1029) | 1029 | `"  session=await api(\"/api/session\");"` | — |
| [SRC-2C8F288796-L001030](../../web/workspace.html#L1030) | 1030 | `" }catch(e){"` | — |
| [SRC-2C8F288796-L001031](../../web/workspace.html#L1031) | 1031 | `"  setConnection(false,\"يلزم تسجيل الدخول\",\"تعذر التحقق من جلسة المستخدم.\");"` | — |
| [SRC-2C8F288796-L001032](../../web/workspace.html#L1032) | 1032 | `"  showAuth(e.message);"` | — |
| [SRC-2C8F288796-L001033](../../web/workspace.html#L1033) | 1033 | `"  $(\"viewRoot\").replaceChildren(emptyState(\"مساحة العمل مقفلة\",\"سجّل الدخول لقراءة البيانات المرتبطة بمساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L001034](../../web/workspace.html#L1034) | 1034 | `"  return;"` | — |
| [SRC-2C8F288796-L001035](../../web/workspace.html#L1035) | 1035 | `" }"` | — |
| [SRC-2C8F288796-L001036](../../web/workspace.html#L1036) | 1036 | `" state.role=session.role\|\|\"unknown\";"` | — |
| [SRC-2C8F288796-L001037](../../web/workspace.html#L1037) | 1037 | `" $(\"rolePill\").textContent=\"صلاحية: \"+state.role;"` | — |
| [SRC-2C8F288796-L001038](../../web/workspace.html#L1038) | 1038 | `" $(\"roleSummary\").textContent=\"الدور: \"+state.role+(canWrite()?\" — إضافة وتحديث السجلات متاح.\":\" — قراءة فقط.\");"` | — |
| [SRC-2C8F288796-L001039](../../web/workspace.html#L1039) | 1039 | `" hideAuth();"` | — |
| [SRC-2C8F288796-L001040](../../web/workspace.html#L1040) | 1040 | `" const results=await Promise.allSettled(["` | — |
| [SRC-2C8F288796-L001041](../../web/workspace.html#L1041) | 1041 | `"  loadLeads(),"` | — |
| [SRC-2C8F288796-L001042](../../web/workspace.html#L1042) | 1042 | `"  loadProductProfiles(),"` | — |
| [SRC-2C8F288796-L001043](../../web/workspace.html#L1043) | 1043 | `"  loadDiscoveryRuns()"` | — |
| [SRC-2C8F288796-L001044](../../web/workspace.html#L1044) | 1044 | `" ]);"` | — |
| [SRC-2C8F288796-L001045](../../web/workspace.html#L1045) | 1045 | `" if($(\"authGate\").classList.contains(\"open\")){"` | — |
| [SRC-2C8F288796-L001046](../../web/workspace.html#L1046) | 1046 | `"  setConnection(false,\"يلزم تسجيل الدخول\",\"انتهت الجلسة أثناء تحميل البيانات.\");"` | — |
| [SRC-2C8F288796-L001047](../../web/workspace.html#L1047) | 1047 | `"  $(\"viewRoot\").replaceChildren(emptyState(\"مساحة العمل مقفلة\",\"سجّل الدخول لقراءة البيانات المرتبطة بمساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L001048](../../web/workspace.html#L1048) | 1048 | `"  return;"` | — |
| [SRC-2C8F288796-L001049](../../web/workspace.html#L1049) | 1049 | `" }"` | — |
| [SRC-2C8F288796-L001050](../../web/workspace.html#L1050) | 1050 | `" state.loadWarnings=[];"` | — |
| [SRC-2C8F288796-L001051](../../web/workspace.html#L1051) | 1051 | `" const labels=[\"سجل الإشارات\",\"ملفات المنتجات\",\"سجل الاكتشاف\"];"` | — |
| [SRC-2C8F288796-L001052](../../web/workspace.html#L1052) | 1052 | `" results.forEach((result,index)=>{"` | — |
| [SRC-2C8F288796-L001053](../../web/workspace.html#L1053) | 1053 | `"  if(result.status!==\"rejected\")return;"` | — |
| [SRC-2C8F288796-L001054](../../web/workspace.html#L1054) | 1054 | `"  state.loadWarnings.push(labels[index]);"` | — |
| [SRC-2C8F288796-L001055](../../web/workspace.html#L1055) | 1055 | `"  if(index===0)state.leads=[];"` | — |
| [SRC-2C8F288796-L001056](../../web/workspace.html#L1056) | 1056 | `"  else if(index===1)state.profiles=[];"` | — |
| [SRC-2C8F288796-L001057](../../web/workspace.html#L1057) | 1057 | `"  else state.discoveryRuns=[];"` | — |
| [SRC-2C8F288796-L001058](../../web/workspace.html#L1058) | 1058 | `" });"` | — |
| [SRC-2C8F288796-L001059](../../web/workspace.html#L1059) | 1059 | `" const note=state.loadWarnings.length"` | — |
| [SRC-2C8F288796-L001060](../../web/workspace.html#L1060) | 1060 | `"  ?\"الجلسة مصادق عليها؛ تعذر تحميل بعض البيانات: \"+state.loadWarnings.join(\"، \")+\". حاول تحديث الوحدة لاحقًا.\""` | — |
| [SRC-2C8F288796-L001061](../../web/workspace.html#L1061) | 1061 | `"  :\"تم تحميل الإشارات وملفات المنتج وسجل الاكتشاف. هذا لا يثبت اتصال جميع الموصلات.\";"` | — |
| [SRC-2C8F288796-L001062](../../web/workspace.html#L1062) | 1062 | `" setConnection(true,state.loadWarnings.length?\"الجلسة مصادق عليها — بيانات جزئية\":\"الجلسة مصادق عليها\",note);"` | — |
| [SRC-2C8F288796-L001063](../../web/workspace.html#L1063) | 1063 | `" renderCurrent();"` | — |
| [SRC-2C8F288796-L001064](../../web/workspace.html#L1064) | 1064 | `"}"` | — |
| [SRC-2C8F288796-L001065](../../web/workspace.html#L1065) | 1065 | `"$(\"loginForm\").addEventListener(\"submit\",async event=>{"` | — |
| [SRC-2C8F288796-L001066](../../web/workspace.html#L1066) | 1066 | `" event.preventDefault();const token=$(\"accessToken\").value.trim();const button=$(\"loginButton\");button.disabled=true;$(\"authError\").textContent=\"\";"` | — |
| [SRC-2C8F288796-L001067](../../web/workspace.html#L1067) | 1067 | `" try{"` | — |
| [SRC-2C8F288796-L001068](../../web/workspace.html#L1068) | 1068 | `"  await api(\"/api/session\",{method:\"POST\",body:{access_token:token}});"` | — |
| [SRC-2C8F288796-L001069](../../web/workspace.html#L1069) | 1069 | `"  advanceWorkspaceSessionVersion();clearChatSession();"` | — |
| [SRC-2C8F288796-L001070](../../web/workspace.html#L1070) | 1070 | `"  $(\"accessToken\").value=\"\";await bootstrap();"` | — |
| [SRC-2C8F288796-L001071](../../web/workspace.html#L1071) | 1071 | `" }catch(e){$(\"authError\").textContent=escapeMessage(e.message)}"` | — |
| [SRC-2C8F288796-L001072](../../web/workspace.html#L1072) | 1072 | `" finally{button.disabled=false}"` | — |
| [SRC-2C8F288796-L001073](../../web/workspace.html#L1073) | 1073 | `"});"` | — |
| [SRC-2C8F288796-L001074](../../web/workspace.html#L1074) | 1074 | `"$(\"logoutButton\").addEventListener(\"click\",async()=>{"` | — |
| [SRC-2C8F288796-L001075](../../web/workspace.html#L1075) | 1075 | `" try{"` | — |
| [SRC-2C8F288796-L001076](../../web/workspace.html#L1076) | 1076 | `"  await api(\"/api/session/logout\",{method:\"POST\",body:{}});"` | — |
| [SRC-2C8F288796-L001077](../../web/workspace.html#L1077) | 1077 | `" }catch(e){"` | — |
| [SRC-2C8F288796-L001078](../../web/workspace.html#L1078) | 1078 | `"  alert(\"تعذر تسجيل الخروج من الخادم؛ لم يتم تغيير حالة الجلسة في الواجهة. \"+escapeMessage(e.message));"` | — |
| [SRC-2C8F288796-L001079](../../web/workspace.html#L1079) | 1079 | `"  return;"` | — |
| [SRC-2C8F288796-L001080](../../web/workspace.html#L1080) | 1080 | `" }"` | — |
| [SRC-2C8F288796-L001081](../../web/workspace.html#L1081) | 1081 | `" state.role=null;state.leads=[];state.profiles=[];state.discoveryRuns=[];state.loadWarnings=[];state.activeDiscovery=null;state.activeProfileId=null;state.activeView=\"overview\";showAuth(\"تم تسجيل الخروج. أدخل رمز الوصول للمتابعة.\");setConnection(false,\"غير متصل\",\"سجّل الدخول لعرض السجلات.\");"` | — |
| [SRC-2C8F288796-L001082](../../web/workspace.html#L1082) | 1082 | `"});"` | — |
| [SRC-2C8F288796-L001083](../../web/workspace.html#L1083) | 1083 | `"$(\"addSignalTop\").addEventListener(\"click\",()=>navigate(\"signals\"));"` | — |
| [SRC-2C8F288796-L001084](../../web/workspace.html#L1084) | 1084 | `"$(\"closeDetail\").addEventListener(\"click\",closeDetails);"` | — |
| [SRC-2C8F288796-L001085](../../web/workspace.html#L1085) | 1085 | `"$(\"chatNav\").addEventListener(\"click\",()=>navigate(\"chat\"));"` | — |
| [SRC-2C8F288796-L001086](../../web/workspace.html#L1086) | 1086 | `"$(\"systemNav\").addEventListener(\"click\",()=>navigate(\"system\"));"` | — |
| [SRC-2C8F288796-L001087](../../web/workspace.html#L1087) | 1087 | `"$(\"detailDrawer\").addEventListener(\"click\",e=>{if(e.target===$(\"detailDrawer\"))closeDetails()});"` | — |
| [SRC-2C8F288796-L001088](../../web/workspace.html#L1088) | 1088 | `"document.addEventListener(\"keydown\",e=>{if(e.key===\"Escape\")closeDetails()});"` | — |
| [SRC-2C8F288796-L001089](../../web/workspace.html#L1089) | 1089 | `"renderNav();bootstrap();"` | — |
| [SRC-2C8F288796-L001090](../../web/workspace.html#L1090) | 1090 | `"})();"` | — |
| [SRC-2C8F288796-L001091](../../web/workspace.html#L1091) | 1091 | `"</script>"` | — |
| [SRC-2C8F288796-L001092](../../web/workspace.html#L1092) | 1092 | `"</body>"` | — |
| [SRC-2C8F288796-L001093](../../web/workspace.html#L1093) | 1093 | `"</html>"` | — |
