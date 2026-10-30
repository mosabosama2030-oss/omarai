# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **051**
- سجلات الأسطر: **7**
- النطاق: SRC-A16FA6D4B5-L000040 إلى SRC-A16FA6D4B5-L000046
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-A16FA6D4B5 — [web/dashboard.html](../../web/dashboard.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A16FA6D4B5-L000040](../../web/dashboard.html#L40) | 40 | `"async function refresh(){try{const d=await request(\"/api/leads?limit=500\");const rows=d.leads;$(\"total\").textContent=rows.length;$(\"qualified\").textContent=rows.filter(x=>[\"qualified\",\"contacted\",\"converted\"].includes(x.status)).length;$(\"review\").textContent=rows.filter(x=>x.status===\"needs_review\").length;if(!rows.length){$(\"leadlist\").innerHTML='<div class=\"empty\">لا توجد إشارات محفوظة بعد. ابدأ بتحليل إشارة ثم احفظها.</div>';return}$(\"leadlist\").innerHTML=rows.map(l=>{const sourceUrl=safeSourceUrl(l.source_url);const sourceLink=sourceUrl?'<a target=\"_blank\" rel=\"noopener noreferrer\" href=\"'+esc(sourceUrl)+'\" style=\"color:#7b9cff\">فتح الرابط</a>':'<span class=\"muted\">لا يوجد رابط HTTP(S) صالح</span>';return '<article class=\"lead\"><div class=\"leadhead\"><span class=\"pill\">'+esc(labels[l.assessment.label]\|\|l.assessment.label)+'</span><span class=\"muted\">'+esc(l.platform)+' · '+esc(l.observed_at)+'</span></div><p>'+esc(l.text)+'</p><div class=\"muted\">المصدر: '+sourceLink+' · الدرجة '+l.assessment.score+'</div><div class=\"row\" style=\"margin-top:10px\"><select aria-label=\"حالة المتابعة\" id=\"status-'+esc(l.id)+'\">'+[\"new\",\"qualified\",\"contacted\",\"converted\",\"rejected\",\"needs_review\"].map(s=>'<option value=\"'+s+'\" '+(s===l.status?\"selected\":\"\")+'>'+({new:\"جديد\",qualified:\"مؤهل\",contacted:\"تم التواصل\",converted:\"تحوّل لعميل\",rejected:\"مرفوض\",needs_review:\"مراجعة\"}[s])+'</option>').join(\"\")+'</select><button class=\"secondary\" data-action=\"save-status\" data-lead-id=\"'+esc(l.id)+'\">تحديث الحالة</button></div></article>'}).join(\"\")}catch(e){$(\"leadlist\").innerHTML='<div class=\"empty\">'+esc(e.message)+'</div>'}}"` | — |
| [SRC-A16FA6D4B5-L000041](../../web/dashboard.html#L41) | 41 | `"$(\"accessToken\").value=localStorage.getItem(ACCESS_TOKEN_STORAGE_KEY)\|\|\"\";"` | — |
| [SRC-A16FA6D4B5-L000042](../../web/dashboard.html#L42) | 42 | `"$(\"saveAccessToken\").onclick=async()=>{const token=$(\"accessToken\").value.trim();if(token)localStorage.setItem(ACCESS_TOKEN_STORAGE_KEY,token);else localStorage.removeItem(ACCESS_TOKEN_STORAGE_KEY);$(\"authMessage\").textContent=token?\"تم حفظ الرمز في هذا المتصفح؛ لن تتم طباعته أو عرضه في السجل.\":\"تم مسح الرمز المحفوظ من هذا المتصفح.\";await refresh()};"` | — |
| [SRC-A16FA6D4B5-L000043](../../web/dashboard.html#L43) | 43 | `"window.saveStatus=async id=>{try{const status=$(\"status-\"+id).value;await request(\"/api/leads/\"+id+\"/status\",{method:\"POST\",body:JSON.stringify({status})});await refresh()}catch(e){alert(e.message)}};"` | — |
| [SRC-A16FA6D4B5-L000044](../../web/dashboard.html#L44) | 44 | `"$(\"leadlist\").addEventListener(\"click\",event=>{const button=event.target.closest('button[data-action=\"save-status\"]');if(!button)return;const id=button.dataset.leadId;if(!/^\\d+$/.test(id\|\|\"\"))return;void window.saveStatus(id)});"` | — |
| [SRC-A16FA6D4B5-L000045](../../web/dashboard.html#L45) | 45 | `"$(\"refresh\").onclick=refresh;$(\"askBtn\").onclick=askOmarai;$(\"askInput\").addEventListener(\"keydown\",e=>{if(e.key===\"Enter\"){e.preventDefault();askOmarai()}});async function askOmarai(){const question=$(\"askInput\").value.trim();if(!question)return;const box=$(\"askMessages\");const user=document.createElement(\"div\");user.className=\"lead\";user.style.borderColor=\"#2e5b62\";user.textContent=\"أنت: \"+question;box.appendChild(user);$(\"askInput\").value=\"\";$(\"askBtn\").disabled=true;try{const result=await request(\"/api/ask\",{method:\"POST\",body:JSON.stringify({question})});const answer=document.createElement(\"div\");answer.className=\"lead\";answer.textContent=\"Omarai: \"+result.answer;box.appendChild(answer)}catch(e){const answer=document.createElement(\"div\");answer.className=\"lead\";answer.textContent=\"تعذر تنفيذ السؤال: \"+e.message;box.appendChild(answer)}finally{$(\"askBtn\").disabled=false;box.scrollTop=box.scrollHeight}}refresh();"` | — |
| [SRC-A16FA6D4B5-L000046](../../web/dashboard.html#L46) | 46 | `"</script></body></html>"` | — |
