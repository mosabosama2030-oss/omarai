# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **014**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L004499 إلى SRC-1AE03B9EC3-L005298
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L004499](../../agents/web_agent.py#L4499) | 4499 | `"        # search was attempted; diagnostics must not imply that a tool ran."` | — |
| [SRC-1AE03B9EC3-L004500](../../agents/web_agent.py#L4500) | 4500 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004501](../../agents/web_agent.py#L4501) | 4501 | `"            report = result.get(\"search_report\")"` | — |
| [SRC-1AE03B9EC3-L004502](../../agents/web_agent.py#L4502) | 4502 | `"            if not isinstance(report, dict):"` | — |
| [SRC-1AE03B9EC3-L004503](../../agents/web_agent.py#L4503) | 4503 | `"                report = {}"` | — |
| [SRC-1AE03B9EC3-L004504](../../agents/web_agent.py#L4504) | 4504 | `"            research_plan = result.get(\"research_plan\")"` | — |
| [SRC-1AE03B9EC3-L004505](../../agents/web_agent.py#L4505) | 4505 | `"            if not isinstance(research_plan, dict):"` | — |
| [SRC-1AE03B9EC3-L004506](../../agents/web_agent.py#L4506) | 4506 | `"                research_plan = {}"` | — |
| [SRC-1AE03B9EC3-L004507](../../agents/web_agent.py#L4507) | 4507 | `"            context = result.get(\"dialogue_context\")"` | — |
| [SRC-1AE03B9EC3-L004508](../../agents/web_agent.py#L4508) | 4508 | `"            if not isinstance(context, dict):"` | — |
| [SRC-1AE03B9EC3-L004509](../../agents/web_agent.py#L4509) | 4509 | `"                context = research_plan.get(\"dialogue_context\")"` | — |
| [SRC-1AE03B9EC3-L004510](../../agents/web_agent.py#L4510) | 4510 | `"            resolved_question = ("` | — |
| [SRC-1AE03B9EC3-L004511](../../agents/web_agent.py#L4511) | 4511 | `"                str(context.get(\"resolved_question\") or question)"` | — |
| [SRC-1AE03B9EC3-L004512](../../agents/web_agent.py#L4512) | 4512 | `"                if isinstance(context, dict) and not context.get(\"topic_shift\")"` | — |
| [SRC-1AE03B9EC3-L004513](../../agents/web_agent.py#L4513) | 4513 | `"                else question"` | — |
| [SRC-1AE03B9EC3-L004514](../../agents/web_agent.py#L4514) | 4514 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004515](../../agents/web_agent.py#L4515) | 4515 | `"            existing_task_data = report.get(\"task_understanding\")"` | — |
| [SRC-1AE03B9EC3-L004516](../../agents/web_agent.py#L4516) | 4516 | `"            if not isinstance(existing_task_data, dict):"` | — |
| [SRC-1AE03B9EC3-L004517](../../agents/web_agent.py#L4517) | 4517 | `"                existing_task_data = {}"` | — |
| [SRC-1AE03B9EC3-L004518](../../agents/web_agent.py#L4518) | 4518 | `"            task_spec = ("` | — |
| [SRC-1AE03B9EC3-L004519](../../agents/web_agent.py#L4519) | 4519 | `"                existing_task_data.get(\"task_spec\")"` | — |
| [SRC-1AE03B9EC3-L004520](../../agents/web_agent.py#L4520) | 4520 | `"                or research_plan.get(\"task_spec\")"` | — |
| [SRC-1AE03B9EC3-L004521](../../agents/web_agent.py#L4521) | 4521 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004522](../../agents/web_agent.py#L4522) | 4522 | `"            requested_mode = mode if isinstance(mode, str) else \"auto\""` | — |
| [SRC-1AE03B9EC3-L004523](../../agents/web_agent.py#L4523) | 4523 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L004524](../../agents/web_agent.py#L4524) | 4524 | `"                not isinstance(task_spec, dict)"` | — |
| [SRC-1AE03B9EC3-L004525](../../agents/web_agent.py#L4525) | 4525 | `"                or task_spec.get(\"schema\") != \"omarai.task_spec.v1\""` | — |
| [SRC-1AE03B9EC3-L004526](../../agents/web_agent.py#L4526) | 4526 | `"                or task_spec.get(\"mode\") != requested_mode.strip().lower()"` | — |
| [SRC-1AE03B9EC3-L004527](../../agents/web_agent.py#L4527) | 4527 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L004528](../../agents/web_agent.py#L4528) | 4528 | `"                task_spec = build_task_spec("` | — |
| [SRC-1AE03B9EC3-L004529](../../agents/web_agent.py#L4529) | 4529 | `"                    resolved_question,"` | — |
| [SRC-1AE03B9EC3-L004530](../../agents/web_agent.py#L4530) | 4530 | `"                    mode=requested_mode,"` | — |
| [SRC-1AE03B9EC3-L004531](../../agents/web_agent.py#L4531) | 4531 | `"                    intent_route=str(result.get(\"intent_route\") or \"\"),"` | — |
| [SRC-1AE03B9EC3-L004532](../../agents/web_agent.py#L4532) | 4532 | `"                    plan=research_plan,"` | — |
| [SRC-1AE03B9EC3-L004533](../../agents/web_agent.py#L4533) | 4533 | `"                    dialogue_context=context if isinstance(context, dict) else None,"` | — |
| [SRC-1AE03B9EC3-L004534](../../agents/web_agent.py#L4534) | 4534 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004535](../../agents/web_agent.py#L4535) | 4535 | `"            actual_queries = result.get(\"search_queries\")"` | — |
| [SRC-1AE03B9EC3-L004536](../../agents/web_agent.py#L4536) | 4536 | `"            if not isinstance(actual_queries, list):"` | — |
| [SRC-1AE03B9EC3-L004537](../../agents/web_agent.py#L4537) | 4537 | `"                actual_queries = []"` | — |
| [SRC-1AE03B9EC3-L004538](../../agents/web_agent.py#L4538) | 4538 | `"            query_matrix = ("` | — |
| [SRC-1AE03B9EC3-L004539](../../agents/web_agent.py#L4539) | 4539 | `"                existing_task_data.get(\"query_strategy_matrix\")"` | — |
| [SRC-1AE03B9EC3-L004540](../../agents/web_agent.py#L4540) | 4540 | `"                or research_plan.get(\"query_strategy_matrix\")"` | — |
| [SRC-1AE03B9EC3-L004541](../../agents/web_agent.py#L4541) | 4541 | `"                or []"` | — |
| [SRC-1AE03B9EC3-L004542](../../agents/web_agent.py#L4542) | 4542 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004543](../../agents/web_agent.py#L4543) | 4543 | `"            if not isinstance(query_matrix, list):"` | — |
| [SRC-1AE03B9EC3-L004544](../../agents/web_agent.py#L4544) | 4544 | `"                query_matrix = []"` | — |
| [SRC-1AE03B9EC3-L004545](../../agents/web_agent.py#L4545) | 4545 | `"            if (result.get(\"search_attempted\") or result.get(\"used_web_search\")) and not query_matrix:"` | — |
| [SRC-1AE03B9EC3-L004546](../../agents/web_agent.py#L4546) | 4546 | `"                query_matrix = build_query_strategy_matrix("` | — |
| [SRC-1AE03B9EC3-L004547](../../agents/web_agent.py#L4547) | 4547 | `"                    resolved_question,"` | — |
| [SRC-1AE03B9EC3-L004548](../../agents/web_agent.py#L4548) | 4548 | `"                    task_spec,"` | — |
| [SRC-1AE03B9EC3-L004549](../../agents/web_agent.py#L4549) | 4549 | `"                    actual_queries,"` | — |
| [SRC-1AE03B9EC3-L004550](../../agents/web_agent.py#L4550) | 4550 | `"                    limit=MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L004551](../../agents/web_agent.py#L4551) | 4551 | `"                    compact_fn=compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L004552](../../agents/web_agent.py#L4552) | 4552 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004553](../../agents/web_agent.py#L4553) | 4553 | `"            provider_diagnostics = report.get(\"provider_diagnostics\")"` | — |
| [SRC-1AE03B9EC3-L004554](../../agents/web_agent.py#L4554) | 4554 | `"            if not isinstance(provider_diagnostics, list):"` | — |
| [SRC-1AE03B9EC3-L004555](../../agents/web_agent.py#L4555) | 4555 | `"                provider_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L004556](../../agents/web_agent.py#L4556) | 4556 | `"            provider_status_rows = []"` | — |
| [SRC-1AE03B9EC3-L004557](../../agents/web_agent.py#L4557) | 4557 | `"            for diagnostic in provider_diagnostics[:24]:"` | — |
| [SRC-1AE03B9EC3-L004558](../../agents/web_agent.py#L4558) | 4558 | `"                if not isinstance(diagnostic, dict):"` | — |
| [SRC-1AE03B9EC3-L004559](../../agents/web_agent.py#L4559) | 4559 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L004560](../../agents/web_agent.py#L4560) | 4560 | `"                status_row = {"` | — |
| [SRC-1AE03B9EC3-L004561](../../agents/web_agent.py#L4561) | 4561 | `"                    key: diagnostic[key]"` | — |
| [SRC-1AE03B9EC3-L004562](../../agents/web_agent.py#L4562) | 4562 | `"                    for key in ("` | — |
| [SRC-1AE03B9EC3-L004563](../../agents/web_agent.py#L4563) | 4563 | `"                        \"provider\", \"connector\", \"status\", \"error_class\","` | — |
| [SRC-1AE03B9EC3-L004564](../../agents/web_agent.py#L4564) | 4564 | `"                        \"http_status\", \"results_count\", \"elapsed_ms\", \"reason\","` | — |
| [SRC-1AE03B9EC3-L004565](../../agents/web_agent.py#L4565) | 4565 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004566](../../agents/web_agent.py#L4566) | 4566 | `"                    if key in diagnostic"` | — |
| [SRC-1AE03B9EC3-L004567](../../agents/web_agent.py#L4567) | 4567 | `"                }"` | — |
| [SRC-1AE03B9EC3-L004568](../../agents/web_agent.py#L4568) | 4568 | `"                if status_row:"` | — |
| [SRC-1AE03B9EC3-L004569](../../agents/web_agent.py#L4569) | 4569 | `"                    provider_status_rows.append(status_row)"` | — |
| [SRC-1AE03B9EC3-L004570](../../agents/web_agent.py#L4570) | 4570 | `"            tool_status_matrix = build_tool_execution_matrix("` | — |
| [SRC-1AE03B9EC3-L004571](../../agents/web_agent.py#L4571) | 4571 | `"                task_spec,"` | — |
| [SRC-1AE03B9EC3-L004572](../../agents/web_agent.py#L4572) | 4572 | `"                result,"` | — |
| [SRC-1AE03B9EC3-L004573](../../agents/web_agent.py#L4573) | 4573 | `"                report,"` | — |
| [SRC-1AE03B9EC3-L004574](../../agents/web_agent.py#L4574) | 4574 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004575](../../agents/web_agent.py#L4575) | 4575 | `"            task_summary = {"` | — |
| [SRC-1AE03B9EC3-L004576](../../agents/web_agent.py#L4576) | 4576 | `"                \"task_spec\": task_spec,"` | — |
| [SRC-1AE03B9EC3-L004577](../../agents/web_agent.py#L4577) | 4577 | `"                \"query_strategy_matrix\": query_matrix,"` | — |
| [SRC-1AE03B9EC3-L004578](../../agents/web_agent.py#L4578) | 4578 | `"                \"actual_queries\": actual_queries,"` | — |
| [SRC-1AE03B9EC3-L004579](../../agents/web_agent.py#L4579) | 4579 | `"                \"actual_query_count\": len(actual_queries),"` | — |
| [SRC-1AE03B9EC3-L004580](../../agents/web_agent.py#L4580) | 4580 | `"                \"search_was_attempted\": bool(result.get(\"search_attempted\")),"` | — |
| [SRC-1AE03B9EC3-L004581](../../agents/web_agent.py#L4581) | 4581 | `"                \"tool_execution\": {"` | — |
| [SRC-1AE03B9EC3-L004582](../../agents/web_agent.py#L4582) | 4582 | `"                    \"required_tools\": list(task_spec.get(\"tool_requirements\") or []),"` | — |
| [SRC-1AE03B9EC3-L004583](../../agents/web_agent.py#L4583) | 4583 | `"                    \"tool_status_matrix\": tool_status_matrix,"` | — |
| [SRC-1AE03B9EC3-L004584](../../agents/web_agent.py#L4584) | 4584 | `"                    \"search_outcome\": report.get(\"search_outcome\", \"not_assessed\"),"` | — |
| [SRC-1AE03B9EC3-L004585](../../agents/web_agent.py#L4585) | 4585 | `"                    \"providers_used\": report.get(\"providers_used\", []),"` | — |
| [SRC-1AE03B9EC3-L004586](../../agents/web_agent.py#L4586) | 4586 | `"                    \"provider_statuses\": provider_status_rows,"` | — |
| [SRC-1AE03B9EC3-L004587](../../agents/web_agent.py#L4587) | 4587 | `"                    \"accepted_source_count\": report.get(\"usable_sources_after_filtering\", \"not_assessed\"),"` | — |
| [SRC-1AE03B9EC3-L004588](../../agents/web_agent.py#L4588) | 4588 | `"                    \"pages_read_count\": report.get(\"pages_fetched\", \"not_assessed\"),"` | — |
| [SRC-1AE03B9EC3-L004589](../../agents/web_agent.py#L4589) | 4589 | `"                    \"connector_summary\": report.get(\"connector_summary\", {}),"` | — |
| [SRC-1AE03B9EC3-L004590](../../agents/web_agent.py#L4590) | 4590 | `"                },"` | — |
| [SRC-1AE03B9EC3-L004591](../../agents/web_agent.py#L4591) | 4591 | `"                \"interpretation_status\": ("` | — |
| [SRC-1AE03B9EC3-L004592](../../agents/web_agent.py#L4592) | 4592 | `"                    \"needs_clarification\""` | — |
| [SRC-1AE03B9EC3-L004593](../../agents/web_agent.py#L4593) | 4593 | `"                    if task_spec.get(\"ambiguity_status\") == \"needs_clarification\""` | — |
| [SRC-1AE03B9EC3-L004594](../../agents/web_agent.py#L4594) | 4594 | `"                    else \"deterministic_task_spec_attached\""` | — |
| [SRC-1AE03B9EC3-L004595](../../agents/web_agent.py#L4595) | 4595 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004596](../../agents/web_agent.py#L4596) | 4596 | `"                \"claim\": \"task interpretation and tool diagnostics only; not factual verification\","` | — |
| [SRC-1AE03B9EC3-L004597](../../agents/web_agent.py#L4597) | 4597 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004598](../../agents/web_agent.py#L4598) | 4598 | `"            result[\"task_understanding\"] = task_summary"` | — |
| [SRC-1AE03B9EC3-L004599](../../agents/web_agent.py#L4599) | 4599 | `"            if isinstance(result.get(\"research_plan\"), dict):"` | — |
| [SRC-1AE03B9EC3-L004600](../../agents/web_agent.py#L4600) | 4600 | `"                result[\"research_plan\"][\"task_spec\"] = task_spec"` | — |
| [SRC-1AE03B9EC3-L004601](../../agents/web_agent.py#L4601) | 4601 | `"                result[\"research_plan\"][\"query_strategy_matrix\"] = query_matrix"` | — |
| [SRC-1AE03B9EC3-L004602](../../agents/web_agent.py#L4602) | 4602 | `"            if isinstance(result.get(\"search_report\"), dict):"` | — |
| [SRC-1AE03B9EC3-L004603](../../agents/web_agent.py#L4603) | 4603 | `"                result[\"search_report\"][\"task_understanding\"] = task_summary"` | — |
| [SRC-1AE03B9EC3-L004604](../../agents/web_agent.py#L4604) | 4604 | `"        except (AttributeError, KeyError, TypeError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L004605](../../agents/web_agent.py#L4605) | 4605 | `"            result[\"task_understanding\"] = {"` | — |
| [SRC-1AE03B9EC3-L004606](../../agents/web_agent.py#L4606) | 4606 | `"                \"status\": \"not_run\","` | — |
| [SRC-1AE03B9EC3-L004607](../../agents/web_agent.py#L4607) | 4607 | `"                \"error_class\": type(exc).__name__,"` | — |
| [SRC-1AE03B9EC3-L004608](../../agents/web_agent.py#L4608) | 4608 | `"                \"claim\": \"task interpretation diagnostics unavailable; answer was not independently verified\","` | — |
| [SRC-1AE03B9EC3-L004609](../../agents/web_agent.py#L4609) | 4609 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004610](../../agents/web_agent.py#L4610) | 4610 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004611](../../agents/web_agent.py#L4611) | 4611 | `"            completion = build_research_completion(result)"` | — |
| [SRC-1AE03B9EC3-L004612](../../agents/web_agent.py#L4612) | 4612 | `"            result[\"research_completion\"] = completion"` | — |
| [SRC-1AE03B9EC3-L004613](../../agents/web_agent.py#L4613) | 4613 | `"            # Keep the public terminal state aligned with evidence warnings discovered"` | — |
| [SRC-1AE03B9EC3-L004614](../../agents/web_agent.py#L4614) | 4614 | `"            # by the final completion audit, including early/fallback result builders."` | — |
| [SRC-1AE03B9EC3-L004615](../../agents/web_agent.py#L4615) | 4615 | `"            completion_phases = completion.get(\"phases\")"` | — |
| [SRC-1AE03B9EC3-L004616](../../agents/web_agent.py#L4616) | 4616 | `"            completion_phases = ("` | — |
| [SRC-1AE03B9EC3-L004617](../../agents/web_agent.py#L4617) | 4617 | `"                completion_phases if isinstance(completion_phases, dict) else {}"` | — |
| [SRC-1AE03B9EC3-L004618](../../agents/web_agent.py#L4618) | 4618 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004619](../../agents/web_agent.py#L4619) | 4619 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L004620](../../agents/web_agent.py#L4620) | 4620 | `"                completion_phases.get(\"citation_support_screen\") == \"warning_signals_detected\""` | — |
| [SRC-1AE03B9EC3-L004621](../../agents/web_agent.py#L4621) | 4621 | `"                or completion.get(\"status\") == \"answer_generated_without_valid_citation_markers\""` | — |
| [SRC-1AE03B9EC3-L004622](../../agents/web_agent.py#L4622) | 4622 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L004623](../../agents/web_agent.py#L4623) | 4623 | `"                result[\"pipeline_completion_status\"] = \"partial\""` | — |
| [SRC-1AE03B9EC3-L004624](../../agents/web_agent.py#L4624) | 4624 | `"            if isinstance(result.get(\"search_report\"), dict):"` | — |
| [SRC-1AE03B9EC3-L004625](../../agents/web_agent.py#L4625) | 4625 | `"                result[\"search_report\"][\"research_completion\"] = completion"` | — |
| [SRC-1AE03B9EC3-L004626](../../agents/web_agent.py#L4626) | 4626 | `"                if result.get(\"pipeline_completion_status\") == \"partial\":"` | — |
| [SRC-1AE03B9EC3-L004627](../../agents/web_agent.py#L4627) | 4627 | `"                    result[\"search_report\"][\"pipeline_completion_status\"] = \"partial\""` | — |
| [SRC-1AE03B9EC3-L004628](../../agents/web_agent.py#L4628) | 4628 | `"        except Exception:"` | — |
| [SRC-1AE03B9EC3-L004629](../../agents/web_agent.py#L4629) | 4629 | `"            # Diagnostics must never replace a valid answer with an internal error."` | — |
| [SRC-1AE03B9EC3-L004630](../../agents/web_agent.py#L4630) | 4630 | `"            result[\"research_completion\"] = {"` | — |
| [SRC-1AE03B9EC3-L004631](../../agents/web_agent.py#L4631) | 4631 | `"                \"status\": \"diagnostics_not_computed\","` | — |
| [SRC-1AE03B9EC3-L004632](../../agents/web_agent.py#L4632) | 4632 | `"                \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L004633](../../agents/web_agent.py#L4633) | 4633 | `"                \"error_class\": \"research_completion_diagnostics_error\","` | — |
| [SRC-1AE03B9EC3-L004634](../../agents/web_agent.py#L4634) | 4634 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004635](../../agents/web_agent.py#L4635) | 4635 | `"            result.setdefault(\"warnings\", []).append("` | — |
| [SRC-1AE03B9EC3-L004636](../../agents/web_agent.py#L4636) | 4636 | `"                \"تعذر حساب حالة إكمال البحث وعداداته؛ لا يُعد ذلك دليلًا على اكتمال البحث.\""` | — |
| [SRC-1AE03B9EC3-L004637](../../agents/web_agent.py#L4637) | 4637 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004638](../../agents/web_agent.py#L4638) | 4638 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L004639](../../agents/web_agent.py#L4639) | 4639 | `""` | — |
| [SRC-1AE03B9EC3-L004640](../../agents/web_agent.py#L4640) | 4640 | `"    def _answer_with_budget("` | — |
| [SRC-1AE03B9EC3-L004641](../../agents/web_agent.py#L4641) | 4641 | `"        self, question: str, history: Any = None, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L004642](../../agents/web_agent.py#L4642) | 4642 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L004643](../../agents/web_agent.py#L4643) | 4643 | `"        if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-1AE03B9EC3-L004644](../../agents/web_agent.py#L4644) | 4644 | `"            raise ValueError(\"اكتب سؤالًا غير فارغ.\")"` | — |
| [SRC-1AE03B9EC3-L004645](../../agents/web_agent.py#L4645) | 4645 | `"        question = question.strip()"` | — |
| [SRC-1AE03B9EC3-L004646](../../agents/web_agent.py#L4646) | 4646 | `"        if len(question) > MAX_QUESTION_CHARS:"` | — |
| [SRC-1AE03B9EC3-L004647](../../agents/web_agent.py#L4647) | 4647 | `"            raise ValueError(f\"السؤال طويل جدًا؛ الحد الأقصى {MAX_QUESTION_CHARS} حرف.\")"` | — |
| [SRC-1AE03B9EC3-L004648](../../agents/web_agent.py#L4648) | 4648 | `"        clean_history = self._sanitize_history(history)"` | — |
| [SRC-1AE03B9EC3-L004649](../../agents/web_agent.py#L4649) | 4649 | `"        # Resolve elliptical follow-ups once and carry the resolved intent through"` | — |
| [SRC-1AE03B9EC3-L004650](../../agents/web_agent.py#L4650) | 4650 | ``"        # planning, generation, review, and evidence checks. Keep `question` intact"`` | — |
| [SRC-1AE03B9EC3-L004651](../../agents/web_agent.py#L4651) | 4651 | `"        # for the public response contract and initial intent routing."` | — |
| [SRC-1AE03B9EC3-L004652](../../agents/web_agent.py#L4652) | 4652 | `"        working_question = self._history_search_query(question, clean_history) or question"` | — |
| [SRC-1AE03B9EC3-L004653](../../agents/web_agent.py#L4653) | 4653 | `"        if not isinstance(working_question, str) or not working_question.strip():"` | — |
| [SRC-1AE03B9EC3-L004654](../../agents/web_agent.py#L4654) | 4654 | `"            working_question = question"` | — |
| [SRC-1AE03B9EC3-L004655](../../agents/web_agent.py#L4655) | 4655 | `"        self._reset_deepseek_search_budget()"` | — |
| [SRC-1AE03B9EC3-L004656](../../agents/web_agent.py#L4656) | 4656 | `"        self.server_search_sources = []"` | — |
| [SRC-1AE03B9EC3-L004657](../../agents/web_agent.py#L4657) | 4657 | `"        self.model_usage = []"` | — |
| [SRC-1AE03B9EC3-L004658](../../agents/web_agent.py#L4658) | 4658 | `"        self.generation_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L004659](../../agents/web_agent.py#L4659) | 4659 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004660](../../agents/web_agent.py#L4660) | 4660 | `"            self._provider_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L004661](../../agents/web_agent.py#L4661) | 4661 | `"        clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-1AE03B9EC3-L004662](../../agents/web_agent.py#L4662) | 4662 | `"        if clean_mode not in {\"auto\", \"deep\", \"latest\", \"social\"}:"` | — |
| [SRC-1AE03B9EC3-L004663](../../agents/web_agent.py#L4663) | 4663 | `"            raise ValueError(\"نمط البحث غير مدعوم. اختر auto أو deep أو latest أو social.\")"` | — |
| [SRC-1AE03B9EC3-L004664](../../agents/web_agent.py#L4664) | 4664 | `"        current_search_status_question = self._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L004665](../../agents/web_agent.py#L4665) | 4665 | `"        # Explicit UI modes control research tasks, but must not turn a status"` | — |
| [SRC-1AE03B9EC3-L004666](../../agents/web_agent.py#L4666) | 4666 | `"        # question about this answer into a new web-search request."` | — |
| [SRC-1AE03B9EC3-L004667](../../agents/web_agent.py#L4667) | 4667 | `"        routing_mode = \"auto\" if current_search_status_question else clean_mode"` | — |
| [SRC-1AE03B9EC3-L004668](../../agents/web_agent.py#L4668) | 4668 | `"        decision = route_intent("` | — |
| [SRC-1AE03B9EC3-L004669](../../agents/web_agent.py#L4669) | 4669 | `"            question,"` | — |
| [SRC-1AE03B9EC3-L004670](../../agents/web_agent.py#L4670) | 4670 | `"            clean_history,"` | — |
| [SRC-1AE03B9EC3-L004671](../../agents/web_agent.py#L4671) | 4671 | `"            routing_mode,"` | — |
| [SRC-1AE03B9EC3-L004672](../../agents/web_agent.py#L4672) | 4672 | `"            capability_question=self._is_self_question(question),"` | — |
| [SRC-1AE03B9EC3-L004673](../../agents/web_agent.py#L4673) | 4673 | `"            requires_web=self._requires_web_research(question, routing_mode),"` | — |
| [SRC-1AE03B9EC3-L004674](../../agents/web_agent.py#L4674) | 4674 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004675](../../agents/web_agent.py#L4675) | 4675 | `"        intent_route = str(decision[\"route\"])"` | — |
| [SRC-1AE03B9EC3-L004676](../../agents/web_agent.py#L4676) | 4676 | `"        intent_reason = str(decision[\"reason\"])"` | — |
| [SRC-1AE03B9EC3-L004677](../../agents/web_agent.py#L4677) | 4677 | `"        context_override: dict[str, Any] \| None = None"` | — |
| [SRC-1AE03B9EC3-L004678](../../agents/web_agent.py#L4678) | 4678 | `""` | — |
| [SRC-1AE03B9EC3-L004679](../../agents/web_agent.py#L4679) | 4679 | `"        # Rules only decide when a context probe may be needed. The model interprets"` | — |
| [SRC-1AE03B9EC3-L004680](../../agents/web_agent.py#L4680) | 4680 | `"        # meaning only on those turns; it never receives authority to execute tools."` | — |
| [SRC-1AE03B9EC3-L004681](../../agents/web_agent.py#L4681) | 4681 | `"        probe_dialogue = ("` | — |
| [SRC-1AE03B9EC3-L004682](../../agents/web_agent.py#L4682) | 4682 | `"            bool(clean_history)"` | — |
| [SRC-1AE03B9EC3-L004683](../../agents/web_agent.py#L4683) | 4683 | `"            and not current_search_status_question"` | — |
| [SRC-1AE03B9EC3-L004684](../../agents/web_agent.py#L4684) | 4684 | `"            and not self._is_self_question(question)"` | — |
| [SRC-1AE03B9EC3-L004685](../../agents/web_agent.py#L4685) | 4685 | `"            and ("` | — |
| [SRC-1AE03B9EC3-L004686](../../agents/web_agent.py#L4686) | 4686 | `"                intent_route != \"LOCAL\""` | — |
| [SRC-1AE03B9EC3-L004687](../../agents/web_agent.py#L4687) | 4687 | `"                or might_be_context_dependent(question)"` | — |
| [SRC-1AE03B9EC3-L004688](../../agents/web_agent.py#L4688) | 4688 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004689](../../agents/web_agent.py#L4689) | 4689 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004690](../../agents/web_agent.py#L4690) | 4690 | `"        if probe_dialogue:"` | — |
| [SRC-1AE03B9EC3-L004691](../../agents/web_agent.py#L4691) | 4691 | `"            semantic_context = self._resolve_dialogue_context(question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L004692](../../agents/web_agent.py#L4692) | 4692 | `"            if semantic_context.get(\"method\") == \"llm_semantic_context\":"` | — |
| [SRC-1AE03B9EC3-L004693](../../agents/web_agent.py#L4693) | 4693 | `"                context_override = semantic_context"` | — |
| [SRC-1AE03B9EC3-L004694](../../agents/web_agent.py#L4694) | 4694 | `"                if semantic_context.get(\"needs_clarification\"):"` | — |
| [SRC-1AE03B9EC3-L004695](../../agents/web_agent.py#L4695) | 4695 | `"                    return self._dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L004696](../../agents/web_agent.py#L4696) | 4696 | `"                        question, clean_mode, semantic_context,"` | — |
| [SRC-1AE03B9EC3-L004697](../../agents/web_agent.py#L4697) | 4697 | `"                        \"semantic_context_has_unresolved_referent\","` | — |
| [SRC-1AE03B9EC3-L004698](../../agents/web_agent.py#L4698) | 4698 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004699](../../agents/web_agent.py#L4699) | 4699 | `"                working_question = ("` | — |
| [SRC-1AE03B9EC3-L004700](../../agents/web_agent.py#L4700) | 4700 | `"                    question if semantic_context.get(\"topic_shift\")"` | — |
| [SRC-1AE03B9EC3-L004701](../../agents/web_agent.py#L4701) | 4701 | `"                    else semantic_context.get(\"resolved_question\") or question"` | — |
| [SRC-1AE03B9EC3-L004702](../../agents/web_agent.py#L4702) | 4702 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004703](../../agents/web_agent.py#L4703) | 4703 | `"                semantic_decision = route_intent("` | — |
| [SRC-1AE03B9EC3-L004704](../../agents/web_agent.py#L4704) | 4704 | `"                    working_question,"` | — |
| [SRC-1AE03B9EC3-L004705](../../agents/web_agent.py#L4705) | 4705 | `"                    clean_history,"` | — |
| [SRC-1AE03B9EC3-L004706](../../agents/web_agent.py#L4706) | 4706 | `"                    routing_mode,"` | — |
| [SRC-1AE03B9EC3-L004707](../../agents/web_agent.py#L4707) | 4707 | `"                    capability_question=self._is_self_question(working_question),"` | — |
| [SRC-1AE03B9EC3-L004708](../../agents/web_agent.py#L4708) | 4708 | `"                    requires_web=("` | — |
| [SRC-1AE03B9EC3-L004709](../../agents/web_agent.py#L4709) | 4709 | `"                        bool(semantic_context.get(\"needs_web\"))"` | — |
| [SRC-1AE03B9EC3-L004710](../../agents/web_agent.py#L4710) | 4710 | `"                        or self._requires_web_research(working_question, routing_mode)"` | — |
| [SRC-1AE03B9EC3-L004711](../../agents/web_agent.py#L4711) | 4711 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L004712](../../agents/web_agent.py#L4712) | 4712 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004713](../../agents/web_agent.py#L4713) | 4713 | `"                if semantic_context.get(\"needs_web\") and routing_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L004714](../../agents/web_agent.py#L4714) | 4714 | `"                    deep_intents = {\"compare\", \"social_opinions\", \"lead_generation\"}"` | — |
| [SRC-1AE03B9EC3-L004715](../../agents/web_agent.py#L4715) | 4715 | `"                    intent_route = ("` | — |
| [SRC-1AE03B9EC3-L004716](../../agents/web_agent.py#L4716) | 4716 | `"                        \"WEB_DEEP\""` | — |
| [SRC-1AE03B9EC3-L004717](../../agents/web_agent.py#L4717) | 4717 | `"                        if semantic_context.get(\"research_depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L004718](../../agents/web_agent.py#L4718) | 4718 | `"                        or semantic_context.get(\"intent\") in deep_intents"` | — |
| [SRC-1AE03B9EC3-L004719](../../agents/web_agent.py#L4719) | 4719 | `"                        else \"WEB_SIMPLE\""` | — |
| [SRC-1AE03B9EC3-L004720](../../agents/web_agent.py#L4720) | 4720 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004721](../../agents/web_agent.py#L4721) | 4721 | `"                    intent_reason = \"semantic_dialogue_context_requires_web\""` | — |
| [SRC-1AE03B9EC3-L004722](../../agents/web_agent.py#L4722) | 4722 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004723](../../agents/web_agent.py#L4723) | 4723 | `"                    intent_route = str(semantic_decision[\"route\"])"` | — |
| [SRC-1AE03B9EC3-L004724](../../agents/web_agent.py#L4724) | 4724 | `"                    intent_reason = \"semantic_dialogue_context_\" + str(semantic_decision[\"reason\"])"` | — |
| [SRC-1AE03B9EC3-L004725](../../agents/web_agent.py#L4725) | 4725 | `"                decision = semantic_decision"` | — |
| [SRC-1AE03B9EC3-L004726](../../agents/web_agent.py#L4726) | 4726 | `""` | — |
| [SRC-1AE03B9EC3-L004727](../../agents/web_agent.py#L4727) | 4727 | `"        # A small deterministic preflight catches requests whose required subject"` | — |
| [SRC-1AE03B9EC3-L004728](../../agents/web_agent.py#L4728) | 4728 | `"        # or source is absent before the planner or search connectors are invoked."` | — |
| [SRC-1AE03B9EC3-L004729](../../agents/web_agent.py#L4729) | 4729 | `"        # This is intentionally limited to hard missing inputs, not optional details."` | — |
| [SRC-1AE03B9EC3-L004730](../../agents/web_agent.py#L4730) | 4730 | `"        preflight_pipeline = build_research_pipeline("` | — |
| [SRC-1AE03B9EC3-L004731](../../agents/web_agent.py#L4731) | 4731 | `"            working_question,"` | — |
| [SRC-1AE03B9EC3-L004732](../../agents/web_agent.py#L4732) | 4732 | `"            mode=clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004733](../../agents/web_agent.py#L4733) | 4733 | `"            intent_route=intent_route,"` | — |
| [SRC-1AE03B9EC3-L004734](../../agents/web_agent.py#L4734) | 4734 | `"            dialogue_context=context_override,"` | — |
| [SRC-1AE03B9EC3-L004735](../../agents/web_agent.py#L4735) | 4735 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004736](../../agents/web_agent.py#L4736) | 4736 | `"        preflight_task_spec = preflight_pipeline[\"task_spec\"]"` | — |
| [SRC-1AE03B9EC3-L004737](../../agents/web_agent.py#L4737) | 4737 | `"        missing_inputs = set(preflight_task_spec.get(\"missing_required_inputs\") or [])"` | — |
| [SRC-1AE03B9EC3-L004738](../../agents/web_agent.py#L4738) | 4738 | `"        actionable_missing_inputs = missing_inputs & {"` | — |
| [SRC-1AE03B9EC3-L004739](../../agents/web_agent.py#L4739) | 4739 | `"            \"official_destination_target_entity\","` | — |
| [SRC-1AE03B9EC3-L004740](../../agents/web_agent.py#L4740) | 4740 | `"            \"summary_source_url_or_pasted_text\","` | — |
| [SRC-1AE03B9EC3-L004741](../../agents/web_agent.py#L4741) | 4741 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004742](../../agents/web_agent.py#L4742) | 4742 | `"        if actionable_missing_inputs and intent_route not in {\"LOCAL\", \"CLARIFY\"}:"` | — |
| [SRC-1AE03B9EC3-L004743](../../agents/web_agent.py#L4743) | 4743 | `"            clarification = self._clarification_result("` | — |
| [SRC-1AE03B9EC3-L004744](../../agents/web_agent.py#L4744) | 4744 | `"                question,"` | — |
| [SRC-1AE03B9EC3-L004745](../../agents/web_agent.py#L4745) | 4745 | `"                clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004746](../../agents/web_agent.py#L4746) | 4746 | `"                {"` | — |
| [SRC-1AE03B9EC3-L004747](../../agents/web_agent.py#L4747) | 4747 | `"                    \"route\": \"CLARIFY\","` | — |
| [SRC-1AE03B9EC3-L004748](../../agents/web_agent.py#L4748) | 4748 | `"                    \"reason\": \"task_spec_missing_required_input\","` | — |
| [SRC-1AE03B9EC3-L004749](../../agents/web_agent.py#L4749) | 4749 | `"                    \"needs_clarification\": True,"` | — |
| [SRC-1AE03B9EC3-L004750](../../agents/web_agent.py#L4750) | 4750 | `"                    \"context_available\": bool(context_override),"` | — |
| [SRC-1AE03B9EC3-L004751](../../agents/web_agent.py#L4751) | 4751 | `"                },"` | — |
| [SRC-1AE03B9EC3-L004752](../../agents/web_agent.py#L4752) | 4752 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004753](../../agents/web_agent.py#L4753) | 4753 | `"            clarification[\"task_spec_preflight\"] = preflight_task_spec"` | — |
| [SRC-1AE03B9EC3-L004754](../../agents/web_agent.py#L4754) | 4754 | `"            if \"official_destination_target_entity\" in actionable_missing_inputs:"` | — |
| [SRC-1AE03B9EC3-L004755](../../agents/web_agent.py#L4755) | 4755 | `"                clarification[\"answer\"] = ("` | — |
| [SRC-1AE03B9EC3-L004756](../../agents/web_agent.py#L4756) | 4756 | `"                    \"ما اسم الجهة أو الشركة التي تريد موقعها الرسمي؟ اكتب الاسم، \""` | — |
| [SRC-1AE03B9EC3-L004757](../../agents/web_agent.py#L4757) | 4757 | `"                    \"والبلد أيضًا إذا كانت الجهة موجودة في أكثر من دولة.\""` | — |
| [SRC-1AE03B9EC3-L004758](../../agents/web_agent.py#L4758) | 4758 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004759](../../agents/web_agent.py#L4759) | 4759 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004760](../../agents/web_agent.py#L4760) | 4760 | `"                clarification[\"answer\"] = ("` | — |
| [SRC-1AE03B9EC3-L004761](../../agents/web_agent.py#L4761) | 4761 | `"                    \"أرسل النص الذي تريد تلخيصه أو رابط الصفحة. لن ألخّص محتوى \""` | — |
| [SRC-1AE03B9EC3-L004762](../../agents/web_agent.py#L4762) | 4762 | `"                    \"لم أتمكن من الاطلاع عليه.\""` | — |
| [SRC-1AE03B9EC3-L004763](../../agents/web_agent.py#L4763) | 4763 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004764](../../agents/web_agent.py#L4764) | 4764 | `"            return clarification"` | — |
| [SRC-1AE03B9EC3-L004765](../../agents/web_agent.py#L4765) | 4765 | `""` | — |
| [SRC-1AE03B9EC3-L004766](../../agents/web_agent.py#L4766) | 4766 | `"        if intent_route == \"LOCAL\":"` | — |
| [SRC-1AE03B9EC3-L004767](../../agents/web_agent.py#L4767) | 4767 | `"            if self._is_self_question(question):"` | — |
| [SRC-1AE03B9EC3-L004768](../../agents/web_agent.py#L4768) | 4768 | `"                local_result = self._self_description_answer(question)"` | — |
| [SRC-1AE03B9EC3-L004769](../../agents/web_agent.py#L4769) | 4769 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004770](../../agents/web_agent.py#L4770) | 4770 | `"                local_result = self._local_answer_result("` | — |
| [SRC-1AE03B9EC3-L004771](../../agents/web_agent.py#L4771) | 4771 | `"                    question, self._local_conversation_reply(question), \"local_conversation\""` | — |
| [SRC-1AE03B9EC3-L004772](../../agents/web_agent.py#L4772) | 4772 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004773](../../agents/web_agent.py#L4773) | 4773 | `"            return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L004774](../../agents/web_agent.py#L4774) | 4774 | `"                local_result, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L004775](../../agents/web_agent.py#L4775) | 4775 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004776](../../agents/web_agent.py#L4776) | 4776 | `""` | — |
| [SRC-1AE03B9EC3-L004777](../../agents/web_agent.py#L4777) | 4777 | `"        if intent_route == \"CLARIFY\":"` | — |
| [SRC-1AE03B9EC3-L004778](../../agents/web_agent.py#L4778) | 4778 | `"            if context_override is not None:"` | — |
| [SRC-1AE03B9EC3-L004779](../../agents/web_agent.py#L4779) | 4779 | `"                return self._dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L004780](../../agents/web_agent.py#L4780) | 4780 | `"                    question, clean_mode, context_override, intent_reason"` | — |
| [SRC-1AE03B9EC3-L004781](../../agents/web_agent.py#L4781) | 4781 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004782](../../agents/web_agent.py#L4782) | 4782 | `"            return self._clarification_result(question, clean_mode, decision)"` | — |
| [SRC-1AE03B9EC3-L004783](../../agents/web_agent.py#L4783) | 4783 | `""` | — |
| [SRC-1AE03B9EC3-L004784](../../agents/web_agent.py#L4784) | 4784 | `"        if intent_route == \"MODEL_ONLY\":"` | — |
| [SRC-1AE03B9EC3-L004785](../../agents/web_agent.py#L4785) | 4785 | `"            general_answer = self._answer_without_search(working_question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L004786](../../agents/web_agent.py#L4786) | 4786 | `"            if general_answer is not None:"` | — |
| [SRC-1AE03B9EC3-L004787](../../agents/web_agent.py#L4787) | 4787 | `"                # Keep the public API question verbatim; the resolved wording is for"` | — |
| [SRC-1AE03B9EC3-L004788](../../agents/web_agent.py#L4788) | 4788 | `"                # internal reasoning and generation, not a replacement for user input."` | — |
| [SRC-1AE03B9EC3-L004789](../../agents/web_agent.py#L4789) | 4789 | `"                general_answer[\"question\"] = question"` | — |
| [SRC-1AE03B9EC3-L004790](../../agents/web_agent.py#L4790) | 4790 | `"                if context_override is not None:"` | — |
| [SRC-1AE03B9EC3-L004791](../../agents/web_agent.py#L4791) | 4791 | `"                    general_answer[\"dialogue_context\"] = context_override"` | — |
| [SRC-1AE03B9EC3-L004792](../../agents/web_agent.py#L4792) | 4792 | `"                    if isinstance(general_answer.get(\"research_plan\"), dict):"` | — |
| [SRC-1AE03B9EC3-L004793](../../agents/web_agent.py#L4793) | 4793 | `"                        general_answer[\"research_plan\"][\"dialogue_context\"] = context_override"` | — |
| [SRC-1AE03B9EC3-L004794](../../agents/web_agent.py#L4794) | 4794 | `"                return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L004795](../../agents/web_agent.py#L4795) | 4795 | `"                    general_answer, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L004796](../../agents/web_agent.py#L4796) | 4796 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004797](../../agents/web_agent.py#L4797) | 4797 | `"            # Preserve the existing degraded-mode behavior when generation is unavailable:"` | — |
| [SRC-1AE03B9EC3-L004798](../../agents/web_agent.py#L4798) | 4798 | `"            # run the current web pipeline rather than fabricate a model-only answer."` | — |
| [SRC-1AE03B9EC3-L004799](../../agents/web_agent.py#L4799) | 4799 | `"            intent_route = \"WEB_SIMPLE\""` | — |
| [SRC-1AE03B9EC3-L004800](../../agents/web_agent.py#L4800) | 4800 | `"            intent_reason = \"model_unavailable_fallback_to_existing_web_research\""` | — |
| [SRC-1AE03B9EC3-L004801](../../agents/web_agent.py#L4801) | 4801 | `""` | — |
| [SRC-1AE03B9EC3-L004802](../../agents/web_agent.py#L4802) | 4802 | `"        if context_override is None:"` | — |
| [SRC-1AE03B9EC3-L004803](../../agents/web_agent.py#L4803) | 4803 | `"            # Preserve compatibility with existing integrations and test doubles."` | — |
| [SRC-1AE03B9EC3-L004804](../../agents/web_agent.py#L4804) | 4804 | `"            plan = self._plan_search(question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L004805](../../agents/web_agent.py#L4805) | 4805 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004806](../../agents/web_agent.py#L4806) | 4806 | `"            plan = self._plan_search("` | — |
| [SRC-1AE03B9EC3-L004807](../../agents/web_agent.py#L4807) | 4807 | `"                question, clean_history, context_override=context_override"` | — |
| [SRC-1AE03B9EC3-L004808](../../agents/web_agent.py#L4808) | 4808 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004809](../../agents/web_agent.py#L4809) | 4809 | `"        dialogue_context = plan.get(\"dialogue_context\")"` | — |
| [SRC-1AE03B9EC3-L004810](../../agents/web_agent.py#L4810) | 4810 | `"        if isinstance(dialogue_context, dict):"` | — |
| [SRC-1AE03B9EC3-L004811](../../agents/web_agent.py#L4811) | 4811 | `"            if dialogue_context.get(\"needs_clarification\"):"` | — |
| [SRC-1AE03B9EC3-L004812](../../agents/web_agent.py#L4812) | 4812 | `"                return self._dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L004813](../../agents/web_agent.py#L4813) | 4813 | `"                    question, clean_mode, dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L004814](../../agents/web_agent.py#L4814) | 4814 | `"                    \"planner_detected_unresolved_referent\","` | — |
| [SRC-1AE03B9EC3-L004815](../../agents/web_agent.py#L4815) | 4815 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004816](../../agents/web_agent.py#L4816) | 4816 | `"            working_question = ("` | — |
| [SRC-1AE03B9EC3-L004817](../../agents/web_agent.py#L4817) | 4817 | `"                question if dialogue_context.get(\"topic_shift\")"` | — |
| [SRC-1AE03B9EC3-L004818](../../agents/web_agent.py#L4818) | 4818 | `"                else dialogue_context.get(\"resolved_question\") or working_question"` | — |
| [SRC-1AE03B9EC3-L004819](../../agents/web_agent.py#L4819) | 4819 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004820](../../agents/web_agent.py#L4820) | 4820 | `"        plan[\"mode\"] = clean_mode"` | — |
| [SRC-1AE03B9EC3-L004821](../../agents/web_agent.py#L4821) | 4821 | `"        plan[\"intent_route\"] = intent_route"` | — |
| [SRC-1AE03B9EC3-L004822](../../agents/web_agent.py#L4822) | 4822 | `"        plan[\"intent_route_reason\"] = intent_reason"` | — |
| [SRC-1AE03B9EC3-L004823](../../agents/web_agent.py#L4823) | 4823 | `"        # Normalize planner output before depth/mode expansion so a raw instruction-only"` | — |
| [SRC-1AE03B9EC3-L004824](../../agents/web_agent.py#L4824) | 4824 | `"        # prompt cannot seed synthetic generic queries when the topic is empty."` | — |
| [SRC-1AE03B9EC3-L004825](../../agents/web_agent.py#L4825) | 4825 | `"        raw_plan_queries = plan.get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L004826](../../agents/web_agent.py#L4826) | 4826 | `"        if not isinstance(raw_plan_queries, list):"` | — |
| [SRC-1AE03B9EC3-L004827](../../agents/web_agent.py#L4827) | 4827 | `"            raw_plan_queries = []"` | — |
| [SRC-1AE03B9EC3-L004828](../../agents/web_agent.py#L4828) | 4828 | `"        normalized_plan_queries = []"` | — |
| [SRC-1AE03B9EC3-L004829](../../agents/web_agent.py#L4829) | 4829 | `"        for raw_query in raw_plan_queries:"` | — |
| [SRC-1AE03B9EC3-L004830](../../agents/web_agent.py#L4830) | 4830 | `"            if not isinstance(raw_query, str) or not raw_query.strip():"` | — |
| [SRC-1AE03B9EC3-L004831](../../agents/web_agent.py#L4831) | 4831 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004832](../../agents/web_agent.py#L4832) | 4832 | `"            compacted_query = compact_search_query(raw_query)"` | — |
| [SRC-1AE03B9EC3-L004833](../../agents/web_agent.py#L4833) | 4833 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L004834](../../agents/web_agent.py#L4834) | 4834 | `"                compacted_query"` | — |
| [SRC-1AE03B9EC3-L004835](../../agents/web_agent.py#L4835) | 4835 | `"                and _relevance_query_tokens(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004836](../../agents/web_agent.py#L4836) | 4836 | `"                and compacted_query not in normalized_plan_queries"` | — |
| [SRC-1AE03B9EC3-L004837](../../agents/web_agent.py#L4837) | 4837 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L004838](../../agents/web_agent.py#L4838) | 4838 | `"                normalized_plan_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004839](../../agents/web_agent.py#L4839) | 4839 | `"        plan[\"queries\"] = normalized_plan_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004840](../../agents/web_agent.py#L4840) | 4840 | `"        # Preserve the requested mode in diagnostics even when no usable query exists."` | — |
| [SRC-1AE03B9EC3-L004841](../../agents/web_agent.py#L4841) | 4841 | `"        if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L004842](../../agents/web_agent.py#L4842) | 4842 | `"            plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004843](../../agents/web_agent.py#L4843) | 4843 | `"        elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L004844](../../agents/web_agent.py#L4844) | 4844 | `"            plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004845](../../agents/web_agent.py#L4845) | 4845 | `"        elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L004846](../../agents/web_agent.py#L4846) | 4846 | `"            plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L004847](../../agents/web_agent.py#L4847) | 4847 | `"            if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L004848](../../agents/web_agent.py#L4848) | 4848 | `"                plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L004849](../../agents/web_agent.py#L4849) | 4849 | `""` | — |
| [SRC-1AE03B9EC3-L004850](../../agents/web_agent.py#L4850) | 4850 | `"        if plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L004851](../../agents/web_agent.py#L4851) | 4851 | `"            if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\":"` | — |
| [SRC-1AE03B9EC3-L004852](../../agents/web_agent.py#L4852) | 4852 | `"                plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004853](../../agents/web_agent.py#L4853) | 4853 | `"            if clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L004854](../../agents/web_agent.py#L4854) | 4854 | `"                normalized_question = _normalize_search_query(working_question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004855](../../agents/web_agent.py#L4855) | 4855 | `"                deep_terms = ("` | — |
| [SRC-1AE03B9EC3-L004856](../../agents/web_agent.py#L4856) | 4856 | `"                    \"بحث عميق\", \"بحث معمق\", \"بحث شامل\", \"بالتفصيل\", \"قارن\", \"مقارنة\","` | — |
| [SRC-1AE03B9EC3-L004857](../../agents/web_agent.py#L4857) | 4857 | `"                    \"تحقق\", \"استقصاء\", \"deep research\", \"comprehensive\", \"in-depth\", \"compare\","` | — |
| [SRC-1AE03B9EC3-L004858](../../agents/web_agent.py#L4858) | 4858 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004859](../../agents/web_agent.py#L4859) | 4859 | `"                explicit_deep = intent_route == \"WEB_DEEP\" or any("` | — |
| [SRC-1AE03B9EC3-L004860](../../agents/web_agent.py#L4860) | 4860 | `"                    term in normalized_question for term in deep_terms"` | — |
| [SRC-1AE03B9EC3-L004861](../../agents/web_agent.py#L4861) | 4861 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004862](../../agents/web_agent.py#L4862) | 4862 | `"                if not explicit_deep:"` | — |
| [SRC-1AE03B9EC3-L004863](../../agents/web_agent.py#L4863) | 4863 | `"                    # The planner may overclassify short lookups as deep research. Preserve"` | — |
| [SRC-1AE03B9EC3-L004864](../../agents/web_agent.py#L4864) | 4864 | `"                    # the user's actual intent first and cap routine searches to three queries."` | — |
| [SRC-1AE03B9EC3-L004865](../../agents/web_agent.py#L4865) | 4865 | `"                    fallback_plan_queries = ("` | — |
| [SRC-1AE03B9EC3-L004866](../../agents/web_agent.py#L4866) | 4866 | `"                        fallback_plan(working_question, clean_history).get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L004867](../../agents/web_agent.py#L4867) | 4867 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004868](../../agents/web_agent.py#L4868) | 4868 | `"                    fallback_queries = ["` | — |
| [SRC-1AE03B9EC3-L004869](../../agents/web_agent.py#L4869) | 4869 | `"                        compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L004870](../../agents/web_agent.py#L4870) | 4870 | `"                        for query in fallback_plan_queries"` | — |
| [SRC-1AE03B9EC3-L004871](../../agents/web_agent.py#L4871) | 4871 | `"                        if isinstance(query, str)"` | — |
| [SRC-1AE03B9EC3-L004872](../../agents/web_agent.py#L4872) | 4872 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004873](../../agents/web_agent.py#L4873) | 4873 | `"                    fallback_queries = [query for query in fallback_queries if query]"` | — |
| [SRC-1AE03B9EC3-L004874](../../agents/web_agent.py#L4874) | 4874 | `"                    model_queries = ["` | — |
| [SRC-1AE03B9EC3-L004875](../../agents/web_agent.py#L4875) | 4875 | `"                        compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L004876](../../agents/web_agent.py#L4876) | 4876 | `"                        for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004877](../../agents/web_agent.py#L4877) | 4877 | `"                        if isinstance(query, str)"` | — |
| [SRC-1AE03B9EC3-L004878](../../agents/web_agent.py#L4878) | 4878 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004879](../../agents/web_agent.py#L4879) | 4879 | `"                    model_queries = [query for query in model_queries if query]"` | — |
| [SRC-1AE03B9EC3-L004880](../../agents/web_agent.py#L4880) | 4880 | `"                    if self._is_navigation_request(working_question):"` | — |
| [SRC-1AE03B9EC3-L004881](../../agents/web_agent.py#L4881) | 4881 | `"                        navigation_seed = ("` | — |
| [SRC-1AE03B9EC3-L004882](../../agents/web_agent.py#L4882) | 4882 | `"                            fallback_queries[0] if fallback_queries"` | — |
| [SRC-1AE03B9EC3-L004883](../../agents/web_agent.py#L4883) | 4883 | `"                            else model_queries[0] if model_queries"` | — |
| [SRC-1AE03B9EC3-L004884](../../agents/web_agent.py#L4884) | 4884 | `"                            else \"\""` | — |
| [SRC-1AE03B9EC3-L004885](../../agents/web_agent.py#L4885) | 4885 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004886](../../agents/web_agent.py#L4886) | 4886 | `"                        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L004887](../../agents/web_agent.py#L4887) | 4887 | `"                            r\"^(?:ابحث\|بحث\|دور\|اعثر)\\s+(?:عن\|على)?\\s*\","` | — |
| [SRC-1AE03B9EC3-L004888](../../agents/web_agent.py#L4888) | 4888 | `"                            \"\","` | — |
| [SRC-1AE03B9EC3-L004889](../../agents/web_agent.py#L4889) | 4889 | `"                            navigation_seed,"` | — |
| [SRC-1AE03B9EC3-L004890](../../agents/web_agent.py#L4890) | 4890 | `"                        ).strip()"` | — |
| [SRC-1AE03B9EC3-L004891](../../agents/web_agent.py#L4891) | 4891 | `"                        plan_queries = ("` | — |
| [SRC-1AE03B9EC3-L004892](../../agents/web_agent.py#L4892) | 4892 | `"                            ["` | — |
| [SRC-1AE03B9EC3-L004893](../../agents/web_agent.py#L4893) | 4893 | `"                                subject,"` | — |
| [SRC-1AE03B9EC3-L004894](../../agents/web_agent.py#L4894) | 4894 | `"                                subject + \" الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L004895](../../agents/web_agent.py#L4895) | 4895 | `"                                subject + \" official website\","` | — |
| [SRC-1AE03B9EC3-L004896](../../agents/web_agent.py#L4896) | 4896 | `"                            ]"` | — |
| [SRC-1AE03B9EC3-L004897](../../agents/web_agent.py#L4897) | 4897 | `"                            if subject else []"` | — |
| [SRC-1AE03B9EC3-L004898](../../agents/web_agent.py#L4898) | 4898 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004899](../../agents/web_agent.py#L4899) | 4899 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004900](../../agents/web_agent.py#L4900) | 4900 | `"                        plan_queries = (fallback_queries[:1] or model_queries[:1]) + model_queries"` | — |
| [SRC-1AE03B9EC3-L004901](../../agents/web_agent.py#L4901) | 4901 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004902](../../agents/web_agent.py#L4902) | 4902 | `"                        query.strip() for query in plan_queries if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004903](../../agents/web_agent.py#L4903) | 4903 | `"                    ))[:3]"` | — |
| [SRC-1AE03B9EC3-L004904](../../agents/web_agent.py#L4904) | 4904 | `"                    plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L004905](../../agents/web_agent.py#L4905) | 4905 | `"            base_query = (plan.get(\"queries\") or [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L004906](../../agents/web_agent.py#L4906) | 4906 | `"            if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\" and base_query:"` | — |
| [SRC-1AE03B9EC3-L004907](../../agents/web_agent.py#L4907) | 4907 | `"                deep_candidates = ["` | — |
| [SRC-1AE03B9EC3-L004908](../../agents/web_agent.py#L4908) | 4908 | `"                    f\"{base_query} official sources evidence\","` | — |
| [SRC-1AE03B9EC3-L004909](../../agents/web_agent.py#L4909) | 4909 | `"                    f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L004910](../../agents/web_agent.py#L4910) | 4910 | `"                    f\"{base_query} recent data reviews comparison\","` | — |
| [SRC-1AE03B9EC3-L004911](../../agents/web_agent.py#L4911) | 4911 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004912](../../agents/web_agent.py#L4912) | 4912 | `"                normalized_question = _normalize_search_query(working_question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004913](../../agents/web_agent.py#L4913) | 4913 | `"                property_terms = ("` | — |
| [SRC-1AE03B9EC3-L004914](../../agents/web_agent.py#L4914) | 4914 | `"                    \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L004915](../../agents/web_agent.py#L4915) | 4915 | `"                    \"apartment\", \"apartments\", \"flat\", \"real estate\", \"property\", \"house\", \"villa\","` | — |
| [SRC-1AE03B9EC3-L004916](../../agents/web_agent.py#L4916) | 4916 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004917](../../agents/web_agent.py#L4917) | 4917 | `"                if self._is_listing_discovery(working_question) and any("` | — |
| [SRC-1AE03B9EC3-L004918](../../agents/web_agent.py#L4918) | 4918 | `"                    term in normalized_question for term in property_terms"` | — |
| [SRC-1AE03B9EC3-L004919](../../agents/web_agent.py#L4919) | 4919 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004920](../../agents/web_agent.py#L4920) | 4920 | `"                    deep_candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L004921](../../agents/web_agent.py#L4921) | 4921 | `"                        f\"{base_query} إعلانات عقارية ومواقع العقارات\","` | — |
| [SRC-1AE03B9EC3-L004922](../../agents/web_agent.py#L4922) | 4922 | `"                        f\"{base_query} متوسط أسعار السوق للمتر\","` | — |
| [SRC-1AE03B9EC3-L004923](../../agents/web_agent.py#L4923) | 4923 | `"                        f\"{base_query} مواصفات الوحدات والمساحات وطرق السداد\","` | — |
| [SRC-1AE03B9EC3-L004924](../../agents/web_agent.py#L4924) | 4924 | `"                    ])"` | — |
| [SRC-1AE03B9EC3-L004925](../../agents/web_agent.py#L4925) | 4925 | `"                # Close the planning loop: give every explicit user criterion its own"` | — |
| [SRC-1AE03B9EC3-L004926](../../agents/web_agent.py#L4926) | 4926 | `"                # query before generic \"deep research\" queries consume the fixed budget."` | — |
| [SRC-1AE03B9EC3-L004927](../../agents/web_agent.py#L4927) | 4927 | `"                # This is a retrieval heuristic, not a guarantee that evidence exists."` | — |
| [SRC-1AE03B9EC3-L004928](../../agents/web_agent.py#L4928) | 4928 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004929](../../agents/web_agent.py#L4929) | 4929 | `"                    compact_search_query(f\"{base_query} {target} official data specifications\")"` | — |
| [SRC-1AE03B9EC3-L004930](../../agents/web_agent.py#L4930) | 4930 | `"                    for target in self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004931](../../agents/web_agent.py#L4931) | 4931 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004932](../../agents/web_agent.py#L4932) | 4932 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004933](../../agents/web_agent.py#L4933) | 4933 | `"                    query for query in criterion_queries"` | — |
| [SRC-1AE03B9EC3-L004934](../../agents/web_agent.py#L4934) | 4934 | `"                    if query and _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L004935](../../agents/web_agent.py#L4935) | 4935 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004936](../../agents/web_agent.py#L4936) | 4936 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L004937](../../agents/web_agent.py#L4937) | 4937 | `"                    query for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004938](../../agents/web_agent.py#L4938) | 4938 | `"                    if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004939](../../agents/web_agent.py#L4939) | 4939 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004940](../../agents/web_agent.py#L4940) | 4940 | `"                # Each criterion query already contains the base subject. When the"` | — |
| [SRC-1AE03B9EC3-L004941](../../agents/web_agent.py#L4941) | 4941 | `"                # question has many criteria, spend the full bounded budget on those"` | — |
| [SRC-1AE03B9EC3-L004942](../../agents/web_agent.py#L4942) | 4942 | `"                # queries rather than silently dropping later criteria for a base query."` | — |
| [SRC-1AE03B9EC3-L004943](../../agents/web_agent.py#L4943) | 4943 | `"                prioritized_queries = criterion_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004944](../../agents/web_agent.py#L4944) | 4944 | `"                if len(prioritized_queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-1AE03B9EC3-L004945](../../agents/web_agent.py#L4945) | 4945 | `"                    prioritized_queries += original_queries[:1] + deep_candidates"` | — |
| [SRC-1AE03B9EC3-L004946](../../agents/web_agent.py#L4946) | 4946 | `"                plan[\"queries\"] = list(dict.fromkeys(prioritized_queries))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004947](../../agents/web_agent.py#L4947) | 4947 | `"                base_query = (plan.get(\"queries\") or [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L004948](../../agents/web_agent.py#L4948) | 4948 | `"            # Explicit user-selected modes are control inputs. They do not bypass source"` | — |
| [SRC-1AE03B9EC3-L004949](../../agents/web_agent.py#L4949) | 4949 | `"            # validation and never permit private-source access."` | — |
| [SRC-1AE03B9EC3-L004950](../../agents/web_agent.py#L4950) | 4950 | `"            if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L004951](../../agents/web_agent.py#L4951) | 4951 | `"                plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004952](../../agents/web_agent.py#L4952) | 4952 | `"                candidates = ["` | — |
| [SRC-1AE03B9EC3-L004953](../../agents/web_agent.py#L4953) | 4953 | `"                    f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L004954](../../agents/web_agent.py#L4954) | 4954 | `"                    f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L004955](../../agents/web_agent.py#L4955) | 4955 | `"                    f\"{base_query} case studies recent analysis\","` | — |
| [SRC-1AE03B9EC3-L004956](../../agents/web_agent.py#L4956) | 4956 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004957](../../agents/web_agent.py#L4957) | 4957 | `"                normalized_question = _normalize_search_query(working_question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004958](../../agents/web_agent.py#L4958) | 4958 | `"                property_terms = ("` | — |
| [SRC-1AE03B9EC3-L004959](../../agents/web_agent.py#L4959) | 4959 | `"                    \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L004960](../../agents/web_agent.py#L4960) | 4960 | `"                    \"apartment\", \"apartments\", \"flat\", \"real estate\", \"property\", \"house\", \"villa\","` | — |
| [SRC-1AE03B9EC3-L004961](../../agents/web_agent.py#L4961) | 4961 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004962](../../agents/web_agent.py#L4962) | 4962 | `"                if self._is_listing_discovery(working_question) and any("` | — |
| [SRC-1AE03B9EC3-L004963](../../agents/web_agent.py#L4963) | 4963 | `"                    term in normalized_question for term in property_terms"` | — |
| [SRC-1AE03B9EC3-L004964](../../agents/web_agent.py#L4964) | 4964 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004965](../../agents/web_agent.py#L4965) | 4965 | `"                    candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L004966](../../agents/web_agent.py#L4966) | 4966 | `"                        f\"{base_query} إعلانات عقارية ومواقع العقارات\","` | — |
| [SRC-1AE03B9EC3-L004967](../../agents/web_agent.py#L4967) | 4967 | `"                        f\"{base_query} متوسط أسعار السوق للمتر\","` | — |
| [SRC-1AE03B9EC3-L004968](../../agents/web_agent.py#L4968) | 4968 | `"                        f\"{base_query} مواصفات الوحدات والمساحات وطرق السداد\","` | — |
| [SRC-1AE03B9EC3-L004969](../../agents/web_agent.py#L4969) | 4969 | `"                    ])"` | — |
| [SRC-1AE03B9EC3-L004970](../../agents/web_agent.py#L4970) | 4970 | `"                # Explicit deep mode follows the same criterion-first budget allocation"` | — |
| [SRC-1AE03B9EC3-L004971](../../agents/web_agent.py#L4971) | 4971 | `"                # as automatic deep mode, so generic modifiers cannot crowd out requested"` | — |
| [SRC-1AE03B9EC3-L004972](../../agents/web_agent.py#L4972) | 4972 | `"                # dimensions such as price, battery, camera, privacy, or reliability."` | — |
| [SRC-1AE03B9EC3-L004973](../../agents/web_agent.py#L4973) | 4973 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004974](../../agents/web_agent.py#L4974) | 4974 | `"                    compact_search_query(f\"{base_query} {target} official data specifications\")"` | — |
| [SRC-1AE03B9EC3-L004975](../../agents/web_agent.py#L4975) | 4975 | `"                    for target in self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004976](../../agents/web_agent.py#L4976) | 4976 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004977](../../agents/web_agent.py#L4977) | 4977 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004978](../../agents/web_agent.py#L4978) | 4978 | `"                    query for query in criterion_queries"` | — |
| [SRC-1AE03B9EC3-L004979](../../agents/web_agent.py#L4979) | 4979 | `"                    if query and _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L004980](../../agents/web_agent.py#L4980) | 4980 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004981](../../agents/web_agent.py#L4981) | 4981 | `"                # Criterion queries include the subject and take priority; retain a"` | — |
| [SRC-1AE03B9EC3-L004982](../../agents/web_agent.py#L4982) | 4982 | `"                # planner query and generic exploration only when budget remains."` | — |
| [SRC-1AE03B9EC3-L004983](../../agents/web_agent.py#L4983) | 4983 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L004984](../../agents/web_agent.py#L4984) | 4984 | `"                    query for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004985](../../agents/web_agent.py#L4985) | 4985 | `"                    if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004986](../../agents/web_agent.py#L4986) | 4986 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004987](../../agents/web_agent.py#L4987) | 4987 | `"                prioritized_queries = criterion_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004988](../../agents/web_agent.py#L4988) | 4988 | `"                if len(prioritized_queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-1AE03B9EC3-L004989](../../agents/web_agent.py#L4989) | 4989 | `"                    prioritized_queries += original_queries[:1] + candidates"` | — |
| [SRC-1AE03B9EC3-L004990](../../agents/web_agent.py#L4990) | 4990 | `"                plan[\"queries\"] = list(dict.fromkeys(prioritized_queries))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004991](../../agents/web_agent.py#L4991) | 4991 | `"            elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L004992](../../agents/web_agent.py#L4992) | 4992 | `"                plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004993](../../agents/web_agent.py#L4993) | 4993 | `"                if self._is_navigation_request(working_question):"` | — |
| [SRC-1AE03B9EC3-L004994](../../agents/web_agent.py#L4994) | 4994 | `"                    # Preserve link-finding intent in the latest mode. Appending broad"` | — |
| [SRC-1AE03B9EC3-L004995](../../agents/web_agent.py#L4995) | 4995 | `"                    # news modifiers here can turn \"find the official website\" into"` | — |
| [SRC-1AE03B9EC3-L004996](../../agents/web_agent.py#L4996) | 4996 | `"                    # a news-search task and hide the destination the user requested."` | — |
| [SRC-1AE03B9EC3-L004997](../../agents/web_agent.py#L4997) | 4997 | `"                    candidates = ["` | — |
| [SRC-1AE03B9EC3-L004998](../../agents/web_agent.py#L4998) | 4998 | `"                        base_query,"` | — |
| [SRC-1AE03B9EC3-L004999](../../agents/web_agent.py#L4999) | 4999 | `"                        f\"{base_query} الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L005000](../../agents/web_agent.py#L5000) | 5000 | `"                        f\"{base_query} official website\","` | — |
| [SRC-1AE03B9EC3-L005001](../../agents/web_agent.py#L5001) | 5001 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L005002](../../agents/web_agent.py#L5002) | 5002 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005003](../../agents/web_agent.py#L5003) | 5003 | `"                        candidates + (plan.get(\"queries\") or [])[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L005004](../../agents/web_agent.py#L5004) | 5004 | `"                    ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L005005](../../agents/web_agent.py#L5005) | 5005 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005006](../../agents/web_agent.py#L5006) | 5006 | `"                    candidates = ["` | — |
| [SRC-1AE03B9EC3-L005007](../../agents/web_agent.py#L5007) | 5007 | `"                        f\"{base_query} latest news updates {dt.datetime.now().year}\","` | — |
| [SRC-1AE03B9EC3-L005008](../../agents/web_agent.py#L5008) | 5008 | `"                        f\"{base_query} recent official announcement\","` | — |
| [SRC-1AE03B9EC3-L005009](../../agents/web_agent.py#L5009) | 5009 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L005010](../../agents/web_agent.py#L5010) | 5010 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005011](../../agents/web_agent.py#L5011) | 5011 | `"                        (plan.get(\"queries\") or [])[:6] + candidates"` | — |
| [SRC-1AE03B9EC3-L005012](../../agents/web_agent.py#L5012) | 5012 | `"                    ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L005013](../../agents/web_agent.py#L5013) | 5013 | `"            elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L005014](../../agents/web_agent.py#L5014) | 5014 | `"                plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L005015](../../agents/web_agent.py#L5015) | 5015 | `"                if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L005016](../../agents/web_agent.py#L5016) | 5016 | `"                    plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L005017](../../agents/web_agent.py#L5017) | 5017 | `"                from agents.research import SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L005018](../../agents/web_agent.py#L5018) | 5018 | `"                candidates = ["` | — |
| [SRC-1AE03B9EC3-L005019](../../agents/web_agent.py#L5019) | 5019 | `"                    f\"site:{SOCIAL_DOMAINS[name]} {base_query}\""` | — |
| [SRC-1AE03B9EC3-L005020](../../agents/web_agent.py#L5020) | 5020 | `"                    for name in plan[\"platforms\"][:3]"` | — |
| [SRC-1AE03B9EC3-L005021](../../agents/web_agent.py#L5021) | 5021 | `"                    if name in SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L005022](../../agents/web_agent.py#L5022) | 5022 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L005023](../../agents/web_agent.py#L5023) | 5023 | `"                plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:5] + candidates))["` | — |
| [SRC-1AE03B9EC3-L005024](../../agents/web_agent.py#L5024) | 5024 | `"                    :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L005025](../../agents/web_agent.py#L5025) | 5025 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L005026](../../agents/web_agent.py#L5026) | 5026 | `"            if intent_route == \"LEAD_GENERATION\" and clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L005027](../../agents/web_agent.py#L5027) | 5027 | `"                # Prospect discovery needs buyer-intent queries and public social signals,"` | — |
| [SRC-1AE03B9EC3-L005028](../../agents/web_agent.py#L5028) | 5028 | `"                # not just broad pages advertising the requested product."` | — |
| [SRC-1AE03B9EC3-L005029](../../agents/web_agent.py#L5029) | 5029 | `"                plan[\"queries\"] = self._lead_generation_queries(working_question, plan.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005030](../../agents/web_agent.py#L5030) | 5030 | `"                plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L005031](../../agents/web_agent.py#L5031) | 5031 | `"                plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L005032](../../agents/web_agent.py#L5032) | 5032 | `"                plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L005033](../../agents/web_agent.py#L5033) | 5033 | `"                allowed_public_platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L005034](../../agents/web_agent.py#L5034) | 5034 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L005035](../../agents/web_agent.py#L5035) | 5035 | `"                    os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L005036](../../agents/web_agent.py#L5036) | 5036 | `"                    and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L005037](../../agents/web_agent.py#L5037) | 5037 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L005038](../../agents/web_agent.py#L5038) | 5038 | `"                    allowed_public_platforms.append(\"facebook\")"` | — |
| [SRC-1AE03B9EC3-L005039](../../agents/web_agent.py#L5039) | 5039 | `"                if os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L005040](../../agents/web_agent.py#L5040) | 5040 | `"                    allowed_public_platforms.append(\"x\")"` | — |
| [SRC-1AE03B9EC3-L005041](../../agents/web_agent.py#L5041) | 5041 | `"                if os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L005042](../../agents/web_agent.py#L5042) | 5042 | `"                    allowed_public_platforms.append(\"youtube\")"` | — |
| [SRC-1AE03B9EC3-L005043](../../agents/web_agent.py#L5043) | 5043 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L005044](../../agents/web_agent.py#L5044) | 5044 | `"                    os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L005045](../../agents/web_agent.py#L5045) | 5045 | `"                    and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L005046](../../agents/web_agent.py#L5046) | 5046 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L005047](../../agents/web_agent.py#L5047) | 5047 | `"                    allowed_public_platforms.append(\"instagram\")"` | — |
| [SRC-1AE03B9EC3-L005048](../../agents/web_agent.py#L5048) | 5048 | `"                plan[\"platforms\"] = list(dict.fromkeys(allowed_public_platforms))"` | — |
| [SRC-1AE03B9EC3-L005049](../../agents/web_agent.py#L5049) | 5049 | `""` | — |
| [SRC-1AE03B9EC3-L005050](../../agents/web_agent.py#L5050) | 5050 | `"        pipeline = build_research_pipeline("` | — |
| [SRC-1AE03B9EC3-L005051](../../agents/web_agent.py#L5051) | 5051 | `"            working_question,"` | — |
| [SRC-1AE03B9EC3-L005052](../../agents/web_agent.py#L5052) | 5052 | `"            plan,"` | — |
| [SRC-1AE03B9EC3-L005053](../../agents/web_agent.py#L5053) | 5053 | `"            mode=clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005054](../../agents/web_agent.py#L5054) | 5054 | `"            intent_route=intent_route,"` | — |
| [SRC-1AE03B9EC3-L005055](../../agents/web_agent.py#L5055) | 5055 | `"            dialogue_context=dialogue_context if isinstance(dialogue_context, dict) else None,"` | — |
| [SRC-1AE03B9EC3-L005056](../../agents/web_agent.py#L5056) | 5056 | `"            compact_fn=compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L005057](../../agents/web_agent.py#L5057) | 5057 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005058](../../agents/web_agent.py#L5058) | 5058 | `"        task_spec = pipeline[\"task_spec\"]"` | — |
| [SRC-1AE03B9EC3-L005059](../../agents/web_agent.py#L5059) | 5059 | `"        query_strategy_limit = ("` | — |
| [SRC-1AE03B9EC3-L005060](../../agents/web_agent.py#L5060) | 5060 | `"            MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L005061](../../agents/web_agent.py#L5061) | 5061 | `"            if clean_mode in {\"deep\", \"latest\", \"social\"}"` | — |
| [SRC-1AE03B9EC3-L005062](../../agents/web_agent.py#L5062) | 5062 | `"            or intent_route in {\"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-1AE03B9EC3-L005063](../../agents/web_agent.py#L5063) | 5063 | `"            else 3"` | — |
| [SRC-1AE03B9EC3-L005064](../../agents/web_agent.py#L5064) | 5064 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005065](../../agents/web_agent.py#L5065) | 5065 | `"        query_strategy_matrix = pipeline[\"query_strategy_matrix\"][:query_strategy_limit]"` | — |
| [SRC-1AE03B9EC3-L005066](../../agents/web_agent.py#L5066) | 5066 | `"        if query_strategy_matrix:"` | — |
| [SRC-1AE03B9EC3-L005067](../../agents/web_agent.py#L5067) | 5067 | `"            plan[\"queries\"] = [item[\"query\"] for item in query_strategy_matrix]"` | — |
| [SRC-1AE03B9EC3-L005068](../../agents/web_agent.py#L5068) | 5068 | `"        plan[\"task_spec\"] = task_spec"` | — |
| [SRC-1AE03B9EC3-L005069](../../agents/web_agent.py#L5069) | 5069 | `"        plan[\"query_strategy_matrix\"] = query_strategy_matrix"` | — |
| [SRC-1AE03B9EC3-L005070](../../agents/web_agent.py#L5070) | 5070 | `"        plan[\"research_pipeline\"] = {"` | — |
| [SRC-1AE03B9EC3-L005071](../../agents/web_agent.py#L5071) | 5071 | `"            \"aspects\": pipeline[\"aspects\"],"` | — |
| [SRC-1AE03B9EC3-L005072](../../agents/web_agent.py#L5072) | 5072 | `"            \"stages\": pipeline[\"stages\"],"` | — |
| [SRC-1AE03B9EC3-L005073](../../agents/web_agent.py#L5073) | 5073 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005074](../../agents/web_agent.py#L5074) | 5074 | `""` | — |
| [SRC-1AE03B9EC3-L005075](../../agents/web_agent.py#L5075) | 5075 | `"        final_topic_queries = []"` | — |
| [SRC-1AE03B9EC3-L005076](../../agents/web_agent.py#L5076) | 5076 | `"        for raw_query in plan.get(\"queries\", []):"` | — |
| [SRC-1AE03B9EC3-L005077](../../agents/web_agent.py#L5077) | 5077 | `"            if not isinstance(raw_query, str) or not raw_query.strip():"` | — |
| [SRC-1AE03B9EC3-L005078](../../agents/web_agent.py#L5078) | 5078 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L005079](../../agents/web_agent.py#L5079) | 5079 | `"            compacted_query = compact_search_query(raw_query)"` | — |
| [SRC-1AE03B9EC3-L005080](../../agents/web_agent.py#L5080) | 5080 | `"            if compacted_query and _relevance_query_tokens(compacted_query):"` | — |
| [SRC-1AE03B9EC3-L005081](../../agents/web_agent.py#L5081) | 5081 | `"                final_topic_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L005082](../../agents/web_agent.py#L5082) | 5082 | `"        coverage_targets_for_budget = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005083](../../agents/web_agent.py#L5083) | 5083 | `"        # Reserve one bounded search slot for a post-review criterion-evidence gap."` | — |
| [SRC-1AE03B9EC3-L005084](../../agents/web_agent.py#L5084) | 5084 | `"        # Keep all explicit criterion queries when there are many dimensions; the"` | — |
| [SRC-1AE03B9EC3-L005085](../../agents/web_agent.py#L5085) | 5085 | `"        # reserve applies only to ordinary compound tasks with up to six targets."` | — |
| [SRC-1AE03B9EC3-L005086](../../agents/web_agent.py#L5086) | 5086 | `"        reserve_coverage_gap_query = ("` | — |
| [SRC-1AE03B9EC3-L005087](../../agents/web_agent.py#L5087) | 5087 | `"            2 <= len(coverage_targets_for_budget) <= 6"` | — |
| [SRC-1AE03B9EC3-L005088](../../agents/web_agent.py#L5088) | 5088 | `"            and plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L005089](../../agents/web_agent.py#L5089) | 5089 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005090](../../agents/web_agent.py#L5090) | 5090 | `"        query_limit = MAX_PLAN_QUERIES - 1 if reserve_coverage_gap_query else MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L005091](../../agents/web_agent.py#L5091) | 5091 | `"        plan[\"coverage_gap_repair_slot_reserved\"] = reserve_coverage_gap_query"` | — |
| [SRC-1AE03B9EC3-L005092](../../agents/web_agent.py#L5092) | 5092 | `"        plan[\"query_limit\"] = query_limit"` | — |
| [SRC-1AE03B9EC3-L005093](../../agents/web_agent.py#L5093) | 5093 | `"        plan[\"coverage_targets\"] = list(coverage_targets_for_budget)"` | — |
| [SRC-1AE03B9EC3-L005094](../../agents/web_agent.py#L5094) | 5094 | `"        plan[\"queries\"] = list(dict.fromkeys(final_topic_queries))[:query_limit]"` | — |
| [SRC-1AE03B9EC3-L005095](../../agents/web_agent.py#L5095) | 5095 | `"        actual_query_keys = set(plan[\"queries\"])"` | — |
| [SRC-1AE03B9EC3-L005096](../../agents/web_agent.py#L5096) | 5096 | `"        plan[\"query_strategy_matrix\"] = ["` | — |
| [SRC-1AE03B9EC3-L005097](../../agents/web_agent.py#L5097) | 5097 | `"            item for item in query_strategy_matrix"` | — |
| [SRC-1AE03B9EC3-L005098](../../agents/web_agent.py#L5098) | 5098 | `"            if item.get(\"query\") in actual_query_keys"` | — |
| [SRC-1AE03B9EC3-L005099](../../agents/web_agent.py#L5099) | 5099 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L005100](../../agents/web_agent.py#L5100) | 5100 | `""` | — |
| [SRC-1AE03B9EC3-L005101](../../agents/web_agent.py#L5101) | 5101 | `"        sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L005102](../../agents/web_agent.py#L5102) | 5102 | `"        search_warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L005103](../../agents/web_agent.py#L5103) | 5103 | `"        report: dict[str, Any] = {}"` | — |
| [SRC-1AE03B9EC3-L005104](../../agents/web_agent.py#L5104) | 5104 | `"        # Scope diagnostic evidence to this research attempt; a reused WebAgent must not"` | — |
| [SRC-1AE03B9EC3-L005105](../../agents/web_agent.py#L5105) | 5105 | `"        # accidentally inherit provider attempts from an earlier question."` | — |
| [SRC-1AE03B9EC3-L005106](../../agents/web_agent.py#L5106) | 5106 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L005107](../../agents/web_agent.py#L5107) | 5107 | `"            research_diagnostic_baseline = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L005108](../../agents/web_agent.py#L5108) | 5108 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005109](../../agents/web_agent.py#L5109) | 5109 | `"            sources, search_warnings, report = self._collect_research(plan)"` | — |
| [SRC-1AE03B9EC3-L005110](../../agents/web_agent.py#L5110) | 5110 | `"        except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005111](../../agents/web_agent.py#L5111) | 5111 | `"            search_warnings.append(str(exc))"` | — |
| [SRC-1AE03B9EC3-L005112](../../agents/web_agent.py#L5112) | 5112 | `"            baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L005113](../../agents/web_agent.py#L5113) | 5113 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L005114](../../agents/web_agent.py#L5114) | 5114 | `"                failure_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L005115](../../agents/web_agent.py#L5115) | 5115 | `"                    item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005116](../../agents/web_agent.py#L5116) | 5116 | `"                    if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L005117](../../agents/web_agent.py#L5117) | 5117 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L005118](../../agents/web_agent.py#L5118) | 5118 | `"            provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L005119](../../agents/web_agent.py#L5119) | 5119 | `"                item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L005120](../../agents/web_agent.py#L5120) | 5120 | `"                for item in failure_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005121](../../agents/web_agent.py#L5121) | 5121 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005122](../../agents/web_agent.py#L5122) | 5122 | `"            report = {"` | — |
| [SRC-1AE03B9EC3-L005123](../../agents/web_agent.py#L5123) | 5123 | `"                \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-1AE03B9EC3-L005124](../../agents/web_agent.py#L5124) | 5124 | `"                # The exact query count is unknowable when the pipeline fails before it"` | — |
| [SRC-1AE03B9EC3-L005125](../../agents/web_agent.py#L5125) | 5125 | `"                # returns its report. A provider diagnostic may still prove an attempt."` | — |
| [SRC-1AE03B9EC3-L005126](../../agents/web_agent.py#L5126) | 5126 | `"                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005127](../../agents/web_agent.py#L5127) | 5127 | `"                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L005128](../../agents/web_agent.py#L5128) | 5128 | `"                \"search_attempted\": True if provider_attempt_observed else None,"` | — |
| [SRC-1AE03B9EC3-L005129](../../agents/web_agent.py#L5129) | 5129 | `"                \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L005130](../../agents/web_agent.py#L5130) | 5130 | `"                    \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L005131](../../agents/web_agent.py#L5131) | 5131 | `"                    if provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L005132](../../agents/web_agent.py#L5132) | 5132 | `"                    else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005133](../../agents/web_agent.py#L5133) | 5133 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005134](../../agents/web_agent.py#L5134) | 5134 | `"                \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L005135](../../agents/web_agent.py#L5135) | 5135 | `"                \"unique_sources\": None,"` | — |
| [SRC-1AE03B9EC3-L005136](../../agents/web_agent.py#L5136) | 5136 | `"                \"pages_fetched\": None,"` | — |
| [SRC-1AE03B9EC3-L005137](../../agents/web_agent.py#L5137) | 5137 | `"                \"providers_used\": [],"` | — |
| [SRC-1AE03B9EC3-L005138](../../agents/web_agent.py#L5138) | 5138 | `"                \"provider_counts\": None,"` | — |
| [SRC-1AE03B9EC3-L005139](../../agents/web_agent.py#L5139) | 5139 | `"                \"platform_counts\": {},"` | — |
| [SRC-1AE03B9EC3-L005140](../../agents/web_agent.py#L5140) | 5140 | `"                \"social_direct_results\": None,"` | — |
| [SRC-1AE03B9EC3-L005141](../../agents/web_agent.py#L5141) | 5141 | `"                \"provider_diagnostics\": failure_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L005142](../../agents/web_agent.py#L5142) | 5142 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005143](../../agents/web_agent.py#L5143) | 5143 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005144](../../agents/web_agent.py#L5144) | 5144 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005145](../../agents/web_agent.py#L5145) | 5145 | `"                \"evidence_signals\": evidence_signal_report([], plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L005146](../../agents/web_agent.py#L5146) | 5146 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005147](../../agents/web_agent.py#L5147) | 5147 | `"        if isinstance(report, dict):"` | — |
| [SRC-1AE03B9EC3-L005148](../../agents/web_agent.py#L5148) | 5148 | `"            report[\"dialogue_context\"] = plan.get(\"dialogue_context\", {})"` | — |
| [SRC-1AE03B9EC3-L005149](../../agents/web_agent.py#L5149) | 5149 | `"            report[\"task_understanding\"] = {"` | — |
| [SRC-1AE03B9EC3-L005150](../../agents/web_agent.py#L5150) | 5150 | `"                \"task_spec\": task_spec,"` | — |
| [SRC-1AE03B9EC3-L005151](../../agents/web_agent.py#L5151) | 5151 | `"                \"query_strategy_matrix\": plan.get(\"query_strategy_matrix\", []),"` | — |
| [SRC-1AE03B9EC3-L005152](../../agents/web_agent.py#L5152) | 5152 | `"                \"actual_queries\": list(plan.get(\"queries\") or []),"` | — |
| [SRC-1AE03B9EC3-L005153](../../agents/web_agent.py#L5153) | 5153 | `"                \"actual_query_count\": len(plan.get(\"queries\") or []),"` | — |
| [SRC-1AE03B9EC3-L005154](../../agents/web_agent.py#L5154) | 5154 | `"                \"max_query_count\": MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L005155](../../agents/web_agent.py#L5155) | 5155 | `"                \"status\": \"deterministic_interpretation_attached\","` | — |
| [SRC-1AE03B9EC3-L005156](../../agents/web_agent.py#L5156) | 5156 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005157](../../agents/web_agent.py#L5157) | 5157 | `"        # Final relevance check is intentionally repeated after fusion, before any answer LLM call."` | — |
| [SRC-1AE03B9EC3-L005158](../../agents/web_agent.py#L5158) | 5158 | `"        filtered_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L005159](../../agents/web_agent.py#L5159) | 5159 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L005160](../../agents/web_agent.py#L5160) | 5160 | `"            if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L005161](../../agents/web_agent.py#L5161) | 5161 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L005162](../../agents/web_agent.py#L5162) | 5162 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L005163](../../agents/web_agent.py#L5163) | 5163 | `"            candidate_queries = ("` | — |
| [SRC-1AE03B9EC3-L005164](../../agents/web_agent.py#L5164) | 5164 | `"                source.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L005165](../../agents/web_agent.py#L5165) | 5165 | `"                or plan.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L005166](../../agents/web_agent.py#L5166) | 5166 | `"                or [compact_search_query(working_question)]"` | — |
| [SRC-1AE03B9EC3-L005167](../../agents/web_agent.py#L5167) | 5167 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005168](../../agents/web_agent.py#L5168) | 5168 | `"            if any(self._source_matches_query(str(q), source) for q in candidate_queries):"` | — |
| [SRC-1AE03B9EC3-L005169](../../agents/web_agent.py#L5169) | 5169 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L005170](../../agents/web_agent.py#L5170) | 5170 | `"        sources = filtered_sources"` | — |
| [SRC-1AE03B9EC3-L005171](../../agents/web_agent.py#L5171) | 5171 | `"        sources, initial_source_guardrails = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L005172](../../agents/web_agent.py#L5172) | 5172 | `"            working_question, clean_mode, plan, sources"` | — |
| [SRC-1AE03B9EC3-L005173](../../agents/web_agent.py#L5173) | 5173 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005174](../../agents/web_agent.py#L5174) | 5174 | `"        report[\"research_pipeline\"] = {"` | — |
| [SRC-1AE03B9EC3-L005175](../../agents/web_agent.py#L5175) | 5175 | `"            \"aspects\": pipeline[\"aspects\"],"` | — |
| [SRC-1AE03B9EC3-L005176](../../agents/web_agent.py#L5176) | 5176 | `"            \"evidence\": evaluate_research_evidence(pipeline[\"aspects\"], sources),"` | — |
| [SRC-1AE03B9EC3-L005177](../../agents/web_agent.py#L5177) | 5177 | `"            \"stages\": pipeline[\"stages\"],"` | — |
| [SRC-1AE03B9EC3-L005178](../../agents/web_agent.py#L5178) | 5178 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005179](../../agents/web_agent.py#L5179) | 5179 | `"        report[\"source_guardrails\"] = {"` | — |
| [SRC-1AE03B9EC3-L005180](../../agents/web_agent.py#L5180) | 5180 | `"            \"initial\": initial_source_guardrails,"` | — |
| [SRC-1AE03B9EC3-L005181](../../agents/web_agent.py#L5181) | 5181 | `"            \"initial_eligible_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L005182](../../agents/web_agent.py#L5182) | 5182 | `"            \"final\": None,"` | — |
| [SRC-1AE03B9EC3-L005183](../../agents/web_agent.py#L5183) | 5183 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005184](../../agents/web_agent.py#L5184) | 5184 | `"        if initial_source_guardrails[\"rejected_sources\"]:"` | — |
| [SRC-1AE03B9EC3-L005185](../../agents/web_agent.py#L5185) | 5185 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005186](../../agents/web_agent.py#L5186) | 5186 | `"                \"استُبعدت نتائج لا تستوفي شروط قبول المصدر الخاصة بهذا الطلب؛ \""` | — |
| [SRC-1AE03B9EC3-L005187](../../agents/web_agent.py#L5187) | 5187 | `"                \"راجع تشخيص حواجز الأدلة لمعرفة الأسباب.\""` | — |
| [SRC-1AE03B9EC3-L005188](../../agents/web_agent.py#L5188) | 5188 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005189](../../agents/web_agent.py#L5189) | 5189 | `"        search_warning = \"؛ \".join(search_warnings) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005190](../../agents/web_agent.py#L5190) | 5190 | `"        independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005191](../../agents/web_agent.py#L5191) | 5191 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005192](../../agents/web_agent.py#L5192) | 5192 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005193](../../agents/web_agent.py#L5193) | 5193 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005194](../../agents/web_agent.py#L5194) | 5194 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L005195](../../agents/web_agent.py#L5195) | 5195 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005196](../../agents/web_agent.py#L5196) | 5196 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005197](../../agents/web_agent.py#L5197) | 5197 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005198](../../agents/web_agent.py#L5198) | 5198 | `"        independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005199](../../agents/web_agent.py#L5199) | 5199 | `"        # A user-requested page summary is a different task from open-ended research:"` | — |
| [SRC-1AE03B9EC3-L005200](../../agents/web_agent.py#L5200) | 5200 | `"        # one successfully extracted, explicitly supplied page can support a summary,"` | — |
| [SRC-1AE03B9EC3-L005201](../../agents/web_agent.py#L5201) | 5201 | `"        # but must never be presented as independently corroborated research."` | — |
| [SRC-1AE03B9EC3-L005202](../../agents/web_agent.py#L5202) | 5202 | `"        has_read_user_supplied_page = any("` | — |
| [SRC-1AE03B9EC3-L005203](../../agents/web_agent.py#L5203) | 5203 | `"            \"user_supplied_url\" in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005204](../../agents/web_agent.py#L5204) | 5204 | `"            and bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1AE03B9EC3-L005205](../../agents/web_agent.py#L5205) | 5205 | `"            and bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1AE03B9EC3-L005206](../../agents/web_agent.py#L5206) | 5206 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005207](../../agents/web_agent.py#L5207) | 5207 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005208](../../agents/web_agent.py#L5208) | 5208 | `"        single_source_page_summary = ("` | — |
| [SRC-1AE03B9EC3-L005209](../../agents/web_agent.py#L5209) | 5209 | `"            has_read_user_supplied_page"` | — |
| [SRC-1AE03B9EC3-L005210](../../agents/web_agent.py#L5210) | 5210 | `"            and len(sources) == 1"` | — |
| [SRC-1AE03B9EC3-L005211](../../agents/web_agent.py#L5211) | 5211 | `"            and len(independent_domains) == 1"` | — |
| [SRC-1AE03B9EC3-L005212](../../agents/web_agent.py#L5212) | 5212 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005213](../../agents/web_agent.py#L5213) | 5213 | `"        if single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005214](../../agents/web_agent.py#L5214) | 5214 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005215](../../agents/web_agent.py#L5215) | 5215 | `"                \"هذا ملخص للرابط الذي قدمته فقط؛ لم يتم تأكيد محتواه من مصدر مستقل آخر.\""` | — |
| [SRC-1AE03B9EC3-L005216](../../agents/web_agent.py#L5216) | 5216 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005217](../../agents/web_agent.py#L5217) | 5217 | `"            search_warning = \"؛ \".join(search_warnings)"` | — |
| [SRC-1AE03B9EC3-L005218](../../agents/web_agent.py#L5218) | 5218 | `"        # Link-finding and lead-discovery are actionable discovery tasks, not broad"` | — |
| [SRC-1AE03B9EC3-L005219](../../agents/web_agent.py#L5219) | 5219 | `"        # fact-checking. Keep useful candidates visible while explicitly labelling them"` | — |
| [SRC-1AE03B9EC3-L005220](../../agents/web_agent.py#L5220) | 5220 | `"        # as uncorroborated instead of refusing a lone result as if it were no result."` | — |
| [SRC-1AE03B9EC3-L005221](../../agents/web_agent.py#L5221) | 5221 | `"        navigation_request = self._is_navigation_request(working_question)"` | — |
| [SRC-1AE03B9EC3-L005222](../../agents/web_agent.py#L5222) | 5222 | `"        lead_request = intent_route == \"LEAD_GENERATION\" or self._is_lead_search(working_question)"` | — |
| [SRC-1AE03B9EC3-L005223](../../agents/web_agent.py#L5223) | 5223 | `"        listing_request = self._is_listing_discovery(working_question)"` | — |
| [SRC-1AE03B9EC3-L005224](../../agents/web_agent.py#L5224) | 5224 | `"        lead_evidence_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L005225](../../agents/web_agent.py#L5225) | 5225 | `"        related_lead_results_count = 0"` | — |
| [SRC-1AE03B9EC3-L005226](../../agents/web_agent.py#L5226) | 5226 | `"        if lead_request:"` | — |
| [SRC-1AE03B9EC3-L005227](../../agents/web_agent.py#L5227) | 5227 | `"            related_lead_results_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005228](../../agents/web_agent.py#L5228) | 5228 | `"            for source in sources:"` | — |
| [SRC-1AE03B9EC3-L005229](../../agents/web_agent.py#L5229) | 5229 | `"                signal = self._lead_intent_evidence(source)"` | — |
| [SRC-1AE03B9EC3-L005230](../../agents/web_agent.py#L5230) | 5230 | `"                if signal:"` | — |
| [SRC-1AE03B9EC3-L005231](../../agents/web_agent.py#L5231) | 5231 | `"                    source[\"lead_qualification\"] = \"public_buyer_intent_signal\""` | — |
| [SRC-1AE03B9EC3-L005232](../../agents/web_agent.py#L5232) | 5232 | `"                    source[\"lead_intent_evidence\"] = signal"` | — |
| [SRC-1AE03B9EC3-L005233](../../agents/web_agent.py#L5233) | 5233 | `"                    lead_evidence_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L005234](../../agents/web_agent.py#L5234) | 5234 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005235](../../agents/web_agent.py#L5235) | 5235 | `"                    source[\"lead_qualification\"] = \"related_result_not_lead\""` | — |
| [SRC-1AE03B9EC3-L005236](../../agents/web_agent.py#L5236) | 5236 | `"            lead_research_incomplete = ("` | — |
| [SRC-1AE03B9EC3-L005237](../../agents/web_agent.py#L5237) | 5237 | `"                not sources"` | — |
| [SRC-1AE03B9EC3-L005238](../../agents/web_agent.py#L5238) | 5238 | `"                and report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L005239](../../agents/web_agent.py#L5239) | 5239 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005240](../../agents/web_agent.py#L5240) | 5240 | `"            report[\"lead_generation\"] = {"` | — |
| [SRC-1AE03B9EC3-L005241](../../agents/web_agent.py#L5241) | 5241 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005242](../../agents/web_agent.py#L5242) | 5242 | `"                    \"research_incomplete\" if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L005243](../../agents/web_agent.py#L5243) | 5243 | `"                    else \"candidate_signals_found\" if lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L005244](../../agents/web_agent.py#L5244) | 5244 | `"                    else \"no_qualified_candidates_found\""` | — |
| [SRC-1AE03B9EC3-L005245](../../agents/web_agent.py#L5245) | 5245 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005246](../../agents/web_agent.py#L5246) | 5246 | `"                \"candidate_signal_count\": ("` | — |
| [SRC-1AE03B9EC3-L005247](../../agents/web_agent.py#L5247) | 5247 | `"                    None if lead_research_incomplete else len(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L005248](../../agents/web_agent.py#L5248) | 5248 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005249](../../agents/web_agent.py#L5249) | 5249 | `"                \"related_results_reviewed\": ("` | — |
| [SRC-1AE03B9EC3-L005250](../../agents/web_agent.py#L5250) | 5250 | `"                    None if lead_research_incomplete else related_lead_results_count"` | — |
| [SRC-1AE03B9EC3-L005251](../../agents/web_agent.py#L5251) | 5251 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005252](../../agents/web_agent.py#L5252) | 5252 | `"                \"qualification_rule\": \"explicit_public_buyer_intent_phrase\","` | — |
| [SRC-1AE03B9EC3-L005253](../../agents/web_agent.py#L5253) | 5253 | `"                \"identity_verified\": False,"` | — |
| [SRC-1AE03B9EC3-L005254](../../agents/web_agent.py#L5254) | 5254 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005255](../../agents/web_agent.py#L5255) | 5255 | `"            if not lead_evidence_sources:"` | — |
| [SRC-1AE03B9EC3-L005256](../../agents/web_agent.py#L5256) | 5256 | `"                if sources:"` | — |
| [SRC-1AE03B9EC3-L005257](../../agents/web_agent.py#L5257) | 5257 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L005258](../../agents/web_agent.py#L5258) | 5258 | `"                        \"لم أعثر على إشارة نصية واضحة تثبت أن أي نتيجة في هذه الجولة تتعلق بشخص \""` | — |
| [SRC-1AE03B9EC3-L005259](../../agents/web_agent.py#L5259) | 5259 | `"                        \"يريد الشراء. راجعت \""` | — |
| [SRC-1AE03B9EC3-L005260](../../agents/web_agent.py#L5260) | 5260 | `"                        + str(len(sources))"` | — |
| [SRC-1AE03B9EC3-L005261](../../agents/web_agent.py#L5261) | 5261 | `"                        + \" نتيجة مرتبطة بالموضوع، لكنني لم أعتبر إعلانات البيع أو صفحات السوق \""` | — |
| [SRC-1AE03B9EC3-L005262](../../agents/web_agent.py#L5262) | 5262 | `"                        \"عملاء محتملين. الروابط أدناه نتائج مرتبطة بالموضوع فقط وليست عملاء.\""` | — |
| [SRC-1AE03B9EC3-L005263](../../agents/web_agent.py#L5263) | 5263 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005264](../../agents/web_agent.py#L5264) | 5264 | `"                elif report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L005265](../../agents/web_agent.py#L5265) | 5265 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L005266](../../agents/web_agent.py#L5266) | 5266 | `"                        \"تعطل مسار البحث أو لم يمكن تأكيد اكتماله؛ لذلك لا أستطيع تحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L005267](../../agents/web_agent.py#L5267) | 5267 | `"                        \"كانت هناك نتائج تصلح كعملاء محتملين في هذه الجولة.\""` | — |
| [SRC-1AE03B9EC3-L005268](../../agents/web_agent.py#L5268) | 5268 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005269](../../agents/web_agent.py#L5269) | 5269 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005270](../../agents/web_agent.py#L5270) | 5270 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L005271](../../agents/web_agent.py#L5271) | 5271 | `"                        \"لم تظهر نتائج قابلة للاستخدام تثبت نية شراء في هذه الجولة. هذا لا يثبت \""` | — |
| [SRC-1AE03B9EC3-L005272](../../agents/web_agent.py#L5272) | 5272 | `"                        \"عدم وجود عملاء؛ بل يعني أن البحث الحالي لم يعثر على دليل كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L005273](../../agents/web_agent.py#L5273) | 5273 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005274](../../agents/web_agent.py#L5274) | 5274 | `"                report[\"research_quality\"] = \"failed\""` | — |
| [SRC-1AE03B9EC3-L005275](../../agents/web_agent.py#L5275) | 5275 | `"                # Distinguish zero qualified signals from unknown counts after an exception."` | — |
| [SRC-1AE03B9EC3-L005276](../../agents/web_agent.py#L5276) | 5276 | `"                report[\"usable_sources_after_filtering\"] = ("` | — |
| [SRC-1AE03B9EC3-L005277](../../agents/web_agent.py#L5277) | 5277 | `"                    None if lead_research_incomplete else len(sources)"` | — |
| [SRC-1AE03B9EC3-L005278](../../agents/web_agent.py#L5278) | 5278 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005279](../../agents/web_agent.py#L5279) | 5279 | `"                report[\"evidence_signals\"] = ("` | — |
| [SRC-1AE03B9EC3-L005280](../../agents/web_agent.py#L5280) | 5280 | `"                    None if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L005281](../../agents/web_agent.py#L5281) | 5281 | `"                    else evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L005282](../../agents/web_agent.py#L5282) | 5282 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005283](../../agents/web_agent.py#L5283) | 5283 | `"                public_related_sources = [{"` | — |
| [SRC-1AE03B9EC3-L005284](../../agents/web_agent.py#L5284) | 5284 | `"                    \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005285](../../agents/web_agent.py#L5285) | 5285 | `"                    \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005286](../../agents/web_agent.py#L5286) | 5286 | `"                    \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005287](../../agents/web_agent.py#L5287) | 5287 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005288](../../agents/web_agent.py#L5288) | 5288 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L005289](../../agents/web_agent.py#L5289) | 5289 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005290](../../agents/web_agent.py#L5290) | 5290 | `"                    \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005291](../../agents/web_agent.py#L5291) | 5291 | `"                    \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005292](../../agents/web_agent.py#L5292) | 5292 | `"                    \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005293](../../agents/web_agent.py#L5293) | 5293 | `"                    \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005294](../../agents/web_agent.py#L5294) | 5294 | `"                    \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005295](../../agents/web_agent.py#L5295) | 5295 | `"                    \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005296](../../agents/web_agent.py#L5296) | 5296 | `"                    \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005297](../../agents/web_agent.py#L5297) | 5297 | `"                    \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005298](../../agents/web_agent.py#L5298) | 5298 | `"                    \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
