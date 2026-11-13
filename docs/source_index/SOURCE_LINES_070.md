# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **070**
- سجلات الأسطر: **65**
- النطاق: SRC-2C8F288796-L001029 إلى SRC-2C8F288796-L001093
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
