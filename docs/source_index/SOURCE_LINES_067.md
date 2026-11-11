# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **067**
- سجلات الأسطر: **314**
- النطاق: SRC-2C8F288796-L000780 إلى SRC-2C8F288796-L001093
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-2C8F288796-L000850](../../web/workspace.html#L850) | 850 | `"   status.className=\"profile-note\";status.textContent=\"جارٍ البحث عن إشارات الطلب؛ ستظل النتائج السابقة متاحة حتى تكتمل الجولة الجديدة.\";"` | — |
| [SRC-2C8F288796-L000851](../../web/workspace.html#L851) | 851 | `"   try{"` | — |
| [SRC-2C8F288796-L000852](../../web/workspace.html#L852) | 852 | `"    const savedRun=await api(\"/api/discoveries\",{method:\"POST\",body:{profile_id:profileSelect.value,allow_optional_providers:optional.checked}});"` | — |
| [SRC-2C8F288796-L000853](../../web/workspace.html#L853) | 853 | `"    state.activeDiscovery=savedRun;"` | — |
| [SRC-2C8F288796-L000854](../../web/workspace.html#L854) | 854 | `"    let refreshWarning=\"\";"` | — |
| [SRC-2C8F288796-L000855](../../web/workspace.html#L855) | 855 | `"    try{await loadDiscoveryRuns()}catch(refreshError){refreshWarning=\" حُفظت نتيجة البحث، لكن تعذر تحديث سجل العمليات: \"+escapeMessage(refreshError.message)}"` | — |
| [SRC-2C8F288796-L000856](../../web/workspace.html#L856) | 856 | `"    renderDiscovery();"` | — |
| [SRC-2C8F288796-L000857](../../web/workspace.html#L857) | 857 | `"    if(refreshWarning){const warning=make(\"p\",\"auth-error\",refreshWarning);warning.setAttribute(\"role\",\"alert\");$(\"viewRoot\").append(warning)}"` | — |
| [SRC-2C8F288796-L000858](../../web/workspace.html#L858) | 858 | `"   }catch(error){"` | — |
| [SRC-2C8F288796-L000859](../../web/workspace.html#L859) | 859 | `"    status.className=\"auth-error\";status.textContent=\"تعذر تشغيل الاكتشاف: \"+escapeMessage(error.message)+\" يمكنك المحاولة مجددًا. لم تُحذف النتائج السابقة.\";"` | — |
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
