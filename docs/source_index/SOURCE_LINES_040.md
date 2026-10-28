# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **040**
- سجلات الأسطر: **3**
- النطاق: SRC-A16FA6D4B5-L000044 إلى SRC-A16FA6D4B5-L000046
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-A16FA6D4B5 — [web/dashboard.html](../../web/dashboard.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A16FA6D4B5-L000044](../../web/dashboard.html#L44) | 44 | `"$(\"leadlist\").addEventListener(\"click\",event=>{const button=event.target.closest('button[data-action=\"save-status\"]');if(!button)return;const id=button.dataset.leadId;if(!/^\\d+$/.test(id\|\|\"\"))return;void window.saveStatus(id)});"` | — |
| [SRC-A16FA6D4B5-L000045](../../web/dashboard.html#L45) | 45 | `"$(\"refresh\").onclick=refresh;$(\"askBtn\").onclick=askOmarai;$(\"askInput\").addEventListener(\"keydown\",e=>{if(e.key===\"Enter\"){e.preventDefault();askOmarai()}});async function askOmarai(){const question=$(\"askInput\").value.trim();if(!question)return;const box=$(\"askMessages\");const user=document.createElement(\"div\");user.className=\"lead\";user.style.borderColor=\"#2e5b62\";user.textContent=\"أنت: \"+question;box.appendChild(user);$(\"askInput\").value=\"\";$(\"askBtn\").disabled=true;try{const result=await request(\"/api/ask\",{method:\"POST\",body:JSON.stringify({question})});const answer=document.createElement(\"div\");answer.className=\"lead\";answer.textContent=\"Omarai: \"+result.answer;box.appendChild(answer)}catch(e){const answer=document.createElement(\"div\");answer.className=\"lead\";answer.textContent=\"تعذر تنفيذ السؤال: \"+e.message;box.appendChild(answer)}finally{$(\"askBtn\").disabled=false;box.scrollTop=box.scrollHeight}}refresh();"` | — |
| [SRC-A16FA6D4B5-L000046](../../web/dashboard.html#L46) | 46 | `"</script></body></html>"` | — |
