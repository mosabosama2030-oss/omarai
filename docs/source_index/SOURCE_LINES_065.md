# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **065**
- سجلات الأسطر: **232**
- النطاق: SRC-2C8F288796-L000676 إلى SRC-2C8F288796-L000907
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-2C8F288796 — [web/workspace.html](../../web/workspace.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2C8F288796-L000676](../../web/workspace.html#L676) | 676 | `" });"` | — |
| [SRC-2C8F288796-L000677](../../web/workspace.html#L677) | 677 | `" const localeField=make(\"div\",\"field\"),locale=make(\"select\",\"\");"` | — |
| [SRC-2C8F288796-L000678](../../web/workspace.html#L678) | 678 | `" [[\"auto\",\"تلقائي\"],[\"ar\",\"العربية\"],[\"en\",\"الإنجليزية\"],[\"mixed\",\"العربية والإنجليزية\"]].forEach(([v,l])=>{const o=make(\"option\",\"\",l);o.value=v;locale.append(o)});"` | — |
| [SRC-2C8F288796-L000679](../../web/workspace.html#L679) | 679 | `" localeField.append(make(\"label\",\"\",\"لغة البحث\"),locale);controls.locale=locale;if(!canWrite())locale.disabled=true;grid.append(localeField);"` | — |
| [SRC-2C8F288796-L000680](../../web/workspace.html#L680) | 680 | `" panel.append(grid,make(\"p\",\"profile-note\",\"افصل القيم المتعددة بفاصلة. تُستخدم المرادفات والمناطق لصياغة استعلامات مرتبطة بالمنتج؛ تطابق ICP وحده لا يثبت وجود طلب.\"));"` | — |
| [SRC-2C8F288796-L000681](../../web/workspace.html#L681) | 681 | `" const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000682](../../web/workspace.html#L682) | 682 | `" const save=action(\"حفظ ملف المنتج والسوق\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000683](../../web/workspace.html#L683) | 683 | `"  save.disabled=true;"` | — |
| [SRC-2C8F288796-L000684](../../web/workspace.html#L684) | 684 | `"  try{"` | — |
| [SRC-2C8F288796-L000685](../../web/workspace.html#L685) | 685 | `"   const payload={"` | — |
| [SRC-2C8F288796-L000686](../../web/workspace.html#L686) | 686 | `"    product:{name:controls.name.value,aliases:csvValues(controls.aliases.value),category_path:csvValues(controls.category.value),use_cases:csvValues(controls.useCases.value),problems_solved:csvValues(controls.problems.value)},"` | — |
| [SRC-2C8F288796-L000687](../../web/workspace.html#L687) | 687 | `"    market:{locations:csvValues(controls.locations.value),industries:csvValues(controls.industries.value),customer_types:csvValues(controls.customers.value),decision_roles:csvValues(controls.roles.value),exclusions:csvValues(controls.exclusions.value)},"` | — |
| [SRC-2C8F288796-L000688](../../web/workspace.html#L688) | 688 | `"    locale:controls.locale.value"` | — |
| [SRC-2C8F288796-L000689](../../web/workspace.html#L689) | 689 | `"   };"` | — |
| [SRC-2C8F288796-L000690](../../web/workspace.html#L690) | 690 | `"   const result=await api(\"/api/product-profiles\",{method:\"POST\",body:payload});"` | — |
| [SRC-2C8F288796-L000691](../../web/workspace.html#L691) | 691 | `"   state.activeProfileId=result.id;await loadProductProfiles();renderProductProfile();"` | — |
| [SRC-2C8F288796-L000692](../../web/workspace.html#L692) | 692 | `"  }catch(error){panel.append(make(\"p\",\"auth-error\",escapeMessage(error.message)))}"` | — |
| [SRC-2C8F288796-L000693](../../web/workspace.html#L693) | 693 | `"  finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000694](../../web/workspace.html#L694) | 694 | `" });"` | — |
| [SRC-2C8F288796-L000695](../../web/workspace.html#L695) | 695 | `" save.disabled=!canWrite();actions.append(save);panel.append(actions);root.append(panel);"` | — |
| [SRC-2C8F288796-L000696](../../web/workspace.html#L696) | 696 | `" const listPanel=make(\"section\",\"glass panel profile-panel\"),lh=make(\"div\",\"panel-head\"),lt=make(\"div\");"` | — |
| [SRC-2C8F288796-L000697](../../web/workspace.html#L697) | 697 | `" lt.append(make(\"h2\",\"\",\"ملفات المنتجات المحفوظة\"),make(\"p\",\"\",\"اختر ملفًا محفوظًا للانتقال إلى تشغيل الاكتشاف.\"));"` | — |
| [SRC-2C8F288796-L000698](../../web/workspace.html#L698) | 698 | `" lh.append(lt);listPanel.append(lh);"` | — |
| [SRC-2C8F288796-L000699](../../web/workspace.html#L699) | 699 | `" if(!state.profiles.length)listPanel.append(emptyState(\"لا توجد ملفات بعد\",\"أنشئ ملف المنتج والسوق ثم احفظه.\"));"` | — |
| [SRC-2C8F288796-L000700](../../web/workspace.html#L700) | 700 | `" else{"` | — |
| [SRC-2C8F288796-L000701](../../web/workspace.html#L701) | 701 | `"  const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000702](../../web/workspace.html#L702) | 702 | `"  state.profiles.forEach(profile=>{"` | — |
| [SRC-2C8F288796-L000703](../../web/workspace.html#L703) | 703 | `"   const card=make(\"article\",\"signal-card\"),p=profile.profile\|\|{},m=p.market\|\|{};"` | — |
| [SRC-2C8F288796-L000704](../../web/workspace.html#L704) | 704 | `"   card.append(make(\"strong\",\"\",profile.name\|\|\"منتج\"));"` | — |
| [SRC-2C8F288796-L000705](../../web/workspace.html#L705) | 705 | `"   card.append(make(\"p\",\"subtle\",\"المناطق: \"+((m.locations\|\|[]).join(\"، \")\|\|\"غير محددة\")));"` | — |
| [SRC-2C8F288796-L000706](../../web/workspace.html#L706) | 706 | `"   const row=make(\"div\",\"form-actions\");row.append(action(\"استخدام في الاكتشاف\",\"\",()=>{state.activeProfileId=profile.id;navigate(\"campaign\")}));"` | — |
| [SRC-2C8F288796-L000707](../../web/workspace.html#L707) | 707 | `"   card.append(row);list.append(card);"` | — |
| [SRC-2C8F288796-L000708](../../web/workspace.html#L708) | 708 | `"  });listPanel.append(list);"` | — |
| [SRC-2C8F288796-L000709](../../web/workspace.html#L709) | 709 | `" }"` | — |
| [SRC-2C8F288796-L000710](../../web/workspace.html#L710) | 710 | `" root.append(listPanel);"` | — |
| [SRC-2C8F288796-L000711](../../web/workspace.html#L711) | 711 | `"}"` | — |
| [SRC-2C8F288796-L000712](../../web/workspace.html#L712) | 712 | `"function renderDiscoveryRun(run){"` | — |
| [SRC-2C8F288796-L000713](../../web/workspace.html#L713) | 713 | `" const panel=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000714](../../web/workspace.html#L714) | 714 | `" const report=run.search_report\|\|{},leadReport=report.lead_generation\|\|{},sources=Array.isArray(run.sources)?run.sources:[];"` | — |
| [SRC-2C8F288796-L000715](../../web/workspace.html#L715) | 715 | `" title.append(make(\"h2\",\"\",\"نتيجة عملية الاكتشاف\"),make(\"p\",\"\",\"ملف المنتج: \"+String(run.profile_name\|\|\"غير محدد\")+\" · \"+String(run.created_at\|\|\"\")));"` | — |
| [SRC-2C8F288796-L000716](../../web/workspace.html#L716) | 716 | `" head.append(title);panel.append(head);"` | — |
| [SRC-2C8F288796-L000717](../../web/workspace.html#L717) | 717 | `" const stats=make(\"div\",\"stats\"),qualifiedCount=sources.filter(s=>s.lead_qualification===\"public_demand_signal\").length;"` | — |
| [SRC-2C8F288796-L000718](../../web/workspace.html#L718) | 718 | `" stats.append("` | — |
| [SRC-2C8F288796-L000719](../../web/workspace.html#L719) | 719 | `"  buildStat(\"إشارات طلب مؤهلة\",leadReport.candidate_signal_count??qualifiedCount,\"إشارات تحمل عبارة طلب معلنة\",\"glow-teal\"),"` | — |
| [SRC-2C8F288796-L000720](../../web/workspace.html#L720) | 720 | `"  buildStat(\"المصادر التي راجعتها الجولة\",leadReport.related_results_reviewed??sources.length,\"لا يعني ذلك اكتمال السوق\",\"glow-blue\"),"` | — |
| [SRC-2C8F288796-L000721](../../web/workspace.html#L721) | 721 | `"  buildStat(\"حالة تشغيل البحث\",report.pipeline_completion_status\|\|\"غير معلومة\",\"حالة المسار كما أعادها الوكيل\",\"glow-amber\")"` | — |
| [SRC-2C8F288796-L000722](../../web/workspace.html#L722) | 722 | `" );"` | — |
| [SRC-2C8F288796-L000723](../../web/workspace.html#L723) | 723 | `" panel.append(stats,make(\"p\",\"profile-note\",run.answer\|\|\"لا يوجد ملخص لهذه العملية.\"));"` | — |
| [SRC-2C8F288796-L000724](../../web/workspace.html#L724) | 724 | `" if(Array.isArray(run.search_queries)&&run.search_queries.length){const qs=make(\"div\",\"query-list\");run.search_queries.forEach(q=>qs.append(tag(q)));panel.append(qs)}"` | — |
| [SRC-2C8F288796-L000725](../../web/workspace.html#L725) | 725 | `" const list=make(\"div\",\"signal-list\");"` | — |
| [SRC-2C8F288796-L000726](../../web/workspace.html#L726) | 726 | `" if(!sources.length)list.append(emptyState(\"لم تُعد العملية مصادر قابلة للعرض\",\"راجع حالة التشغيل والتحذيرات؛ هذا لا يثبت عدم وجود طلب.\"));"` | — |
| [SRC-2C8F288796-L000727](../../web/workspace.html#L727) | 727 | `" sources.forEach((source,index)=>{"` | — |
| [SRC-2C8F288796-L000728](../../web/workspace.html#L728) | 728 | `"  const qualified=source.lead_qualification===\"public_demand_signal\";"` | — |
| [SRC-2C8F288796-L000729](../../web/workspace.html#L729) | 729 | `"  const card=make(\"article\",\"discovery-source\"+(qualified?\" qualified\":\"\")),meta=make(\"div\",\"discovery-source-meta\");"` | — |
| [SRC-2C8F288796-L000730](../../web/workspace.html#L730) | 730 | `"  meta.append(tag(qualified?\"إشارة طلب معلنة\":\"نتيجة مرتبطة فقط\",qualified?\"teal\":\"\"));"` | — |
| [SRC-2C8F288796-L000731](../../web/workspace.html#L731) | 731 | `"  if(source.platform)meta.append(tag(source.platform));"` | — |
| [SRC-2C8F288796-L000732](../../web/workspace.html#L732) | 732 | `"  meta.append(tag(source.page_fetched?\"تمت قراءة الصفحة\":\"مقتطف/عنوان فقط\"));"` | — |
| [SRC-2C8F288796-L000733](../../web/workspace.html#L733) | 733 | `"  card.append(meta,make(\"h3\",\"\",source.title\|\|\"نتيجة ويب\"));"` | — |
| [SRC-2C8F288796-L000734](../../web/workspace.html#L734) | 734 | `"  if(source.snippet)card.append(make(\"p\",\"\",source.snippet));"` | — |
| [SRC-2C8F288796-L000735](../../web/workspace.html#L735) | 735 | `"  const evidence=source.lead_intent_evidence;"` | — |
| [SRC-2C8F288796-L000736](../../web/workspace.html#L736) | 736 | `"  if(qualified&&evidence){"` | — |
| [SRC-2C8F288796-L000737](../../web/workspace.html#L737) | 737 | `"   card.append(make(\"p\",\"\",\"عبارة الدليل: \"+String(evidence.phrase\|\|\"غير محددة\")));"` | — |
| [SRC-2C8F288796-L000738](../../web/workspace.html#L738) | 738 | `"   card.append(make(\"p\",\"\",\"نوع الإشارة: \"+String(evidence.signal_type\|\|\"غير محدد\")+\" · أساس النص: \"+String(evidence.basis\|\|\"غير محدد\")));"` | — |
| [SRC-2C8F288796-L000739](../../web/workspace.html#L739) | 739 | `"   card.append(make(\"p\",\"discovery-note\",\"ملاءمة المنتج لم تُحسم من العبارة وحدها؛ راجع المصدر قبل اعتماد الفرصة.\"));"` | — |
| [SRC-2C8F288796-L000740](../../web/workspace.html#L740) | 740 | `"  }else card.append(make(\"p\",\"discovery-note\",\"لم يعثر المحرك على عبارة كافية تثبت طلب شراء. لن تُحفظ هذه النتيجة كإشارة طلب من هذه الشاشة.\"));"` | — |
| [SRC-2C8F288796-L000741](../../web/workspace.html#L741) | 741 | `"  card.append(make(\"p\",\"discovery-note\",\"تاريخ النشر: \"+String(source.published_at\|\|\"غير متاح من المصدر\")));"` | — |
| [SRC-2C8F288796-L000742](../../web/workspace.html#L742) | 742 | `"  const url=safeHttp(source.url);if(url){const link=make(\"a\",\"\",url);link.href=url;link.target=\"_blank\";link.rel=\"noopener noreferrer\";card.append(link)}"` | — |
| [SRC-2C8F288796-L000743](../../web/workspace.html#L743) | 743 | `"  if(qualified&&canWrite()){"` | — |
| [SRC-2C8F288796-L000744](../../web/workspace.html#L744) | 744 | `"   const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000745](../../web/workspace.html#L745) | 745 | `"   const save=action(\"حفظ الإشارة في صندوق الطلب\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000746](../../web/workspace.html#L746) | 746 | `"    save.disabled=true;"` | — |
| [SRC-2C8F288796-L000747](../../web/workspace.html#L747) | 747 | `"    try{"` | — |
| [SRC-2C8F288796-L000748](../../web/workspace.html#L748) | 748 | `"     const response=await api(\"/api/discoveries/\"+encodeURIComponent(run.id)+\"/signals/\"+index+\"/save\",{method:\"POST\",body:{}});"` | — |
| [SRC-2C8F288796-L000749](../../web/workspace.html#L749) | 749 | `"     save.textContent=response.created?\"تم الحفظ\":\"الإشارة موجودة بالفعل\";"` | — |
| [SRC-2C8F288796-L000750](../../web/workspace.html#L750) | 750 | `"     await loadLeads();"` | — |
| [SRC-2C8F288796-L000751](../../web/workspace.html#L751) | 751 | `"    }catch(error){card.append(make(\"p\",\"auth-error\",escapeMessage(error.message)))}"` | — |
| [SRC-2C8F288796-L000752](../../web/workspace.html#L752) | 752 | `"    finally{save.disabled=false}"` | — |
| [SRC-2C8F288796-L000753](../../web/workspace.html#L753) | 753 | `"   });"` | — |
| [SRC-2C8F288796-L000754](../../web/workspace.html#L754) | 754 | `"   actions.append(save);card.append(actions);"` | — |
| [SRC-2C8F288796-L000755](../../web/workspace.html#L755) | 755 | `"  }"` | — |
| [SRC-2C8F288796-L000756](../../web/workspace.html#L756) | 756 | `"  list.append(card);"` | — |
| [SRC-2C8F288796-L000757](../../web/workspace.html#L757) | 757 | `" });"` | — |
| [SRC-2C8F288796-L000758](../../web/workspace.html#L758) | 758 | `" panel.append(list);return panel;"` | — |
| [SRC-2C8F288796-L000759](../../web/workspace.html#L759) | 759 | `"}"` | — |
| [SRC-2C8F288796-L000760](../../web/workspace.html#L760) | 760 | `"function renderDiscovery(){"` | — |
| [SRC-2C8F288796-L000761](../../web/workspace.html#L761) | 761 | `" setPage(\"حملات الاكتشاف\",\"ابحث عن إشارات طلب شراء أو توريد معلنة مرتبطة بملف المنتج والسوق. لا تُعرض النتائج العامة كعملاء محتملين.\",\"BUYER INTENT DISCOVERY\");"` | — |
| [SRC-2C8F288796-L000762](../../web/workspace.html#L762) | 762 | `" const root=$(\"viewRoot\");root.replaceChildren();"` | — |
| [SRC-2C8F288796-L000763](../../web/workspace.html#L763) | 763 | `" const controls=make(\"section\",\"glass panel profile-panel\"),head=make(\"div\",\"panel-head\"),title=make(\"div\");"` | — |
| [SRC-2C8F288796-L000764](../../web/workspace.html#L764) | 764 | `" title.append(make(\"h2\",\"\",\"تشغيل اكتشاف جديد\"),make(\"p\",\"\",\"يستخدم محرك البحث الحالي ويولّد الاستعلامات من ملف المنتج المحفوظ.\"));"` | — |
| [SRC-2C8F288796-L000765](../../web/workspace.html#L765) | 765 | `" head.append(title);controls.append(head);"` | — |
| [SRC-2C8F288796-L000766](../../web/workspace.html#L766) | 766 | `" if(!state.profiles.length){"` | — |
| [SRC-2C8F288796-L000767](../../web/workspace.html#L767) | 767 | `"  controls.append(emptyState(\"لا يوجد ملف منتج محفوظ\",\"أنشئ ملف المنتج والسوق قبل تشغيل الاكتشاف.\"));"` | — |
| [SRC-2C8F288796-L000768](../../web/workspace.html#L768) | 768 | `"  controls.append(action(\"إنشاء ملف المنتج ←\",\"primary\",()=>navigate(\"offer\")));"` | — |
| [SRC-2C8F288796-L000769](../../web/workspace.html#L769) | 769 | `" }else{"` | — |
| [SRC-2C8F288796-L000770](../../web/workspace.html#L770) | 770 | `"  const field=make(\"div\",\"field\"),profileSelect=make(\"select\",\"\");"` | — |
| [SRC-2C8F288796-L000771](../../web/workspace.html#L771) | 771 | `"  state.profiles.forEach(profile=>{const option=make(\"option\",\"\",profile.name);option.value=profile.id;option.selected=profile.id===state.activeProfileId;profileSelect.append(option)});"` | — |
| [SRC-2C8F288796-L000772](../../web/workspace.html#L772) | 772 | `"  field.append(make(\"label\",\"\",\"ملف المنتج والسوق\"),profileSelect);controls.append(field);"` | — |
| [SRC-2C8F288796-L000773](../../web/workspace.html#L773) | 773 | `"  const consent=make(\"label\",\"consent-row\"),optional=make(\"input\",\"\");optional.type=\"checkbox\";optional.checked=false;optional.disabled=state.role!==\"owner\";"` | — |
| [SRC-2C8F288796-L000774](../../web/workspace.html#L774) | 774 | `"  consent.append(optional,make(\"span\",\"\",\"السماح بالموصلات الاختيارية (DeepSeek Search وBrave وTavily وبعض واجهات المنصات الرسمية). قد تستهلك حصصًا أو تكلفة؛ تبقى معطلة افتراضيًا ولا يستطيع تفعيلها إلا مالك مساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000775](../../web/workspace.html#L775) | 775 | `"  controls.append(consent);"` | — |
| [SRC-2C8F288796-L000776](../../web/workspace.html#L776) | 776 | `"  const actions=make(\"div\",\"form-actions\");"` | — |
| [SRC-2C8F288796-L000777](../../web/workspace.html#L777) | 777 | `"  const status=make(\"p\",\"profile-note\");status.setAttribute(\"role\",\"status\");status.setAttribute(\"aria-live\",\"polite\");"` | — |
| [SRC-2C8F288796-L000778](../../web/workspace.html#L778) | 778 | `"  const run=action(\"بدء اكتشاف الطلب\",\"primary\",async()=>{"` | — |
| [SRC-2C8F288796-L000779](../../web/workspace.html#L779) | 779 | `"   run.disabled=true;run.setAttribute(\"aria-busy\",\"true\");state.activeProfileId=profileSelect.value;"` | — |
| [SRC-2C8F288796-L000780](../../web/workspace.html#L780) | 780 | `"   status.className=\"profile-note\";status.textContent=\"جارٍ البحث عن إشارات الطلب؛ ستظل النتائج السابقة متاحة حتى تكتمل الجولة الجديدة.\";"` | — |
| [SRC-2C8F288796-L000781](../../web/workspace.html#L781) | 781 | `"   try{"` | — |
| [SRC-2C8F288796-L000782](../../web/workspace.html#L782) | 782 | `"    const savedRun=await api(\"/api/discoveries\",{method:\"POST\",body:{profile_id:profileSelect.value,allow_optional_providers:optional.checked}});"` | — |
| [SRC-2C8F288796-L000783](../../web/workspace.html#L783) | 783 | `"    state.activeDiscovery=savedRun;"` | — |
| [SRC-2C8F288796-L000784](../../web/workspace.html#L784) | 784 | `"    let refreshWarning=\"\";"` | — |
| [SRC-2C8F288796-L000785](../../web/workspace.html#L785) | 785 | `"    try{await loadDiscoveryRuns()}catch(refreshError){refreshWarning=\" حُفظت نتيجة البحث، لكن تعذر تحديث سجل العمليات: \"+escapeMessage(refreshError.message)}"` | — |
| [SRC-2C8F288796-L000786](../../web/workspace.html#L786) | 786 | `"    renderDiscovery();"` | — |
| [SRC-2C8F288796-L000787](../../web/workspace.html#L787) | 787 | `"    if(refreshWarning){const warning=make(\"p\",\"auth-error\",refreshWarning);warning.setAttribute(\"role\",\"alert\");$(\"viewRoot\").append(warning)}"` | — |
| [SRC-2C8F288796-L000788](../../web/workspace.html#L788) | 788 | `"   }catch(error){"` | — |
| [SRC-2C8F288796-L000789](../../web/workspace.html#L789) | 789 | `"    status.className=\"auth-error\";status.textContent=\"تعذر تشغيل الاكتشاف: \"+escapeMessage(error.message)+\" يمكنك المحاولة مجددًا. لم تُحذف النتائج السابقة.\";"` | — |
| [SRC-2C8F288796-L000790](../../web/workspace.html#L790) | 790 | `"   }finally{"` | — |
| [SRC-2C8F288796-L000791](../../web/workspace.html#L791) | 791 | `"    run.disabled=false;run.removeAttribute(\"aria-busy\");"` | — |
| [SRC-2C8F288796-L000792](../../web/workspace.html#L792) | 792 | `"   }"` | — |
| [SRC-2C8F288796-L000793](../../web/workspace.html#L793) | 793 | `"  });"` | — |
| [SRC-2C8F288796-L000794](../../web/workspace.html#L794) | 794 | `"  run.disabled=!canWrite();actions.append(run);controls.append(actions,status);"` | — |
| [SRC-2C8F288796-L000795](../../web/workspace.html#L795) | 795 | `" }"` | — |
| [SRC-2C8F288796-L000796](../../web/workspace.html#L796) | 796 | `" controls.append(make(\"p\",\"profile-note\",\"تاريخ النشر قد يكون غير متاح. المقتطف لا يعني أن الصفحة قُرئت. فشل الموصل لا يثبت عدم وجود عملاء. لا يتم إرسال أي رسالة من هذه الشاشة.\"));"` | — |
| [SRC-2C8F288796-L000797](../../web/workspace.html#L797) | 797 | `" controls.append(make(\"p\",\"profile-note\",\"تشغيل الاكتشاف يستخدم النموذج اللغوي المهيأ حاليًا في Omarai؛ قد يستهلك حصة أو تكلفة بحسب إعدادات مزود النموذج. لا تدخل بيانات سرية. الموصلات الاختيارية منفصلة وتظل معطلة افتراضيًا حتى موافقة المالك.\"));"` | — |
| [SRC-2C8F288796-L000798](../../web/workspace.html#L798) | 798 | `" root.append(controls);"` | — |
| [SRC-2C8F288796-L000799](../../web/workspace.html#L799) | 799 | `" if(state.discoveryRuns.length){"` | — |
| [SRC-2C8F288796-L000800](../../web/workspace.html#L800) | 800 | `"  const history=make(\"section\",\"glass panel profile-panel\"),hh=make(\"div\",\"panel-head\"),ht=make(\"div\");"` | — |
| [SRC-2C8F288796-L000801](../../web/workspace.html#L801) | 801 | `"  ht.append(make(\"h2\",\"\",\"سجل عمليات الاكتشاف\"),make(\"p\",\"\",\"عمليات محفوظة ضمن مساحة العمل الحالية.\"));"` | — |
| [SRC-2C8F288796-L000802](../../web/workspace.html#L802) | 802 | `"  hh.append(ht);history.append(hh);const list=make(\"div\",\"discovery-history\");"` | — |
| [SRC-2C8F288796-L000803](../../web/workspace.html#L803) | 803 | `"  state.discoveryRuns.forEach(item=>list.append(action("` | — |
| [SRC-2C8F288796-L000804](../../web/workspace.html#L804) | 804 | `"   String(item.profile_name\|\|\"ملف منتج\")+\" · \"+String(item.qualified_signal_count\|\|0)+\" إشارة · \"+String(item.created_at\|\|\"\"),"` | — |
| [SRC-2C8F288796-L000805](../../web/workspace.html#L805) | 805 | `"   \"\","` | — |
| [SRC-2C8F288796-L000806](../../web/workspace.html#L806) | 806 | `"   async()=>{try{state.activeDiscovery=await api(\"/api/discoveries/\"+encodeURIComponent(item.id));renderDiscovery()}catch(error){const message=make(\"p\",\"auth-error\",escapeMessage(error.message));message.setAttribute(\"role\",\"alert\");history.append(message)}}"` | — |
| [SRC-2C8F288796-L000807](../../web/workspace.html#L807) | 807 | `"  )));"` | — |
| [SRC-2C8F288796-L000808](../../web/workspace.html#L808) | 808 | `"  history.append(list);root.append(history);"` | — |
| [SRC-2C8F288796-L000809](../../web/workspace.html#L809) | 809 | `" }"` | — |
| [SRC-2C8F288796-L000810](../../web/workspace.html#L810) | 810 | `" if(state.activeDiscovery)root.append(renderDiscoveryRun(state.activeDiscovery));"` | — |
| [SRC-2C8F288796-L000811](../../web/workspace.html#L811) | 811 | `"}"` | — |
| [SRC-2C8F288796-L000812](../../web/workspace.html#L812) | 812 | `"function renderCurrent(){"` | — |
| [SRC-2C8F288796-L000813](../../web/workspace.html#L813) | 813 | `" renderNav();"` | — |
| [SRC-2C8F288796-L000814](../../web/workspace.html#L814) | 814 | `" if(state.activeView===\"overview\")renderOverview();"` | — |
| [SRC-2C8F288796-L000815](../../web/workspace.html#L815) | 815 | `" else if(state.activeView===\"indicators\")renderIndicators();"` | — |
| [SRC-2C8F288796-L000816](../../web/workspace.html#L816) | 816 | `" else if(state.activeView===\"offer\")renderProductProfile();"` | — |
| [SRC-2C8F288796-L000817](../../web/workspace.html#L817) | 817 | `" else if(state.activeView===\"campaign\")renderDiscovery();"` | — |
| [SRC-2C8F288796-L000818](../../web/workspace.html#L818) | 818 | `" else if(state.activeView===\"signals\")renderSignals();"` | — |
| [SRC-2C8F288796-L000819](../../web/workspace.html#L819) | 819 | `" else if(state.activeView===\"pipeline\")renderPipeline();"` | — |
| [SRC-2C8F288796-L000820](../../web/workspace.html#L820) | 820 | `" else if(state.activeView===\"system\")renderSystem();"` | — |
| [SRC-2C8F288796-L000821](../../web/workspace.html#L821) | 821 | `" else renderPlaceholder(state.activeView);"` | — |
| [SRC-2C8F288796-L000822](../../web/workspace.html#L822) | 822 | `" if(state.loadWarnings.length){"` | — |
| [SRC-2C8F288796-L000823](../../web/workspace.html#L823) | 823 | `"  $(\"viewRoot\").prepend(make(\"p\",\"auth-error\",\"تم التحقق من الجلسة؛ تعذر تحميل بعض البيانات: \"+state.loadWarnings.join(\"، \")+\". قد تكون بعض القوائم والأرقام غير مكتملة.\"));"` | — |
| [SRC-2C8F288796-L000824](../../web/workspace.html#L824) | 824 | `" }"` | — |
| [SRC-2C8F288796-L000825](../../web/workspace.html#L825) | 825 | `"}"` | — |
| [SRC-2C8F288796-L000826](../../web/workspace.html#L826) | 826 | `"function navigate(view){"` | — |
| [SRC-2C8F288796-L000827](../../web/workspace.html#L827) | 827 | `" state.activeView=view;renderCurrent();"` | — |
| [SRC-2C8F288796-L000828](../../web/workspace.html#L828) | 828 | `"}"` | — |
| [SRC-2C8F288796-L000829](../../web/workspace.html#L829) | 829 | `"async function loadProductProfiles(){"` | — |
| [SRC-2C8F288796-L000830](../../web/workspace.html#L830) | 830 | `" const data=await api(\"/api/product-profiles\");"` | — |
| [SRC-2C8F288796-L000831](../../web/workspace.html#L831) | 831 | `" state.profiles=Array.isArray(data.profiles)?data.profiles:[];"` | — |
| [SRC-2C8F288796-L000832](../../web/workspace.html#L832) | 832 | `" if(!state.profiles.some(item=>item.id===state.activeProfileId))state.activeProfileId=state.profiles[0]?.id\|\|null;"` | — |
| [SRC-2C8F288796-L000833](../../web/workspace.html#L833) | 833 | `"}"` | — |
| [SRC-2C8F288796-L000834](../../web/workspace.html#L834) | 834 | `"async function loadDiscoveryRuns(){"` | — |
| [SRC-2C8F288796-L000835](../../web/workspace.html#L835) | 835 | `" const data=await api(\"/api/discoveries\");"` | — |
| [SRC-2C8F288796-L000836](../../web/workspace.html#L836) | 836 | `" state.discoveryRuns=Array.isArray(data.runs)?data.runs:[];"` | — |
| [SRC-2C8F288796-L000837](../../web/workspace.html#L837) | 837 | `"}"` | — |
| [SRC-2C8F288796-L000838](../../web/workspace.html#L838) | 838 | `"async function loadLeads(){"` | — |
| [SRC-2C8F288796-L000839](../../web/workspace.html#L839) | 839 | `" const data=await api(\"/api/leads?limit=500\");"` | — |
| [SRC-2C8F288796-L000840](../../web/workspace.html#L840) | 840 | `" state.leads=Array.isArray(data.leads)?data.leads:[];"` | — |
| [SRC-2C8F288796-L000841](../../web/workspace.html#L841) | 841 | `"}"` | — |
| [SRC-2C8F288796-L000842](../../web/workspace.html#L842) | 842 | `"async function bootstrap(){"` | — |
| [SRC-2C8F288796-L000843](../../web/workspace.html#L843) | 843 | `" let session;"` | — |
| [SRC-2C8F288796-L000844](../../web/workspace.html#L844) | 844 | `" try{"` | — |
| [SRC-2C8F288796-L000845](../../web/workspace.html#L845) | 845 | `"  session=await api(\"/api/session\");"` | — |
| [SRC-2C8F288796-L000846](../../web/workspace.html#L846) | 846 | `" }catch(e){"` | — |
| [SRC-2C8F288796-L000847](../../web/workspace.html#L847) | 847 | `"  setConnection(false,\"يلزم تسجيل الدخول\",\"تعذر التحقق من جلسة المستخدم.\");"` | — |
| [SRC-2C8F288796-L000848](../../web/workspace.html#L848) | 848 | `"  showAuth(e.message);"` | — |
| [SRC-2C8F288796-L000849](../../web/workspace.html#L849) | 849 | `"  $(\"viewRoot\").replaceChildren(emptyState(\"مساحة العمل مقفلة\",\"سجّل الدخول لقراءة البيانات المرتبطة بمساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000850](../../web/workspace.html#L850) | 850 | `"  return;"` | — |
| [SRC-2C8F288796-L000851](../../web/workspace.html#L851) | 851 | `" }"` | — |
| [SRC-2C8F288796-L000852](../../web/workspace.html#L852) | 852 | `" state.role=session.role\|\|\"unknown\";"` | — |
| [SRC-2C8F288796-L000853](../../web/workspace.html#L853) | 853 | `" $(\"rolePill\").textContent=\"صلاحية: \"+state.role;"` | — |
| [SRC-2C8F288796-L000854](../../web/workspace.html#L854) | 854 | `" $(\"roleSummary\").textContent=\"الدور: \"+state.role+(canWrite()?\" — إضافة وتحديث السجلات متاح.\":\" — قراءة فقط.\");"` | — |
| [SRC-2C8F288796-L000855](../../web/workspace.html#L855) | 855 | `" hideAuth();"` | — |
| [SRC-2C8F288796-L000856](../../web/workspace.html#L856) | 856 | `" const results=await Promise.allSettled(["` | — |
| [SRC-2C8F288796-L000857](../../web/workspace.html#L857) | 857 | `"  loadLeads(),"` | — |
| [SRC-2C8F288796-L000858](../../web/workspace.html#L858) | 858 | `"  loadProductProfiles(),"` | — |
| [SRC-2C8F288796-L000859](../../web/workspace.html#L859) | 859 | `"  loadDiscoveryRuns()"` | — |
| [SRC-2C8F288796-L000860](../../web/workspace.html#L860) | 860 | `" ]);"` | — |
| [SRC-2C8F288796-L000861](../../web/workspace.html#L861) | 861 | `" if($(\"authGate\").classList.contains(\"open\")){"` | — |
| [SRC-2C8F288796-L000862](../../web/workspace.html#L862) | 862 | `"  setConnection(false,\"يلزم تسجيل الدخول\",\"انتهت الجلسة أثناء تحميل البيانات.\");"` | — |
| [SRC-2C8F288796-L000863](../../web/workspace.html#L863) | 863 | `"  $(\"viewRoot\").replaceChildren(emptyState(\"مساحة العمل مقفلة\",\"سجّل الدخول لقراءة البيانات المرتبطة بمساحة العمل.\"));"` | — |
| [SRC-2C8F288796-L000864](../../web/workspace.html#L864) | 864 | `"  return;"` | — |
| [SRC-2C8F288796-L000865](../../web/workspace.html#L865) | 865 | `" }"` | — |
| [SRC-2C8F288796-L000866](../../web/workspace.html#L866) | 866 | `" state.loadWarnings=[];"` | — |
| [SRC-2C8F288796-L000867](../../web/workspace.html#L867) | 867 | `" const labels=[\"سجل الإشارات\",\"ملفات المنتجات\",\"سجل الاكتشاف\"];"` | — |
| [SRC-2C8F288796-L000868](../../web/workspace.html#L868) | 868 | `" results.forEach((result,index)=>{"` | — |
| [SRC-2C8F288796-L000869](../../web/workspace.html#L869) | 869 | `"  if(result.status!==\"rejected\")return;"` | — |
| [SRC-2C8F288796-L000870](../../web/workspace.html#L870) | 870 | `"  state.loadWarnings.push(labels[index]);"` | — |
| [SRC-2C8F288796-L000871](../../web/workspace.html#L871) | 871 | `"  if(index===0)state.leads=[];"` | — |
| [SRC-2C8F288796-L000872](../../web/workspace.html#L872) | 872 | `"  else if(index===1)state.profiles=[];"` | — |
| [SRC-2C8F288796-L000873](../../web/workspace.html#L873) | 873 | `"  else state.discoveryRuns=[];"` | — |
| [SRC-2C8F288796-L000874](../../web/workspace.html#L874) | 874 | `" });"` | — |
| [SRC-2C8F288796-L000875](../../web/workspace.html#L875) | 875 | `" const note=state.loadWarnings.length"` | — |
| [SRC-2C8F288796-L000876](../../web/workspace.html#L876) | 876 | `"  ?\"الجلسة مصادق عليها؛ تعذر تحميل بعض البيانات: \"+state.loadWarnings.join(\"، \")+\". حاول تحديث الوحدة لاحقًا.\""` | — |
| [SRC-2C8F288796-L000877](../../web/workspace.html#L877) | 877 | `"  :\"تم تحميل الإشارات وملفات المنتج وسجل الاكتشاف. هذا لا يثبت اتصال جميع الموصلات.\";"` | — |
| [SRC-2C8F288796-L000878](../../web/workspace.html#L878) | 878 | `" setConnection(true,state.loadWarnings.length?\"الجلسة مصادق عليها — بيانات جزئية\":\"الجلسة مصادق عليها\",note);"` | — |
| [SRC-2C8F288796-L000879](../../web/workspace.html#L879) | 879 | `" renderCurrent();"` | — |
| [SRC-2C8F288796-L000880](../../web/workspace.html#L880) | 880 | `"}"` | — |
| [SRC-2C8F288796-L000881](../../web/workspace.html#L881) | 881 | `"$(\"loginForm\").addEventListener(\"submit\",async event=>{"` | — |
| [SRC-2C8F288796-L000882](../../web/workspace.html#L882) | 882 | `" event.preventDefault();const token=$(\"accessToken\").value.trim();const button=$(\"loginButton\");button.disabled=true;$(\"authError\").textContent=\"\";"` | — |
| [SRC-2C8F288796-L000883](../../web/workspace.html#L883) | 883 | `" try{"` | — |
| [SRC-2C8F288796-L000884](../../web/workspace.html#L884) | 884 | `"  await api(\"/api/session\",{method:\"POST\",body:{access_token:token}});"` | — |
| [SRC-2C8F288796-L000885](../../web/workspace.html#L885) | 885 | `"  $(\"accessToken\").value=\"\";await bootstrap();"` | — |
| [SRC-2C8F288796-L000886](../../web/workspace.html#L886) | 886 | `" }catch(e){$(\"authError\").textContent=escapeMessage(e.message)}"` | — |
| [SRC-2C8F288796-L000887](../../web/workspace.html#L887) | 887 | `" finally{button.disabled=false}"` | — |
| [SRC-2C8F288796-L000888](../../web/workspace.html#L888) | 888 | `"});"` | — |
| [SRC-2C8F288796-L000889](../../web/workspace.html#L889) | 889 | `"$(\"logoutButton\").addEventListener(\"click\",async()=>{"` | — |
| [SRC-2C8F288796-L000890](../../web/workspace.html#L890) | 890 | `" try{"` | — |
| [SRC-2C8F288796-L000891](../../web/workspace.html#L891) | 891 | `"  await api(\"/api/session/logout\",{method:\"POST\",body:{}});"` | — |
| [SRC-2C8F288796-L000892](../../web/workspace.html#L892) | 892 | `" }catch(e){"` | — |
| [SRC-2C8F288796-L000893](../../web/workspace.html#L893) | 893 | `"  alert(\"تعذر تسجيل الخروج من الخادم؛ لم يتم تغيير حالة الجلسة في الواجهة. \"+escapeMessage(e.message));"` | — |
| [SRC-2C8F288796-L000894](../../web/workspace.html#L894) | 894 | `"  return;"` | — |
| [SRC-2C8F288796-L000895](../../web/workspace.html#L895) | 895 | `" }"` | — |
| [SRC-2C8F288796-L000896](../../web/workspace.html#L896) | 896 | `" state.role=null;state.leads=[];state.profiles=[];state.discoveryRuns=[];state.loadWarnings=[];state.activeDiscovery=null;state.activeProfileId=null;state.activeView=\"overview\";showAuth(\"تم تسجيل الخروج. أدخل رمز الوصول للمتابعة.\");setConnection(false,\"غير متصل\",\"سجّل الدخول لعرض السجلات.\");"` | — |
| [SRC-2C8F288796-L000897](../../web/workspace.html#L897) | 897 | `"});"` | — |
| [SRC-2C8F288796-L000898](../../web/workspace.html#L898) | 898 | `"$(\"addSignalTop\").addEventListener(\"click\",()=>navigate(\"signals\"));"` | — |
| [SRC-2C8F288796-L000899](../../web/workspace.html#L899) | 899 | `"$(\"closeDetail\").addEventListener(\"click\",closeDetails);"` | — |
| [SRC-2C8F288796-L000900](../../web/workspace.html#L900) | 900 | `"$(\"systemNav\").addEventListener(\"click\",()=>navigate(\"system\"));"` | — |
| [SRC-2C8F288796-L000901](../../web/workspace.html#L901) | 901 | `"$(\"detailDrawer\").addEventListener(\"click\",e=>{if(e.target===$(\"detailDrawer\"))closeDetails()});"` | — |
| [SRC-2C8F288796-L000902](../../web/workspace.html#L902) | 902 | `"document.addEventListener(\"keydown\",e=>{if(e.key===\"Escape\")closeDetails()});"` | — |
| [SRC-2C8F288796-L000903](../../web/workspace.html#L903) | 903 | `"renderNav();bootstrap();"` | — |
| [SRC-2C8F288796-L000904](../../web/workspace.html#L904) | 904 | `"})();"` | — |
| [SRC-2C8F288796-L000905](../../web/workspace.html#L905) | 905 | `"</script>"` | — |
| [SRC-2C8F288796-L000906](../../web/workspace.html#L906) | 906 | `"</body>"` | — |
| [SRC-2C8F288796-L000907](../../web/workspace.html#L907) | 907 | `"</html>"` | — |
