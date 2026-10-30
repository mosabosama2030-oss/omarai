# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **007**
- سجلات الأسطر: **800**
- النطاق: SRC-686F71AA50-L000120 إلى SRC-686F71AA50-L000919
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-686F71AA50 — [agents/task_understanding.py](../../agents/task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-686F71AA50-L000120](../../agents/task_understanding.py#L120) | 120 | `"    if not isinstance(ids, list):"` | — |
| [SRC-686F71AA50-L000121](../../agents/task_understanding.py#L121) | 121 | `"        return []"` | — |
| [SRC-686F71AA50-L000122](../../agents/task_understanding.py#L122) | 122 | `"    return [_REASONING_GUIDANCE[item] for item in ids if isinstance(item, str) and item in _REASONING_GUIDANCE][:12]"` | — |
| [SRC-686F71AA50-L000123](../../agents/task_understanding.py#L123) | 123 | `""` | — |
| [SRC-686F71AA50-L000124](../../agents/task_understanding.py#L124) | 124 | `"_ARABIC_DIACRITICS = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-686F71AA50-L000125](../../agents/task_understanding.py#L125) | 125 | `"_PUNCTUATION = re.compile(r\"[؟?!.،,؛;:(){}\\[\\]\\\"'«»]+\")"` | — |
| [SRC-686F71AA50-L000126](../../agents/task_understanding.py#L126) | 126 | `"_SPACE = re.compile(r\"\\s+\")"` | — |
| [SRC-686F71AA50-L000127](../../agents/task_understanding.py#L127) | 127 | `"_TOKEN_RE = re.compile(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", re.IGNORECASE)"` | — |
| [SRC-686F71AA50-L000128](../../agents/task_understanding.py#L128) | 128 | `""` | — |
| [SRC-686F71AA50-L000129](../../agents/task_understanding.py#L129) | 129 | `"_PATTERNS: dict[str, tuple[str, ...]] = {"` | — |
| [SRC-686F71AA50-L000130](../../agents/task_understanding.py#L130) | 130 | `"    \"official_site_lookup\": ("` | — |
| [SRC-686F71AA50-L000131](../../agents/task_understanding.py#L131) | 131 | `"        \"الموقع الرسمي\", \"موقع رسمي\", \"رابط الموقع الرسمي\", \"الصفحه الرسميه\","` | — |
| [SRC-686F71AA50-L000132](../../agents/task_understanding.py#L132) | 132 | `"        \"الموقع الحكومي\", \"official website\", \"official site\", \"official homepage\","` | — |
| [SRC-686F71AA50-L000133](../../agents/task_understanding.py#L133) | 133 | `"    ),"` | — |
| [SRC-686F71AA50-L000134](../../agents/task_understanding.py#L134) | 134 | `"    \"social_opinions\": ("` | — |
| [SRC-686F71AA50-L000135](../../agents/task_understanding.py#L135) | 135 | `"        \"اراء الناس\", \"اراء المستخدمين\", \"تجارب الناس\", \"تجارب المستخدمين\","` | — |
| [SRC-686F71AA50-L000136](../../agents/task_understanding.py#L136) | 136 | `"        \"تجارب الملاك\", \"تجارب ملاك\", \"تجربة مالك\", \"مراجعات المستخدمين\", \"الناس بتقول ايه\","` | — |
| [SRC-686F71AA50-L000137](../../agents/task_understanding.py#L137) | 137 | `"        \"real user reviews\", \"owner experience\", \"customer opinions\", \"people's opinions\","` | — |
| [SRC-686F71AA50-L000138](../../agents/task_understanding.py#L138) | 138 | `"        \"user experiences\", \"what do owners say\","` | — |
| [SRC-686F71AA50-L000139](../../agents/task_understanding.py#L139) | 139 | `"    ),"` | — |
| [SRC-686F71AA50-L000140](../../agents/task_understanding.py#L140) | 140 | `"    \"summarize\": ("` | — |
| [SRC-686F71AA50-L000141](../../agents/task_understanding.py#L141) | 141 | `"        \"لخص\", \"تلخيص\", \"ملخص\", \"summarize\", \"summarise\", \"summary of\","` | — |
| [SRC-686F71AA50-L000142](../../agents/task_understanding.py#L142) | 142 | `"    ),"` | — |
| [SRC-686F71AA50-L000143](../../agents/task_understanding.py#L143) | 143 | `"    \"troubleshoot\": ("` | — |
| [SRC-686F71AA50-L000144](../../agents/task_understanding.py#L144) | 144 | `"        \"حل مشكلة\", \"عطل\", \"اعطال\", \"مش بيشتغل\", \"لا يعمل\", \"خطأ\", \"رساله خطأ\","` | — |
| [SRC-686F71AA50-L000145](../../agents/task_understanding.py#L145) | 145 | `"        \"اصلح\", \"استكشاف الاعطال\", \"troubleshoot\", \"debug\", \"does not work\","` | — |
| [SRC-686F71AA50-L000146](../../agents/task_understanding.py#L146) | 146 | `"        \"not working\", \"error message\", \"fix the problem\", \"common failures\","` | — |
| [SRC-686F71AA50-L000147](../../agents/task_understanding.py#L147) | 147 | `"    ),"` | — |
| [SRC-686F71AA50-L000148](../../agents/task_understanding.py#L148) | 148 | `"    \"how_to\": ("` | — |
| [SRC-686F71AA50-L000149](../../agents/task_understanding.py#L149) | 149 | `"        \"ازاي\", \"كيف\", \"طريقة\", \"خطوات\", \"اشرح لي كيف\", \"علمني\", \"كيفية\","` | — |
| [SRC-686F71AA50-L000150](../../agents/task_understanding.py#L150) | 150 | `"        \"how to\", \"steps to\", \"walk me through\", \"teach me\","` | — |
| [SRC-686F71AA50-L000151](../../agents/task_understanding.py#L151) | 151 | `"    ),"` | — |
| [SRC-686F71AA50-L000152](../../agents/task_understanding.py#L152) | 152 | `"    \"compare\": ("` | — |
| [SRC-686F71AA50-L000153](../../agents/task_understanding.py#L153) | 153 | `"        \"قارن\", \"مقارنه\", \"الفرق بين\", \"ايهما افضل\", \"مميزات وعيوب\","` | — |
| [SRC-686F71AA50-L000154](../../agents/task_understanding.py#L154) | 154 | `"        \"الايجابيات والسلبيات\", \"مفاضله\", \"compare\", \"comparison\", \"versus\","` | — |
| [SRC-686F71AA50-L000155](../../agents/task_understanding.py#L155) | 155 | `"        \"trade-offs\", \"pros and cons\", \"which is better\","` | — |
| [SRC-686F71AA50-L000156](../../agents/task_understanding.py#L156) | 156 | `"    ),"` | — |
| [SRC-686F71AA50-L000157](../../agents/task_understanding.py#L157) | 157 | `"    \"current_information\": ("` | — |
| [SRC-686F71AA50-L000158](../../agents/task_understanding.py#L158) | 158 | `"        \"اليوم\", \"النهارده\", \"النهاردة\", \"دلوقتي\", \"الان\", \"حاليا\", \"احدث\","` | — |
| [SRC-686F71AA50-L000159](../../agents/task_understanding.py#L159) | 159 | `"        \"اخر الاخبار\", \"الاسعار الحاليه\", \"المواعيد الحاليه\", \"في الوقت الحالي\","` | — |
| [SRC-686F71AA50-L000160](../../agents/task_understanding.py#L160) | 160 | `"        \"today\", \"right now\", \"currently\", \"latest\", \"breaking news\", \"current price\","` | — |
| [SRC-686F71AA50-L000161](../../agents/task_understanding.py#L161) | 161 | `"        \"current hours\", \"this week\", \"this month\","` | — |
| [SRC-686F71AA50-L000162](../../agents/task_understanding.py#L162) | 162 | `"    ),"` | — |
| [SRC-686F71AA50-L000163](../../agents/task_understanding.py#L163) | 163 | `"    \"lead_generation\": ("` | — |
| [SRC-686F71AA50-L000164](../../agents/task_understanding.py#L164) | 164 | `"        \"عميل محتمل\", \"عملاء محتملين\", \"ابحث عن مشترين\", \"ابحث عن عميل\","` | — |
| [SRC-686F71AA50-L000165](../../agents/task_understanding.py#L165) | 165 | `"        \"دور على عملاء\", \"buyers looking to buy\", \"find prospects\", \"lead generation\","` | — |
| [SRC-686F71AA50-L000166](../../agents/task_understanding.py#L166) | 166 | `"        \"prospective customers\","` | — |
| [SRC-686F71AA50-L000167](../../agents/task_understanding.py#L167) | 167 | `"    ),"` | — |
| [SRC-686F71AA50-L000168](../../agents/task_understanding.py#L168) | 168 | `"    \"recommendation\": ("` | — |
| [SRC-686F71AA50-L000169](../../agents/task_understanding.py#L169) | 169 | `"        \"رشح\", \"ترشيح\", \"تنصحني\", \"هل اشتري\", \"اختار ايه\", \"افضل خيار\","` | — |
| [SRC-686F71AA50-L000170](../../agents/task_understanding.py#L170) | 170 | `"        \"recommend\", \"recommendation\", \"should i buy\", \"best option\", \"what should i choose\","` | — |
| [SRC-686F71AA50-L000171](../../agents/task_understanding.py#L171) | 171 | `"    ),"` | — |
| [SRC-686F71AA50-L000172](../../agents/task_understanding.py#L172) | 172 | `"    \"find_or_discover\": ("` | — |
| [SRC-686F71AA50-L000173](../../agents/task_understanding.py#L173) | 173 | `"        \"ابحث عن\", \"دور على\", \"دورلي على\", \"اعثر على\", \"هات رابط\", \"هاتلي\","` | — |
| [SRC-686F71AA50-L000174](../../agents/task_understanding.py#L174) | 174 | `"        \"فين الاقي\", \"اماكن بيع\", \"ابحث لي عن\", \"find\", \"search for\", \"look up\","` | — |
| [SRC-686F71AA50-L000175](../../agents/task_understanding.py#L175) | 175 | `"        \"where can i find\", \"list of\","` | — |
| [SRC-686F71AA50-L000176](../../agents/task_understanding.py#L176) | 176 | `"    ),"` | — |
| [SRC-686F71AA50-L000177](../../agents/task_understanding.py#L177) | 177 | `"    \"medical_information\": ("` | — |
| [SRC-686F71AA50-L000178](../../agents/task_understanding.py#L178) | 178 | `"        \"اعراض\", \"أعراض\", \"جرعة\", \"جرعات\", \"دواء\", \"ادوية\", \"علاج\", \"تشخيص\","` | — |
| [SRC-686F71AA50-L000179](../../agents/task_understanding.py#L179) | 179 | `"        \"medical symptoms\", \"dosage\", \"medicine\", \"medication\", \"treatment\", \"diagnosis\","` | — |
| [SRC-686F71AA50-L000180](../../agents/task_understanding.py#L180) | 180 | `"    ),"` | — |
| [SRC-686F71AA50-L000181](../../agents/task_understanding.py#L181) | 181 | `"    \"legal_information\": ("` | — |
| [SRC-686F71AA50-L000182](../../agents/task_understanding.py#L182) | 182 | `"        \"قانون\", \"قانوني\", \"نص قانوني\", \"عقد\", \"دعوى\", \"لائحة\", \"تشريع\","` | — |
| [SRC-686F71AA50-L000183](../../agents/task_understanding.py#L183) | 183 | `"        \"legal advice\", \"law\", \"contract\", \"lawsuit\", \"regulation\", \"legislation\","` | — |
| [SRC-686F71AA50-L000184](../../agents/task_understanding.py#L184) | 184 | `"    ),"` | — |
| [SRC-686F71AA50-L000185](../../agents/task_understanding.py#L185) | 185 | `"    \"coding_or_technical_design\": ("` | — |
| [SRC-686F71AA50-L000186](../../agents/task_understanding.py#L186) | 186 | `"        \"اكتب كود\", \"برمج\", \"كود بايثون\", \"اشرح الكود\", \"راجع الكود\","` | — |
| [SRC-686F71AA50-L000187](../../agents/task_understanding.py#L187) | 187 | `"        \"الكود التالي\", \"تصميم api\", \"اكتب سكربت\", \"code\", \"programming\","` | — |
| [SRC-686F71AA50-L000188](../../agents/task_understanding.py#L188) | 188 | `"        \"python code\", \"javascript\", \"api design\", \"stack trace\", \"unit test\","` | — |
| [SRC-686F71AA50-L000189](../../agents/task_understanding.py#L189) | 189 | `"        \"refactor\", \"debug this code\","` | — |
| [SRC-686F71AA50-L000190](../../agents/task_understanding.py#L190) | 190 | `"    ),"` | — |
| [SRC-686F71AA50-L000191](../../agents/task_understanding.py#L191) | 191 | `"    \"data_analysis\": ("` | — |
| [SRC-686F71AA50-L000192](../../agents/task_understanding.py#L192) | 192 | `"        \"حلل البيانات\", \"تحليل البيانات\", \"ملف csv\", \"تحليل جدول\", \"احسب المتوسط\","` | — |
| [SRC-686F71AA50-L000193](../../agents/task_understanding.py#L193) | 193 | `"        \"data analysis\", \"analyze data\", \"analyse data\", \"dataset\", \"spreadsheet\","` | — |
| [SRC-686F71AA50-L000194](../../agents/task_understanding.py#L194) | 194 | `"        \"csv file\", \"trend analysis\", \"calculate average\", \"pivot table\","` | — |
| [SRC-686F71AA50-L000195](../../agents/task_understanding.py#L195) | 195 | `"    ),"` | — |
| [SRC-686F71AA50-L000196](../../agents/task_understanding.py#L196) | 196 | `"    \"calculation\": ("` | — |
| [SRC-686F71AA50-L000197](../../agents/task_understanding.py#L197) | 197 | `"        \"احسب\", \"كم يساوي\", \"ما ناتج\", \"حساب النسبة\", \"احسب الفرق\","` | — |
| [SRC-686F71AA50-L000198](../../agents/task_understanding.py#L198) | 198 | `"        \"calculate\", \"compute\", \"what is the result\", \"percentage calculation\","` | — |
| [SRC-686F71AA50-L000199](../../agents/task_understanding.py#L199) | 199 | `"        \"how many\", \"how much is\","` | — |
| [SRC-686F71AA50-L000200](../../agents/task_understanding.py#L200) | 200 | `"    ),"` | — |
| [SRC-686F71AA50-L000201](../../agents/task_understanding.py#L201) | 201 | `"    \"translation\": ("` | — |
| [SRC-686F71AA50-L000202](../../agents/task_understanding.py#L202) | 202 | `"        \"ترجم\", \"ترجمة\", \"ترجم إلى\", \"ترجم للانجليزية\", \"ترجم للعربية\","` | — |
| [SRC-686F71AA50-L000203](../../agents/task_understanding.py#L203) | 203 | `"        \"translate\", \"translation\", \"translate into\", \"localize this\","` | — |
| [SRC-686F71AA50-L000204](../../agents/task_understanding.py#L204) | 204 | `"    ),"` | — |
| [SRC-686F71AA50-L000205](../../agents/task_understanding.py#L205) | 205 | `"    \"writing_or_editing\": ("` | — |
| [SRC-686F71AA50-L000206](../../agents/task_understanding.py#L206) | 206 | `"        \"اكتب\", \"اكتب رسالة\", \"اكتب بريد\", \"اعد صياغة\", \"أعد صياغة\","` | — |
| [SRC-686F71AA50-L000207](../../agents/task_understanding.py#L207) | 207 | `"        \"صحح لغويا\", \"راجع النص\", \"حسن الصياغة\", \"draft\", \"write\", \"rewrite\","` | — |
| [SRC-686F71AA50-L000208](../../agents/task_understanding.py#L208) | 208 | `"        \"proofread\", \"edit this\", \"polish this\", \"compose an email\","` | — |
| [SRC-686F71AA50-L000209](../../agents/task_understanding.py#L209) | 209 | `"    ),"` | — |
| [SRC-686F71AA50-L000210](../../agents/task_understanding.py#L210) | 210 | `"    \"planning\": ("` | — |
| [SRC-686F71AA50-L000211](../../agents/task_understanding.py#L211) | 211 | `"        \"ضع خطة\", \"خطة عمل\", \"خطة زمنية\", \"جدول زمني\", \"خطوات تنفيذ\","` | — |
| [SRC-686F71AA50-L000212](../../agents/task_understanding.py#L212) | 212 | `"        \"نظم لي\", \"رتب لي\", \"plan\", \"planning\", \"roadmap\", \"itinerary\","` | — |
| [SRC-686F71AA50-L000213](../../agents/task_understanding.py#L213) | 213 | `"        \"project schedule\", \"timeline\", \"project plan\","` | — |
| [SRC-686F71AA50-L000214](../../agents/task_understanding.py#L214) | 214 | `"    ),"` | — |
| [SRC-686F71AA50-L000215](../../agents/task_understanding.py#L215) | 215 | `"    \"creative_generation\": ("` | — |
| [SRC-686F71AA50-L000216](../../agents/task_understanding.py#L216) | 216 | `"        \"اكتب قصة\", \"قصة قصيرة\", \"قصيدة\", \"سيناريو\", \"اقترح افكار\","` | — |
| [SRC-686F71AA50-L000217](../../agents/task_understanding.py#L217) | 217 | `"        \"اقترح أفكار\", \"عصف ذهني\", \"brainstorm\", \"creative writing\","` | — |
| [SRC-686F71AA50-L000218](../../agents/task_understanding.py#L218) | 218 | `"        \"write a story\", \"poem\", \"generate ideas\","` | — |
| [SRC-686F71AA50-L000219](../../agents/task_understanding.py#L219) | 219 | `"    ),"` | — |
| [SRC-686F71AA50-L000220](../../agents/task_understanding.py#L220) | 220 | `"    \"explain_or_define\": ("` | — |
| [SRC-686F71AA50-L000221](../../agents/task_understanding.py#L221) | 221 | `"        \"ما معنى\", \"يعني ايه\", \"ما هو\", \"ما هي\", \"اشرح\", \"وضح مفهوم\","` | — |
| [SRC-686F71AA50-L000222](../../agents/task_understanding.py#L222) | 222 | `"        \"what is\", \"what does\", \"explain\", \"define\","` | — |
| [SRC-686F71AA50-L000223](../../agents/task_understanding.py#L223) | 223 | `"    ),"` | — |
| [SRC-686F71AA50-L000224](../../agents/task_understanding.py#L224) | 224 | `"    \"general_research\": ("` | — |
| [SRC-686F71AA50-L000225](../../agents/task_understanding.py#L225) | 225 | `"        \"بحث عميق\", \"بحث شامل\", \"بحث معمق\", \"تحقق من\", \"مصادر موثوقه\","` | — |
| [SRC-686F71AA50-L000226](../../agents/task_understanding.py#L226) | 226 | `"        \"اذكر المصادر\", \"مع مصادر\", \"بالمصادر\", \"deep research\", \"research\","` | — |
| [SRC-686F71AA50-L000227](../../agents/task_understanding.py#L227) | 227 | `"        \"verify\", \"fact check\", \"with sources\", \"cite sources\","` | — |
| [SRC-686F71AA50-L000228](../../agents/task_understanding.py#L228) | 228 | `"    ),"` | — |
| [SRC-686F71AA50-L000229](../../agents/task_understanding.py#L229) | 229 | `"    \"output_concise\": ("` | — |
| [SRC-686F71AA50-L000230](../../agents/task_understanding.py#L230) | 230 | `"        \"باختصار\", \"بإيجاز\", \"مختصر\", \"من غير إطالة\", \"بدون إطالة\","` | — |
| [SRC-686F71AA50-L000231](../../agents/task_understanding.py#L231) | 231 | `"        \"briefly\", \"in brief\", \"concise\", \"short answer\", \"keep it short\","` | — |
| [SRC-686F71AA50-L000232](../../agents/task_understanding.py#L232) | 232 | `"    ),"` | — |
| [SRC-686F71AA50-L000233](../../agents/task_understanding.py#L233) | 233 | `"    \"output_detailed\": ("` | — |
| [SRC-686F71AA50-L000234](../../agents/task_understanding.py#L234) | 234 | `"        \"بالتفصيل\", \"شرح وافي\", \"اشرح بالتفصيل\", \"خطوة بخطوة\","` | — |
| [SRC-686F71AA50-L000235](../../agents/task_understanding.py#L235) | 235 | `"        \"in detail\", \"step by step\", \"comprehensive explanation\", \"walkthrough\","` | — |
| [SRC-686F71AA50-L000236](../../agents/task_understanding.py#L236) | 236 | `"    ),"` | — |
| [SRC-686F71AA50-L000237](../../agents/task_understanding.py#L237) | 237 | `"    \"output_examples\": ("` | — |
| [SRC-686F71AA50-L000238](../../agents/task_understanding.py#L238) | 238 | `"        \"مع مثال\", \"امثلة\", \"مثال عملي\", \"بأمثلة\", \"for example\","` | — |
| [SRC-686F71AA50-L000239](../../agents/task_understanding.py#L239) | 239 | `"        \"give examples\", \"practical example\", \"worked example\","` | — |
| [SRC-686F71AA50-L000240](../../agents/task_understanding.py#L240) | 240 | `"    ),"` | — |
| [SRC-686F71AA50-L000241](../../agents/task_understanding.py#L241) | 241 | `"    \"output_table\": ("` | — |
| [SRC-686F71AA50-L000242](../../agents/task_understanding.py#L242) | 242 | `"        \"في جدول\", \"اعمل جدول\", \"جدول مقارنة\", \"as a table\", \"in a table\","` | — |
| [SRC-686F71AA50-L000243](../../agents/task_understanding.py#L243) | 243 | `"        \"comparison table\", \"tabulate\","` | — |
| [SRC-686F71AA50-L000244](../../agents/task_understanding.py#L244) | 244 | `"    ),"` | — |
| [SRC-686F71AA50-L000245](../../agents/task_understanding.py#L245) | 245 | `"    \"output_bullets\": ("` | — |
| [SRC-686F71AA50-L000246](../../agents/task_understanding.py#L246) | 246 | `"        \"نقاط\", \"على شكل نقاط\", \"قائمة\", \"bullet points\", \"as a list\","` | — |
| [SRC-686F71AA50-L000247](../../agents/task_understanding.py#L247) | 247 | `"        \"in bullets\", \"checklist\","` | — |
| [SRC-686F71AA50-L000248](../../agents/task_understanding.py#L248) | 248 | `"    ),"` | — |
| [SRC-686F71AA50-L000249](../../agents/task_understanding.py#L249) | 249 | `"    \"output_beginner_friendly\": ("` | — |
| [SRC-686F71AA50-L000250](../../agents/task_understanding.py#L250) | 250 | `"        \"ببساطة\", \"بشرح بسيط\", \"للمبتدئين\", \"من الصفر\", \"بلغة سهلة\","` | — |
| [SRC-686F71AA50-L000251](../../agents/task_understanding.py#L251) | 251 | `"        \"simple language\", \"beginner friendly\", \"beginner-friendly\","` | — |
| [SRC-686F71AA50-L000252](../../agents/task_understanding.py#L252) | 252 | `"        \"explain like i'm five\", \"eli5\","` | — |
| [SRC-686F71AA50-L000253](../../agents/task_understanding.py#L253) | 253 | `"    ),"` | — |
| [SRC-686F71AA50-L000254](../../agents/task_understanding.py#L254) | 254 | `"    \"output_citations\": ("` | — |
| [SRC-686F71AA50-L000255](../../agents/task_understanding.py#L255) | 255 | `"        \"مع مصادر\", \"اذكر المصادر\", \"مصادر موثوقة\", \"روابط مباشرة\","` | — |
| [SRC-686F71AA50-L000256](../../agents/task_understanding.py#L256) | 256 | `"        \"with sources\", \"cite sources\", \"include references\", \"with citations\","` | — |
| [SRC-686F71AA50-L000257](../../agents/task_understanding.py#L257) | 257 | `"    ),"` | — |
| [SRC-686F71AA50-L000258](../../agents/task_understanding.py#L258) | 258 | `"    \"output_links\": ("` | — |
| [SRC-686F71AA50-L000259](../../agents/task_understanding.py#L259) | 259 | `"        \"رابط مباشر\", \"روابط مباشرة\", \"هات الرابط\", \"لينك\", \"url\","` | — |
| [SRC-686F71AA50-L000260](../../agents/task_understanding.py#L260) | 260 | `"        \"direct link\", \"direct links\", \"include links\", \"source url\","` | — |
| [SRC-686F71AA50-L000261](../../agents/task_understanding.py#L261) | 261 | `"    ),"` | — |
| [SRC-686F71AA50-L000262](../../agents/task_understanding.py#L262) | 262 | `"    \"output_json\": ("` | — |
| [SRC-686F71AA50-L000263](../../agents/task_understanding.py#L263) | 263 | `"        \"بصيغة json\", \"تنسيق json\", \"return json\", \"output json\", \"as json\","` | — |
| [SRC-686F71AA50-L000264](../../agents/task_understanding.py#L264) | 264 | `"    ),"` | — |
| [SRC-686F71AA50-L000265](../../agents/task_understanding.py#L265) | 265 | `"}"` | — |
| [SRC-686F71AA50-L000266](../../agents/task_understanding.py#L266) | 266 | `""` | — |
| [SRC-686F71AA50-L000267](../../agents/task_understanding.py#L267) | 267 | `"_FRESHNESS_CUES = _PATTERNS[\"current_information\"]"` | — |
| [SRC-686F71AA50-L000268](../../agents/task_understanding.py#L268) | 268 | `"_SOCIAL_CUES = _PATTERNS[\"social_opinions\"]"` | — |
| [SRC-686F71AA50-L000269](../../agents/task_understanding.py#L269) | 269 | `"_LOCATION_CUES = ("` | — |
| [SRC-686F71AA50-L000270](../../agents/task_understanding.py#L270) | 270 | `"    \"في مصر\", \"داخل مصر\", \"بالقاهرة\", \"في القاهره\", \"بالاسكندريه\", \"في السعودية\","` | — |
| [SRC-686F71AA50-L000271](../../agents/task_understanding.py#L271) | 271 | `"    \"في الامارات\", \"in egypt\", \"within egypt\", \"in cairo\", \"in saudi arabia\","` | — |
| [SRC-686F71AA50-L000272](../../agents/task_understanding.py#L272) | 272 | `"    \"in the uae\", \"in the united states\", \"in the uk\","` | — |
| [SRC-686F71AA50-L000273](../../agents/task_understanding.py#L273) | 273 | `")"` | — |
| [SRC-686F71AA50-L000274](../../agents/task_understanding.py#L274) | 274 | `"_OFFICIAL_WORDS = (\"وزارة\", \"هيئة حكومية\", \"جهة حكومية\", \"مصلحة حكومية\", \"ministry\", \"government agency\")"` | — |
| [SRC-686F71AA50-L000275](../../agents/task_understanding.py#L275) | 275 | `"_YEAR_RE = re.compile(r\"(?<!\\d)(?:19\\d{2}\|20\\d{2})(?!\\d)\")"` | — |
| [SRC-686F71AA50-L000276](../../agents/task_understanding.py#L276) | 276 | `"_DATE_RE = re.compile(r\"(?<!\\d)(?:\\d{4}-\\d{2}-\\d{2}\|\\d{1,2}[/-]\\d{1,2}[/-]\\d{2,4})(?!\\d)\")"` | — |
| [SRC-686F71AA50-L000277](../../agents/task_understanding.py#L277) | 277 | `"_URL_RE = re.compile(r\"https?://[^\\s<>]+\", re.IGNORECASE)"` | — |
| [SRC-686F71AA50-L000278](../../agents/task_understanding.py#L278) | 278 | `"_BUDGET_RE = re.compile("` | — |
| [SRC-686F71AA50-L000279](../../agents/task_understanding.py#L279) | 279 | `"    r\"(?:ميزاني(?:ة\|تي)(?:\\s+(?:(?:أقل\|اقل)\\s+من\|بحد\\s+اقصى\|في\\s+حدود))?\""` | — |
| [SRC-686F71AA50-L000280](../../agents/task_understanding.py#L280) | 280 | `"    r\"\|بحد\\s+اقصى\|(?:أقل\|اقل)\\s+من\|في\\s+حدود\|budget(?:\\s+of)?\|under\|below\|up\\s+to)\""` | — |
| [SRC-686F71AA50-L000281](../../agents/task_understanding.py#L281) | 281 | `"    r\"\\s*[:：]?\\s*(?:egp\|usd\|eur\|جنيه\|دولار\|ريال)?\\s*[\\d,.\\u0660-\\u0669]+\""` | — |
| [SRC-686F71AA50-L000282](../../agents/task_understanding.py#L282) | 282 | `"    r\"(?:\\s*(?:الف\|ألف\|مليون\|thousand\|million\|k))?\","` | — |
| [SRC-686F71AA50-L000283](../../agents/task_understanding.py#L283) | 283 | `"    re.IGNORECASE,"` | — |
| [SRC-686F71AA50-L000284](../../agents/task_understanding.py#L284) | 284 | `")"` | — |
| [SRC-686F71AA50-L000285](../../agents/task_understanding.py#L285) | 285 | `"_FOLLOWUP_CUES = ("` | — |
| [SRC-686F71AA50-L000286](../../agents/task_understanding.py#L286) | 286 | `"    \"سعرها\", \"سعره\", \"قارنهم\", \"بينهم\", \"ما رايك فيها\", \"هل هي كويسه\","` | — |
| [SRC-686F71AA50-L000287](../../agents/task_understanding.py#L287) | 287 | `"    \"what about it\", \"compare them\", \"is it good\", \"should i buy it\","` | — |
| [SRC-686F71AA50-L000288](../../agents/task_understanding.py#L288) | 288 | `"    \"its price\", \"the warranty\","` | — |
| [SRC-686F71AA50-L000289](../../agents/task_understanding.py#L289) | 289 | `")"` | — |
| [SRC-686F71AA50-L000290](../../agents/task_understanding.py#L290) | 290 | `"_QUERY_STOP = re.compile("` | — |
| [SRC-686F71AA50-L000291](../../agents/task_understanding.py#L291) | 291 | `"    r\"\\b(?:من حيث\|in terms of\|taking into account\|with respect to)\\b.*$\","` | — |
| [SRC-686F71AA50-L000292](../../agents/task_understanding.py#L292) | 292 | `"    re.IGNORECASE,"` | — |
| [SRC-686F71AA50-L000293](../../agents/task_understanding.py#L293) | 293 | `")"` | — |
| [SRC-686F71AA50-L000294](../../agents/task_understanding.py#L294) | 294 | `""` | — |
| [SRC-686F71AA50-L000295](../../agents/task_understanding.py#L295) | 295 | `""` | — |
| [SRC-686F71AA50-L000296](../../agents/task_understanding.py#L296) | 296 | `"def normalize_text(value: Any) -> str:"` | — |
| [SRC-686F71AA50-L000297](../../agents/task_understanding.py#L297) | 297 | `"    \"\"\"Normalize orthographic variation for matching; preserve the original elsewhere.\"\"\""` | — |
| [SRC-686F71AA50-L000298](../../agents/task_understanding.py#L298) | 298 | `"    if not isinstance(value, str):"` | — |
| [SRC-686F71AA50-L000299](../../agents/task_understanding.py#L299) | 299 | `"        return \"\""` | — |
| [SRC-686F71AA50-L000300](../../agents/task_understanding.py#L300) | 300 | `"    text = unicodedata.normalize(\"NFKC\", value).casefold()"` | — |
| [SRC-686F71AA50-L000301](../../agents/task_understanding.py#L301) | 301 | `"    text = _ARABIC_DIACRITICS.sub(\"\", text)"` | — |
| [SRC-686F71AA50-L000302](../../agents/task_understanding.py#L302) | 302 | `"    text = text.replace(\"ـ\", \"\").translate(str.maketrans({"` | — |
| [SRC-686F71AA50-L000303](../../agents/task_understanding.py#L303) | 303 | `"        \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\", \"ة\": \"ه\","` | — |
| [SRC-686F71AA50-L000304](../../agents/task_understanding.py#L304) | 304 | `"    }))"` | — |
| [SRC-686F71AA50-L000305](../../agents/task_understanding.py#L305) | 305 | `"    return _SPACE.sub(\" \", _PUNCTUATION.sub(\" \", text)).strip()"` | — |
| [SRC-686F71AA50-L000306](../../agents/task_understanding.py#L306) | 306 | `""` | — |
| [SRC-686F71AA50-L000307](../../agents/task_understanding.py#L307) | 307 | `""` | — |
| [SRC-686F71AA50-L000308](../../agents/task_understanding.py#L308) | 308 | `"def _contains(text: str, phrases: tuple[str, ...]) -> list[str]:"` | — |
| [SRC-686F71AA50-L000309](../../agents/task_understanding.py#L309) | 309 | `"    \"\"\"Match phrases on token boundaries with conservative Arabic clitic handling."` | — |
| [SRC-686F71AA50-L000310](../../agents/task_understanding.py#L310) | 310 | `""` | — |
| [SRC-686F71AA50-L000311](../../agents/task_understanding.py#L311) | 311 | `"    The matcher never accepts arbitrary substrings: variants are formed only by"` | — |
| [SRC-686F71AA50-L000312](../../agents/task_understanding.py#L312) | 312 | `"    removing a short, explicit list of common prefixes/suffixes. This avoids"` | — |
| [SRC-686F71AA50-L000313](../../agents/task_understanding.py#L313) | 313 | `"    collisions such as treating \"الإنذار\" as \"الآن\"."` | — |
| [SRC-686F71AA50-L000314](../../agents/task_understanding.py#L314) | 314 | `"    \"\"\""` | — |
| [SRC-686F71AA50-L000315](../../agents/task_understanding.py#L315) | 315 | `"    tokens = _TOKEN_RE.findall(text)"` | — |
| [SRC-686F71AA50-L000316](../../agents/task_understanding.py#L316) | 316 | `"    matched: list[str] = []"` | — |
| [SRC-686F71AA50-L000317](../../agents/task_understanding.py#L317) | 317 | `"    prefixes = (\"وال\", \"بال\", \"فال\", \"كال\", \"لل\", \"ال\", \"و\", \"ف\", \"ب\", \"ل\", \"ك\")"` | — |
| [SRC-686F71AA50-L000318](../../agents/task_understanding.py#L318) | 318 | `"    suffixes = (\"هما\", \"هم\", \"هن\", \"ها\", \"ه\", \"كم\", \"كن\", \"ك\", \"نا\", \"ني\", \"ين\", \"ات\", \"ون\")"` | — |
| [SRC-686F71AA50-L000319](../../agents/task_understanding.py#L319) | 319 | `"    english_suffixes = (\"ing\", \"ed\", \"es\", \"s\")"` | — |
| [SRC-686F71AA50-L000320](../../agents/task_understanding.py#L320) | 320 | `"    cache: dict[str, set[str]] = {}"` | — |
| [SRC-686F71AA50-L000321](../../agents/task_understanding.py#L321) | 321 | `""` | — |
| [SRC-686F71AA50-L000322](../../agents/task_understanding.py#L322) | 322 | `"    def token_forms(raw_token: str) -> set[str]:"` | — |
| [SRC-686F71AA50-L000323](../../agents/task_understanding.py#L323) | 323 | `"        original = normalize_text(raw_token)"` | — |
| [SRC-686F71AA50-L000324](../../agents/task_understanding.py#L324) | 324 | `"        if original in cache:"` | — |
| [SRC-686F71AA50-L000325](../../agents/task_understanding.py#L325) | 325 | `"            return cache[original]"` | — |
| [SRC-686F71AA50-L000326](../../agents/task_understanding.py#L326) | 326 | `"        forms = {original} if original else set()"` | — |
| [SRC-686F71AA50-L000327](../../agents/task_understanding.py#L327) | 327 | `"        queue = list(forms)"` | — |
| [SRC-686F71AA50-L000328](../../agents/task_understanding.py#L328) | 328 | `"        while queue:"` | — |
| [SRC-686F71AA50-L000329](../../agents/task_understanding.py#L329) | 329 | `"            current = queue.pop()"` | — |
| [SRC-686F71AA50-L000330](../../agents/task_understanding.py#L330) | 330 | `"            for prefix in prefixes:"` | — |
| [SRC-686F71AA50-L000331](../../agents/task_understanding.py#L331) | 331 | `"                if current.startswith(prefix) and len(current) - len(prefix) >= 3:"` | — |
| [SRC-686F71AA50-L000332](../../agents/task_understanding.py#L332) | 332 | `"                    candidate = current[len(prefix):]"` | — |
| [SRC-686F71AA50-L000333](../../agents/task_understanding.py#L333) | 333 | `"                    if candidate not in forms:"` | — |
| [SRC-686F71AA50-L000334](../../agents/task_understanding.py#L334) | 334 | `"                        forms.add(candidate)"` | — |
| [SRC-686F71AA50-L000335](../../agents/task_understanding.py#L335) | 335 | `"                        queue.append(candidate)"` | — |
| [SRC-686F71AA50-L000336](../../agents/task_understanding.py#L336) | 336 | `"            for suffix in suffixes:"` | — |
| [SRC-686F71AA50-L000337](../../agents/task_understanding.py#L337) | 337 | `"                if current.endswith(suffix) and len(current) - len(suffix) >= 3:"` | — |
| [SRC-686F71AA50-L000338](../../agents/task_understanding.py#L338) | 338 | `"                    candidate = current[:-len(suffix)]"` | — |
| [SRC-686F71AA50-L000339](../../agents/task_understanding.py#L339) | 339 | `"                    if candidate not in forms:"` | — |
| [SRC-686F71AA50-L000340](../../agents/task_understanding.py#L340) | 340 | `"                        forms.add(candidate)"` | — |
| [SRC-686F71AA50-L000341](../../agents/task_understanding.py#L341) | 341 | `"                        queue.append(candidate)"` | — |
| [SRC-686F71AA50-L000342](../../agents/task_understanding.py#L342) | 342 | `"            if current.isascii() and len(current) >= 5:"` | — |
| [SRC-686F71AA50-L000343](../../agents/task_understanding.py#L343) | 343 | `"                for suffix in english_suffixes:"` | — |
| [SRC-686F71AA50-L000344](../../agents/task_understanding.py#L344) | 344 | `"                    if current.endswith(suffix) and len(current) - len(suffix) >= 3:"` | — |
| [SRC-686F71AA50-L000345](../../agents/task_understanding.py#L345) | 345 | `"                        candidate = current[:-len(suffix)]"` | — |
| [SRC-686F71AA50-L000346](../../agents/task_understanding.py#L346) | 346 | `"                        if candidate not in forms:"` | — |
| [SRC-686F71AA50-L000347](../../agents/task_understanding.py#L347) | 347 | `"                            forms.add(candidate)"` | — |
| [SRC-686F71AA50-L000348](../../agents/task_understanding.py#L348) | 348 | `"                            queue.append(candidate)"` | — |
| [SRC-686F71AA50-L000349](../../agents/task_understanding.py#L349) | 349 | `"        cache[original] = forms"` | — |
| [SRC-686F71AA50-L000350](../../agents/task_understanding.py#L350) | 350 | `"        return forms"` | — |
| [SRC-686F71AA50-L000351](../../agents/task_understanding.py#L351) | 351 | `""` | — |
| [SRC-686F71AA50-L000352](../../agents/task_understanding.py#L352) | 352 | `"    token_forms_cache = [token_forms(token) for token in tokens]"` | — |
| [SRC-686F71AA50-L000353](../../agents/task_understanding.py#L353) | 353 | `"    for phrase in phrases:"` | — |
| [SRC-686F71AA50-L000354](../../agents/task_understanding.py#L354) | 354 | `"        normalized = normalize_text(phrase)"` | — |
| [SRC-686F71AA50-L000355](../../agents/task_understanding.py#L355) | 355 | `"        phrase_tokens = _TOKEN_RE.findall(normalized)"` | — |
| [SRC-686F71AA50-L000356](../../agents/task_understanding.py#L356) | 356 | `"        if not phrase_tokens:"` | — |
| [SRC-686F71AA50-L000357](../../agents/task_understanding.py#L357) | 357 | `"            continue"` | — |
| [SRC-686F71AA50-L000358](../../agents/task_understanding.py#L358) | 358 | `"        phrase_forms = [token_forms(token) for token in phrase_tokens]"` | — |
| [SRC-686F71AA50-L000359](../../agents/task_understanding.py#L359) | 359 | `"        width = len(phrase_tokens)"` | — |
| [SRC-686F71AA50-L000360](../../agents/task_understanding.py#L360) | 360 | `"        found = any("` | — |
| [SRC-686F71AA50-L000361](../../agents/task_understanding.py#L361) | 361 | `"            all(token_forms_cache[index + offset] & phrase_forms[offset] for offset in range(width))"` | — |
| [SRC-686F71AA50-L000362](../../agents/task_understanding.py#L362) | 362 | `"            for index in range(max(0, len(tokens) - width + 1))"` | — |
| [SRC-686F71AA50-L000363](../../agents/task_understanding.py#L363) | 363 | `"        )"` | — |
| [SRC-686F71AA50-L000364](../../agents/task_understanding.py#L364) | 364 | `"        if found and normalized not in matched:"` | — |
| [SRC-686F71AA50-L000365](../../agents/task_understanding.py#L365) | 365 | `"            matched.append(normalized)"` | — |
| [SRC-686F71AA50-L000366](../../agents/task_understanding.py#L366) | 366 | `"    return matched"` | — |
| [SRC-686F71AA50-L000367](../../agents/task_understanding.py#L367) | 367 | `""` | — |
| [SRC-686F71AA50-L000368](../../agents/task_understanding.py#L368) | 368 | `"def _has_inline_summary_text(question: str) -> bool:"` | — |
| [SRC-686F71AA50-L000369](../../agents/task_understanding.py#L369) | 369 | `"    \"\"\"Detect explicitly supplied summary text without treating a URL as pasted content.\"\"\""` | — |
| [SRC-686F71AA50-L000370](../../agents/task_understanding.py#L370) | 370 | `"    if not isinstance(question, str) or _URL_RE.search(question):"` | — |
| [SRC-686F71AA50-L000371](../../agents/task_understanding.py#L371) | 371 | `"        return False"` | — |
| [SRC-686F71AA50-L000372](../../agents/task_understanding.py#L372) | 372 | `"    normalized = normalize_text(question)"` | — |
| [SRC-686F71AA50-L000373](../../agents/task_understanding.py#L373) | 373 | `"    markers = ("` | — |
| [SRC-686F71AA50-L000374](../../agents/task_understanding.py#L374) | 374 | `"        \"النص التالي\", \"النص الاتي\", \"النص ده\", \"النص اللي جاي\","` | — |
| [SRC-686F71AA50-L000375](../../agents/task_understanding.py#L375) | 375 | `"        \"المحتوى التالي\", \"هذا النص\", \"following text\", \"the following text\","` | — |
| [SRC-686F71AA50-L000376](../../agents/task_understanding.py#L376) | 376 | `"        \"text below\", \"content below\", \"this text\","` | — |
| [SRC-686F71AA50-L000377](../../agents/task_understanding.py#L377) | 377 | `"    )"` | — |
| [SRC-686F71AA50-L000378](../../agents/task_understanding.py#L378) | 378 | `"    for marker in markers:"` | — |
| [SRC-686F71AA50-L000379](../../agents/task_understanding.py#L379) | 379 | `"        candidate = normalize_text(marker)"` | — |
| [SRC-686F71AA50-L000380](../../agents/task_understanding.py#L380) | 380 | `"        if candidate and candidate in normalized:"` | — |
| [SRC-686F71AA50-L000381](../../agents/task_understanding.py#L381) | 381 | `"            remainder = normalized.split(candidate, 1)[1].strip()"` | — |
| [SRC-686F71AA50-L000382](../../agents/task_understanding.py#L382) | 382 | `"            if len(remainder) >= 8:"` | — |
| [SRC-686F71AA50-L000383](../../agents/task_understanding.py#L383) | 383 | `"                return True"` | — |
| [SRC-686F71AA50-L000384](../../agents/task_understanding.py#L384) | 384 | `"    return bool("` | — |
| [SRC-686F71AA50-L000385](../../agents/task_understanding.py#L385) | 385 | `"        re.search("` | — |
| [SRC-686F71AA50-L000386](../../agents/task_understanding.py#L386) | 386 | `"            r\"^\\s*(?:لخص(?:\\s+لي)?\|تلخيص\|summari[sz]e\|summary)\\s*[:：]\\s*\\S.{12,}$\","` | — |
| [SRC-686F71AA50-L000387](../../agents/task_understanding.py#L387) | 387 | `"            question,"` | — |
| [SRC-686F71AA50-L000388](../../agents/task_understanding.py#L388) | 388 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-686F71AA50-L000389](../../agents/task_understanding.py#L389) | 389 | `"        )"` | — |
| [SRC-686F71AA50-L000390](../../agents/task_understanding.py#L390) | 390 | `"    )"` | — |
| [SRC-686F71AA50-L000391](../../agents/task_understanding.py#L391) | 391 | `""` | — |
| [SRC-686F71AA50-L000392](../../agents/task_understanding.py#L392) | 392 | `""` | — |
| [SRC-686F71AA50-L000393](../../agents/task_understanding.py#L393) | 393 | `"def _has_official_site_target(question: str) -> bool:"` | — |
| [SRC-686F71AA50-L000394](../../agents/task_understanding.py#L394) | 394 | `"    \"\"\"Conservatively check whether an official-site request names a target.\"\"\""` | — |
| [SRC-686F71AA50-L000395](../../agents/task_understanding.py#L395) | 395 | `"    normalized = normalize_text(question)"` | — |
| [SRC-686F71AA50-L000396](../../agents/task_understanding.py#L396) | 396 | `"    for phrase in _PATTERNS[\"official_site_lookup\"]:"` | — |
| [SRC-686F71AA50-L000397](../../agents/task_understanding.py#L397) | 397 | `"        normalized = normalized.replace(normalize_text(phrase), \" \")"` | — |
| [SRC-686F71AA50-L000398](../../agents/task_understanding.py#L398) | 398 | `"    action_phrases = ("` | — |
| [SRC-686F71AA50-L000399](../../agents/task_understanding.py#L399) | 399 | `"        \"من فضلك\", \"لو سمحت\", \"اريد\", \"عايز\", \"عاوزه\", \"ابحث لي عن\","` | — |
| [SRC-686F71AA50-L000400](../../agents/task_understanding.py#L400) | 400 | `"        \"ابحث عن\", \"هات لي\", \"هاتلي\", \"هات\", \"اعثر على\", \"دور على\", \"دورلي على\","` | — |
| [SRC-686F71AA50-L000401](../../agents/task_understanding.py#L401) | 401 | `"        \"find\", \"search for\", \"look up\", \"please\", \"can you\", \"could you\", \"get me\","` | — |
| [SRC-686F71AA50-L000402](../../agents/task_understanding.py#L402) | 402 | `"        \"the\", \"of\", \"for\", \"government\","` | — |
| [SRC-686F71AA50-L000403](../../agents/task_understanding.py#L403) | 403 | `"    )"` | — |
| [SRC-686F71AA50-L000404](../../agents/task_understanding.py#L404) | 404 | `"    for phrase in action_phrases:"` | — |
| [SRC-686F71AA50-L000405](../../agents/task_understanding.py#L405) | 405 | `"        normalized = re.sub("` | — |
| [SRC-686F71AA50-L000406](../../agents/task_understanding.py#L406) | 406 | `"            rf\"(?<!\\w){re.escape(normalize_text(phrase))}(?!\\w)\", \" \", normalized"` | — |
| [SRC-686F71AA50-L000407](../../agents/task_understanding.py#L407) | 407 | `"        )"` | — |
| [SRC-686F71AA50-L000408](../../agents/task_understanding.py#L408) | 408 | `"    generic_target_words = {"` | — |
| [SRC-686F71AA50-L000409](../../agents/task_understanding.py#L409) | 409 | `"        \"الموقع\", \"موقع\", \"الرابط\", \"رابط\", \"لينك\", \"الصفحه\", \"صفحه\","` | — |
| [SRC-686F71AA50-L000410](../../agents/task_understanding.py#L410) | 410 | `"        \"رسمي\", \"الرسمي\", \"الرسمى\", \"حكومي\", \"الحكومي\","` | — |
| [SRC-686F71AA50-L000411](../../agents/task_understanding.py#L411) | 411 | `"        \"وزاره\", \"هيئه\", \"جهة\", \"جهه\", \"حكوميه\","` | — |
| [SRC-686F71AA50-L000412](../../agents/task_understanding.py#L412) | 412 | `"        \"شركه\", \"الشركه\", \"مؤسسه\", \"المؤسسه\", \"بنك\", \"البنك\","` | — |
| [SRC-686F71AA50-L000413](../../agents/task_understanding.py#L413) | 413 | `"        \"منظمه\", \"المنظمه\", \"مصلحه\", \"المصلحه\", \"اداره\", \"الاداره\","` | — |
| [SRC-686F71AA50-L000414](../../agents/task_understanding.py#L414) | 414 | `"        \"وزارة\", \"شركة\", \"الشركة\", \"مؤسسة\", \"الهيئة\", \"الحكومية\","` | — |
| [SRC-686F71AA50-L000415](../../agents/task_understanding.py#L415) | 415 | `"        \"website\", \"site\", \"homepage\", \"official\", \"ministry\", \"agency\","` | — |
| [SRC-686F71AA50-L000416](../../agents/task_understanding.py#L416) | 416 | `"        \"department\", \"organization\", \"organisation\", \"company\", \"bank\","` | — |
| [SRC-686F71AA50-L000417](../../agents/task_understanding.py#L417) | 417 | `"        \"authority\", \"portal\", \"url\", \"link\", \"gov\", \"the\","` | — |
| [SRC-686F71AA50-L000418](../../agents/task_understanding.py#L418) | 418 | `"    }"` | — |
| [SRC-686F71AA50-L000419](../../agents/task_understanding.py#L419) | 419 | `"    ignored = {normalize_text(word) for word in generic_target_words}"` | — |
| [SRC-686F71AA50-L000420](../../agents/task_understanding.py#L420) | 420 | `"    for raw_token in _TOKEN_RE.findall(normalized):"` | — |
| [SRC-686F71AA50-L000421](../../agents/task_understanding.py#L421) | 421 | `"        token = normalize_text(raw_token)"` | — |
| [SRC-686F71AA50-L000422](../../agents/task_understanding.py#L422) | 422 | `"        changed = True"` | — |
| [SRC-686F71AA50-L000423](../../agents/task_understanding.py#L423) | 423 | `"        while changed:"` | — |
| [SRC-686F71AA50-L000424](../../agents/task_understanding.py#L424) | 424 | `"            changed = False"` | — |
| [SRC-686F71AA50-L000425](../../agents/task_understanding.py#L425) | 425 | `"            for prefix in (\"وال\", \"بال\", \"فال\", \"كال\", \"لل\", \"ال\", \"و\", \"ف\", \"ب\", \"ل\", \"ك\"):"` | — |
| [SRC-686F71AA50-L000426](../../agents/task_understanding.py#L426) | 426 | `"                if token.startswith(prefix) and len(token) - len(prefix) >= 3:"` | — |
| [SRC-686F71AA50-L000427](../../agents/task_understanding.py#L427) | 427 | `"                    token = token[len(prefix):]"` | — |
| [SRC-686F71AA50-L000428](../../agents/task_understanding.py#L428) | 428 | `"                    changed = True"` | — |
| [SRC-686F71AA50-L000429](../../agents/task_understanding.py#L429) | 429 | `"                    break"` | — |
| [SRC-686F71AA50-L000430](../../agents/task_understanding.py#L430) | 430 | `"        if token and token not in ignored and len(token) >= 2:"` | — |
| [SRC-686F71AA50-L000431](../../agents/task_understanding.py#L431) | 431 | `"            return True"` | — |
| [SRC-686F71AA50-L000432](../../agents/task_understanding.py#L432) | 432 | `"    return False"` | — |
| [SRC-686F71AA50-L000433](../../agents/task_understanding.py#L433) | 433 | `""` | — |
| [SRC-686F71AA50-L000434](../../agents/task_understanding.py#L434) | 434 | `""` | — |
| [SRC-686F71AA50-L000435](../../agents/task_understanding.py#L435) | 435 | `"def _extract_explicit_locations(question: str) -> list[str]:"` | — |
| [SRC-686F71AA50-L000436](../../agents/task_understanding.py#L436) | 436 | `"    \"\"\"Return only a small, explicit location vocabulary; never infer geolocation.\"\"\""` | — |
| [SRC-686F71AA50-L000437](../../agents/task_understanding.py#L437) | 437 | `"    normalized = normalize_text(question)"` | — |
| [SRC-686F71AA50-L000438](../../agents/task_understanding.py#L438) | 438 | `"    known = ("` | — |
| [SRC-686F71AA50-L000439](../../agents/task_understanding.py#L439) | 439 | `"        (\"مصر\", (\"في مصر\", \"داخل مصر\", \"المصري\", \"المصرية\", \"مصر\", \"egypt\", \"egyptian\")),"` | — |
| [SRC-686F71AA50-L000440](../../agents/task_understanding.py#L440) | 440 | `"        (\"القاهرة\", (\"القاهرة\", \"القاهره\", \"cairo\")),"` | — |
| [SRC-686F71AA50-L000441](../../agents/task_understanding.py#L441) | 441 | `"        (\"الإسكندرية\", (\"الاسكندرية\", \"الاسكندريه\", \"alexandria\")),"` | — |
| [SRC-686F71AA50-L000442](../../agents/task_understanding.py#L442) | 442 | `"        (\"السعودية\", (\"السعودية\", \"السعوديه\", \"saudi arabia\")),"` | — |
| [SRC-686F71AA50-L000443](../../agents/task_understanding.py#L443) | 443 | `"        (\"الإمارات\", (\"الامارات\", \"uae\", \"united arab emirates\")),"` | — |
| [SRC-686F71AA50-L000444](../../agents/task_understanding.py#L444) | 444 | `"        (\"المملكة المتحدة\", (\"المملكة المتحدة\", \"united kingdom\", \"the uk\")),"` | — |
| [SRC-686F71AA50-L000445](../../agents/task_understanding.py#L445) | 445 | `"        (\"الولايات المتحدة\", (\"الولايات المتحدة\", \"united states\", \"the us\")),"` | — |
| [SRC-686F71AA50-L000446](../../agents/task_understanding.py#L446) | 446 | `"    )"` | — |
| [SRC-686F71AA50-L000447](../../agents/task_understanding.py#L447) | 447 | `"    result: list[str] = []"` | — |
| [SRC-686F71AA50-L000448](../../agents/task_understanding.py#L448) | 448 | `"    for canonical, cues in known:"` | — |
| [SRC-686F71AA50-L000449](../../agents/task_understanding.py#L449) | 449 | `"        if any(_contains(normalized, (cue,)) for cue in cues):"` | — |
| [SRC-686F71AA50-L000450](../../agents/task_understanding.py#L450) | 450 | `"            result.append(canonical)"` | — |
| [SRC-686F71AA50-L000451](../../agents/task_understanding.py#L451) | 451 | `"    return result"` | — |
| [SRC-686F71AA50-L000452](../../agents/task_understanding.py#L452) | 452 | `""` | — |
| [SRC-686F71AA50-L000453](../../agents/task_understanding.py#L453) | 453 | `""` | — |
| [SRC-686F71AA50-L000454](../../agents/task_understanding.py#L454) | 454 | `"def _language_profile(question: str) -> str:"` | — |
| [SRC-686F71AA50-L000455](../../agents/task_understanding.py#L455) | 455 | `"    arabic = len(re.findall(r\"[\\u0600-\\u06FF]\", question))"` | — |
| [SRC-686F71AA50-L000456](../../agents/task_understanding.py#L456) | 456 | `"    latin = len(re.findall(r\"[A-Za-z]\", question))"` | — |
| [SRC-686F71AA50-L000457](../../agents/task_understanding.py#L457) | 457 | `"    if arabic and latin:"` | — |
| [SRC-686F71AA50-L000458](../../agents/task_understanding.py#L458) | 458 | `"        return \"mixed\""` | — |
| [SRC-686F71AA50-L000459](../../agents/task_understanding.py#L459) | 459 | `"    if arabic:"` | — |
| [SRC-686F71AA50-L000460](../../agents/task_understanding.py#L460) | 460 | `"        return \"ar\""` | — |
| [SRC-686F71AA50-L000461](../../agents/task_understanding.py#L461) | 461 | `"    if latin:"` | — |
| [SRC-686F71AA50-L000462](../../agents/task_understanding.py#L462) | 462 | `"        return \"en\""` | — |
| [SRC-686F71AA50-L000463](../../agents/task_understanding.py#L463) | 463 | `"    return \"und\""` | — |
| [SRC-686F71AA50-L000464](../../agents/task_understanding.py#L464) | 464 | `""` | — |
| [SRC-686F71AA50-L000465](../../agents/task_understanding.py#L465) | 465 | `""` | — |
| [SRC-686F71AA50-L000466](../../agents/task_understanding.py#L466) | 466 | `"def _primary_family(matches: dict[str, list[str]], mode: str, route: str, normalized: str) -> str:"` | — |
| [SRC-686F71AA50-L000467](../../agents/task_understanding.py#L467) | 467 | `"    # An explicit official-destination request is different from a request for an"` | — |
| [SRC-686F71AA50-L000468](../../agents/task_understanding.py#L468) | 468 | `"    # article mentioning the organization; government verification is a separate slot."` | — |
| [SRC-686F71AA50-L000469](../../agents/task_understanding.py#L469) | 469 | `"    if matches[\"official_site_lookup\"]:"` | — |
| [SRC-686F71AA50-L000470](../../agents/task_understanding.py#L470) | 470 | `"        return \"official_site_lookup\""` | — |
| [SRC-686F71AA50-L000471](../../agents/task_understanding.py#L471) | 471 | `"    for family in ("` | — |
| [SRC-686F71AA50-L000472](../../agents/task_understanding.py#L472) | 472 | `"        \"social_opinions\", \"summarize\", \"troubleshoot\", \"compare\","` | — |
| [SRC-686F71AA50-L000473](../../agents/task_understanding.py#L473) | 473 | `"        \"medical_information\", \"legal_information\", \"coding_or_technical_design\","` | — |
| [SRC-686F71AA50-L000474](../../agents/task_understanding.py#L474) | 474 | `"        \"data_analysis\", \"translation\", \"calculation\", \"planning\","` | — |
| [SRC-686F71AA50-L000475](../../agents/task_understanding.py#L475) | 475 | `"        \"creative_generation\", \"writing_or_editing\", \"lead_generation\","` | — |
| [SRC-686F71AA50-L000476](../../agents/task_understanding.py#L476) | 476 | `"        \"how_to\", \"recommendation\", \"current_information\", \"find_or_discover\","` | — |
| [SRC-686F71AA50-L000477](../../agents/task_understanding.py#L477) | 477 | `"        \"explain_or_define\", \"general_research\","` | — |
| [SRC-686F71AA50-L000478](../../agents/task_understanding.py#L478) | 478 | `"    ):"` | — |
| [SRC-686F71AA50-L000479](../../agents/task_understanding.py#L479) | 479 | `"        if matches.get(family):"` | — |
| [SRC-686F71AA50-L000480](../../agents/task_understanding.py#L480) | 480 | `"            return family"` | — |
| [SRC-686F71AA50-L000481](../../agents/task_understanding.py#L481) | 481 | `"    if route == \"CLARIFY\":"` | — |
| [SRC-686F71AA50-L000482](../../agents/task_understanding.py#L482) | 482 | `"        return \"ambiguous_or_incomplete\""` | — |
| [SRC-686F71AA50-L000483](../../agents/task_understanding.py#L483) | 483 | `"    if route in {\"WEB_SIMPLE\", \"WEB_DEEP\", \"LEAD_GENERATION\"} or mode != \"auto\":"` | — |
| [SRC-686F71AA50-L000484](../../agents/task_understanding.py#L484) | 484 | `"        return \"web_research\""` | — |
| [SRC-686F71AA50-L000485](../../agents/task_understanding.py#L485) | 485 | `"    return \"general_question\""` | — |
| [SRC-686F71AA50-L000486](../../agents/task_understanding.py#L486) | 486 | `""` | — |
| [SRC-686F71AA50-L000487](../../agents/task_understanding.py#L487) | 487 | `""` | — |
| [SRC-686F71AA50-L000488](../../agents/task_understanding.py#L488) | 488 | `"def build_task_spec("` | — |
| [SRC-686F71AA50-L000489](../../agents/task_understanding.py#L489) | 489 | `"    question: str,"` | — |
| [SRC-686F71AA50-L000490](../../agents/task_understanding.py#L490) | 490 | `"    *,"` | — |
| [SRC-686F71AA50-L000491](../../agents/task_understanding.py#L491) | 491 | `"    mode: str = \"auto\","` | — |
| [SRC-686F71AA50-L000492](../../agents/task_understanding.py#L492) | 492 | `"    intent_route: str = \"\","` | — |
| [SRC-686F71AA50-L000493](../../agents/task_understanding.py#L493) | 493 | `"    plan: dict[str, Any] \| None = None,"` | — |
| [SRC-686F71AA50-L000494](../../agents/task_understanding.py#L494) | 494 | `"    dialogue_context: dict[str, Any] \| None = None,"` | — |
| [SRC-686F71AA50-L000495](../../agents/task_understanding.py#L495) | 495 | `") -> dict[str, Any]:"` | — |
| [SRC-686F71AA50-L000496](../../agents/task_understanding.py#L496) | 496 | `"    \"\"\"Build a bounded task specification, interpretation hypotheses, and test matrix.\"\"\""` | — |
| [SRC-686F71AA50-L000497](../../agents/task_understanding.py#L497) | 497 | `"    raw = question if isinstance(question, str) else \"\""` | — |
| [SRC-686F71AA50-L000498](../../agents/task_understanding.py#L498) | 498 | `"    raw = raw[:MAX_TASK_CHARS]"` | — |
| [SRC-686F71AA50-L000499](../../agents/task_understanding.py#L499) | 499 | `"    normalized = normalize_text(raw)"` | — |
| [SRC-686F71AA50-L000500](../../agents/task_understanding.py#L500) | 500 | `"    clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-686F71AA50-L000501](../../agents/task_understanding.py#L501) | 501 | `"    if clean_mode not in SUPPORTED_MODES:"` | — |
| [SRC-686F71AA50-L000502](../../agents/task_understanding.py#L502) | 502 | `"        clean_mode = \"auto\""` | — |
| [SRC-686F71AA50-L000503](../../agents/task_understanding.py#L503) | 503 | `"    matches = {"` | — |
| [SRC-686F71AA50-L000504](../../agents/task_understanding.py#L504) | 504 | `"        family: _contains(normalized, phrases)"` | — |
| [SRC-686F71AA50-L000505](../../agents/task_understanding.py#L505) | 505 | `"        for family, phrases in _PATTERNS.items()"` | — |
| [SRC-686F71AA50-L000506](../../agents/task_understanding.py#L506) | 506 | `"        if not family.startswith(\"output_\")"` | — |
| [SRC-686F71AA50-L000507](../../agents/task_understanding.py#L507) | 507 | `"    }"` | — |
| [SRC-686F71AA50-L000508](../../agents/task_understanding.py#L508) | 508 | `"    output_matches = {"` | — |
| [SRC-686F71AA50-L000509](../../agents/task_understanding.py#L509) | 509 | `"        family: _contains(normalized, phrases)"` | — |
| [SRC-686F71AA50-L000510](../../agents/task_understanding.py#L510) | 510 | `"        for family, phrases in _PATTERNS.items()"` | — |
| [SRC-686F71AA50-L000511](../../agents/task_understanding.py#L511) | 511 | `"        if family.startswith(\"output_\")"` | — |
| [SRC-686F71AA50-L000512](../../agents/task_understanding.py#L512) | 512 | `"    }"` | — |
| [SRC-686F71AA50-L000513](../../agents/task_understanding.py#L513) | 513 | `"    aspect_values: list[str] = []"` | — |
| [SRC-686F71AA50-L000514](../../agents/task_understanding.py#L514) | 514 | `"    try:"` | — |
| [SRC-686F71AA50-L000515](../../agents/task_understanding.py#L515) | 515 | `"        from agents.aspect_planning import extract_aspects"` | — |
| [SRC-686F71AA50-L000516](../../agents/task_understanding.py#L516) | 516 | `"        aspect_values = extract_aspects(raw)[:MAX_TASK_ASPECTS]"` | — |
| [SRC-686F71AA50-L000517](../../agents/task_understanding.py#L517) | 517 | `"    except (ImportError, TypeError, ValueError):"` | — |
| [SRC-686F71AA50-L000518](../../agents/task_understanding.py#L518) | 518 | `"        aspect_values = []"` | — |
| [SRC-686F71AA50-L000519](../../agents/task_understanding.py#L519) | 519 | `""` | — |
| [SRC-686F71AA50-L000520](../../agents/task_understanding.py#L520) | 520 | `"    official_destination = bool(matches[\"official_site_lookup\"])"` | — |
| [SRC-686F71AA50-L000521](../../agents/task_understanding.py#L521) | 521 | `"    government_official_site = bool("` | — |
| [SRC-686F71AA50-L000522](../../agents/task_understanding.py#L522) | 522 | `"        official_destination"` | — |
| [SRC-686F71AA50-L000523](../../agents/task_understanding.py#L523) | 523 | `"        and bool(_contains(normalized, _OFFICIAL_WORDS))"` | — |
| [SRC-686F71AA50-L000524](../../agents/task_understanding.py#L524) | 524 | `"    )"` | — |
| [SRC-686F71AA50-L000525](../../agents/task_understanding.py#L525) | 525 | `"    navigation = official_destination or bool("` | — |
| [SRC-686F71AA50-L000526](../../agents/task_understanding.py#L526) | 526 | `"        _URL_RE.search(raw)"` | — |
| [SRC-686F71AA50-L000527](../../agents/task_understanding.py#L527) | 527 | `"        or any(normalize_text(term) in normalized for term in (\"هات رابط\", \"website\", \"homepage\"))"` | — |
| [SRC-686F71AA50-L000528](../../agents/task_understanding.py#L528) | 528 | `"    )"` | — |
| [SRC-686F71AA50-L000529](../../agents/task_understanding.py#L529) | 529 | `"    explicit_freshness = bool(_contains(normalized, _FRESHNESS_CUES))"` | — |
| [SRC-686F71AA50-L000530](../../agents/task_understanding.py#L530) | 530 | `"    current_required = (clean_mode == \"latest\" or explicit_freshness) and not navigation"` | — |
| [SRC-686F71AA50-L000531](../../agents/task_understanding.py#L531) | 531 | `"    social_required = clean_mode == \"social\" or bool(matches[\"social_opinions\"])"` | — |
| [SRC-686F71AA50-L000532](../../agents/task_understanding.py#L532) | 532 | `"    family = _primary_family(matches, clean_mode, intent_route, normalized)"` | — |
| [SRC-686F71AA50-L000533](../../agents/task_understanding.py#L533) | 533 | `""` | — |
| [SRC-686F71AA50-L000534](../../agents/task_understanding.py#L534) | 534 | `"    if family == \"official_site_lookup\":"` | — |
| [SRC-686F71AA50-L000535](../../agents/task_understanding.py#L535) | 535 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000536](../../agents/task_understanding.py#L536) | 536 | `"            \"target_entity_match\","` | — |
| [SRC-686F71AA50-L000537](../../agents/task_understanding.py#L537) | 537 | `"            \"official_domain_or_independently_linked_official_destination\","` | — |
| [SRC-686F71AA50-L000538](../../agents/task_understanding.py#L538) | 538 | `"            \"never_substitute_an_article_or_unrelated_directory\","` | — |
| [SRC-686F71AA50-L000539](../../agents/task_understanding.py#L539) | 539 | `"        ]"` | — |
| [SRC-686F71AA50-L000540](../../agents/task_understanding.py#L540) | 540 | `"        query_strategies = [\"exact_entity\", \"official_domain\", \"government_portal_cross_check\"]"` | — |
| [SRC-686F71AA50-L000541](../../agents/task_understanding.py#L541) | 541 | `"    elif family == \"social_opinions\":"` | — |
| [SRC-686F71AA50-L000542](../../agents/task_understanding.py#L542) | 542 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000543](../../agents/task_understanding.py#L543) | 543 | `"            \"public_social_platform_url\","` | — |
| [SRC-686F71AA50-L000544](../../agents/task_understanding.py#L544) | 544 | `"            \"original_post_or_readable_post_content_when_available\","` | — |
| [SRC-686F71AA50-L000545](../../agents/task_understanding.py#L545) | 545 | `"            \"heuristic_classification_is_not_identity_or_truth_verification\","` | — |
| [SRC-686F71AA50-L000546](../../agents/task_understanding.py#L546) | 546 | `"        ]"` | — |
| [SRC-686F71AA50-L000547](../../agents/task_understanding.py#L547) | 547 | `"        query_strategies = [\"topic_platform\", \"personal_experience\", \"discussion\", \"commercial_exclusion\"]"` | — |
| [SRC-686F71AA50-L000548](../../agents/task_understanding.py#L548) | 548 | `"    elif family == \"summarize\":"` | — |
| [SRC-686F71AA50-L000549](../../agents/task_understanding.py#L549) | 549 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000550](../../agents/task_understanding.py#L550) | 550 | `"            \"read_the_requested_text_or_page\","` | — |
| [SRC-686F71AA50-L000551](../../agents/task_understanding.py#L551) | 551 | `"            \"do_not_summarize_unread_content_from_title_only\","` | — |
| [SRC-686F71AA50-L000552](../../agents/task_understanding.py#L552) | 552 | `"            \"preserve_source_scope_and_important_qualifiers\","` | — |
| [SRC-686F71AA50-L000553](../../agents/task_understanding.py#L553) | 553 | `"        ]"` | — |
| [SRC-686F71AA50-L000554](../../agents/task_understanding.py#L554) | 554 | `"        query_strategies = [\"exact_url_or_supplied_text\", \"page_read\", \"scope_preserving_summary\"]"` | — |
| [SRC-686F71AA50-L000555](../../agents/task_understanding.py#L555) | 555 | `"    elif family == \"troubleshoot\":"` | — |
| [SRC-686F71AA50-L000556](../../agents/task_understanding.py#L556) | 556 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000557](../../agents/task_understanding.py#L557) | 557 | `"            \"preserve_error_message_and_environment\","` | — |
| [SRC-686F71AA50-L000558](../../agents/task_understanding.py#L558) | 558 | `"            \"prefer_manual_or_primary_technical_source\","` | — |
| [SRC-686F71AA50-L000559](../../agents/task_understanding.py#L559) | 559 | `"            \"separate_diagnosis_hypotheses_from_confirmed_cause\","` | — |
| [SRC-686F71AA50-L000560](../../agents/task_understanding.py#L560) | 560 | `"        ]"` | — |
| [SRC-686F71AA50-L000561](../../agents/task_understanding.py#L561) | 561 | `"        query_strategies = [\"symptom_exact_text\", \"cause_hypotheses\", \"official_manual\", \"safe_remedy\"]"` | — |
| [SRC-686F71AA50-L000562](../../agents/task_understanding.py#L562) | 562 | `"    elif family == \"compare\":"` | — |
| [SRC-686F71AA50-L000563](../../agents/task_understanding.py#L563) | 563 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000564](../../agents/task_understanding.py#L564) | 564 | `"            \"preserve_each_explicit_comparison_criterion\","` | — |
| [SRC-686F71AA50-L000565](../../agents/task_understanding.py#L565) | 565 | `"            \"source_support_for_each_material_comparison\","` | — |
| [SRC-686F71AA50-L000566](../../agents/task_understanding.py#L566) | 566 | `"            \"distinguish_primary_specs_from_individual_experience\","` | — |
| [SRC-686F71AA50-L000567](../../agents/task_understanding.py#L567) | 567 | `"        ]"` | — |
| [SRC-686F71AA50-L000568](../../agents/task_understanding.py#L568) | 568 | `"        query_strategies = [\"topic_baseline\", \"one_query_per_criterion\", \"primary_specification\", \"independent_comparison\"]"` | — |
| [SRC-686F71AA50-L000569](../../agents/task_understanding.py#L569) | 569 | `"    elif family == \"how_to\":"` | — |
| [SRC-686F71AA50-L000570](../../agents/task_understanding.py#L570) | 570 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000571](../../agents/task_understanding.py#L571) | 571 | `"            \"ordered_actionable_steps\","` | — |
| [SRC-686F71AA50-L000572](../../agents/task_understanding.py#L572) | 572 | `"            \"surface prerequisites and safety constraints\","` | — |
| [SRC-686F71AA50-L000573](../../agents/task_understanding.py#L573) | 573 | `"            \"distinguish general guidance from product-specific instructions\","` | — |
| [SRC-686F71AA50-L000574](../../agents/task_understanding.py#L574) | 574 | `"        ]"` | — |
| [SRC-686F71AA50-L000575](../../agents/task_understanding.py#L575) | 575 | `"        query_strategies = [\"goal_exact_match\", \"official_guide\", \"stepwise_method\"]"` | — |
| [SRC-686F71AA50-L000576](../../agents/task_understanding.py#L576) | 576 | `"    elif family == \"lead_generation\":"` | — |
| [SRC-686F71AA50-L000577](../../agents/task_understanding.py#L577) | 577 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000578](../../agents/task_understanding.py#L578) | 578 | `"            \"public_buyer_intent_signal\","` | — |
| [SRC-686F71AA50-L000579](../../agents/task_understanding.py#L579) | 579 | `"            \"do_not_treat_listing_or_ad_as_a_buyer\","` | — |
| [SRC-686F71AA50-L000580](../../agents/task_understanding.py#L580) | 580 | `"            \"identity_not_verified_without_separate_evidence\","` | — |
| [SRC-686F71AA50-L000581](../../agents/task_understanding.py#L581) | 581 | `"        ]"` | — |
| [SRC-686F71AA50-L000582](../../agents/task_understanding.py#L582) | 582 | `"        query_strategies = [\"buyer_intent_phrase\", \"public_discussion\", \"recent_signal\"]"` | — |
| [SRC-686F71AA50-L000583](../../agents/task_understanding.py#L583) | 583 | `"    elif family == \"recommendation\":"` | — |
| [SRC-686F71AA50-L000584](../../agents/task_understanding.py#L584) | 584 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000585](../../agents/task_understanding.py#L585) | 585 | `"            \"preserve_budget_location_and_use_case_if_explicit\","` | — |
| [SRC-686F71AA50-L000586](../../agents/task_understanding.py#L586) | 586 | `"            \"compare_alternatives\","` | — |
| [SRC-686F71AA50-L000587](../../agents/task_understanding.py#L587) | 587 | `"            \"make_tradeoffs_and_missing_information_visible\","` | — |
| [SRC-686F71AA50-L000588](../../agents/task_understanding.py#L588) | 588 | `"        ]"` | — |
| [SRC-686F71AA50-L000589](../../agents/task_understanding.py#L589) | 589 | `"        query_strategies = [\"use_case\", \"budget_and_location\", \"pros_cons\", \"alternatives\"]"` | — |
| [SRC-686F71AA50-L000590](../../agents/task_understanding.py#L590) | 590 | `"    elif family == \"medical_information\":"` | — |
| [SRC-686F71AA50-L000591](../../agents/task_understanding.py#L591) | 591 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000592](../../agents/task_understanding.py#L592) | 592 | `"            \"distinguish_general_health_information_from_personal_diagnosis\","` | — |
| [SRC-686F71AA50-L000593](../../agents/task_understanding.py#L593) | 593 | `"            \"prefer_current_authoritative_health_sources_when_research_is_requested\","` | — |
| [SRC-686F71AA50-L000594](../../agents/task_understanding.py#L594) | 594 | `"            \"preserve_units_dosage_context_and_uncertainty\","` | — |
| [SRC-686F71AA50-L000595](../../agents/task_understanding.py#L595) | 595 | `"            \"escalate_urgent_or_emergency_symptoms_to_appropriate_care\","` | — |
| [SRC-686F71AA50-L000596](../../agents/task_understanding.py#L596) | 596 | `"        ]"` | — |
| [SRC-686F71AA50-L000597](../../agents/task_understanding.py#L597) | 597 | `"        query_strategies = [\"authoritative_health_source\", \"symptom_context\", \"limitations_and_urgency\"]"` | — |
| [SRC-686F71AA50-L000598](../../agents/task_understanding.py#L598) | 598 | `"    elif family == \"legal_information\":"` | — |
| [SRC-686F71AA50-L000599](../../agents/task_understanding.py#L599) | 599 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000600](../../agents/task_understanding.py#L600) | 600 | `"            \"identify_jurisdiction_and_effective_date_if_relevant\","` | — |
| [SRC-686F71AA50-L000601](../../agents/task_understanding.py#L601) | 601 | `"            \"prefer_primary_law_or_official_regulatory_text\","` | — |
| [SRC-686F71AA50-L000602](../../agents/task_understanding.py#L602) | 602 | `"            \"distinguish_general_information_from_legal_advice\","` | — |
| [SRC-686F71AA50-L000603](../../agents/task_understanding.py#L603) | 603 | `"        ]"` | — |
| [SRC-686F71AA50-L000604](../../agents/task_understanding.py#L604) | 604 | `"        query_strategies = [\"official_law_text\", \"jurisdiction_and_date\", \"interpretive_context\"]"` | — |
| [SRC-686F71AA50-L000605](../../agents/task_understanding.py#L605) | 605 | `"    elif family == \"coding_or_technical_design\":"` | — |
| [SRC-686F71AA50-L000606](../../agents/task_understanding.py#L606) | 606 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000607](../../agents/task_understanding.py#L607) | 607 | `"            \"preserve_language_version_runtime_and_error_text_if_supplied\","` | — |
| [SRC-686F71AA50-L000608](../../agents/task_understanding.py#L608) | 608 | `"            \"separate_observed_failure_from_cause_hypotheses\","` | — |
| [SRC-686F71AA50-L000609](../../agents/task_understanding.py#L609) | 609 | `"            \"provide_testable_changes_and_regression_tests\","` | — |
| [SRC-686F71AA50-L000610](../../agents/task_understanding.py#L610) | 610 | `"        ]"` | — |
| [SRC-686F71AA50-L000611](../../agents/task_understanding.py#L611) | 611 | `"        query_strategies = [\"minimal_reproducer\", \"documentation_or_api_reference\", \"test_and_verify\"]"` | — |
| [SRC-686F71AA50-L000612](../../agents/task_understanding.py#L612) | 612 | `"    elif family == \"data_analysis\":"` | — |
| [SRC-686F71AA50-L000613](../../agents/task_understanding.py#L613) | 613 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000614](../../agents/task_understanding.py#L614) | 614 | `"            \"preserve_dataset_grain_and_metric_definition\","` | — |
| [SRC-686F71AA50-L000615](../../agents/task_understanding.py#L615) | 615 | `"            \"inspect_missingness_duplicates_outliers_and_time_coverage\","` | — |
| [SRC-686F71AA50-L000616](../../agents/task_understanding.py#L616) | 616 | `"            \"separate_observed_association_from_causal_explanation\","` | — |
| [SRC-686F71AA50-L000617](../../agents/task_understanding.py#L617) | 617 | `"        ]"` | — |
| [SRC-686F71AA50-L000618](../../agents/task_understanding.py#L618) | 618 | `"        query_strategies = [\"schema_and_grain\", \"data_quality\", \"metric_and_segment_checks\"]"` | — |
| [SRC-686F71AA50-L000619](../../agents/task_understanding.py#L619) | 619 | `"    elif family == \"calculation\":"` | — |
| [SRC-686F71AA50-L000620](../../agents/task_understanding.py#L620) | 620 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000621](../../agents/task_understanding.py#L621) | 621 | `"            \"show_formula_and_units_when_useful\","` | — |
| [SRC-686F71AA50-L000622](../../agents/task_understanding.py#L622) | 622 | `"            \"validate_input_units_and_rounding\","` | — |
| [SRC-686F71AA50-L000623](../../agents/task_understanding.py#L623) | 623 | `"            \"distinguish_exact_result_from_assumption_based_estimate\","` | — |
| [SRC-686F71AA50-L000624](../../agents/task_understanding.py#L624) | 624 | `"        ]"` | — |
| [SRC-686F71AA50-L000625](../../agents/task_understanding.py#L625) | 625 | `"        query_strategies = [\"formula\", \"unit_validation\", \"independent_arithmetic_check\"]"` | — |
| [SRC-686F71AA50-L000626](../../agents/task_understanding.py#L626) | 626 | `"    elif family == \"translation\":"` | — |
| [SRC-686F71AA50-L000627](../../agents/task_understanding.py#L627) | 627 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000628](../../agents/task_understanding.py#L628) | 628 | `"            \"preserve_meaning_tone_and_named_entities\","` | — |
| [SRC-686F71AA50-L000629](../../agents/task_understanding.py#L629) | 629 | `"            \"surface_ambiguous_source_phrasing_instead_of_silently_inventing_meaning\","` | — |
| [SRC-686F71AA50-L000630](../../agents/task_understanding.py#L630) | 630 | `"            \"respect_explicit_target_language_and_script\","` | — |
| [SRC-686F71AA50-L000631](../../agents/task_understanding.py#L631) | 631 | `"        ]"` | — |
| [SRC-686F71AA50-L000632](../../agents/task_understanding.py#L632) | 632 | `"        query_strategies = [\"source_text\", \"target_language\", \"terminology_and_tone\"]"` | — |
| [SRC-686F71AA50-L000633](../../agents/task_understanding.py#L633) | 633 | `"    elif family == \"writing_or_editing\":"` | — |
| [SRC-686F71AA50-L000634](../../agents/task_understanding.py#L634) | 634 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000635](../../agents/task_understanding.py#L635) | 635 | `"            \"follow_requested_audience_tone_and_format\","` | — |
| [SRC-686F71AA50-L000636](../../agents/task_understanding.py#L636) | 636 | `"            \"preserve_user_provided_facts_without_adding_unverified_claims\","` | — |
| [SRC-686F71AA50-L000637](../../agents/task_understanding.py#L637) | 637 | `"            \"distinguish_rewrite_from_fact_check\","` | — |
| [SRC-686F71AA50-L000638](../../agents/task_understanding.py#L638) | 638 | `"        ]"` | — |
| [SRC-686F71AA50-L000639](../../agents/task_understanding.py#L639) | 639 | `"        query_strategies = [\"audience_and_purpose\", \"tone_and_format\", \"fact_preservation\"]"` | — |
| [SRC-686F71AA50-L000640](../../agents/task_understanding.py#L640) | 640 | `"    elif family == \"planning\":"` | — |
| [SRC-686F71AA50-L000641](../../agents/task_understanding.py#L641) | 641 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000642](../../agents/task_understanding.py#L642) | 642 | `"            \"preserve_goal_constraints_dependencies_and_deadline\","` | — |
| [SRC-686F71AA50-L000643](../../agents/task_understanding.py#L643) | 643 | `"            \"make_assumptions_and_unavailable_resources_explicit\","` | — |
| [SRC-686F71AA50-L000644](../../agents/task_understanding.py#L644) | 644 | `"            \"separate_proposed_steps_from_completed_actions\","` | — |
| [SRC-686F71AA50-L000645](../../agents/task_understanding.py#L645) | 645 | `"        ]"` | — |
| [SRC-686F71AA50-L000646](../../agents/task_understanding.py#L646) | 646 | `"        query_strategies = [\"goal_and_constraints\", \"dependency_order\", \"risks_and_fallbacks\"]"` | — |
| [SRC-686F71AA50-L000647](../../agents/task_understanding.py#L647) | 647 | `"    elif family == \"creative_generation\":"` | — |
| [SRC-686F71AA50-L000648](../../agents/task_understanding.py#L648) | 648 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000649](../../agents/task_understanding.py#L649) | 649 | `"            \"follow_requested_genre_voice_and_constraints\","` | — |
| [SRC-686F71AA50-L000650](../../agents/task_understanding.py#L650) | 650 | `"            \"do_not_present_invented_story_details_as_real_facts\","` | — |
| [SRC-686F71AA50-L000651](../../agents/task_understanding.py#L651) | 651 | `"            \"preserve_explicit_content_boundaries\","` | — |
| [SRC-686F71AA50-L000652](../../agents/task_understanding.py#L652) | 652 | `"        ]"` | — |
| [SRC-686F71AA50-L000653](../../agents/task_understanding.py#L653) | 653 | `"        query_strategies = [\"genre_and_voice\", \"creative_constraints\", \"revision_options\"]"` | — |
| [SRC-686F71AA50-L000654](../../agents/task_understanding.py#L654) | 654 | `"    else:"` | — |
| [SRC-686F71AA50-L000655](../../agents/task_understanding.py#L655) | 655 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000656](../../agents/task_understanding.py#L656) | 656 | `"            \"match_sources_to_the_question\","` | — |
| [SRC-686F71AA50-L000657](../../agents/task_understanding.py#L657) | 657 | `"            \"distinguish_search_snippet_from_read_page\","` | — |
| [SRC-686F71AA50-L000658](../../agents/task_understanding.py#L658) | 658 | `"            \"cite_material_web_claims\","` | — |
| [SRC-686F71AA50-L000659](../../agents/task_understanding.py#L659) | 659 | `"        ]"` | — |
| [SRC-686F71AA50-L000660](../../agents/task_understanding.py#L660) | 660 | `"        query_strategies = [\"exact_topic\", \"primary_source\", \"cross_check_if_needed\"]"` | — |
| [SRC-686F71AA50-L000661](../../agents/task_understanding.py#L661) | 661 | `""` | — |
| [SRC-686F71AA50-L000662](../../agents/task_understanding.py#L662) | 662 | `"    # Source freshness, requested officiality, and social evidence are orthogonal"` | — |
| [SRC-686F71AA50-L000663](../../agents/task_understanding.py#L663) | 663 | `"    # constraints. Preserve them even when another intent is the primary family."` | — |
| [SRC-686F71AA50-L000664](../../agents/task_understanding.py#L664) | 664 | `"    if current_required and not official_destination:"` | — |
| [SRC-686F71AA50-L000665](../../agents/task_understanding.py#L665) | 665 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000666](../../agents/task_understanding.py#L666) | 666 | `"            \"publication_or_update_date\","` | — |
| [SRC-686F71AA50-L000667](../../agents/task_understanding.py#L667) | 667 | `"            \"page_text_successfully_read\","` | — |
| [SRC-686F71AA50-L000668](../../agents/task_understanding.py#L668) | 668 | `"            \"prefer_primary_current_source\","` | — |
| [SRC-686F71AA50-L000669](../../agents/task_understanding.py#L669) | 669 | `"            \"do_not_use_stale_page_as_current_proof\","` | — |
| [SRC-686F71AA50-L000670](../../agents/task_understanding.py#L670) | 670 | `"        ])"` | — |
| [SRC-686F71AA50-L000671](../../agents/task_understanding.py#L671) | 671 | `"        query_strategies.extend([\"recent_official_update\", \"primary_source\", \"date_check\"])"` | — |
| [SRC-686F71AA50-L000672](../../agents/task_understanding.py#L672) | 672 | `"    if social_required and family != \"social_opinions\":"` | — |
| [SRC-686F71AA50-L000673](../../agents/task_understanding.py#L673) | 673 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000674](../../agents/task_understanding.py#L674) | 674 | `"            \"public_social_platform_url\","` | — |
| [SRC-686F71AA50-L000675](../../agents/task_understanding.py#L675) | 675 | `"            \"separate_personal_experience_from_promotion\","` | — |
| [SRC-686F71AA50-L000676](../../agents/task_understanding.py#L676) | 676 | `"            \"heuristic_classification_is_not_identity_or_truth_verification\","` | — |
| [SRC-686F71AA50-L000677](../../agents/task_understanding.py#L677) | 677 | `"        ])"` | — |
| [SRC-686F71AA50-L000678](../../agents/task_understanding.py#L678) | 678 | `"        query_strategies.extend([\"personal_experience\", \"discussion\", \"commercial_exclusion\"])"` | — |
| [SRC-686F71AA50-L000679](../../agents/task_understanding.py#L679) | 679 | `"    if official_destination and family != \"official_site_lookup\":"` | — |
| [SRC-686F71AA50-L000680](../../agents/task_understanding.py#L680) | 680 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000681](../../agents/task_understanding.py#L681) | 681 | `"            \"distinguish_official_destination_from_mentions_or_articles\","` | — |
| [SRC-686F71AA50-L000682](../../agents/task_understanding.py#L682) | 682 | `"            \"do_not_claim_domain_ownership_without_independent_evidence\","` | — |
| [SRC-686F71AA50-L000683](../../agents/task_understanding.py#L683) | 683 | `"        ])"` | — |
| [SRC-686F71AA50-L000684](../../agents/task_understanding.py#L684) | 684 | `"        query_strategies.extend([\"official_domain\", \"government_portal_cross_check\"])"` | — |
| [SRC-686F71AA50-L000685](../../agents/task_understanding.py#L685) | 685 | `"    if \"compare\" in matches and family != \"compare\":"` | — |
| [SRC-686F71AA50-L000686](../../agents/task_understanding.py#L686) | 686 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000687](../../agents/task_understanding.py#L687) | 687 | `"            \"preserve_explicit_comparison_criteria\","` | — |
| [SRC-686F71AA50-L000688](../../agents/task_understanding.py#L688) | 688 | `"            \"do_not_collapse_multiple_dimensions_into_one_generic_answer\","` | — |
| [SRC-686F71AA50-L000689](../../agents/task_understanding.py#L689) | 689 | `"        ])"` | — |
| [SRC-686F71AA50-L000690](../../agents/task_understanding.py#L690) | 690 | `"        query_strategies.extend([\"one_query_per_criterion\", \"independent_comparison\"])"` | — |
| [SRC-686F71AA50-L000691](../../agents/task_understanding.py#L691) | 691 | `"    if len(explicit_aspects := aspect_values) > 1:"` | — |
| [SRC-686F71AA50-L000692](../../agents/task_understanding.py#L692) | 692 | `"        evidence_requirements.append(\"track_evidence_coverage_per_explicit_aspect\")"` | — |
| [SRC-686F71AA50-L000693](../../agents/task_understanding.py#L693) | 693 | `"        query_strategies.append(\"one_query_per_criterion\")"` | — |
| [SRC-686F71AA50-L000694](../../agents/task_understanding.py#L694) | 694 | `"    query_strategies = list(dict.fromkeys(query_strategies))"` | — |
| [SRC-686F71AA50-L000695](../../agents/task_understanding.py#L695) | 695 | `"    evidence_requirements = list(dict.fromkeys(evidence_requirements))"` | — |
| [SRC-686F71AA50-L000696](../../agents/task_understanding.py#L696) | 696 | `""` | — |
| [SRC-686F71AA50-L000697](../../agents/task_understanding.py#L697) | 697 | `"    location = _extract_explicit_locations(raw)"` | — |
| [SRC-686F71AA50-L000698](../../agents/task_understanding.py#L698) | 698 | `"    years = list(dict.fromkeys(_YEAR_RE.findall(raw)))"` | — |
| [SRC-686F71AA50-L000699](../../agents/task_understanding.py#L699) | 699 | `"    dates = list(dict.fromkeys(_DATE_RE.findall(raw)))"` | — |
| [SRC-686F71AA50-L000700](../../agents/task_understanding.py#L700) | 700 | `"    budgets = [m.group(0).strip()[:100] for m in _BUDGET_RE.finditer(raw)]"` | — |
| [SRC-686F71AA50-L000701](../../agents/task_understanding.py#L701) | 701 | `"    urls = list(dict.fromkeys(_URL_RE.findall(raw)))[:5]"` | — |
| [SRC-686F71AA50-L000702](../../agents/task_understanding.py#L702) | 702 | `"    inline_summary_text = _has_inline_summary_text(raw)"` | — |
| [SRC-686F71AA50-L000703](../../agents/task_understanding.py#L703) | 703 | `"    unresolved_followup = any(normalize_text(cue) in normalized for cue in _FOLLOWUP_CUES)"` | — |
| [SRC-686F71AA50-L000704](../../agents/task_understanding.py#L704) | 704 | `"    missing_required_inputs: list[str] = []"` | — |
| [SRC-686F71AA50-L000705](../../agents/task_understanding.py#L705) | 705 | `"    if intent_route == \"CLARIFY\":"` | — |
| [SRC-686F71AA50-L000706](../../agents/task_understanding.py#L706) | 706 | `"        missing_required_inputs.append(\"unresolved_referent_or_incomplete_request\")"` | — |
| [SRC-686F71AA50-L000707](../../agents/task_understanding.py#L707) | 707 | `"    if official_destination and not _has_official_site_target(raw):"` | — |
| [SRC-686F71AA50-L000708](../../agents/task_understanding.py#L708) | 708 | `"        missing_required_inputs.append(\"official_destination_target_entity\")"` | — |
| [SRC-686F71AA50-L000709](../../agents/task_understanding.py#L709) | 709 | `"    if family == \"summarize\" and not urls and not inline_summary_text:"` | — |
| [SRC-686F71AA50-L000710](../../agents/task_understanding.py#L710) | 710 | `"        missing_required_inputs.append(\"summary_source_url_or_pasted_text\")"` | — |
| [SRC-686F71AA50-L000711](../../agents/task_understanding.py#L711) | 711 | `"    context = dialogue_context if isinstance(dialogue_context, dict) else {}"` | — |
| [SRC-686F71AA50-L000712](../../agents/task_understanding.py#L712) | 712 | `"    explicit_aspects = list(dict.fromkeys(aspect_values))[:MAX_TASK_ASPECTS]"` | — |
| [SRC-686F71AA50-L000713](../../agents/task_understanding.py#L713) | 713 | `""` | — |
| [SRC-686F71AA50-L000714](../../agents/task_understanding.py#L714) | 714 | `"    # Hypotheses are alternatives considered by the deterministic classifier. Counts"` | — |
| [SRC-686F71AA50-L000715](../../agents/task_understanding.py#L715) | 715 | `"    # are matched lexical signals, not calibrated confidence or probability."` | — |
| [SRC-686F71AA50-L000716](../../agents/task_understanding.py#L716) | 716 | `"    hypothesis_rows: list[dict[str, Any]] = []"` | — |
| [SRC-686F71AA50-L000717](../../agents/task_understanding.py#L717) | 717 | `"    for candidate_family, signals in matches.items():"` | — |
| [SRC-686F71AA50-L000718](../../agents/task_understanding.py#L718) | 718 | `"        if signals:"` | — |
| [SRC-686F71AA50-L000719](../../agents/task_understanding.py#L719) | 719 | `"            hypothesis_rows.append({"` | — |
| [SRC-686F71AA50-L000720](../../agents/task_understanding.py#L720) | 720 | `"                \"family\": candidate_family,"` | — |
| [SRC-686F71AA50-L000721](../../agents/task_understanding.py#L721) | 721 | `"                \"matched_signal_count\": len(signals),"` | — |
| [SRC-686F71AA50-L000722](../../agents/task_understanding.py#L722) | 722 | `"                \"signals\": signals[:4],"` | — |
| [SRC-686F71AA50-L000723](../../agents/task_understanding.py#L723) | 723 | `"                \"status\": \"candidate_interpretation\","` | — |
| [SRC-686F71AA50-L000724](../../agents/task_understanding.py#L724) | 724 | `"            })"` | — |
| [SRC-686F71AA50-L000725](../../agents/task_understanding.py#L725) | 725 | `"    hypothesis_rows.sort("` | — |
| [SRC-686F71AA50-L000726](../../agents/task_understanding.py#L726) | 726 | `"        key=lambda item: (-item[\"matched_signal_count\"], item[\"family\"])"` | — |
| [SRC-686F71AA50-L000727](../../agents/task_understanding.py#L727) | 727 | `"    )"` | — |
| [SRC-686F71AA50-L000728](../../agents/task_understanding.py#L728) | 728 | `"    for item in hypothesis_rows:"` | — |
| [SRC-686F71AA50-L000729](../../agents/task_understanding.py#L729) | 729 | `"        item[\"selected\"] = item[\"family\"] == family"` | — |
| [SRC-686F71AA50-L000730](../../agents/task_understanding.py#L730) | 730 | `"    if len(hypothesis_rows) > 8:"` | — |
| [SRC-686F71AA50-L000731](../../agents/task_understanding.py#L731) | 731 | `"        hypothesis_rows = hypothesis_rows[:8]"` | — |
| [SRC-686F71AA50-L000732](../../agents/task_understanding.py#L732) | 732 | `""` | — |
| [SRC-686F71AA50-L000733](../../agents/task_understanding.py#L733) | 733 | `"    # A conflict is a reason to preserve alternatives in diagnostics, not a reason to"` | — |
| [SRC-686F71AA50-L000734](../../agents/task_understanding.py#L734) | 734 | `"    # invent certainty. High ambiguity is limited to unresolved references or a"` | — |
| [SRC-686F71AA50-L000735](../../agents/task_understanding.py#L735) | 735 | `"    # short fragment explicitly marked as contextual."` | — |
| [SRC-686F71AA50-L000736](../../agents/task_understanding.py#L736) | 736 | `"    unresolved = bool(missing_required_inputs) or bool(context.get(\"needs_clarification\")) or ("` | — |
| [SRC-686F71AA50-L000737](../../agents/task_understanding.py#L737) | 737 | `"        len(raw.strip()) <= 28 and unresolved_followup"` | — |
| [SRC-686F71AA50-L000738](../../agents/task_understanding.py#L738) | 738 | `"        and not context.get(\"resolved_question\")"` | — |
| [SRC-686F71AA50-L000739](../../agents/task_understanding.py#L739) | 739 | `"    )"` | — |
| [SRC-686F71AA50-L000740](../../agents/task_understanding.py#L740) | 740 | `"    if unresolved:"` | — |
| [SRC-686F71AA50-L000741](../../agents/task_understanding.py#L741) | 741 | `"        ambiguity_status = \"needs_clarification\""` | — |
| [SRC-686F71AA50-L000742](../../agents/task_understanding.py#L742) | 742 | `"    elif len(hypothesis_rows) >= 3:"` | — |
| [SRC-686F71AA50-L000743](../../agents/task_understanding.py#L743) | 743 | `"        ambiguity_status = \"multiple_overlapping_signals\""` | — |
| [SRC-686F71AA50-L000744](../../agents/task_understanding.py#L744) | 744 | `"    elif len(hypothesis_rows) == 2:"` | — |
| [SRC-686F71AA50-L000745](../../agents/task_understanding.py#L745) | 745 | `"        ambiguity_status = \"some_intent_overlap\""` | — |
| [SRC-686F71AA50-L000746](../../agents/task_understanding.py#L746) | 746 | `"    else:"` | — |
| [SRC-686F71AA50-L000747](../../agents/task_understanding.py#L747) | 747 | `"        ambiguity_status = \"no_strong_lexical_conflict_detected\""` | — |
| [SRC-686F71AA50-L000748](../../agents/task_understanding.py#L748) | 748 | `""` | — |
| [SRC-686F71AA50-L000749](../../agents/task_understanding.py#L749) | 749 | `"    # Tool requirements are advisory planning metadata, not executable permission."` | — |
| [SRC-686F71AA50-L000750](../../agents/task_understanding.py#L750) | 750 | `"    # A clarification route is a hard stop even when the UI has a research mode selected."` | — |
| [SRC-686F71AA50-L000751](../../agents/task_understanding.py#L751) | 751 | `"    route_is_clarification = intent_route == \"CLARIFY\""` | — |
| [SRC-686F71AA50-L000752](../../agents/task_understanding.py#L752) | 752 | `"    route_is_local = intent_route == \"LOCAL\""` | — |
| [SRC-686F71AA50-L000753](../../agents/task_understanding.py#L753) | 753 | `"    search_requested = ("` | — |
| [SRC-686F71AA50-L000754](../../agents/task_understanding.py#L754) | 754 | `"        intent_route in {\"WEB_SIMPLE\", \"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-686F71AA50-L000755](../../agents/task_understanding.py#L755) | 755 | `"        or ("` | — |
| [SRC-686F71AA50-L000756](../../agents/task_understanding.py#L756) | 756 | `"            intent_route == \"deterministic_fallback\""` | — |
| [SRC-686F71AA50-L000757](../../agents/task_understanding.py#L757) | 757 | `"            and isinstance(plan, dict)"` | — |
| [SRC-686F71AA50-L000758](../../agents/task_understanding.py#L758) | 758 | `"            and bool(plan.get(\"queries\"))"` | — |
| [SRC-686F71AA50-L000759](../../agents/task_understanding.py#L759) | 759 | `"        )"` | — |
| [SRC-686F71AA50-L000760](../../agents/task_understanding.py#L760) | 760 | `"        or ("` | — |
| [SRC-686F71AA50-L000761](../../agents/task_understanding.py#L761) | 761 | `"            intent_route not in {\"LOCAL\", \"CLARIFY\", \"BUDGET_EXHAUSTED\"}"` | — |
| [SRC-686F71AA50-L000762](../../agents/task_understanding.py#L762) | 762 | `"            and ("` | — |
| [SRC-686F71AA50-L000763](../../agents/task_understanding.py#L763) | 763 | `"                social_required"` | — |
| [SRC-686F71AA50-L000764](../../agents/task_understanding.py#L764) | 764 | `"                or official_destination"` | — |
| [SRC-686F71AA50-L000765](../../agents/task_understanding.py#L765) | 765 | `"                or current_required"` | — |
| [SRC-686F71AA50-L000766](../../agents/task_understanding.py#L766) | 766 | `"                or family in {\"find_or_discover\", \"lead_generation\", \"general_research\"}"` | — |
| [SRC-686F71AA50-L000767](../../agents/task_understanding.py#L767) | 767 | `"            )"` | — |
| [SRC-686F71AA50-L000768](../../agents/task_understanding.py#L768) | 768 | `"        )"` | — |
| [SRC-686F71AA50-L000769](../../agents/task_understanding.py#L769) | 769 | `"        or ("` | — |
| [SRC-686F71AA50-L000770](../../agents/task_understanding.py#L770) | 770 | `"            clean_mode != \"auto\""` | — |
| [SRC-686F71AA50-L000771](../../agents/task_understanding.py#L771) | 771 | `"            and not route_is_clarification"` | — |
| [SRC-686F71AA50-L000772](../../agents/task_understanding.py#L772) | 772 | `"            and not route_is_local"` | — |
| [SRC-686F71AA50-L000773](../../agents/task_understanding.py#L773) | 773 | `"        )"` | — |
| [SRC-686F71AA50-L000774](../../agents/task_understanding.py#L774) | 774 | `"    )"` | — |
| [SRC-686F71AA50-L000775](../../agents/task_understanding.py#L775) | 775 | `"    page_fetch_requested = bool(urls) or ("` | — |
| [SRC-686F71AA50-L000776](../../agents/task_understanding.py#L776) | 776 | `"        family == \"summarize\""` | — |
| [SRC-686F71AA50-L000777](../../agents/task_understanding.py#L777) | 777 | `"        and not inline_summary_text"` | — |
| [SRC-686F71AA50-L000778](../../agents/task_understanding.py#L778) | 778 | `"        and not route_is_clarification"` | — |
| [SRC-686F71AA50-L000779](../../agents/task_understanding.py#L779) | 779 | `"    )"` | — |
| [SRC-686F71AA50-L000780](../../agents/task_understanding.py#L780) | 780 | `"    tools: list[str] = []"` | — |
| [SRC-686F71AA50-L000781](../../agents/task_understanding.py#L781) | 781 | `"    if search_requested and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000782](../../agents/task_understanding.py#L782) | 782 | `"        tools.append(\"web_search\")"` | — |
| [SRC-686F71AA50-L000783](../../agents/task_understanding.py#L783) | 783 | `"    if page_fetch_requested and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000784](../../agents/task_understanding.py#L784) | 784 | `"        tools.append(\"page_fetch\")"` | — |
| [SRC-686F71AA50-L000785](../../agents/task_understanding.py#L785) | 785 | `"    if social_required and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000786](../../agents/task_understanding.py#L786) | 786 | `"        tools.append(\"public_social_search_if_configured\")"` | — |
| [SRC-686F71AA50-L000787](../../agents/task_understanding.py#L787) | 787 | `"    if ("` | — |
| [SRC-686F71AA50-L000788](../../agents/task_understanding.py#L788) | 788 | `"        intent_route in {\"MODEL_ONLY\", \"WEB_SIMPLE\", \"WEB_DEEP\", \"LEAD_GENERATION\", \"deterministic_fallback\"}"` | — |
| [SRC-686F71AA50-L000789](../../agents/task_understanding.py#L789) | 789 | `"        or (clean_mode != \"auto\" and not route_is_clarification and not route_is_local)"` | — |
| [SRC-686F71AA50-L000790](../../agents/task_understanding.py#L790) | 790 | `"    ):"` | — |
| [SRC-686F71AA50-L000791](../../agents/task_understanding.py#L791) | 791 | `"        tools.append(\"language_model_generation_if_configured\")"` | — |
| [SRC-686F71AA50-L000792](../../agents/task_understanding.py#L792) | 792 | `"    if tools and (\"web_search\" in tools or social_required) and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000793](../../agents/task_understanding.py#L793) | 793 | `"        tools.append(\"claim_review_if_configured\")"` | — |
| [SRC-686F71AA50-L000794](../../agents/task_understanding.py#L794) | 794 | `"    raw_context_entities = context.get(\"entities\")"` | — |
| [SRC-686F71AA50-L000795](../../agents/task_understanding.py#L795) | 795 | `"    context_entities = ["` | — |
| [SRC-686F71AA50-L000796](../../agents/task_understanding.py#L796) | 796 | `"        str(item).strip()[:120]"` | — |
| [SRC-686F71AA50-L000797](../../agents/task_understanding.py#L797) | 797 | `"        for item in raw_context_entities[:8]"` | — |
| [SRC-686F71AA50-L000798](../../agents/task_understanding.py#L798) | 798 | `"        if isinstance(item, str) and item.strip()"` | — |
| [SRC-686F71AA50-L000799](../../agents/task_understanding.py#L799) | 799 | `"    ] if isinstance(raw_context_entities, list) else []"` | — |
| [SRC-686F71AA50-L000800](../../agents/task_understanding.py#L800) | 800 | `"    raw_context_slots = context.get(\"slots\")"` | — |
| [SRC-686F71AA50-L000801](../../agents/task_understanding.py#L801) | 801 | `"    context_slots: dict[str, str] = {}"` | — |
| [SRC-686F71AA50-L000802](../../agents/task_understanding.py#L802) | 802 | `"    if isinstance(raw_context_slots, dict):"` | — |
| [SRC-686F71AA50-L000803](../../agents/task_understanding.py#L803) | 803 | `"        for raw_key, raw_value in list(raw_context_slots.items())[:16]:"` | — |
| [SRC-686F71AA50-L000804](../../agents/task_understanding.py#L804) | 804 | `"            if isinstance(raw_key, str) and isinstance(raw_value, str) and raw_key.strip() and raw_value.strip():"` | — |
| [SRC-686F71AA50-L000805](../../agents/task_understanding.py#L805) | 805 | `"                context_slots[raw_key.strip()[:40]] = raw_value.strip()[:180]"` | — |
| [SRC-686F71AA50-L000806](../../agents/task_understanding.py#L806) | 806 | `"    raw_changed_slots = context.get(\"changed_slots\")"` | — |
| [SRC-686F71AA50-L000807](../../agents/task_understanding.py#L807) | 807 | `"    context_changed_slots = ["` | — |
| [SRC-686F71AA50-L000808](../../agents/task_understanding.py#L808) | 808 | `"        str(item).strip()[:40]"` | — |
| [SRC-686F71AA50-L000809](../../agents/task_understanding.py#L809) | 809 | `"        for item in raw_changed_slots[:8]"` | — |
| [SRC-686F71AA50-L000810](../../agents/task_understanding.py#L810) | 810 | `"        if isinstance(item, str) and item.strip()"` | — |
| [SRC-686F71AA50-L000811](../../agents/task_understanding.py#L811) | 811 | `"    ] if isinstance(raw_changed_slots, list) else []"` | — |
| [SRC-686F71AA50-L000812](../../agents/task_understanding.py#L812) | 812 | `"    context_resolution = {"` | — |
| [SRC-686F71AA50-L000813](../../agents/task_understanding.py#L813) | 813 | `"        \"method\": str(context.get(\"method\") or \"not_provided\")[:80],"` | — |
| [SRC-686F71AA50-L000814](../../agents/task_understanding.py#L814) | 814 | `"        \"resolved_question\": ("` | — |
| [SRC-686F71AA50-L000815](../../agents/task_understanding.py#L815) | 815 | `"            str(context.get(\"resolved_question\") or raw)[:MAX_TASK_CHARS]"` | — |
| [SRC-686F71AA50-L000816](../../agents/task_understanding.py#L816) | 816 | `"            if not context.get(\"topic_shift\") else raw"` | — |
| [SRC-686F71AA50-L000817](../../agents/task_understanding.py#L817) | 817 | `"        ),"` | — |
| [SRC-686F71AA50-L000818](../../agents/task_understanding.py#L818) | 818 | `"        \"topic\": str(context.get(\"topic\") or \"\")[:180],"` | — |
| [SRC-686F71AA50-L000819](../../agents/task_understanding.py#L819) | 819 | `"        \"entities\": context_entities,"` | — |
| [SRC-686F71AA50-L000820](../../agents/task_understanding.py#L820) | 820 | `"        \"slots\": context_slots,"` | — |
| [SRC-686F71AA50-L000821](../../agents/task_understanding.py#L821) | 821 | `"        \"changed_slots\": context_changed_slots,"` | — |
| [SRC-686F71AA50-L000822](../../agents/task_understanding.py#L822) | 822 | `"        \"is_follow_up\": context.get(\"is_follow_up\") is True,"` | — |
| [SRC-686F71AA50-L000823](../../agents/task_understanding.py#L823) | 823 | `"        \"topic_shift\": context.get(\"topic_shift\") is True,"` | — |
| [SRC-686F71AA50-L000824](../../agents/task_understanding.py#L824) | 824 | `"        \"resolution_basis\": str(context.get(\"resolution_basis\") or \"unassessed\")[:80],"` | — |
| [SRC-686F71AA50-L000825](../../agents/task_understanding.py#L825) | 825 | `"        \"confidence_band\": str(context.get(\"confidence_band\") or \"unassessed\")[:30],"` | — |
| [SRC-686F71AA50-L000826](../../agents/task_understanding.py#L826) | 826 | `"        \"needs_clarification\": context.get(\"needs_clarification\") is True,"` | — |
| [SRC-686F71AA50-L000827](../../agents/task_understanding.py#L827) | 827 | `"        \"unresolved_references\": ["` | — |
| [SRC-686F71AA50-L000828](../../agents/task_understanding.py#L828) | 828 | `"            str(item).strip()[:100]"` | — |
| [SRC-686F71AA50-L000829](../../agents/task_understanding.py#L829) | 829 | `"            for item in context.get(\"unresolved_references\", [])[:8]"` | — |
| [SRC-686F71AA50-L000830](../../agents/task_understanding.py#L830) | 830 | `"            if isinstance(item, str) and item.strip()"` | — |
| [SRC-686F71AA50-L000831](../../agents/task_understanding.py#L831) | 831 | `"        ] if isinstance(context.get(\"unresolved_references\"), list) else [],"` | — |
| [SRC-686F71AA50-L000832](../../agents/task_understanding.py#L832) | 832 | `"    }"` | — |
| [SRC-686F71AA50-L000833](../../agents/task_understanding.py#L833) | 833 | `""` | — |
| [SRC-686F71AA50-L000834](../../agents/task_understanding.py#L834) | 834 | `"    constraints = {"` | — |
| [SRC-686F71AA50-L000835](../../agents/task_understanding.py#L835) | 835 | `"        \"explicit_locations\": location,"` | — |
| [SRC-686F71AA50-L000836](../../agents/task_understanding.py#L836) | 836 | `"        \"explicit_years\": years,"` | — |
| [SRC-686F71AA50-L000837](../../agents/task_understanding.py#L837) | 837 | `"        \"explicit_dates\": dates,"` | — |
| [SRC-686F71AA50-L000838](../../agents/task_understanding.py#L838) | 838 | `"        \"explicit_budgets\": budgets,"` | — |
| [SRC-686F71AA50-L000839](../../agents/task_understanding.py#L839) | 839 | `"        \"explicit_urls\": urls,"` | — |
| [SRC-686F71AA50-L000840](../../agents/task_understanding.py#L840) | 840 | `"        \"explicit_aspects\": explicit_aspects,"` | — |
| [SRC-686F71AA50-L000841](../../agents/task_understanding.py#L841) | 841 | `"        \"inline_text_supplied_for_summary\": inline_summary_text,"` | — |
| [SRC-686F71AA50-L000842](../../agents/task_understanding.py#L842) | 842 | `"        \"time_sensitive_request\": current_required,"` | — |
| [SRC-686F71AA50-L000843](../../agents/task_understanding.py#L843) | 843 | `"        \"official_site_required\": government_official_site,"` | — |
| [SRC-686F71AA50-L000844](../../agents/task_understanding.py#L844) | 844 | `"        \"official_destination_required\": official_destination,"` | — |
| [SRC-686F71AA50-L000845](../../agents/task_understanding.py#L845) | 845 | `"        \"social_evidence_requested\": social_required,"` | — |
| [SRC-686F71AA50-L000846](../../agents/task_understanding.py#L846) | 846 | `"        \"language_profile\": _language_profile(raw),"` | — |
| [SRC-686F71AA50-L000847](../../agents/task_understanding.py#L847) | 847 | `"        \"source_policy\": ("` | — |
| [SRC-686F71AA50-L000848](../../agents/task_understanding.py#L848) | 848 | `"            \"government_official_destination\" if government_official_site"` | — |
| [SRC-686F71AA50-L000849](../../agents/task_understanding.py#L849) | 849 | `"            else \"official_destination\" if official_destination"` | — |
| [SRC-686F71AA50-L000850](../../agents/task_understanding.py#L850) | 850 | `"            else \"current_read_page\" if current_required"` | — |
| [SRC-686F71AA50-L000851](../../agents/task_understanding.py#L851) | 851 | `"            else \"public_social_content\" if social_required"` | — |
| [SRC-686F71AA50-L000852](../../agents/task_understanding.py#L852) | 852 | `"            else \"task_relevant_sources\""` | — |
| [SRC-686F71AA50-L000853](../../agents/task_understanding.py#L853) | 853 | `"        ),"` | — |
| [SRC-686F71AA50-L000854](../../agents/task_understanding.py#L854) | 854 | `"        \"source_policies\": list(dict.fromkeys("` | — |
| [SRC-686F71AA50-L000855](../../agents/task_understanding.py#L855) | 855 | `"            ([\"government_official_destination\"] if government_official_site else [])"` | — |
| [SRC-686F71AA50-L000856](../../agents/task_understanding.py#L856) | 856 | `"            + ([\"official_destination\"] if official_destination else [])"` | — |
| [SRC-686F71AA50-L000857](../../agents/task_understanding.py#L857) | 857 | `"            + ([\"current_read_page\"] if current_required else [])"` | — |
| [SRC-686F71AA50-L000858](../../agents/task_understanding.py#L858) | 858 | `"            + ([\"public_social_content\"] if social_required else [])"` | — |
| [SRC-686F71AA50-L000859](../../agents/task_understanding.py#L859) | 859 | `"            + ([\"authoritative_health_content\"] if matches[\"medical_information\"] else [])"` | — |
| [SRC-686F71AA50-L000860](../../agents/task_understanding.py#L860) | 860 | `"            + ([\"official_legal_text\"] if matches[\"legal_information\"] else [])"` | — |
| [SRC-686F71AA50-L000861](../../agents/task_understanding.py#L861) | 861 | `"            + ([\"task_relevant_sources\"] if not (government_official_site or official_destination or current_required or social_required or matches[\"medical_information\"] or matches[\"legal_information\"]) else [])"` | — |
| [SRC-686F71AA50-L000862](../../agents/task_understanding.py#L862) | 862 | `"        )),"` | — |
| [SRC-686F71AA50-L000863](../../agents/task_understanding.py#L863) | 863 | `"    }"` | — |
| [SRC-686F71AA50-L000864](../../agents/task_understanding.py#L864) | 864 | `"    spec = {"` | — |
| [SRC-686F71AA50-L000865](../../agents/task_understanding.py#L865) | 865 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L000866](../../agents/task_understanding.py#L866) | 866 | `"        \"task_family\": family,"` | — |
| [SRC-686F71AA50-L000867](../../agents/task_understanding.py#L867) | 867 | `"        \"mode\": clean_mode,"` | — |
| [SRC-686F71AA50-L000868](../../agents/task_understanding.py#L868) | 868 | `"        \"intent_route\": intent_route or \"unassessed\","` | — |
| [SRC-686F71AA50-L000869](../../agents/task_understanding.py#L869) | 869 | `"        \"normalization\": \"unicode_nfkc_arabic_diacritic_and_letter_normalization\","` | — |
| [SRC-686F71AA50-L000870](../../agents/task_understanding.py#L870) | 870 | `"        \"classification_method\": \"deterministic_multi_pattern_hypotheses\","` | — |
| [SRC-686F71AA50-L000871](../../agents/task_understanding.py#L871) | 871 | `"        \"classification_is_probability\": False,"` | — |
| [SRC-686F71AA50-L000872](../../agents/task_understanding.py#L872) | 872 | `"        \"ambiguity_status\": ambiguity_status,"` | — |
| [SRC-686F71AA50-L000873](../../agents/task_understanding.py#L873) | 873 | `"        \"missing_required_inputs\": list(dict.fromkeys(missing_required_inputs)),"` | — |
| [SRC-686F71AA50-L000874](../../agents/task_understanding.py#L874) | 874 | `"        \"requires_clarification\": ambiguity_status == \"needs_clarification\","` | — |
| [SRC-686F71AA50-L000875](../../agents/task_understanding.py#L875) | 875 | `"        \"context_resolution\": context_resolution,"` | — |
| [SRC-686F71AA50-L000876](../../agents/task_understanding.py#L876) | 876 | `"        \"secondary_task_types\": ["` | — |
| [SRC-686F71AA50-L000877](../../agents/task_understanding.py#L877) | 877 | `"            name for name, signals in matches.items()"` | — |
| [SRC-686F71AA50-L000878](../../agents/task_understanding.py#L878) | 878 | `"            if signals and name != family"` | — |
| [SRC-686F71AA50-L000879](../../agents/task_understanding.py#L879) | 879 | `"        ],"` | — |
| [SRC-686F71AA50-L000880](../../agents/task_understanding.py#L880) | 880 | `"        \"clarification_reason\": ("` | — |
| [SRC-686F71AA50-L000881](../../agents/task_understanding.py#L881) | 881 | `"            \"missing_required_input\""` | — |
| [SRC-686F71AA50-L000882](../../agents/task_understanding.py#L882) | 882 | `"            if missing_required_inputs"` | — |
| [SRC-686F71AA50-L000883](../../agents/task_understanding.py#L883) | 883 | `"            else \"no_strong_lexical_conflict_detected\""` | — |
| [SRC-686F71AA50-L000884](../../agents/task_understanding.py#L884) | 884 | `"        ),"` | — |
| [SRC-686F71AA50-L000885](../../agents/task_understanding.py#L885) | 885 | `"        \"hypothesis_interpretations\": hypothesis_rows,"` | — |
| [SRC-686F71AA50-L000886](../../agents/task_understanding.py#L886) | 886 | `"        \"constraints\": constraints,"` | — |
| [SRC-686F71AA50-L000887](../../agents/task_understanding.py#L887) | 887 | `"        \"output_preferences\": {"` | — |
| [SRC-686F71AA50-L000888](../../agents/task_understanding.py#L888) | 888 | `"            \"concise\": bool(output_matches[\"output_concise\"]),"` | — |
| [SRC-686F71AA50-L000889](../../agents/task_understanding.py#L889) | 889 | `"            \"detailed\": bool(output_matches[\"output_detailed\"]),"` | — |
| [SRC-686F71AA50-L000890](../../agents/task_understanding.py#L890) | 890 | `"            \"examples_requested\": bool(output_matches[\"output_examples\"]),"` | — |
| [SRC-686F71AA50-L000891](../../agents/task_understanding.py#L891) | 891 | `"            \"table_requested\": bool(output_matches[\"output_table\"]),"` | — |
| [SRC-686F71AA50-L000892](../../agents/task_understanding.py#L892) | 892 | `"            \"bullets_or_checklist_requested\": bool(output_matches[\"output_bullets\"]),"` | — |
| [SRC-686F71AA50-L000893](../../agents/task_understanding.py#L893) | 893 | `"            \"beginner_friendly_requested\": bool(output_matches[\"output_beginner_friendly\"]),"` | — |
| [SRC-686F71AA50-L000894](../../agents/task_understanding.py#L894) | 894 | `"            \"citations_requested\": bool(output_matches[\"output_citations\"]),"` | — |
| [SRC-686F71AA50-L000895](../../agents/task_understanding.py#L895) | 895 | `"            \"links_requested\": bool(output_matches[\"output_links\"]),"` | — |
| [SRC-686F71AA50-L000896](../../agents/task_understanding.py#L896) | 896 | `"            \"json_requested\": bool(output_matches[\"output_json\"]),"` | — |
| [SRC-686F71AA50-L000897](../../agents/task_understanding.py#L897) | 897 | `"        },"` | — |
| [SRC-686F71AA50-L000898](../../agents/task_understanding.py#L898) | 898 | `"        \"evidence_requirements\": evidence_requirements,"` | — |
| [SRC-686F71AA50-L000899](../../agents/task_understanding.py#L899) | 899 | `"        \"query_strategies\": query_strategies,"` | — |
| [SRC-686F71AA50-L000900](../../agents/task_understanding.py#L900) | 900 | `"        \"tool_requirements\": list(dict.fromkeys(tools)),"` | — |
| [SRC-686F71AA50-L000901](../../agents/task_understanding.py#L901) | 901 | `"        \"decision_checks\": ["` | — |
| [SRC-686F71AA50-L000902](../../agents/task_understanding.py#L902) | 902 | `"            \"resolve_context_without_carrying_stale_topic\","` | — |
| [SRC-686F71AA50-L000903](../../agents/task_understanding.py#L903) | 903 | `"            \"preserve_explicit_entities_and_constraints\","` | — |
| [SRC-686F71AA50-L000904](../../agents/task_understanding.py#L904) | 904 | `"            \"validate_topic_relevance\","` | — |
| [SRC-686F71AA50-L000905](../../agents/task_understanding.py#L905) | 905 | `"            \"check_tool_permission_and_configuration_before_execution\","` | — |
| [SRC-686F71AA50-L000906](../../agents/task_understanding.py#L906) | 906 | `"            \"bound_query_count_retries_concurrency_and_deadlines\","` | — |
| [SRC-686F71AA50-L000907](../../agents/task_understanding.py#L907) | 907 | `"            \"treat_retrieved_content_as_untrusted_data_not_tool_instructions\","` | — |
| [SRC-686F71AA50-L000908](../../agents/task_understanding.py#L908) | 908 | `"            \"apply_mode_specific_source_guardrails\","` | — |
| [SRC-686F71AA50-L000909](../../agents/task_understanding.py#L909) | 909 | `"            \"distinguish_planned_queries_from_queries_actually_attempted\","` | — |
| [SRC-686F71AA50-L000910](../../agents/task_understanding.py#L910) | 910 | `"            \"distinguish_search_snippets_from_successfully_read_pages\","` | — |
| [SRC-686F71AA50-L000911](../../agents/task_understanding.py#L911) | 911 | `"            \"separate_connector_success_from_evidence_validity\","` | — |
| [SRC-686F71AA50-L000912](../../agents/task_understanding.py#L912) | 912 | `"            \"report_each_failed_stage_without_claiming_unperformed_checks\","` | — |
| [SRC-686F71AA50-L000913](../../agents/task_understanding.py#L913) | 913 | `"            \"cite_claims_or_abstain_when_evidence_is_insufficient\","` | — |
| [SRC-686F71AA50-L000914](../../agents/task_understanding.py#L914) | 914 | `"        ],"` | — |
| [SRC-686F71AA50-L000915](../../agents/task_understanding.py#L915) | 915 | `"        \"reasoning_strategy_ids\": _reasoning_strategy_ids("` | — |
| [SRC-686F71AA50-L000916](../../agents/task_understanding.py#L916) | 916 | `"            family, constraints, context_resolution, missing_required_inputs"` | — |
| [SRC-686F71AA50-L000917](../../agents/task_understanding.py#L917) | 917 | `"        ),"` | — |
| [SRC-686F71AA50-L000918](../../agents/task_understanding.py#L918) | 918 | `"        \"decision_matrix\": [dict(row) for row in _DECISION_MATRIX],"` | — |
| [SRC-686F71AA50-L000919](../../agents/task_understanding.py#L919) | 919 | `"        \"limits\": {"` | — |
