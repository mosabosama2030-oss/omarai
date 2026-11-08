# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **065**
- سجلات الأسطر: **800**
- النطاق: SRC-DE7EABE998-L000461 إلى SRC-2C8F288796-L000665
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-DE7EABE998 — [web/agent.html](../../web/agent.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-2C8F288796-L000245](../../web/workspace.html#L245) | 245 | `".chat-sources{margin:6px 0 0;padding:0 18px;font-size:11px;line-height:1.9}.chat-sources a{color:var(--teal)}.chat-note{margin-top:8px;font-size:10px;color:var(--muted)}"` | — |
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
| [SRC-2C8F288796-L000331](../../web/workspace.html#L331) | 331 | `" const response=await fetch(path,{method:opts.method\|\|\"GET\",credentials:\"same-origin\",headers:headers,body:opts.body===undefined?undefined:JSON.stringify(opts.body)});"` | — |
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
| [SRC-2C8F288796-L000471](../../web/workspace.html#L471) | 471 | `" const panel=make(\"section\",\"glass panel\");const ph=make(\"div\",\"panel-head\");const ptitle=make(\"div\");ptitle.append(make(\"h2\",\"\",\"الإشارات المحفوظة\"),make(\"p\",\"\",\"بيانات من GET /api/leads، محمية بجلسة المستخدم وعزل مساحة العمل.\"));ph.append(ptitle,action(\"تحديث ↻\",\"ghost\",async()=>{await loadLeads();renderSignals()}));panel.append(ph);"` | — |
| [SRC-2C8F288796-L000472](../../web/workspace.html#L472) | 472 | `" if(canWrite())panel.append(createSignalForm());"` | — |
| [SRC-2C8F288796-L000473](../../web/workspace.html#L473) | 473 | `" const toolbar=make(\"div\",\"toolbar\");const search=make(\"input\",\"\");search.type=\"search\";search.placeholder=\"ابحث داخل نصوص الإشارات…\";search.value=state.search;search.setAttribute(\"aria-label\",\"البحث في الإشارات\");"` | — |
| [SRC-2C8F288796-L000474](../../web/workspace.html#L474) | 474 | `" search.addEventListener(\"input\",()=>{state.search=search.value;drawSignalRows(list)});"` | — |
| [SRC-2C8F288796-L000475](../../web/workspace.html#L475) | 475 | `" const filter=make(\"select\",\"\");filter.setAttribute(\"aria-label\",\"تصفية حسب الحالة\");const all=make(\"option\",\"\",\"كل الحالات\");all.value=\"all\";filter.append(all);"` | — |
| [SRC-2C8F288796-L000476](../../web/workspace.html#L476) | 476 | `" statuses.forEach(s=>{const o=make(\"option\",\"\",s.label);o.value=s.id;filter.append(o)});filter.value=state.filter;"` | — |
| [SRC-2C8F288796-L000477](../../web/workspace.html#L477) | 477 | `" filter.addEventListener(\"change\",()=>{state.filter=filter.value;drawSignalRows(list)});"` | — |
| [SRC-2C8F288796-L000478](../../web/workspace.html#L478) | 478 | `" toolbar.append(search,filter);panel.append(toolbar);"` | — |
| [SRC-2C8F288796-L000479](../../web/workspace.html#L479) | 479 | `" const list=make(\"div\",\"signal-list\");drawSignalRows(list);panel.append(list);"` | — |
| [SRC-2C8F288796-L000480](../../web/workspace.html#L480) | 480 | `" if(!canWrite())panel.append(make(\"p\",\"disclaimer\",\"دور المستخدم الحالي للقراءة فقط؛ لا يمكنه إضافة إشارات أو تغيير الحالات.\"));"` | — |
| [SRC-2C8F288796-L000481](../../web/workspace.html#L481) | 481 | `" root.append(panel);"` | — |
| [SRC-2C8F288796-L000482](../../web/workspace.html#L482) | 482 | `"}"` | — |
| [SRC-2C8F288796-L000483](../../web/workspace.html#L483) | 483 | `"function drawSignalRows(list){"` | — |
| [SRC-2C8F288796-L000484](../../web/workspace.html#L484) | 484 | `" list.replaceChildren();"` | — |
| [SRC-2C8F288796-L000485](../../web/workspace.html#L485) | 485 | `" const query=state.search.trim().toLocaleLowerCase();"` | — |
| [SRC-2C8F288796-L000486](../../web/workspace.html#L486) | 486 | `" const rows=state.leads.filter(l=>(state.filter===\"all\"\|\|l.status===state.filter)&&(!query\|\|String(l.text\|\|\"\").toLocaleLowerCase().includes(query)));"` | — |
| [SRC-2C8F288796-L000487](../../web/workspace.html#L487) | 487 | `" if(!rows.length)list.append(emptyState(\"لا توجد نتائج مطابقة\",\"غيّر مرشح الحالة أو عبارة البحث، أو أضف إشارة جديدة إن كانت صلاحيتك تسمح.\"));"` | — |
| [SRC-2C8F288796-L000488](../../web/workspace.html#L488) | 488 | `" else rows.forEach(l=>list.append(signalCard(l)));"` | — |
| [SRC-2C8F288796-L000489](../../web/workspace.html#L489) | 489 | `"}"` | — |
| [SRC-2C8F288796-L000490](../../web/workspace.html#L490) | 490 | `"function createSignalForm(){"` | — |
| [SRC-2C8F288796-L000491](../../web/workspace.html#L491) | 491 | `" const wrapper=make(\"section\",\"signal-card\");const head=make(\"div\",\"panel-head\");const title=make(\"div\");title.append(make(\"h2\",\"\",\"إضافة إشارة جديدة\"),make(\"p\",\"\",\"أدخل نصًا منشورًا ورابطه العام. التحليل محلي ولا يشغّل البحث الخارجي.\"));head.append(title);wrapper.append(head);"` | — |
| [SRC-2C8F288796-L000492](../../web/workspace.html#L492) | 492 | `" const text=make(\"textarea\",\"\");text.id=\"newSignalText\";text.placeholder=\"انسخ نص الطلب أو الاحتياج المعلن من المصدر المسموح…\";text.maxLength=20000;text.required=true;"` | — |
| [SRC-2C8F288796-L000493](../../web/workspace.html#L493) | 493 | `" const url=make(\"input\",\"\");url.type=\"url\";url.id=\"newSignalUrl\";url.placeholder=\"https://رابط-المصدر\";url.required=true;"` | — |
| [SRC-2C8F288796-L000494](../../web/workspace.html#L494) | 494 | `" const grid=make(\"div\",\"form-grid\");"` | — |
| [SRC-2C8F288796-L000495](../../web/workspace.html#L495) | 495 | `" const platform=make(\"select\",\"\");platform.id=\"newSignalPlatform\";[\"manual\",\"Facebook\",\"Website\",\"OLX\",\"Other\"].forEach(value=>{const o=make(\"option\",\"\",value===\"manual\"?\"إدخال يدوي\":value);o.value=value;platform.append(o)});"` | — |
| [SRC-2C8F288796-L000496](../../web/workspace.html#L496) | 496 | `" const product=make(\"input\",\"\");product.id=\"newSignalProduct\";product.placeholder=\"مثال: أنظمة إنذار، عقارات\";"` | — |
| [SRC-2C8F288796-L000497](../../web/workspace.html#L497) | 497 | `" const location=make(\"input\",\"\");location.id=\"newSignalLocation\";location.placeholder=\"مثال: القاهرة، التجمع الخامس\";"` | — |
| [SRC-2C8F288796-L000498](../../web/workspace.html#L498) | 498 | `" const note=make(\"input\",\"\");note.id=\"newSignalNote\";note.placeholder=\"ملاحظاتك (اختياري)\";"` | — |
| [SRC-2C8F288796-L000499](../../web/workspace.html#L499) | 499 | `" const fields=[[\"النص\",text],[\"رابط المصدر\",url],[\"المنصة\",platform],[\"مصطلحات المنتج (افصل بفاصلة)\",product],[\"السوق أو المنطقة\",location],[\"ملاحظة\",note]];"` | — |
| [SRC-2C8F288796-L000500](../../web/workspace.html#L500) | 500 | `" fields.forEach(([label,input])=>{const field=make(\"div\",\"field\");field.append(make(\"label\",\"\",label));field.lastChild.htmlFor=input.id;field.append(input);grid.append(field)});"` | — |
| [SRC-2C8F288796-L000501](../../web/workspace.html#L501) | 501 | `" wrapper.append(grid);"` | — |
| [SRC-2C8F288796-L000502](../../web/workspace.html#L502) | 502 | `" const result=make(\"div\",\"\");result.id=\"analysisResult\";"` | — |
| [SRC-2C8F288796-L000503](../../web/workspace.html#L503) | 503 | `" const buttons=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000504](../../web/workspace.html#L504) | 504 | `" const analyze=action(\"١. حلّل الإشارة\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000505](../../web/workspace.html#L505) | 505 | `"  analyze.disabled=true;"` | — |
| [SRC-2C8F288796-L000506](../../web/workspace.html#L506) | 506 | `"  try{"` | — |
| [SRC-2C8F288796-L000507](../../web/workspace.html#L507) | 507 | `"   if(!text.value.trim())throw new Error(\"أدخل نص الإشارة أولًا.\");"` | — |
| [SRC-2C8F288796-L000508](../../web/workspace.html#L508) | 508 | `"   if(!safeHttp(url.value))throw new Error(\"أدخل رابط مصدر عام صالحًا يبدأ بـ HTTP أو HTTPS.\");"` | — |
| [SRC-2C8F288796-L000509](../../web/workspace.html#L509) | 509 | `"   const product_terms=product.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000510](../../web/workspace.html#L510) | 510 | `"   const location_terms=location.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000511](../../web/workspace.html#L511) | 511 | `"   const data=await api(\"/api/analyze\",{method:\"POST\",body:{text:text.value,product_terms:product_terms,location_terms:location_terms}});"` | — |
| [SRC-2C8F288796-L000512](../../web/workspace.html#L512) | 512 | `"   state.analysis={text:text.value,url:url.value,product_terms:product_terms,location_terms:location_terms,assessment:data};"` | — |
| [SRC-2C8F288796-L000513](../../web/workspace.html#L513) | 513 | `"   result.replaceChildren();"` | — |
| [SRC-2C8F288796-L000514](../../web/workspace.html#L514) | 514 | `"   const box=make(\"div\",\"analysis-result\");box.append(make(\"div\",\"analysis-score\",String(data.score??\"—\")+\"/100\"),make(\"div\",\"\",labels[data.label]\|\|data.label\|\|\"غير مصنفة\"),make(\"p\",\"\",data.summary\|\|\"لا يوجد ملخص.\"));"` | — |
| [SRC-2C8F288796-L000515](../../web/workspace.html#L515) | 515 | `"   box.append(make(\"p\",\"disclaimer\",\"هذه درجة قواعد إرشادية لا تمثل احتمال شراء. راجع النص والمصدر قبل اعتماد الإشارة.\"));"` | — |
| [SRC-2C8F288796-L000516](../../web/workspace.html#L516) | 516 | `"   result.append(box);"` | — |
| [SRC-2C8F288796-L000517](../../web/workspace.html#L517) | 517 | `"  }catch(e){result.replaceChildren(make(\"p\",\"auth-error\",escapeMessage(e.message)))}"` | — |
| [SRC-2C8F288796-L000518](../../web/workspace.html#L518) | 518 | `"  finally{analyze.disabled=false}"` | — |
| [SRC-2C8F288796-L000519](../../web/workspace.html#L519) | 519 | `" });"` | — |
| [SRC-2C8F288796-L000520](../../web/workspace.html#L520) | 520 | `" const save=action(\"٢. احفظ الإشارة\",\"\",async()=>{"` | — |
| [SRC-2C8F288796-L000521](../../web/workspace.html#L521) | 521 | `"  save.disabled=true;"` | — |
| [SRC-2C8F288796-L000522](../../web/workspace.html#L522) | 522 | `"  try{"` | — |
| [SRC-2C8F288796-L000523](../../web/workspace.html#L523) | 523 | `"   const item=state.analysis;"` | — |
| [SRC-2C8F288796-L000524](../../web/workspace.html#L524) | 524 | `"   if(!item\|\|item.text!==text.value\|\|item.url!==url.value)throw new Error(\"أعد التحليل بعد أي تغيير في النص أو رابط المصدر.\");"` | — |
| [SRC-2C8F288796-L000525](../../web/workspace.html#L525) | 525 | `"   if(!safeHttp(url.value))throw new Error(\"رابط المصدر غير صالح.\");"` | — |
| [SRC-2C8F288796-L000526](../../web/workspace.html#L526) | 526 | `"   const product_terms=product.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000527](../../web/workspace.html#L527) | 527 | `"   const location_terms=location.value.split(\",\").map(x=>x.trim()).filter(Boolean);"` | — |
| [SRC-2C8F288796-L000528](../../web/workspace.html#L528) | 528 | `"   if(JSON.stringify(product_terms)!==JSON.stringify(item.product_terms)\|\|JSON.stringify(location_terms)!==JSON.stringify(item.location_terms))throw new Error(\"تغيرت مصطلحات المنتج أو المنطقة؛ أعد التحليل.\");"` | — |
| [SRC-2C8F288796-L000529](../../web/workspace.html#L529) | 529 | `"   const response=await api(\"/api/leads\",{method:\"POST\",body:{text:text.value,source_url:url.value,platform:platform.value,note:note.value,product_terms:product_terms,location_terms:location_terms}});"` | — |
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
