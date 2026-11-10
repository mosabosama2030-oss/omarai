# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **067**
- سجلات الأسطر: **43**
- النطاق: SRC-2C8F288796-L000980 إلى SRC-2C8F288796-L001022
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
