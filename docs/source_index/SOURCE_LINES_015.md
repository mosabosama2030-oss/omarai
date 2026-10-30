# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **015**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L004741 إلى SRC-1AE03B9EC3-L005540
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L004741](../../agents/web_agent.py#L4741) | 4741 | `"                clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004742](../../agents/web_agent.py#L4742) | 4742 | `"                {"` | — |
| [SRC-1AE03B9EC3-L004743](../../agents/web_agent.py#L4743) | 4743 | `"                    \"route\": \"CLARIFY\","` | — |
| [SRC-1AE03B9EC3-L004744](../../agents/web_agent.py#L4744) | 4744 | `"                    \"reason\": \"task_spec_missing_required_input\","` | — |
| [SRC-1AE03B9EC3-L004745](../../agents/web_agent.py#L4745) | 4745 | `"                    \"needs_clarification\": True,"` | — |
| [SRC-1AE03B9EC3-L004746](../../agents/web_agent.py#L4746) | 4746 | `"                    \"context_available\": bool(context_override),"` | — |
| [SRC-1AE03B9EC3-L004747](../../agents/web_agent.py#L4747) | 4747 | `"                },"` | — |
| [SRC-1AE03B9EC3-L004748](../../agents/web_agent.py#L4748) | 4748 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004749](../../agents/web_agent.py#L4749) | 4749 | `"            clarification[\"task_spec_preflight\"] = preflight_task_spec"` | — |
| [SRC-1AE03B9EC3-L004750](../../agents/web_agent.py#L4750) | 4750 | `"            if \"official_destination_target_entity\" in actionable_missing_inputs:"` | — |
| [SRC-1AE03B9EC3-L004751](../../agents/web_agent.py#L4751) | 4751 | `"                clarification[\"answer\"] = ("` | — |
| [SRC-1AE03B9EC3-L004752](../../agents/web_agent.py#L4752) | 4752 | `"                    \"ما اسم الجهة أو الشركة التي تريد موقعها الرسمي؟ اكتب الاسم، \""` | — |
| [SRC-1AE03B9EC3-L004753](../../agents/web_agent.py#L4753) | 4753 | `"                    \"والبلد أيضًا إذا كانت الجهة موجودة في أكثر من دولة.\""` | — |
| [SRC-1AE03B9EC3-L004754](../../agents/web_agent.py#L4754) | 4754 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004755](../../agents/web_agent.py#L4755) | 4755 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004756](../../agents/web_agent.py#L4756) | 4756 | `"                clarification[\"answer\"] = ("` | — |
| [SRC-1AE03B9EC3-L004757](../../agents/web_agent.py#L4757) | 4757 | `"                    \"أرسل النص الذي تريد تلخيصه أو رابط الصفحة. لن ألخّص محتوى \""` | — |
| [SRC-1AE03B9EC3-L004758](../../agents/web_agent.py#L4758) | 4758 | `"                    \"لم أتمكن من الاطلاع عليه.\""` | — |
| [SRC-1AE03B9EC3-L004759](../../agents/web_agent.py#L4759) | 4759 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004760](../../agents/web_agent.py#L4760) | 4760 | `"            return clarification"` | — |
| [SRC-1AE03B9EC3-L004761](../../agents/web_agent.py#L4761) | 4761 | `""` | — |
| [SRC-1AE03B9EC3-L004762](../../agents/web_agent.py#L4762) | 4762 | `"        if intent_route == \"LOCAL\":"` | — |
| [SRC-1AE03B9EC3-L004763](../../agents/web_agent.py#L4763) | 4763 | `"            if self._is_self_question(question):"` | — |
| [SRC-1AE03B9EC3-L004764](../../agents/web_agent.py#L4764) | 4764 | `"                local_result = self._self_description_answer(question)"` | — |
| [SRC-1AE03B9EC3-L004765](../../agents/web_agent.py#L4765) | 4765 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004766](../../agents/web_agent.py#L4766) | 4766 | `"                local_result = self._local_answer_result("` | — |
| [SRC-1AE03B9EC3-L004767](../../agents/web_agent.py#L4767) | 4767 | `"                    question, self._local_conversation_reply(question), \"local_conversation\""` | — |
| [SRC-1AE03B9EC3-L004768](../../agents/web_agent.py#L4768) | 4768 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004769](../../agents/web_agent.py#L4769) | 4769 | `"            return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L004770](../../agents/web_agent.py#L4770) | 4770 | `"                local_result, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L004771](../../agents/web_agent.py#L4771) | 4771 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004772](../../agents/web_agent.py#L4772) | 4772 | `""` | — |
| [SRC-1AE03B9EC3-L004773](../../agents/web_agent.py#L4773) | 4773 | `"        if intent_route == \"CLARIFY\":"` | — |
| [SRC-1AE03B9EC3-L004774](../../agents/web_agent.py#L4774) | 4774 | `"            if context_override is not None:"` | — |
| [SRC-1AE03B9EC3-L004775](../../agents/web_agent.py#L4775) | 4775 | `"                return self._dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L004776](../../agents/web_agent.py#L4776) | 4776 | `"                    question, clean_mode, context_override, intent_reason"` | — |
| [SRC-1AE03B9EC3-L004777](../../agents/web_agent.py#L4777) | 4777 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004778](../../agents/web_agent.py#L4778) | 4778 | `"            return self._clarification_result(question, clean_mode, decision)"` | — |
| [SRC-1AE03B9EC3-L004779](../../agents/web_agent.py#L4779) | 4779 | `""` | — |
| [SRC-1AE03B9EC3-L004780](../../agents/web_agent.py#L4780) | 4780 | `"        if intent_route == \"MODEL_ONLY\":"` | — |
| [SRC-1AE03B9EC3-L004781](../../agents/web_agent.py#L4781) | 4781 | `"            general_answer = self._answer_without_search(working_question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L004782](../../agents/web_agent.py#L4782) | 4782 | `"            if general_answer is not None:"` | — |
| [SRC-1AE03B9EC3-L004783](../../agents/web_agent.py#L4783) | 4783 | `"                # Keep the public API question verbatim; the resolved wording is for"` | — |
| [SRC-1AE03B9EC3-L004784](../../agents/web_agent.py#L4784) | 4784 | `"                # internal reasoning and generation, not a replacement for user input."` | — |
| [SRC-1AE03B9EC3-L004785](../../agents/web_agent.py#L4785) | 4785 | `"                general_answer[\"question\"] = question"` | — |
| [SRC-1AE03B9EC3-L004786](../../agents/web_agent.py#L4786) | 4786 | `"                if context_override is not None:"` | — |
| [SRC-1AE03B9EC3-L004787](../../agents/web_agent.py#L4787) | 4787 | `"                    general_answer[\"dialogue_context\"] = context_override"` | — |
| [SRC-1AE03B9EC3-L004788](../../agents/web_agent.py#L4788) | 4788 | `"                    if isinstance(general_answer.get(\"research_plan\"), dict):"` | — |
| [SRC-1AE03B9EC3-L004789](../../agents/web_agent.py#L4789) | 4789 | `"                        general_answer[\"research_plan\"][\"dialogue_context\"] = context_override"` | — |
| [SRC-1AE03B9EC3-L004790](../../agents/web_agent.py#L4790) | 4790 | `"                return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L004791](../../agents/web_agent.py#L4791) | 4791 | `"                    general_answer, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L004792](../../agents/web_agent.py#L4792) | 4792 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004793](../../agents/web_agent.py#L4793) | 4793 | `"            # Preserve the existing degraded-mode behavior when generation is unavailable:"` | — |
| [SRC-1AE03B9EC3-L004794](../../agents/web_agent.py#L4794) | 4794 | `"            # run the current web pipeline rather than fabricate a model-only answer."` | — |
| [SRC-1AE03B9EC3-L004795](../../agents/web_agent.py#L4795) | 4795 | `"            intent_route = \"WEB_SIMPLE\""` | — |
| [SRC-1AE03B9EC3-L004796](../../agents/web_agent.py#L4796) | 4796 | `"            intent_reason = \"model_unavailable_fallback_to_existing_web_research\""` | — |
| [SRC-1AE03B9EC3-L004797](../../agents/web_agent.py#L4797) | 4797 | `""` | — |
| [SRC-1AE03B9EC3-L004798](../../agents/web_agent.py#L4798) | 4798 | `"        if context_override is None:"` | — |
| [SRC-1AE03B9EC3-L004799](../../agents/web_agent.py#L4799) | 4799 | `"            # Preserve compatibility with existing integrations and test doubles."` | — |
| [SRC-1AE03B9EC3-L004800](../../agents/web_agent.py#L4800) | 4800 | `"            plan = self._plan_search(question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L004801](../../agents/web_agent.py#L4801) | 4801 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004802](../../agents/web_agent.py#L4802) | 4802 | `"            plan = self._plan_search("` | — |
| [SRC-1AE03B9EC3-L004803](../../agents/web_agent.py#L4803) | 4803 | `"                question, clean_history, context_override=context_override"` | — |
| [SRC-1AE03B9EC3-L004804](../../agents/web_agent.py#L4804) | 4804 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004805](../../agents/web_agent.py#L4805) | 4805 | `"        dialogue_context = plan.get(\"dialogue_context\")"` | — |
| [SRC-1AE03B9EC3-L004806](../../agents/web_agent.py#L4806) | 4806 | `"        if isinstance(dialogue_context, dict):"` | — |
| [SRC-1AE03B9EC3-L004807](../../agents/web_agent.py#L4807) | 4807 | `"            if dialogue_context.get(\"needs_clarification\"):"` | — |
| [SRC-1AE03B9EC3-L004808](../../agents/web_agent.py#L4808) | 4808 | `"                return self._dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L004809](../../agents/web_agent.py#L4809) | 4809 | `"                    question, clean_mode, dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L004810](../../agents/web_agent.py#L4810) | 4810 | `"                    \"planner_detected_unresolved_referent\","` | — |
| [SRC-1AE03B9EC3-L004811](../../agents/web_agent.py#L4811) | 4811 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004812](../../agents/web_agent.py#L4812) | 4812 | `"            working_question = ("` | — |
| [SRC-1AE03B9EC3-L004813](../../agents/web_agent.py#L4813) | 4813 | `"                question if dialogue_context.get(\"topic_shift\")"` | — |
| [SRC-1AE03B9EC3-L004814](../../agents/web_agent.py#L4814) | 4814 | `"                else dialogue_context.get(\"resolved_question\") or working_question"` | — |
| [SRC-1AE03B9EC3-L004815](../../agents/web_agent.py#L4815) | 4815 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004816](../../agents/web_agent.py#L4816) | 4816 | `"        plan[\"mode\"] = clean_mode"` | — |
| [SRC-1AE03B9EC3-L004817](../../agents/web_agent.py#L4817) | 4817 | `"        plan[\"intent_route\"] = intent_route"` | — |
| [SRC-1AE03B9EC3-L004818](../../agents/web_agent.py#L4818) | 4818 | `"        plan[\"intent_route_reason\"] = intent_reason"` | — |
| [SRC-1AE03B9EC3-L004819](../../agents/web_agent.py#L4819) | 4819 | `"        # Normalize planner output before depth/mode expansion so a raw instruction-only"` | — |
| [SRC-1AE03B9EC3-L004820](../../agents/web_agent.py#L4820) | 4820 | `"        # prompt cannot seed synthetic generic queries when the topic is empty."` | — |
| [SRC-1AE03B9EC3-L004821](../../agents/web_agent.py#L4821) | 4821 | `"        raw_plan_queries = plan.get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L004822](../../agents/web_agent.py#L4822) | 4822 | `"        if not isinstance(raw_plan_queries, list):"` | — |
| [SRC-1AE03B9EC3-L004823](../../agents/web_agent.py#L4823) | 4823 | `"            raw_plan_queries = []"` | — |
| [SRC-1AE03B9EC3-L004824](../../agents/web_agent.py#L4824) | 4824 | `"        normalized_plan_queries = []"` | — |
| [SRC-1AE03B9EC3-L004825](../../agents/web_agent.py#L4825) | 4825 | `"        for raw_query in raw_plan_queries:"` | — |
| [SRC-1AE03B9EC3-L004826](../../agents/web_agent.py#L4826) | 4826 | `"            if not isinstance(raw_query, str) or not raw_query.strip():"` | — |
| [SRC-1AE03B9EC3-L004827](../../agents/web_agent.py#L4827) | 4827 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004828](../../agents/web_agent.py#L4828) | 4828 | `"            compacted_query = compact_search_query(raw_query)"` | — |
| [SRC-1AE03B9EC3-L004829](../../agents/web_agent.py#L4829) | 4829 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L004830](../../agents/web_agent.py#L4830) | 4830 | `"                compacted_query"` | — |
| [SRC-1AE03B9EC3-L004831](../../agents/web_agent.py#L4831) | 4831 | `"                and _relevance_query_tokens(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004832](../../agents/web_agent.py#L4832) | 4832 | `"                and compacted_query not in normalized_plan_queries"` | — |
| [SRC-1AE03B9EC3-L004833](../../agents/web_agent.py#L4833) | 4833 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L004834](../../agents/web_agent.py#L4834) | 4834 | `"                normalized_plan_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004835](../../agents/web_agent.py#L4835) | 4835 | `"        plan[\"queries\"] = normalized_plan_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004836](../../agents/web_agent.py#L4836) | 4836 | `"        # Preserve the requested mode in diagnostics even when no usable query exists."` | — |
| [SRC-1AE03B9EC3-L004837](../../agents/web_agent.py#L4837) | 4837 | `"        if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L004838](../../agents/web_agent.py#L4838) | 4838 | `"            plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004839](../../agents/web_agent.py#L4839) | 4839 | `"        elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L004840](../../agents/web_agent.py#L4840) | 4840 | `"            plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004841](../../agents/web_agent.py#L4841) | 4841 | `"        elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L004842](../../agents/web_agent.py#L4842) | 4842 | `"            plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L004843](../../agents/web_agent.py#L4843) | 4843 | `"            if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L004844](../../agents/web_agent.py#L4844) | 4844 | `"                plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L004845](../../agents/web_agent.py#L4845) | 4845 | `""` | — |
| [SRC-1AE03B9EC3-L004846](../../agents/web_agent.py#L4846) | 4846 | `"        if plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L004847](../../agents/web_agent.py#L4847) | 4847 | `"            if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\":"` | — |
| [SRC-1AE03B9EC3-L004848](../../agents/web_agent.py#L4848) | 4848 | `"                plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004849](../../agents/web_agent.py#L4849) | 4849 | `"            if clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L004850](../../agents/web_agent.py#L4850) | 4850 | `"                normalized_question = _normalize_search_query(working_question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004851](../../agents/web_agent.py#L4851) | 4851 | `"                deep_terms = ("` | — |
| [SRC-1AE03B9EC3-L004852](../../agents/web_agent.py#L4852) | 4852 | `"                    \"بحث عميق\", \"بحث معمق\", \"بحث شامل\", \"بالتفصيل\", \"قارن\", \"مقارنة\","` | — |
| [SRC-1AE03B9EC3-L004853](../../agents/web_agent.py#L4853) | 4853 | `"                    \"تحقق\", \"استقصاء\", \"deep research\", \"comprehensive\", \"in-depth\", \"compare\","` | — |
| [SRC-1AE03B9EC3-L004854](../../agents/web_agent.py#L4854) | 4854 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004855](../../agents/web_agent.py#L4855) | 4855 | `"                explicit_deep = intent_route == \"WEB_DEEP\" or any("` | — |
| [SRC-1AE03B9EC3-L004856](../../agents/web_agent.py#L4856) | 4856 | `"                    term in normalized_question for term in deep_terms"` | — |
| [SRC-1AE03B9EC3-L004857](../../agents/web_agent.py#L4857) | 4857 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004858](../../agents/web_agent.py#L4858) | 4858 | `"                if not explicit_deep:"` | — |
| [SRC-1AE03B9EC3-L004859](../../agents/web_agent.py#L4859) | 4859 | `"                    # The planner may overclassify short lookups as deep research. Preserve"` | — |
| [SRC-1AE03B9EC3-L004860](../../agents/web_agent.py#L4860) | 4860 | `"                    # the user's actual intent first and cap routine searches to three queries."` | — |
| [SRC-1AE03B9EC3-L004861](../../agents/web_agent.py#L4861) | 4861 | `"                    fallback_plan_queries = ("` | — |
| [SRC-1AE03B9EC3-L004862](../../agents/web_agent.py#L4862) | 4862 | `"                        fallback_plan(working_question, clean_history).get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L004863](../../agents/web_agent.py#L4863) | 4863 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004864](../../agents/web_agent.py#L4864) | 4864 | `"                    fallback_queries = ["` | — |
| [SRC-1AE03B9EC3-L004865](../../agents/web_agent.py#L4865) | 4865 | `"                        compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L004866](../../agents/web_agent.py#L4866) | 4866 | `"                        for query in fallback_plan_queries"` | — |
| [SRC-1AE03B9EC3-L004867](../../agents/web_agent.py#L4867) | 4867 | `"                        if isinstance(query, str)"` | — |
| [SRC-1AE03B9EC3-L004868](../../agents/web_agent.py#L4868) | 4868 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004869](../../agents/web_agent.py#L4869) | 4869 | `"                    fallback_queries = [query for query in fallback_queries if query]"` | — |
| [SRC-1AE03B9EC3-L004870](../../agents/web_agent.py#L4870) | 4870 | `"                    model_queries = ["` | — |
| [SRC-1AE03B9EC3-L004871](../../agents/web_agent.py#L4871) | 4871 | `"                        compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L004872](../../agents/web_agent.py#L4872) | 4872 | `"                        for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004873](../../agents/web_agent.py#L4873) | 4873 | `"                        if isinstance(query, str)"` | — |
| [SRC-1AE03B9EC3-L004874](../../agents/web_agent.py#L4874) | 4874 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004875](../../agents/web_agent.py#L4875) | 4875 | `"                    model_queries = [query for query in model_queries if query]"` | — |
| [SRC-1AE03B9EC3-L004876](../../agents/web_agent.py#L4876) | 4876 | `"                    if self._is_navigation_request(working_question):"` | — |
| [SRC-1AE03B9EC3-L004877](../../agents/web_agent.py#L4877) | 4877 | `"                        navigation_seed = ("` | — |
| [SRC-1AE03B9EC3-L004878](../../agents/web_agent.py#L4878) | 4878 | `"                            fallback_queries[0] if fallback_queries"` | — |
| [SRC-1AE03B9EC3-L004879](../../agents/web_agent.py#L4879) | 4879 | `"                            else model_queries[0] if model_queries"` | — |
| [SRC-1AE03B9EC3-L004880](../../agents/web_agent.py#L4880) | 4880 | `"                            else \"\""` | — |
| [SRC-1AE03B9EC3-L004881](../../agents/web_agent.py#L4881) | 4881 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004882](../../agents/web_agent.py#L4882) | 4882 | `"                        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L004883](../../agents/web_agent.py#L4883) | 4883 | `"                            r\"^(?:ابحث\|بحث\|دور\|اعثر)\\s+(?:عن\|على)?\\s*\","` | — |
| [SRC-1AE03B9EC3-L004884](../../agents/web_agent.py#L4884) | 4884 | `"                            \"\","` | — |
| [SRC-1AE03B9EC3-L004885](../../agents/web_agent.py#L4885) | 4885 | `"                            navigation_seed,"` | — |
| [SRC-1AE03B9EC3-L004886](../../agents/web_agent.py#L4886) | 4886 | `"                        ).strip()"` | — |
| [SRC-1AE03B9EC3-L004887](../../agents/web_agent.py#L4887) | 4887 | `"                        plan_queries = ("` | — |
| [SRC-1AE03B9EC3-L004888](../../agents/web_agent.py#L4888) | 4888 | `"                            ["` | — |
| [SRC-1AE03B9EC3-L004889](../../agents/web_agent.py#L4889) | 4889 | `"                                subject,"` | — |
| [SRC-1AE03B9EC3-L004890](../../agents/web_agent.py#L4890) | 4890 | `"                                subject + \" الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L004891](../../agents/web_agent.py#L4891) | 4891 | `"                                subject + \" official website\","` | — |
| [SRC-1AE03B9EC3-L004892](../../agents/web_agent.py#L4892) | 4892 | `"                            ]"` | — |
| [SRC-1AE03B9EC3-L004893](../../agents/web_agent.py#L4893) | 4893 | `"                            if subject else []"` | — |
| [SRC-1AE03B9EC3-L004894](../../agents/web_agent.py#L4894) | 4894 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004895](../../agents/web_agent.py#L4895) | 4895 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004896](../../agents/web_agent.py#L4896) | 4896 | `"                        plan_queries = (fallback_queries[:1] or model_queries[:1]) + model_queries"` | — |
| [SRC-1AE03B9EC3-L004897](../../agents/web_agent.py#L4897) | 4897 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004898](../../agents/web_agent.py#L4898) | 4898 | `"                        query.strip() for query in plan_queries if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004899](../../agents/web_agent.py#L4899) | 4899 | `"                    ))[:3]"` | — |
| [SRC-1AE03B9EC3-L004900](../../agents/web_agent.py#L4900) | 4900 | `"                    plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L004901](../../agents/web_agent.py#L4901) | 4901 | `"            base_query = (plan.get(\"queries\") or [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L004902](../../agents/web_agent.py#L4902) | 4902 | `"            if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\" and base_query:"` | — |
| [SRC-1AE03B9EC3-L004903](../../agents/web_agent.py#L4903) | 4903 | `"                deep_candidates = ["` | — |
| [SRC-1AE03B9EC3-L004904](../../agents/web_agent.py#L4904) | 4904 | `"                    f\"{base_query} official sources evidence\","` | — |
| [SRC-1AE03B9EC3-L004905](../../agents/web_agent.py#L4905) | 4905 | `"                    f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L004906](../../agents/web_agent.py#L4906) | 4906 | `"                    f\"{base_query} recent data reviews comparison\","` | — |
| [SRC-1AE03B9EC3-L004907](../../agents/web_agent.py#L4907) | 4907 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004908](../../agents/web_agent.py#L4908) | 4908 | `"                normalized_question = _normalize_search_query(working_question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004909](../../agents/web_agent.py#L4909) | 4909 | `"                property_terms = ("` | — |
| [SRC-1AE03B9EC3-L004910](../../agents/web_agent.py#L4910) | 4910 | `"                    \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L004911](../../agents/web_agent.py#L4911) | 4911 | `"                    \"apartment\", \"apartments\", \"flat\", \"real estate\", \"property\", \"house\", \"villa\","` | — |
| [SRC-1AE03B9EC3-L004912](../../agents/web_agent.py#L4912) | 4912 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004913](../../agents/web_agent.py#L4913) | 4913 | `"                if self._is_listing_discovery(working_question) and any("` | — |
| [SRC-1AE03B9EC3-L004914](../../agents/web_agent.py#L4914) | 4914 | `"                    term in normalized_question for term in property_terms"` | — |
| [SRC-1AE03B9EC3-L004915](../../agents/web_agent.py#L4915) | 4915 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004916](../../agents/web_agent.py#L4916) | 4916 | `"                    deep_candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L004917](../../agents/web_agent.py#L4917) | 4917 | `"                        f\"{base_query} إعلانات عقارية ومواقع العقارات\","` | — |
| [SRC-1AE03B9EC3-L004918](../../agents/web_agent.py#L4918) | 4918 | `"                        f\"{base_query} متوسط أسعار السوق للمتر\","` | — |
| [SRC-1AE03B9EC3-L004919](../../agents/web_agent.py#L4919) | 4919 | `"                        f\"{base_query} مواصفات الوحدات والمساحات وطرق السداد\","` | — |
| [SRC-1AE03B9EC3-L004920](../../agents/web_agent.py#L4920) | 4920 | `"                    ])"` | — |
| [SRC-1AE03B9EC3-L004921](../../agents/web_agent.py#L4921) | 4921 | `"                # Close the planning loop: give every explicit user criterion its own"` | — |
| [SRC-1AE03B9EC3-L004922](../../agents/web_agent.py#L4922) | 4922 | `"                # query before generic \"deep research\" queries consume the fixed budget."` | — |
| [SRC-1AE03B9EC3-L004923](../../agents/web_agent.py#L4923) | 4923 | `"                # This is a retrieval heuristic, not a guarantee that evidence exists."` | — |
| [SRC-1AE03B9EC3-L004924](../../agents/web_agent.py#L4924) | 4924 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004925](../../agents/web_agent.py#L4925) | 4925 | `"                    compact_search_query(f\"{base_query} {target} official data specifications\")"` | — |
| [SRC-1AE03B9EC3-L004926](../../agents/web_agent.py#L4926) | 4926 | `"                    for target in self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004927](../../agents/web_agent.py#L4927) | 4927 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004928](../../agents/web_agent.py#L4928) | 4928 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004929](../../agents/web_agent.py#L4929) | 4929 | `"                    query for query in criterion_queries"` | — |
| [SRC-1AE03B9EC3-L004930](../../agents/web_agent.py#L4930) | 4930 | `"                    if query and _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L004931](../../agents/web_agent.py#L4931) | 4931 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004932](../../agents/web_agent.py#L4932) | 4932 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L004933](../../agents/web_agent.py#L4933) | 4933 | `"                    query for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004934](../../agents/web_agent.py#L4934) | 4934 | `"                    if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004935](../../agents/web_agent.py#L4935) | 4935 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004936](../../agents/web_agent.py#L4936) | 4936 | `"                # Each criterion query already contains the base subject. When the"` | — |
| [SRC-1AE03B9EC3-L004937](../../agents/web_agent.py#L4937) | 4937 | `"                # question has many criteria, spend the full bounded budget on those"` | — |
| [SRC-1AE03B9EC3-L004938](../../agents/web_agent.py#L4938) | 4938 | `"                # queries rather than silently dropping later criteria for a base query."` | — |
| [SRC-1AE03B9EC3-L004939](../../agents/web_agent.py#L4939) | 4939 | `"                prioritized_queries = criterion_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004940](../../agents/web_agent.py#L4940) | 4940 | `"                if len(prioritized_queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-1AE03B9EC3-L004941](../../agents/web_agent.py#L4941) | 4941 | `"                    prioritized_queries += original_queries[:1] + deep_candidates"` | — |
| [SRC-1AE03B9EC3-L004942](../../agents/web_agent.py#L4942) | 4942 | `"                plan[\"queries\"] = list(dict.fromkeys(prioritized_queries))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004943](../../agents/web_agent.py#L4943) | 4943 | `"                base_query = (plan.get(\"queries\") or [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L004944](../../agents/web_agent.py#L4944) | 4944 | `"            # Explicit user-selected modes are control inputs. They do not bypass source"` | — |
| [SRC-1AE03B9EC3-L004945](../../agents/web_agent.py#L4945) | 4945 | `"            # validation and never permit private-source access."` | — |
| [SRC-1AE03B9EC3-L004946](../../agents/web_agent.py#L4946) | 4946 | `"            if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L004947](../../agents/web_agent.py#L4947) | 4947 | `"                plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004948](../../agents/web_agent.py#L4948) | 4948 | `"                candidates = ["` | — |
| [SRC-1AE03B9EC3-L004949](../../agents/web_agent.py#L4949) | 4949 | `"                    f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L004950](../../agents/web_agent.py#L4950) | 4950 | `"                    f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L004951](../../agents/web_agent.py#L4951) | 4951 | `"                    f\"{base_query} case studies recent analysis\","` | — |
| [SRC-1AE03B9EC3-L004952](../../agents/web_agent.py#L4952) | 4952 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004953](../../agents/web_agent.py#L4953) | 4953 | `"                normalized_question = _normalize_search_query(working_question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004954](../../agents/web_agent.py#L4954) | 4954 | `"                property_terms = ("` | — |
| [SRC-1AE03B9EC3-L004955](../../agents/web_agent.py#L4955) | 4955 | `"                    \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L004956](../../agents/web_agent.py#L4956) | 4956 | `"                    \"apartment\", \"apartments\", \"flat\", \"real estate\", \"property\", \"house\", \"villa\","` | — |
| [SRC-1AE03B9EC3-L004957](../../agents/web_agent.py#L4957) | 4957 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004958](../../agents/web_agent.py#L4958) | 4958 | `"                if self._is_listing_discovery(working_question) and any("` | — |
| [SRC-1AE03B9EC3-L004959](../../agents/web_agent.py#L4959) | 4959 | `"                    term in normalized_question for term in property_terms"` | — |
| [SRC-1AE03B9EC3-L004960](../../agents/web_agent.py#L4960) | 4960 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004961](../../agents/web_agent.py#L4961) | 4961 | `"                    candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L004962](../../agents/web_agent.py#L4962) | 4962 | `"                        f\"{base_query} إعلانات عقارية ومواقع العقارات\","` | — |
| [SRC-1AE03B9EC3-L004963](../../agents/web_agent.py#L4963) | 4963 | `"                        f\"{base_query} متوسط أسعار السوق للمتر\","` | — |
| [SRC-1AE03B9EC3-L004964](../../agents/web_agent.py#L4964) | 4964 | `"                        f\"{base_query} مواصفات الوحدات والمساحات وطرق السداد\","` | — |
| [SRC-1AE03B9EC3-L004965](../../agents/web_agent.py#L4965) | 4965 | `"                    ])"` | — |
| [SRC-1AE03B9EC3-L004966](../../agents/web_agent.py#L4966) | 4966 | `"                # Explicit deep mode follows the same criterion-first budget allocation"` | — |
| [SRC-1AE03B9EC3-L004967](../../agents/web_agent.py#L4967) | 4967 | `"                # as automatic deep mode, so generic modifiers cannot crowd out requested"` | — |
| [SRC-1AE03B9EC3-L004968](../../agents/web_agent.py#L4968) | 4968 | `"                # dimensions such as price, battery, camera, privacy, or reliability."` | — |
| [SRC-1AE03B9EC3-L004969](../../agents/web_agent.py#L4969) | 4969 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004970](../../agents/web_agent.py#L4970) | 4970 | `"                    compact_search_query(f\"{base_query} {target} official data specifications\")"` | — |
| [SRC-1AE03B9EC3-L004971](../../agents/web_agent.py#L4971) | 4971 | `"                    for target in self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004972](../../agents/web_agent.py#L4972) | 4972 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004973](../../agents/web_agent.py#L4973) | 4973 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004974](../../agents/web_agent.py#L4974) | 4974 | `"                    query for query in criterion_queries"` | — |
| [SRC-1AE03B9EC3-L004975](../../agents/web_agent.py#L4975) | 4975 | `"                    if query and _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L004976](../../agents/web_agent.py#L4976) | 4976 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004977](../../agents/web_agent.py#L4977) | 4977 | `"                # Criterion queries include the subject and take priority; retain a"` | — |
| [SRC-1AE03B9EC3-L004978](../../agents/web_agent.py#L4978) | 4978 | `"                # planner query and generic exploration only when budget remains."` | — |
| [SRC-1AE03B9EC3-L004979](../../agents/web_agent.py#L4979) | 4979 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L004980](../../agents/web_agent.py#L4980) | 4980 | `"                    query for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004981](../../agents/web_agent.py#L4981) | 4981 | `"                    if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004982](../../agents/web_agent.py#L4982) | 4982 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004983](../../agents/web_agent.py#L4983) | 4983 | `"                prioritized_queries = criterion_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004984](../../agents/web_agent.py#L4984) | 4984 | `"                if len(prioritized_queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-1AE03B9EC3-L004985](../../agents/web_agent.py#L4985) | 4985 | `"                    prioritized_queries += original_queries[:1] + candidates"` | — |
| [SRC-1AE03B9EC3-L004986](../../agents/web_agent.py#L4986) | 4986 | `"                plan[\"queries\"] = list(dict.fromkeys(prioritized_queries))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004987](../../agents/web_agent.py#L4987) | 4987 | `"            elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L004988](../../agents/web_agent.py#L4988) | 4988 | `"                plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004989](../../agents/web_agent.py#L4989) | 4989 | `"                if self._is_navigation_request(working_question):"` | — |
| [SRC-1AE03B9EC3-L004990](../../agents/web_agent.py#L4990) | 4990 | `"                    # Preserve link-finding intent in the latest mode. Appending broad"` | — |
| [SRC-1AE03B9EC3-L004991](../../agents/web_agent.py#L4991) | 4991 | `"                    # news modifiers here can turn \"find the official website\" into"` | — |
| [SRC-1AE03B9EC3-L004992](../../agents/web_agent.py#L4992) | 4992 | `"                    # a news-search task and hide the destination the user requested."` | — |
| [SRC-1AE03B9EC3-L004993](../../agents/web_agent.py#L4993) | 4993 | `"                    candidates = ["` | — |
| [SRC-1AE03B9EC3-L004994](../../agents/web_agent.py#L4994) | 4994 | `"                        base_query,"` | — |
| [SRC-1AE03B9EC3-L004995](../../agents/web_agent.py#L4995) | 4995 | `"                        f\"{base_query} الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L004996](../../agents/web_agent.py#L4996) | 4996 | `"                        f\"{base_query} official website\","` | — |
| [SRC-1AE03B9EC3-L004997](../../agents/web_agent.py#L4997) | 4997 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004998](../../agents/web_agent.py#L4998) | 4998 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004999](../../agents/web_agent.py#L4999) | 4999 | `"                        candidates + (plan.get(\"queries\") or [])[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L005000](../../agents/web_agent.py#L5000) | 5000 | `"                    ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L005001](../../agents/web_agent.py#L5001) | 5001 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005002](../../agents/web_agent.py#L5002) | 5002 | `"                    candidates = ["` | — |
| [SRC-1AE03B9EC3-L005003](../../agents/web_agent.py#L5003) | 5003 | `"                        f\"{base_query} latest news updates {dt.datetime.now().year}\","` | — |
| [SRC-1AE03B9EC3-L005004](../../agents/web_agent.py#L5004) | 5004 | `"                        f\"{base_query} recent official announcement\","` | — |
| [SRC-1AE03B9EC3-L005005](../../agents/web_agent.py#L5005) | 5005 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L005006](../../agents/web_agent.py#L5006) | 5006 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005007](../../agents/web_agent.py#L5007) | 5007 | `"                        (plan.get(\"queries\") or [])[:6] + candidates"` | — |
| [SRC-1AE03B9EC3-L005008](../../agents/web_agent.py#L5008) | 5008 | `"                    ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L005009](../../agents/web_agent.py#L5009) | 5009 | `"            elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L005010](../../agents/web_agent.py#L5010) | 5010 | `"                plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L005011](../../agents/web_agent.py#L5011) | 5011 | `"                if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L005012](../../agents/web_agent.py#L5012) | 5012 | `"                    plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L005013](../../agents/web_agent.py#L5013) | 5013 | `"                from agents.research import SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L005014](../../agents/web_agent.py#L5014) | 5014 | `"                candidates = ["` | — |
| [SRC-1AE03B9EC3-L005015](../../agents/web_agent.py#L5015) | 5015 | `"                    f\"site:{SOCIAL_DOMAINS[name]} {base_query}\""` | — |
| [SRC-1AE03B9EC3-L005016](../../agents/web_agent.py#L5016) | 5016 | `"                    for name in plan[\"platforms\"][:3]"` | — |
| [SRC-1AE03B9EC3-L005017](../../agents/web_agent.py#L5017) | 5017 | `"                    if name in SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L005018](../../agents/web_agent.py#L5018) | 5018 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L005019](../../agents/web_agent.py#L5019) | 5019 | `"                plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:5] + candidates))["` | — |
| [SRC-1AE03B9EC3-L005020](../../agents/web_agent.py#L5020) | 5020 | `"                    :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L005021](../../agents/web_agent.py#L5021) | 5021 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L005022](../../agents/web_agent.py#L5022) | 5022 | `"            if intent_route == \"LEAD_GENERATION\" and clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L005023](../../agents/web_agent.py#L5023) | 5023 | `"                # Prospect discovery needs buyer-intent queries and public social signals,"` | — |
| [SRC-1AE03B9EC3-L005024](../../agents/web_agent.py#L5024) | 5024 | `"                # not just broad pages advertising the requested product."` | — |
| [SRC-1AE03B9EC3-L005025](../../agents/web_agent.py#L5025) | 5025 | `"                plan[\"queries\"] = self._lead_generation_queries(working_question, plan.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005026](../../agents/web_agent.py#L5026) | 5026 | `"                plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L005027](../../agents/web_agent.py#L5027) | 5027 | `"                plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L005028](../../agents/web_agent.py#L5028) | 5028 | `"                plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L005029](../../agents/web_agent.py#L5029) | 5029 | `"                allowed_public_platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L005030](../../agents/web_agent.py#L5030) | 5030 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L005031](../../agents/web_agent.py#L5031) | 5031 | `"                    os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L005032](../../agents/web_agent.py#L5032) | 5032 | `"                    and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L005033](../../agents/web_agent.py#L5033) | 5033 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L005034](../../agents/web_agent.py#L5034) | 5034 | `"                    allowed_public_platforms.append(\"facebook\")"` | — |
| [SRC-1AE03B9EC3-L005035](../../agents/web_agent.py#L5035) | 5035 | `"                if os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L005036](../../agents/web_agent.py#L5036) | 5036 | `"                    allowed_public_platforms.append(\"x\")"` | — |
| [SRC-1AE03B9EC3-L005037](../../agents/web_agent.py#L5037) | 5037 | `"                if os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L005038](../../agents/web_agent.py#L5038) | 5038 | `"                    allowed_public_platforms.append(\"youtube\")"` | — |
| [SRC-1AE03B9EC3-L005039](../../agents/web_agent.py#L5039) | 5039 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L005040](../../agents/web_agent.py#L5040) | 5040 | `"                    os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L005041](../../agents/web_agent.py#L5041) | 5041 | `"                    and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L005042](../../agents/web_agent.py#L5042) | 5042 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L005043](../../agents/web_agent.py#L5043) | 5043 | `"                    allowed_public_platforms.append(\"instagram\")"` | — |
| [SRC-1AE03B9EC3-L005044](../../agents/web_agent.py#L5044) | 5044 | `"                plan[\"platforms\"] = list(dict.fromkeys(allowed_public_platforms))"` | — |
| [SRC-1AE03B9EC3-L005045](../../agents/web_agent.py#L5045) | 5045 | `""` | — |
| [SRC-1AE03B9EC3-L005046](../../agents/web_agent.py#L5046) | 5046 | `"        pipeline = build_research_pipeline("` | — |
| [SRC-1AE03B9EC3-L005047](../../agents/web_agent.py#L5047) | 5047 | `"            working_question,"` | — |
| [SRC-1AE03B9EC3-L005048](../../agents/web_agent.py#L5048) | 5048 | `"            plan,"` | — |
| [SRC-1AE03B9EC3-L005049](../../agents/web_agent.py#L5049) | 5049 | `"            mode=clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005050](../../agents/web_agent.py#L5050) | 5050 | `"            intent_route=intent_route,"` | — |
| [SRC-1AE03B9EC3-L005051](../../agents/web_agent.py#L5051) | 5051 | `"            dialogue_context=dialogue_context if isinstance(dialogue_context, dict) else None,"` | — |
| [SRC-1AE03B9EC3-L005052](../../agents/web_agent.py#L5052) | 5052 | `"            compact_fn=compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L005053](../../agents/web_agent.py#L5053) | 5053 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005054](../../agents/web_agent.py#L5054) | 5054 | `"        task_spec = pipeline[\"task_spec\"]"` | — |
| [SRC-1AE03B9EC3-L005055](../../agents/web_agent.py#L5055) | 5055 | `"        query_strategy_limit = ("` | — |
| [SRC-1AE03B9EC3-L005056](../../agents/web_agent.py#L5056) | 5056 | `"            MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L005057](../../agents/web_agent.py#L5057) | 5057 | `"            if clean_mode in {\"deep\", \"latest\", \"social\"}"` | — |
| [SRC-1AE03B9EC3-L005058](../../agents/web_agent.py#L5058) | 5058 | `"            or intent_route in {\"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-1AE03B9EC3-L005059](../../agents/web_agent.py#L5059) | 5059 | `"            else 3"` | — |
| [SRC-1AE03B9EC3-L005060](../../agents/web_agent.py#L5060) | 5060 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005061](../../agents/web_agent.py#L5061) | 5061 | `"        query_strategy_matrix = pipeline[\"query_strategy_matrix\"][:query_strategy_limit]"` | — |
| [SRC-1AE03B9EC3-L005062](../../agents/web_agent.py#L5062) | 5062 | `"        if query_strategy_matrix:"` | — |
| [SRC-1AE03B9EC3-L005063](../../agents/web_agent.py#L5063) | 5063 | `"            plan[\"queries\"] = [item[\"query\"] for item in query_strategy_matrix]"` | — |
| [SRC-1AE03B9EC3-L005064](../../agents/web_agent.py#L5064) | 5064 | `"        plan[\"task_spec\"] = task_spec"` | — |
| [SRC-1AE03B9EC3-L005065](../../agents/web_agent.py#L5065) | 5065 | `"        plan[\"query_strategy_matrix\"] = query_strategy_matrix"` | — |
| [SRC-1AE03B9EC3-L005066](../../agents/web_agent.py#L5066) | 5066 | `"        plan[\"research_pipeline\"] = {"` | — |
| [SRC-1AE03B9EC3-L005067](../../agents/web_agent.py#L5067) | 5067 | `"            \"aspects\": pipeline[\"aspects\"],"` | — |
| [SRC-1AE03B9EC3-L005068](../../agents/web_agent.py#L5068) | 5068 | `"            \"stages\": pipeline[\"stages\"],"` | — |
| [SRC-1AE03B9EC3-L005069](../../agents/web_agent.py#L5069) | 5069 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005070](../../agents/web_agent.py#L5070) | 5070 | `""` | — |
| [SRC-1AE03B9EC3-L005071](../../agents/web_agent.py#L5071) | 5071 | `"        final_topic_queries = []"` | — |
| [SRC-1AE03B9EC3-L005072](../../agents/web_agent.py#L5072) | 5072 | `"        for raw_query in plan.get(\"queries\", []):"` | — |
| [SRC-1AE03B9EC3-L005073](../../agents/web_agent.py#L5073) | 5073 | `"            if not isinstance(raw_query, str) or not raw_query.strip():"` | — |
| [SRC-1AE03B9EC3-L005074](../../agents/web_agent.py#L5074) | 5074 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L005075](../../agents/web_agent.py#L5075) | 5075 | `"            compacted_query = compact_search_query(raw_query)"` | — |
| [SRC-1AE03B9EC3-L005076](../../agents/web_agent.py#L5076) | 5076 | `"            if compacted_query and _relevance_query_tokens(compacted_query):"` | — |
| [SRC-1AE03B9EC3-L005077](../../agents/web_agent.py#L5077) | 5077 | `"                final_topic_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L005078](../../agents/web_agent.py#L5078) | 5078 | `"        coverage_targets_for_budget = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005079](../../agents/web_agent.py#L5079) | 5079 | `"        # Reserve one bounded search slot for a post-review criterion-evidence gap."` | — |
| [SRC-1AE03B9EC3-L005080](../../agents/web_agent.py#L5080) | 5080 | `"        # Keep all explicit criterion queries when there are many dimensions; the"` | — |
| [SRC-1AE03B9EC3-L005081](../../agents/web_agent.py#L5081) | 5081 | `"        # reserve applies only to ordinary compound tasks with up to six targets."` | — |
| [SRC-1AE03B9EC3-L005082](../../agents/web_agent.py#L5082) | 5082 | `"        reserve_coverage_gap_query = ("` | — |
| [SRC-1AE03B9EC3-L005083](../../agents/web_agent.py#L5083) | 5083 | `"            2 <= len(coverage_targets_for_budget) <= 6"` | — |
| [SRC-1AE03B9EC3-L005084](../../agents/web_agent.py#L5084) | 5084 | `"            and plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L005085](../../agents/web_agent.py#L5085) | 5085 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005086](../../agents/web_agent.py#L5086) | 5086 | `"        query_limit = MAX_PLAN_QUERIES - 1 if reserve_coverage_gap_query else MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L005087](../../agents/web_agent.py#L5087) | 5087 | `"        plan[\"coverage_gap_repair_slot_reserved\"] = reserve_coverage_gap_query"` | — |
| [SRC-1AE03B9EC3-L005088](../../agents/web_agent.py#L5088) | 5088 | `"        plan[\"query_limit\"] = query_limit"` | — |
| [SRC-1AE03B9EC3-L005089](../../agents/web_agent.py#L5089) | 5089 | `"        plan[\"coverage_targets\"] = list(coverage_targets_for_budget)"` | — |
| [SRC-1AE03B9EC3-L005090](../../agents/web_agent.py#L5090) | 5090 | `"        plan[\"queries\"] = list(dict.fromkeys(final_topic_queries))[:query_limit]"` | — |
| [SRC-1AE03B9EC3-L005091](../../agents/web_agent.py#L5091) | 5091 | `"        actual_query_keys = set(plan[\"queries\"])"` | — |
| [SRC-1AE03B9EC3-L005092](../../agents/web_agent.py#L5092) | 5092 | `"        plan[\"query_strategy_matrix\"] = ["` | — |
| [SRC-1AE03B9EC3-L005093](../../agents/web_agent.py#L5093) | 5093 | `"            item for item in query_strategy_matrix"` | — |
| [SRC-1AE03B9EC3-L005094](../../agents/web_agent.py#L5094) | 5094 | `"            if item.get(\"query\") in actual_query_keys"` | — |
| [SRC-1AE03B9EC3-L005095](../../agents/web_agent.py#L5095) | 5095 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L005096](../../agents/web_agent.py#L5096) | 5096 | `""` | — |
| [SRC-1AE03B9EC3-L005097](../../agents/web_agent.py#L5097) | 5097 | `"        sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L005098](../../agents/web_agent.py#L5098) | 5098 | `"        search_warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L005099](../../agents/web_agent.py#L5099) | 5099 | `"        report: dict[str, Any] = {}"` | — |
| [SRC-1AE03B9EC3-L005100](../../agents/web_agent.py#L5100) | 5100 | `"        # Scope diagnostic evidence to this research attempt; a reused WebAgent must not"` | — |
| [SRC-1AE03B9EC3-L005101](../../agents/web_agent.py#L5101) | 5101 | `"        # accidentally inherit provider attempts from an earlier question."` | — |
| [SRC-1AE03B9EC3-L005102](../../agents/web_agent.py#L5102) | 5102 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L005103](../../agents/web_agent.py#L5103) | 5103 | `"            research_diagnostic_baseline = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L005104](../../agents/web_agent.py#L5104) | 5104 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005105](../../agents/web_agent.py#L5105) | 5105 | `"            sources, search_warnings, report = self._collect_research(plan)"` | — |
| [SRC-1AE03B9EC3-L005106](../../agents/web_agent.py#L5106) | 5106 | `"        except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005107](../../agents/web_agent.py#L5107) | 5107 | `"            search_warnings.append(str(exc))"` | — |
| [SRC-1AE03B9EC3-L005108](../../agents/web_agent.py#L5108) | 5108 | `"            baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L005109](../../agents/web_agent.py#L5109) | 5109 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L005110](../../agents/web_agent.py#L5110) | 5110 | `"                failure_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L005111](../../agents/web_agent.py#L5111) | 5111 | `"                    item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005112](../../agents/web_agent.py#L5112) | 5112 | `"                    if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L005113](../../agents/web_agent.py#L5113) | 5113 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L005114](../../agents/web_agent.py#L5114) | 5114 | `"            provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L005115](../../agents/web_agent.py#L5115) | 5115 | `"                item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L005116](../../agents/web_agent.py#L5116) | 5116 | `"                for item in failure_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005117](../../agents/web_agent.py#L5117) | 5117 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005118](../../agents/web_agent.py#L5118) | 5118 | `"            report = {"` | — |
| [SRC-1AE03B9EC3-L005119](../../agents/web_agent.py#L5119) | 5119 | `"                \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-1AE03B9EC3-L005120](../../agents/web_agent.py#L5120) | 5120 | `"                # The exact query count is unknowable when the pipeline fails before it"` | — |
| [SRC-1AE03B9EC3-L005121](../../agents/web_agent.py#L5121) | 5121 | `"                # returns its report. A provider diagnostic may still prove an attempt."` | — |
| [SRC-1AE03B9EC3-L005122](../../agents/web_agent.py#L5122) | 5122 | `"                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005123](../../agents/web_agent.py#L5123) | 5123 | `"                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L005124](../../agents/web_agent.py#L5124) | 5124 | `"                \"search_attempted\": True if provider_attempt_observed else None,"` | — |
| [SRC-1AE03B9EC3-L005125](../../agents/web_agent.py#L5125) | 5125 | `"                \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L005126](../../agents/web_agent.py#L5126) | 5126 | `"                    \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L005127](../../agents/web_agent.py#L5127) | 5127 | `"                    if provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L005128](../../agents/web_agent.py#L5128) | 5128 | `"                    else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005129](../../agents/web_agent.py#L5129) | 5129 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005130](../../agents/web_agent.py#L5130) | 5130 | `"                \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L005131](../../agents/web_agent.py#L5131) | 5131 | `"                \"unique_sources\": None,"` | — |
| [SRC-1AE03B9EC3-L005132](../../agents/web_agent.py#L5132) | 5132 | `"                \"pages_fetched\": None,"` | — |
| [SRC-1AE03B9EC3-L005133](../../agents/web_agent.py#L5133) | 5133 | `"                \"providers_used\": [],"` | — |
| [SRC-1AE03B9EC3-L005134](../../agents/web_agent.py#L5134) | 5134 | `"                \"provider_counts\": None,"` | — |
| [SRC-1AE03B9EC3-L005135](../../agents/web_agent.py#L5135) | 5135 | `"                \"platform_counts\": {},"` | — |
| [SRC-1AE03B9EC3-L005136](../../agents/web_agent.py#L5136) | 5136 | `"                \"social_direct_results\": None,"` | — |
| [SRC-1AE03B9EC3-L005137](../../agents/web_agent.py#L5137) | 5137 | `"                \"provider_diagnostics\": failure_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L005138](../../agents/web_agent.py#L5138) | 5138 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005139](../../agents/web_agent.py#L5139) | 5139 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005140](../../agents/web_agent.py#L5140) | 5140 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005141](../../agents/web_agent.py#L5141) | 5141 | `"                \"evidence_signals\": evidence_signal_report([], plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L005142](../../agents/web_agent.py#L5142) | 5142 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005143](../../agents/web_agent.py#L5143) | 5143 | `"        if isinstance(report, dict):"` | — |
| [SRC-1AE03B9EC3-L005144](../../agents/web_agent.py#L5144) | 5144 | `"            report[\"dialogue_context\"] = plan.get(\"dialogue_context\", {})"` | — |
| [SRC-1AE03B9EC3-L005145](../../agents/web_agent.py#L5145) | 5145 | `"            report[\"task_understanding\"] = {"` | — |
| [SRC-1AE03B9EC3-L005146](../../agents/web_agent.py#L5146) | 5146 | `"                \"task_spec\": task_spec,"` | — |
| [SRC-1AE03B9EC3-L005147](../../agents/web_agent.py#L5147) | 5147 | `"                \"query_strategy_matrix\": plan.get(\"query_strategy_matrix\", []),"` | — |
| [SRC-1AE03B9EC3-L005148](../../agents/web_agent.py#L5148) | 5148 | `"                \"actual_queries\": list(plan.get(\"queries\") or []),"` | — |
| [SRC-1AE03B9EC3-L005149](../../agents/web_agent.py#L5149) | 5149 | `"                \"actual_query_count\": len(plan.get(\"queries\") or []),"` | — |
| [SRC-1AE03B9EC3-L005150](../../agents/web_agent.py#L5150) | 5150 | `"                \"max_query_count\": MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L005151](../../agents/web_agent.py#L5151) | 5151 | `"                \"status\": \"deterministic_interpretation_attached\","` | — |
| [SRC-1AE03B9EC3-L005152](../../agents/web_agent.py#L5152) | 5152 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005153](../../agents/web_agent.py#L5153) | 5153 | `"        # Final relevance check is intentionally repeated after fusion, before any answer LLM call."` | — |
| [SRC-1AE03B9EC3-L005154](../../agents/web_agent.py#L5154) | 5154 | `"        filtered_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L005155](../../agents/web_agent.py#L5155) | 5155 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L005156](../../agents/web_agent.py#L5156) | 5156 | `"            if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L005157](../../agents/web_agent.py#L5157) | 5157 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L005158](../../agents/web_agent.py#L5158) | 5158 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L005159](../../agents/web_agent.py#L5159) | 5159 | `"            candidate_queries = ("` | — |
| [SRC-1AE03B9EC3-L005160](../../agents/web_agent.py#L5160) | 5160 | `"                source.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L005161](../../agents/web_agent.py#L5161) | 5161 | `"                or plan.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L005162](../../agents/web_agent.py#L5162) | 5162 | `"                or [compact_search_query(working_question)]"` | — |
| [SRC-1AE03B9EC3-L005163](../../agents/web_agent.py#L5163) | 5163 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005164](../../agents/web_agent.py#L5164) | 5164 | `"            if any(self._source_matches_query(str(q), source) for q in candidate_queries):"` | — |
| [SRC-1AE03B9EC3-L005165](../../agents/web_agent.py#L5165) | 5165 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L005166](../../agents/web_agent.py#L5166) | 5166 | `"        sources = filtered_sources"` | — |
| [SRC-1AE03B9EC3-L005167](../../agents/web_agent.py#L5167) | 5167 | `"        sources, initial_source_guardrails = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L005168](../../agents/web_agent.py#L5168) | 5168 | `"            working_question, clean_mode, plan, sources"` | — |
| [SRC-1AE03B9EC3-L005169](../../agents/web_agent.py#L5169) | 5169 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005170](../../agents/web_agent.py#L5170) | 5170 | `"        report[\"research_pipeline\"] = {"` | — |
| [SRC-1AE03B9EC3-L005171](../../agents/web_agent.py#L5171) | 5171 | `"            \"aspects\": pipeline[\"aspects\"],"` | — |
| [SRC-1AE03B9EC3-L005172](../../agents/web_agent.py#L5172) | 5172 | `"            \"evidence\": evaluate_research_evidence(pipeline[\"aspects\"], sources),"` | — |
| [SRC-1AE03B9EC3-L005173](../../agents/web_agent.py#L5173) | 5173 | `"            \"stages\": pipeline[\"stages\"],"` | — |
| [SRC-1AE03B9EC3-L005174](../../agents/web_agent.py#L5174) | 5174 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005175](../../agents/web_agent.py#L5175) | 5175 | `"        report[\"source_guardrails\"] = {"` | — |
| [SRC-1AE03B9EC3-L005176](../../agents/web_agent.py#L5176) | 5176 | `"            \"initial\": initial_source_guardrails,"` | — |
| [SRC-1AE03B9EC3-L005177](../../agents/web_agent.py#L5177) | 5177 | `"            \"initial_eligible_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L005178](../../agents/web_agent.py#L5178) | 5178 | `"            \"final\": None,"` | — |
| [SRC-1AE03B9EC3-L005179](../../agents/web_agent.py#L5179) | 5179 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005180](../../agents/web_agent.py#L5180) | 5180 | `"        if initial_source_guardrails[\"rejected_sources\"]:"` | — |
| [SRC-1AE03B9EC3-L005181](../../agents/web_agent.py#L5181) | 5181 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005182](../../agents/web_agent.py#L5182) | 5182 | `"                \"استُبعدت نتائج لا تستوفي شروط قبول المصدر الخاصة بهذا الطلب؛ \""` | — |
| [SRC-1AE03B9EC3-L005183](../../agents/web_agent.py#L5183) | 5183 | `"                \"راجع تشخيص حواجز الأدلة لمعرفة الأسباب.\""` | — |
| [SRC-1AE03B9EC3-L005184](../../agents/web_agent.py#L5184) | 5184 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005185](../../agents/web_agent.py#L5185) | 5185 | `"        search_warning = \"؛ \".join(search_warnings) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005186](../../agents/web_agent.py#L5186) | 5186 | `"        independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005187](../../agents/web_agent.py#L5187) | 5187 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005188](../../agents/web_agent.py#L5188) | 5188 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005189](../../agents/web_agent.py#L5189) | 5189 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005190](../../agents/web_agent.py#L5190) | 5190 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L005191](../../agents/web_agent.py#L5191) | 5191 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005192](../../agents/web_agent.py#L5192) | 5192 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005193](../../agents/web_agent.py#L5193) | 5193 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005194](../../agents/web_agent.py#L5194) | 5194 | `"        independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005195](../../agents/web_agent.py#L5195) | 5195 | `"        # A user-requested page summary is a different task from open-ended research:"` | — |
| [SRC-1AE03B9EC3-L005196](../../agents/web_agent.py#L5196) | 5196 | `"        # one successfully extracted, explicitly supplied page can support a summary,"` | — |
| [SRC-1AE03B9EC3-L005197](../../agents/web_agent.py#L5197) | 5197 | `"        # but must never be presented as independently corroborated research."` | — |
| [SRC-1AE03B9EC3-L005198](../../agents/web_agent.py#L5198) | 5198 | `"        has_read_user_supplied_page = any("` | — |
| [SRC-1AE03B9EC3-L005199](../../agents/web_agent.py#L5199) | 5199 | `"            \"user_supplied_url\" in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005200](../../agents/web_agent.py#L5200) | 5200 | `"            and bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1AE03B9EC3-L005201](../../agents/web_agent.py#L5201) | 5201 | `"            and bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1AE03B9EC3-L005202](../../agents/web_agent.py#L5202) | 5202 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005203](../../agents/web_agent.py#L5203) | 5203 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005204](../../agents/web_agent.py#L5204) | 5204 | `"        single_source_page_summary = ("` | — |
| [SRC-1AE03B9EC3-L005205](../../agents/web_agent.py#L5205) | 5205 | `"            has_read_user_supplied_page"` | — |
| [SRC-1AE03B9EC3-L005206](../../agents/web_agent.py#L5206) | 5206 | `"            and len(sources) == 1"` | — |
| [SRC-1AE03B9EC3-L005207](../../agents/web_agent.py#L5207) | 5207 | `"            and len(independent_domains) == 1"` | — |
| [SRC-1AE03B9EC3-L005208](../../agents/web_agent.py#L5208) | 5208 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005209](../../agents/web_agent.py#L5209) | 5209 | `"        if single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005210](../../agents/web_agent.py#L5210) | 5210 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005211](../../agents/web_agent.py#L5211) | 5211 | `"                \"هذا ملخص للرابط الذي قدمته فقط؛ لم يتم تأكيد محتواه من مصدر مستقل آخر.\""` | — |
| [SRC-1AE03B9EC3-L005212](../../agents/web_agent.py#L5212) | 5212 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005213](../../agents/web_agent.py#L5213) | 5213 | `"            search_warning = \"؛ \".join(search_warnings)"` | — |
| [SRC-1AE03B9EC3-L005214](../../agents/web_agent.py#L5214) | 5214 | `"        # Link-finding and lead-discovery are actionable discovery tasks, not broad"` | — |
| [SRC-1AE03B9EC3-L005215](../../agents/web_agent.py#L5215) | 5215 | `"        # fact-checking. Keep useful candidates visible while explicitly labelling them"` | — |
| [SRC-1AE03B9EC3-L005216](../../agents/web_agent.py#L5216) | 5216 | `"        # as uncorroborated instead of refusing a lone result as if it were no result."` | — |
| [SRC-1AE03B9EC3-L005217](../../agents/web_agent.py#L5217) | 5217 | `"        navigation_request = self._is_navigation_request(working_question)"` | — |
| [SRC-1AE03B9EC3-L005218](../../agents/web_agent.py#L5218) | 5218 | `"        lead_request = intent_route == \"LEAD_GENERATION\" or self._is_lead_search(working_question)"` | — |
| [SRC-1AE03B9EC3-L005219](../../agents/web_agent.py#L5219) | 5219 | `"        listing_request = self._is_listing_discovery(working_question)"` | — |
| [SRC-1AE03B9EC3-L005220](../../agents/web_agent.py#L5220) | 5220 | `"        lead_evidence_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L005221](../../agents/web_agent.py#L5221) | 5221 | `"        related_lead_results_count = 0"` | — |
| [SRC-1AE03B9EC3-L005222](../../agents/web_agent.py#L5222) | 5222 | `"        if lead_request:"` | — |
| [SRC-1AE03B9EC3-L005223](../../agents/web_agent.py#L5223) | 5223 | `"            related_lead_results_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005224](../../agents/web_agent.py#L5224) | 5224 | `"            for source in sources:"` | — |
| [SRC-1AE03B9EC3-L005225](../../agents/web_agent.py#L5225) | 5225 | `"                signal = self._lead_intent_evidence(source)"` | — |
| [SRC-1AE03B9EC3-L005226](../../agents/web_agent.py#L5226) | 5226 | `"                if signal:"` | — |
| [SRC-1AE03B9EC3-L005227](../../agents/web_agent.py#L5227) | 5227 | `"                    source[\"lead_qualification\"] = \"public_buyer_intent_signal\""` | — |
| [SRC-1AE03B9EC3-L005228](../../agents/web_agent.py#L5228) | 5228 | `"                    source[\"lead_intent_evidence\"] = signal"` | — |
| [SRC-1AE03B9EC3-L005229](../../agents/web_agent.py#L5229) | 5229 | `"                    lead_evidence_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L005230](../../agents/web_agent.py#L5230) | 5230 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005231](../../agents/web_agent.py#L5231) | 5231 | `"                    source[\"lead_qualification\"] = \"related_result_not_lead\""` | — |
| [SRC-1AE03B9EC3-L005232](../../agents/web_agent.py#L5232) | 5232 | `"            lead_research_incomplete = ("` | — |
| [SRC-1AE03B9EC3-L005233](../../agents/web_agent.py#L5233) | 5233 | `"                not sources"` | — |
| [SRC-1AE03B9EC3-L005234](../../agents/web_agent.py#L5234) | 5234 | `"                and report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L005235](../../agents/web_agent.py#L5235) | 5235 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005236](../../agents/web_agent.py#L5236) | 5236 | `"            report[\"lead_generation\"] = {"` | — |
| [SRC-1AE03B9EC3-L005237](../../agents/web_agent.py#L5237) | 5237 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005238](../../agents/web_agent.py#L5238) | 5238 | `"                    \"research_incomplete\" if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L005239](../../agents/web_agent.py#L5239) | 5239 | `"                    else \"candidate_signals_found\" if lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L005240](../../agents/web_agent.py#L5240) | 5240 | `"                    else \"no_qualified_candidates_found\""` | — |
| [SRC-1AE03B9EC3-L005241](../../agents/web_agent.py#L5241) | 5241 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005242](../../agents/web_agent.py#L5242) | 5242 | `"                \"candidate_signal_count\": ("` | — |
| [SRC-1AE03B9EC3-L005243](../../agents/web_agent.py#L5243) | 5243 | `"                    None if lead_research_incomplete else len(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L005244](../../agents/web_agent.py#L5244) | 5244 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005245](../../agents/web_agent.py#L5245) | 5245 | `"                \"related_results_reviewed\": ("` | — |
| [SRC-1AE03B9EC3-L005246](../../agents/web_agent.py#L5246) | 5246 | `"                    None if lead_research_incomplete else related_lead_results_count"` | — |
| [SRC-1AE03B9EC3-L005247](../../agents/web_agent.py#L5247) | 5247 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005248](../../agents/web_agent.py#L5248) | 5248 | `"                \"qualification_rule\": \"explicit_public_buyer_intent_phrase\","` | — |
| [SRC-1AE03B9EC3-L005249](../../agents/web_agent.py#L5249) | 5249 | `"                \"identity_verified\": False,"` | — |
| [SRC-1AE03B9EC3-L005250](../../agents/web_agent.py#L5250) | 5250 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005251](../../agents/web_agent.py#L5251) | 5251 | `"            if not lead_evidence_sources:"` | — |
| [SRC-1AE03B9EC3-L005252](../../agents/web_agent.py#L5252) | 5252 | `"                if sources:"` | — |
| [SRC-1AE03B9EC3-L005253](../../agents/web_agent.py#L5253) | 5253 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L005254](../../agents/web_agent.py#L5254) | 5254 | `"                        \"لم أعثر على إشارة نصية واضحة تثبت أن أي نتيجة في هذه الجولة تتعلق بشخص \""` | — |
| [SRC-1AE03B9EC3-L005255](../../agents/web_agent.py#L5255) | 5255 | `"                        \"يريد الشراء. راجعت \""` | — |
| [SRC-1AE03B9EC3-L005256](../../agents/web_agent.py#L5256) | 5256 | `"                        + str(len(sources))"` | — |
| [SRC-1AE03B9EC3-L005257](../../agents/web_agent.py#L5257) | 5257 | `"                        + \" نتيجة مرتبطة بالموضوع، لكنني لم أعتبر إعلانات البيع أو صفحات السوق \""` | — |
| [SRC-1AE03B9EC3-L005258](../../agents/web_agent.py#L5258) | 5258 | `"                        \"عملاء محتملين. الروابط أدناه نتائج مرتبطة بالموضوع فقط وليست عملاء.\""` | — |
| [SRC-1AE03B9EC3-L005259](../../agents/web_agent.py#L5259) | 5259 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005260](../../agents/web_agent.py#L5260) | 5260 | `"                elif report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L005261](../../agents/web_agent.py#L5261) | 5261 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L005262](../../agents/web_agent.py#L5262) | 5262 | `"                        \"تعطل مسار البحث أو لم يمكن تأكيد اكتماله؛ لذلك لا أستطيع تحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L005263](../../agents/web_agent.py#L5263) | 5263 | `"                        \"كانت هناك نتائج تصلح كعملاء محتملين في هذه الجولة.\""` | — |
| [SRC-1AE03B9EC3-L005264](../../agents/web_agent.py#L5264) | 5264 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005265](../../agents/web_agent.py#L5265) | 5265 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005266](../../agents/web_agent.py#L5266) | 5266 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L005267](../../agents/web_agent.py#L5267) | 5267 | `"                        \"لم تظهر نتائج قابلة للاستخدام تثبت نية شراء في هذه الجولة. هذا لا يثبت \""` | — |
| [SRC-1AE03B9EC3-L005268](../../agents/web_agent.py#L5268) | 5268 | `"                        \"عدم وجود عملاء؛ بل يعني أن البحث الحالي لم يعثر على دليل كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L005269](../../agents/web_agent.py#L5269) | 5269 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005270](../../agents/web_agent.py#L5270) | 5270 | `"                report[\"research_quality\"] = \"failed\""` | — |
| [SRC-1AE03B9EC3-L005271](../../agents/web_agent.py#L5271) | 5271 | `"                # Distinguish zero qualified signals from unknown counts after an exception."` | — |
| [SRC-1AE03B9EC3-L005272](../../agents/web_agent.py#L5272) | 5272 | `"                report[\"usable_sources_after_filtering\"] = ("` | — |
| [SRC-1AE03B9EC3-L005273](../../agents/web_agent.py#L5273) | 5273 | `"                    None if lead_research_incomplete else len(sources)"` | — |
| [SRC-1AE03B9EC3-L005274](../../agents/web_agent.py#L5274) | 5274 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005275](../../agents/web_agent.py#L5275) | 5275 | `"                report[\"evidence_signals\"] = ("` | — |
| [SRC-1AE03B9EC3-L005276](../../agents/web_agent.py#L5276) | 5276 | `"                    None if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L005277](../../agents/web_agent.py#L5277) | 5277 | `"                    else evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L005278](../../agents/web_agent.py#L5278) | 5278 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005279](../../agents/web_agent.py#L5279) | 5279 | `"                public_related_sources = [{"` | — |
| [SRC-1AE03B9EC3-L005280](../../agents/web_agent.py#L5280) | 5280 | `"                    \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005281](../../agents/web_agent.py#L5281) | 5281 | `"                    \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005282](../../agents/web_agent.py#L5282) | 5282 | `"                    \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005283](../../agents/web_agent.py#L5283) | 5283 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005284](../../agents/web_agent.py#L5284) | 5284 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L005285](../../agents/web_agent.py#L5285) | 5285 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005286](../../agents/web_agent.py#L5286) | 5286 | `"                    \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005287](../../agents/web_agent.py#L5287) | 5287 | `"                    \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005288](../../agents/web_agent.py#L5288) | 5288 | `"                    \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005289](../../agents/web_agent.py#L5289) | 5289 | `"                    \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005290](../../agents/web_agent.py#L5290) | 5290 | `"                    \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005291](../../agents/web_agent.py#L5291) | 5291 | `"                    \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005292](../../agents/web_agent.py#L5292) | 5292 | `"                    \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005293](../../agents/web_agent.py#L5293) | 5293 | `"                    \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005294](../../agents/web_agent.py#L5294) | 5294 | `"                    \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005295](../../agents/web_agent.py#L5295) | 5295 | `"                    \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-1AE03B9EC3-L005296](../../agents/web_agent.py#L5296) | 5296 | `"                } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L005297](../../agents/web_agent.py#L5297) | 5297 | `"                return {"` | — |
| [SRC-1AE03B9EC3-L005298](../../agents/web_agent.py#L5298) | 5298 | `"                    \"answer\": lead_answer,"` | — |
| [SRC-1AE03B9EC3-L005299](../../agents/web_agent.py#L5299) | 5299 | `"                    \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005300](../../agents/web_agent.py#L5300) | 5300 | `"                    \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005301](../../agents/web_agent.py#L5301) | 5301 | `"                    \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005302](../../agents/web_agent.py#L5302) | 5302 | `"                    \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005303](../../agents/web_agent.py#L5303) | 5303 | `"                        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005304](../../agents/web_agent.py#L5304) | 5304 | `"                        \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005305](../../agents/web_agent.py#L5305) | 5305 | `"                        \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005306](../../agents/web_agent.py#L5306) | 5306 | `"                        \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005307](../../agents/web_agent.py#L5307) | 5307 | `"                        \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005308](../../agents/web_agent.py#L5308) | 5308 | `"                        \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005309](../../agents/web_agent.py#L5309) | 5309 | `"                        \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005310](../../agents/web_agent.py#L5310) | 5310 | `"                        \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005311](../../agents/web_agent.py#L5311) | 5311 | `"                        \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005312](../../agents/web_agent.py#L5312) | 5312 | `"                        \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005313](../../agents/web_agent.py#L5313) | 5313 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L005314](../../agents/web_agent.py#L5314) | 5314 | `"                    \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005315](../../agents/web_agent.py#L5315) | 5315 | `"                    \"sources\": public_related_sources,"` | — |
| [SRC-1AE03B9EC3-L005316](../../agents/web_agent.py#L5316) | 5316 | `"                    \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L005317](../../agents/web_agent.py#L5317) | 5317 | `"                    \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005318](../../agents/web_agent.py#L5318) | 5318 | `"                    \"search_attempted\": report.get("` | — |
| [SRC-1AE03B9EC3-L005319](../../agents/web_agent.py#L5319) | 5319 | `"                        \"search_attempted\","` | — |
| [SRC-1AE03B9EC3-L005320](../../agents/web_agent.py#L5320) | 5320 | `"                        bool(report.get(\"queries_attempted\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005321](../../agents/web_agent.py#L5321) | 5321 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L005322](../../agents/web_agent.py#L5322) | 5322 | `"                    \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005323](../../agents/web_agent.py#L5323) | 5323 | `"                    \"warnings\": [lead_answer],"` | — |
| [SRC-1AE03B9EC3-L005324](../../agents/web_agent.py#L5324) | 5324 | `"                    \"kind\": \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1AE03B9EC3-L005325](../../agents/web_agent.py#L5325) | 5325 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005326](../../agents/web_agent.py#L5326) | 5326 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005327](../../agents/web_agent.py#L5327) | 5327 | `"                    \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005328](../../agents/web_agent.py#L5328) | 5328 | `"                }"` | — |
| [SRC-1AE03B9EC3-L005329](../../agents/web_agent.py#L5329) | 5329 | `"            # Only explicit public buyer-intent signals may be synthesized as lead candidates."` | — |
| [SRC-1AE03B9EC3-L005330](../../agents/web_agent.py#L5330) | 5330 | `"            sources = lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L005331](../../agents/web_agent.py#L5331) | 5331 | `"            report[\"evidence_signals\"] = evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L005332](../../agents/web_agent.py#L5332) | 5332 | `"            report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005333](../../agents/web_agent.py#L5333) | 5333 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005334](../../agents/web_agent.py#L5334) | 5334 | `"            report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005335](../../agents/web_agent.py#L5335) | 5335 | `"            independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005336](../../agents/web_agent.py#L5336) | 5336 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005337](../../agents/web_agent.py#L5337) | 5337 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005338](../../agents/web_agent.py#L5338) | 5338 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005339](../../agents/web_agent.py#L5339) | 5339 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L005340](../../agents/web_agent.py#L5340) | 5340 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005341](../../agents/web_agent.py#L5341) | 5341 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L005342](../../agents/web_agent.py#L5342) | 5342 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005343](../../agents/web_agent.py#L5343) | 5343 | `"            independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005344](../../agents/web_agent.py#L5344) | 5344 | `"        single_source_navigation = navigation_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005345](../../agents/web_agent.py#L5345) | 5345 | `"        single_source_social = bool(plan.get(\"social_focus\")) and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005346](../../agents/web_agent.py#L5346) | 5346 | `"        single_source_lead = lead_request and bool(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L005347](../../agents/web_agent.py#L5347) | 5347 | `"        single_source_listing = listing_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005348](../../agents/web_agent.py#L5348) | 5348 | `"        task_specific_partial_evidence = ("` | — |
| [SRC-1AE03B9EC3-L005349](../../agents/web_agent.py#L5349) | 5349 | `"            single_source_page_summary"` | — |
| [SRC-1AE03B9EC3-L005350](../../agents/web_agent.py#L5350) | 5350 | `"            or single_source_navigation"` | — |
| [SRC-1AE03B9EC3-L005351](../../agents/web_agent.py#L5351) | 5351 | `"            or single_source_social"` | — |
| [SRC-1AE03B9EC3-L005352](../../agents/web_agent.py#L5352) | 5352 | `"            or single_source_lead"` | — |
| [SRC-1AE03B9EC3-L005353](../../agents/web_agent.py#L5353) | 5353 | `"            or single_source_listing"` | — |
| [SRC-1AE03B9EC3-L005354](../../agents/web_agent.py#L5354) | 5354 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005355](../../agents/web_agent.py#L5355) | 5355 | `"        needs_corroboration = len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L005356](../../agents/web_agent.py#L5356) | 5356 | `"        evidence_repair: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L005357](../../agents/web_agent.py#L5357) | 5357 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L005358](../../agents/web_agent.py#L5358) | 5358 | `"            \"max_extra_queries\": 1,"` | — |
| [SRC-1AE03B9EC3-L005359](../../agents/web_agent.py#L5359) | 5359 | `"            \"reason\": \"initial_evidence_gate_satisfied\" if not needs_corroboration else \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L005360](../../agents/web_agent.py#L5360) | 5360 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005361](../../agents/web_agent.py#L5361) | 5361 | `"        if needs_corroboration and not plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L005362](../../agents/web_agent.py#L5362) | 5362 | `"            evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L005363](../../agents/web_agent.py#L5363) | 5363 | `"        elif needs_corroboration:"` | — |
| [SRC-1AE03B9EC3-L005364](../../agents/web_agent.py#L5364) | 5364 | `"            if task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L005365](../../agents/web_agent.py#L5365) | 5365 | `"                evidence_repair[\"reason\"] = \"task_specific_partial_evidence\""` | — |
| [SRC-1AE03B9EC3-L005366](../../agents/web_agent.py#L5366) | 5366 | `"            elif plan.get(\"social_focus\"):"` | — |
| [SRC-1AE03B9EC3-L005367](../../agents/web_agent.py#L5367) | 5367 | `"                evidence_repair[\"reason\"] = \"social_search_not_retried\""` | — |
| [SRC-1AE03B9EC3-L005368](../../agents/web_agent.py#L5368) | 5368 | `"            elif plan.get(\"depth\") == \"deep\" or report.get(\"expansion_queries\"):"` | — |
| [SRC-1AE03B9EC3-L005369](../../agents/web_agent.py#L5369) | 5369 | `"                evidence_repair[\"reason\"] = \"deep_research_already_expanded\""` | — |
| [SRC-1AE03B9EC3-L005370](../../agents/web_agent.py#L5370) | 5370 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005371](../../agents/web_agent.py#L5371) | 5371 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L005372](../../agents/web_agent.py#L5372) | 5372 | `"                    str(item).strip()"` | — |
| [SRC-1AE03B9EC3-L005373](../../agents/web_agent.py#L5373) | 5373 | `"                    for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005374](../../agents/web_agent.py#L5374) | 5374 | `"                    if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L005375](../../agents/web_agent.py#L5375) | 5375 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L005376](../../agents/web_agent.py#L5376) | 5376 | `"                base_query = ("` | — |
| [SRC-1AE03B9EC3-L005377](../../agents/web_agent.py#L5377) | 5377 | `"                    original_queries[0]"` | — |
| [SRC-1AE03B9EC3-L005378](../../agents/web_agent.py#L5378) | 5378 | `"                    if original_queries"` | — |
| [SRC-1AE03B9EC3-L005379](../../agents/web_agent.py#L5379) | 5379 | `"                    else compact_search_query(working_question)"` | — |
| [SRC-1AE03B9EC3-L005380](../../agents/web_agent.py#L5380) | 5380 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005381](../../agents/web_agent.py#L5381) | 5381 | `"                suffix = ("` | — |
| [SRC-1AE03B9EC3-L005382](../../agents/web_agent.py#L5382) | 5382 | `"                    \"latest official primary source\""` | — |
| [SRC-1AE03B9EC3-L005383](../../agents/web_agent.py#L5383) | 5383 | `"                    if plan.get(\"freshness\") == \"current\""` | — |
| [SRC-1AE03B9EC3-L005384](../../agents/web_agent.py#L5384) | 5384 | `"                    else \"official primary source data\""` | — |
| [SRC-1AE03B9EC3-L005385](../../agents/web_agent.py#L5385) | 5385 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005386](../../agents/web_agent.py#L5386) | 5386 | `"                repair_query = compact_search_query(f\"{base_query} {suffix}\")"` | — |
| [SRC-1AE03B9EC3-L005387](../../agents/web_agent.py#L5387) | 5387 | `"                if not repair_query or not _relevance_query_tokens(repair_query):"` | — |
| [SRC-1AE03B9EC3-L005388](../../agents/web_agent.py#L5388) | 5388 | `"                    evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L005389](../../agents/web_agent.py#L5389) | 5389 | `"                    repair_query = \"\""` | — |
| [SRC-1AE03B9EC3-L005390](../../agents/web_agent.py#L5390) | 5390 | `"                known_queries = {"` | — |
| [SRC-1AE03B9EC3-L005391](../../agents/web_agent.py#L5391) | 5391 | `"                    _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L005392](../../agents/web_agent.py#L5392) | 5392 | `"                    for item in original_queries"` | — |
| [SRC-1AE03B9EC3-L005393](../../agents/web_agent.py#L5393) | 5393 | `"                }"` | — |
| [SRC-1AE03B9EC3-L005394](../../agents/web_agent.py#L5394) | 5394 | `"                if repair_query and _normalize_search_query(repair_query).casefold() in known_queries:"` | — |
| [SRC-1AE03B9EC3-L005395](../../agents/web_agent.py#L5395) | 5395 | `"                    repair_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005396](../../agents/web_agent.py#L5396) | 5396 | `"                        f\"{base_query} independent corroborating evidence\""` | — |
| [SRC-1AE03B9EC3-L005397](../../agents/web_agent.py#L5397) | 5397 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005398](../../agents/web_agent.py#L5398) | 5398 | `"                if repair_query and _relevance_query_tokens(repair_query) and ("` | — |
| [SRC-1AE03B9EC3-L005399](../../agents/web_agent.py#L5399) | 5399 | `"                    _normalize_search_query(repair_query).casefold() not in known_queries"` | — |
| [SRC-1AE03B9EC3-L005400](../../agents/web_agent.py#L5400) | 5400 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L005401](../../agents/web_agent.py#L5401) | 5401 | `"                    initial_source_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005402](../../agents/web_agent.py#L5402) | 5402 | `"                    initial_domain_count = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005403](../../agents/web_agent.py#L5403) | 5403 | `"                    evidence_repair[\"attempted\"] = True"` | — |
| [SRC-1AE03B9EC3-L005404](../../agents/web_agent.py#L5404) | 5404 | `"                    evidence_repair[\"reason\"] = \"thin_or_unrelated_initial_evidence\""` | — |
| [SRC-1AE03B9EC3-L005405](../../agents/web_agent.py#L5405) | 5405 | `"                    evidence_repair[\"query\"] = repair_query"` | — |
| [SRC-1AE03B9EC3-L005406](../../agents/web_agent.py#L5406) | 5406 | `"                    repair_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L005407](../../agents/web_agent.py#L5407) | 5407 | `"                    repair_plan.update({"` | — |
| [SRC-1AE03B9EC3-L005408](../../agents/web_agent.py#L5408) | 5408 | `"                        \"queries\": [repair_query],"` | — |
| [SRC-1AE03B9EC3-L005409](../../agents/web_agent.py#L5409) | 5409 | `"                        \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L005410](../../agents/web_agent.py#L5410) | 5410 | `"                        \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L005411](../../agents/web_agent.py#L5411) | 5411 | `"                        \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L005412](../../agents/web_agent.py#L5412) | 5412 | `"                        \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L005413](../../agents/web_agent.py#L5413) | 5413 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L005414](../../agents/web_agent.py#L5414) | 5414 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L005415](../../agents/web_agent.py#L5415) | 5415 | `"                        repair_sources, repair_warnings, repair_report = self._collect_research("` | — |
| [SRC-1AE03B9EC3-L005416](../../agents/web_agent.py#L5416) | 5416 | `"                            repair_plan"` | — |
| [SRC-1AE03B9EC3-L005417](../../agents/web_agent.py#L5417) | 5417 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005418](../../agents/web_agent.py#L5418) | 5418 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005419](../../agents/web_agent.py#L5419) | 5419 | `"                        repair_sources = []"` | — |
| [SRC-1AE03B9EC3-L005420](../../agents/web_agent.py#L5420) | 5420 | `"                        repair_warnings = []"` | — |
| [SRC-1AE03B9EC3-L005421](../../agents/web_agent.py#L5421) | 5421 | `"                        repair_report = {"` | — |
| [SRC-1AE03B9EC3-L005422](../../agents/web_agent.py#L5422) | 5422 | `"                            \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L005423](../../agents/web_agent.py#L5423) | 5423 | `"                            \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005424](../../agents/web_agent.py#L5424) | 5424 | `"                            \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L005425](../../agents/web_agent.py#L5425) | 5425 | `"                            \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005426](../../agents/web_agent.py#L5426) | 5426 | `"                            \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L005427](../../agents/web_agent.py#L5427) | 5427 | `"                            \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L005428](../../agents/web_agent.py#L5428) | 5428 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L005429](../../agents/web_agent.py#L5429) | 5429 | `"                        search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005430](../../agents/web_agent.py#L5430) | 5430 | `"                            \"تعذر تنفيذ محاولة البحث الإضافية المحدودة (\""` | — |
| [SRC-1AE03B9EC3-L005431](../../agents/web_agent.py#L5431) | 5431 | `"                            + type(exc).__name__ + \").\""` | — |
| [SRC-1AE03B9EC3-L005432](../../agents/web_agent.py#L5432) | 5432 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005433](../../agents/web_agent.py#L5433) | 5433 | `"                    search_warnings.extend(repair_warnings)"` | — |
| [SRC-1AE03B9EC3-L005434](../../agents/web_agent.py#L5434) | 5434 | `"                    evidence_repair[\"attempted_query_count\"] = 1"` | — |
| [SRC-1AE03B9EC3-L005435](../../agents/web_agent.py#L5435) | 5435 | `"                    evidence_repair[\"initial_source_count\"] = initial_source_count"` | — |
| [SRC-1AE03B9EC3-L005436](../../agents/web_agent.py#L5436) | 5436 | `"                    evidence_repair[\"initial_independent_domain_count\"] = initial_domain_count"` | — |
| [SRC-1AE03B9EC3-L005437](../../agents/web_agent.py#L5437) | 5437 | `"                    evidence_repair[\"new_sources_added\"] = 0"` | — |
| [SRC-1AE03B9EC3-L005438](../../agents/web_agent.py#L5438) | 5438 | `"                    source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L005439](../../agents/web_agent.py#L5439) | 5439 | `"                    for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L005440](../../agents/web_agent.py#L5440) | 5440 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005441](../../agents/web_agent.py#L5441) | 5441 | `"                        if source_key:"` | — |
| [SRC-1AE03B9EC3-L005442](../../agents/web_agent.py#L5442) | 5442 | `"                            source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L005443](../../agents/web_agent.py#L5443) | 5443 | `"                    relevant_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005444](../../agents/web_agent.py#L5444) | 5444 | `"                        query"` | — |
| [SRC-1AE03B9EC3-L005445](../../agents/web_agent.py#L5445) | 5445 | `"                        for query in ("` | — |
| [SRC-1AE03B9EC3-L005446](../../agents/web_agent.py#L5446) | 5446 | `"                            compact_search_query(working_question),"` | — |
| [SRC-1AE03B9EC3-L005447](../../agents/web_agent.py#L5447) | 5447 | `"                            *("` | — |
| [SRC-1AE03B9EC3-L005448](../../agents/web_agent.py#L5448) | 5448 | `"                                compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L005449](../../agents/web_agent.py#L5449) | 5449 | `"                                for candidate in original_queries"` | — |
| [SRC-1AE03B9EC3-L005450](../../agents/web_agent.py#L5450) | 5450 | `"                                if isinstance(candidate, str)"` | — |
| [SRC-1AE03B9EC3-L005451](../../agents/web_agent.py#L5451) | 5451 | `"                            ),"` | — |
| [SRC-1AE03B9EC3-L005452](../../agents/web_agent.py#L5452) | 5452 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005453](../../agents/web_agent.py#L5453) | 5453 | `"                        if query"` | — |
| [SRC-1AE03B9EC3-L005454](../../agents/web_agent.py#L5454) | 5454 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L005455](../../agents/web_agent.py#L5455) | 5455 | `"                    for source in repair_sources:"` | — |
| [SRC-1AE03B9EC3-L005456](../../agents/web_agent.py#L5456) | 5456 | `"                        if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L005457](../../agents/web_agent.py#L5457) | 5457 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005458](../../agents/web_agent.py#L5458) | 5458 | `"                        if not any("` | — |
| [SRC-1AE03B9EC3-L005459](../../agents/web_agent.py#L5459) | 5459 | `"                            self._source_matches_query(candidate, source)"` | — |
| [SRC-1AE03B9EC3-L005460](../../agents/web_agent.py#L5460) | 5460 | `"                            for candidate in relevant_queries if candidate"` | — |
| [SRC-1AE03B9EC3-L005461](../../agents/web_agent.py#L5461) | 5461 | `"                        ):"` | — |
| [SRC-1AE03B9EC3-L005462](../../agents/web_agent.py#L5462) | 5462 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005463](../../agents/web_agent.py#L5463) | 5463 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005464](../../agents/web_agent.py#L5464) | 5464 | `"                        if not source_key:"` | — |
| [SRC-1AE03B9EC3-L005465](../../agents/web_agent.py#L5465) | 5465 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005466](../../agents/web_agent.py#L5466) | 5466 | `"                        existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L005467](../../agents/web_agent.py#L5467) | 5467 | `"                        if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L005468](../../agents/web_agent.py#L5468) | 5468 | `"                            source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005469](../../agents/web_agent.py#L5469) | 5469 | `"                            sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L005470](../../agents/web_agent.py#L5470) | 5470 | `"                            evidence_repair[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L005471](../../agents/web_agent.py#L5471) | 5471 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005472](../../agents/web_agent.py#L5472) | 5472 | `"                        existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L005473](../../agents/web_agent.py#L5473) | 5473 | `"                        providers = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005474](../../agents/web_agent.py#L5474) | 5474 | `"                            list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005475](../../agents/web_agent.py#L5475) | 5475 | `"                            + list(source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005476](../../agents/web_agent.py#L5476) | 5476 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L005477](../../agents/web_agent.py#L5477) | 5477 | `"                        source_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005478](../../agents/web_agent.py#L5478) | 5478 | `"                            list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005479](../../agents/web_agent.py#L5479) | 5479 | `"                            + list(source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005480](../../agents/web_agent.py#L5480) | 5480 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L005481](../../agents/web_agent.py#L5481) | 5481 | `"                        if source.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L005482](../../agents/web_agent.py#L5482) | 5482 | `"                            merged_source = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L005483](../../agents/web_agent.py#L5483) | 5483 | `"                            merged_source.update(source)"` | — |
| [SRC-1AE03B9EC3-L005484](../../agents/web_agent.py#L5484) | 5484 | `"                            merged_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L005485](../../agents/web_agent.py#L5485) | 5485 | `"                            merged_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L005486](../../agents/web_agent.py#L5486) | 5486 | `"                            sources[existing_index] = merged_source"` | — |
| [SRC-1AE03B9EC3-L005487](../../agents/web_agent.py#L5487) | 5487 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L005488](../../agents/web_agent.py#L5488) | 5488 | `"                            existing_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L005489](../../agents/web_agent.py#L5489) | 5489 | `"                            existing_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L005490](../../agents/web_agent.py#L5490) | 5490 | `"                    sources.sort("` | — |
| [SRC-1AE03B9EC3-L005491](../../agents/web_agent.py#L5491) | 5491 | `"                        key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L005492](../../agents/web_agent.py#L5492) | 5492 | `"                        reverse=True,"` | — |
| [SRC-1AE03B9EC3-L005493](../../agents/web_agent.py#L5493) | 5493 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005494](../../agents/web_agent.py#L5494) | 5494 | `"                    plan[\"queries\"] = list(dict.fromkeys(original_queries + [repair_query]))"` | — |
| [SRC-1AE03B9EC3-L005495](../../agents/web_agent.py#L5495) | 5495 | `"                    independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005496](../../agents/web_agent.py#L5496) | 5496 | `"                        registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005497](../../agents/web_agent.py#L5497) | 5497 | `"                            source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005498](../../agents/web_agent.py#L5498) | 5498 | `"                            or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005499](../../agents/web_agent.py#L5499) | 5499 | `"                            or \"\""` | — |
| [SRC-1AE03B9EC3-L005500](../../agents/web_agent.py#L5500) | 5500 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005501](../../agents/web_agent.py#L5501) | 5501 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L005502](../../agents/web_agent.py#L5502) | 5502 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005503](../../agents/web_agent.py#L5503) | 5503 | `"                    independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005504](../../agents/web_agent.py#L5504) | 5504 | `"                    needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L005505](../../agents/web_agent.py#L5505) | 5505 | `"                        len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L005506](../../agents/web_agent.py#L5506) | 5506 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005507](../../agents/web_agent.py#L5507) | 5507 | `"                    evidence_repair.update({"` | — |
| [SRC-1AE03B9EC3-L005508](../../agents/web_agent.py#L5508) | 5508 | `"                        \"final_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L005509](../../agents/web_agent.py#L5509) | 5509 | `"                        \"final_independent_domain_count\": len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005510](../../agents/web_agent.py#L5510) | 5510 | `"                        \"recovered\": not needs_corroboration,"` | — |
| [SRC-1AE03B9EC3-L005511](../../agents/web_agent.py#L5511) | 5511 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L005512](../../agents/web_agent.py#L5512) | 5512 | `"                    evidence_repair[\"reason\"] = ("` | — |
| [SRC-1AE03B9EC3-L005513](../../agents/web_agent.py#L5513) | 5513 | `"                        \"single_bounded_retry_still_insufficient\""` | — |
| [SRC-1AE03B9EC3-L005514](../../agents/web_agent.py#L5514) | 5514 | `"                        if needs_corroboration else \"evidence_gate_recovered\""` | — |
| [SRC-1AE03B9EC3-L005515](../../agents/web_agent.py#L5515) | 5515 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005516](../../agents/web_agent.py#L5516) | 5516 | `"                    report[\"queries_planned\"] = int(report.get(\"queries_planned\", 0) or 0) + int("` | — |
| [SRC-1AE03B9EC3-L005517](../../agents/web_agent.py#L5517) | 5517 | `"                        repair_report.get(\"queries_planned\", 1) or 0"` | — |
| [SRC-1AE03B9EC3-L005518](../../agents/web_agent.py#L5518) | 5518 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005519](../../agents/web_agent.py#L5519) | 5519 | `"                    initial_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L005520](../../agents/web_agent.py#L5520) | 5520 | `"                    repair_attempt_count = repair_report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L005521](../../agents/web_agent.py#L5521) | 5521 | `"                    if initial_attempt_count is None or repair_attempt_count is None:"` | — |
| [SRC-1AE03B9EC3-L005522](../../agents/web_agent.py#L5522) | 5522 | `"                        report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L005523](../../agents/web_agent.py#L5523) | 5523 | `"                        report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L005524](../../agents/web_agent.py#L5524) | 5524 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L005525](../../agents/web_agent.py#L5525) | 5525 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005526](../../agents/web_agent.py#L5526) | 5526 | `"                            report[\"queries_attempted\"] = max(0, int(initial_attempt_count or 0)) + max("` | — |
| [SRC-1AE03B9EC3-L005527](../../agents/web_agent.py#L5527) | 5527 | `"                                0, int(repair_attempt_count or 0)"` | — |
| [SRC-1AE03B9EC3-L005528](../../agents/web_agent.py#L5528) | 5528 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005529](../../agents/web_agent.py#L5529) | 5529 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L005530](../../agents/web_agent.py#L5530) | 5530 | `"                        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L005531](../../agents/web_agent.py#L5531) | 5531 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L005532](../../agents/web_agent.py#L5532) | 5532 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L005533](../../agents/web_agent.py#L5533) | 5533 | `"                    report[\"query_results\"] = list(report.get(\"query_results\", [])) + list("` | — |
| [SRC-1AE03B9EC3-L005534](../../agents/web_agent.py#L5534) | 5534 | `"                        repair_report.get(\"query_results\", [])"` | — |
| [SRC-1AE03B9EC3-L005535](../../agents/web_agent.py#L5535) | 5535 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005536](../../agents/web_agent.py#L5536) | 5536 | `"                    merged_providers = {"` | — |
| [SRC-1AE03B9EC3-L005537](../../agents/web_agent.py#L5537) | 5537 | `"                        provider"` | — |
| [SRC-1AE03B9EC3-L005538](../../agents/web_agent.py#L5538) | 5538 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L005539](../../agents/web_agent.py#L5539) | 5539 | `"                        for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005540](../../agents/web_agent.py#L5540) | 5540 | `"                    }"` | — |
