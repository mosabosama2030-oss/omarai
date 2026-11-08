# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **066**
- سجلات الأسطر: **160**
- النطاق: SRC-2C8F288796-L000863 إلى SRC-2C8F288796-L001022
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
