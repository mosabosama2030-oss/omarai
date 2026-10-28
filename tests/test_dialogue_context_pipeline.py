from __future__ import annotations

import json
from typing import Any

import pytest

from agents.research import evidence_signal_report
from agents.dialogue_state import might_be_context_dependent
from agents.web_agent import WebAgent


def _source(domain: str, queries: list[str]) -> dict[str, Any]:
    return {
        "title": "iPhone 17 256GB international warranty coverage in Egypt",
        "url": f"https://{domain}/iphone-warranty",
        "snippet": "Warranty coverage and service policy for iPhone 17 in Egypt.",
        "page_text": "Warranty coverage and service policy for iPhone 17 in Egypt.",
        "page_fetched": True,
        "providers": ["test_search"],
        "queries": list(queries),
        "domain": domain,
        "source_class": "general",
        "platform": "web",
        "published_at": "",
        "rank_score": 1.0,
    }


def _report(plan: dict[str, Any], sources: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "queries_planned": len(plan.get("queries", [])),
        "queries_attempted": len(plan.get("queries", [])),
        "queries_attempted_known": True,
        "search_attempted": True,
        "search_outcome": "attempted_with_usable_sources",
        "query_results": [],
        "unique_sources": len(sources),
        "pages_fetched": len(sources),
        "providers_used": ["test_search"],
        "provider_counts": {"test_search": len(sources)},
        "platform_counts": {"web": len(sources)},
        "social_direct_results": 0,
        "depth": plan.get("depth", "standard"),
        "planning_method": plan.get("planning_method", "test"),
        "evidence_signals": evidence_signal_report(sources),
    }


def _semantic_context(*, needs_clarification: bool = False) -> dict[str, Any]:
    return {
        "resolved_question": (
            "هل الضمان الدولي لهاتف iPhone 17 سعة 256 جيجابايت الذي اشتريته "
            "في مصر يغطي الصيانة داخل مصر؟"
        ),
        "intent": "current_information",
        "topic": "تغطية الضمان",
        "entities": ["iPhone 17"],
        "slots": {
            "product": "iPhone 17",
            "capacity": "256 جيجابايت",
            "country": "مصر",
            "aspect": "الضمان الدولي والصيانة داخل مصر",
        },
        "changed_slots": ["aspect"],
        "is_follow_up": True,
        "topic_shift": False,
        "needs_web": True,
        "research_depth": "standard",
        "needs_clarification": needs_clarification,
        "clarification_question": (
            "تقصد ضمان أي هاتف تحديدًا، أم تريد مقارنة ضمان الهاتفين؟"
            if needs_clarification else ""
        ),
        "unresolved_references": ["الضمان"] if needs_clarification else [],
        "resolution_basis": "history_inferred",
        "confidence_band": "medium",
    }


def test_semantic_context_probe_routes_natural_followup_to_search_and_answer(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    agent = WebAgent()
    agent.api_key = "test-key"  # All model responses are mocked; no provider call is made.
    history = [
        {"role": "user", "content": "اشتريت iPhone 17 النسخة الأساسية سعة 256 جيجابايت من مصر."},
        {"role": "assistant", "content": "نتحدث عن نسخة iPhone 17 سعة 256 جيجابايت في مصر."},
    ]
    context = _semantic_context()
    seen: dict[str, Any] = {"model_prompts": []}

    def mocked_completion(messages, **kwargs):
        system_prompt = messages[0]["content"]
        seen["model_prompts"].append(system_prompt)
        if "أنت محلل سياق حواري" in system_prompt:
            return json.dumps(context, ensure_ascii=False)
        if "أنت مخطط بحث ومحلل دلالي حواري" in system_prompt:
            return json.dumps(
                {
                    "queries": [
                        "iPhone 17 256GB الضمان الدولي في مصر تغطية الصيانة warranty Egypt"
                    ],
                    "direct_urls": [],
                    "social_focus": False,
                    "freshness": "current",
                    "depth": "standard",
                    "platforms": [],
                    "dialogue_context": context,
                },
                ensure_ascii=False,
            )
        pytest.fail("Unexpected model prompt in mocked offline test")

    monkeypatch.setattr(agent, "_request_completion", mocked_completion)
    seen["generated_question"] = None
    seen["reviewed_question"] = None

    def collect(plan):
        seen["plan"] = dict(plan)
        sources = [_source("example.com", plan["queries"]), _source("example.net", plan["queries"])]
        return sources, [], _report(plan, sources)

    def generate(resolved_question, *args, **kwargs):
        seen["generated_question"] = resolved_question
        return "لم أؤكد شروط الضمان من النصوص المتاحة؛ راجع الشروط الرسمية [المصدر 1]."

    def review(resolved_question, answer, sources):
        seen["reviewed_question"] = resolved_question
        return answer

    monkeypatch.setattr(agent, "_collect_research", collect)
    monkeypatch.setattr(agent, "_source_matches_query", lambda _query, _source: True)
    monkeypatch.setattr(agent, "_generate", generate)
    monkeypatch.setattr(agent, "_review_answer", review)

    question = "وطب الضمان الدولي بيسري في مصر؟"
    result = agent.answer(question, history=history)

    assert result["intent_route"] == "WEB_SIMPLE"
    assert result["question"] == question  # Preserve the visible user utterance.
    assert result["used_web_search"] is True
    assert len(seen["model_prompts"]) == 2  # one context pass + one search-plan pass
    assert "iPhone 17" in seen["generated_question"]
    assert "256 جيجابايت" in seen["generated_question"]
    assert "الضمان الدولي" in seen["generated_question"]
    assert seen["reviewed_question"] == seen["generated_question"]
    context_result = result["research_plan"]["dialogue_context"]
    assert context_result["method"] == "llm_semantic_context"
    assert context_result["slots"]["country"] == "مصر"
    assert context_result["changed_slots"] == ["aspect"]
    assert context_result["needs_web"] is True


def test_semantic_context_asks_before_search_when_two_referents_are_plausible(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    agent = WebAgent()
    agent.api_key = "test-key"
    history = [
        {"role": "user", "content": "قارن بين iPhone 17 وSamsung S26"},
        {"role": "assistant", "content": "ذكرت الهاتفين في المقارنة."},
    ]
    ambiguous = {
        "resolved_question": "What about the second one?",
        "intent": "compare",
        "topic": "اختيار الهاتف",
        "entities": ["iPhone 17", "Samsung S26"],
        "slots": {"aspect": "الاختيار"},
        "changed_slots": [],
        "is_follow_up": True,
        "topic_shift": False,
        "needs_web": False,
        "research_depth": "standard",
        "needs_clarification": True,
        "clarification_question": "تقصد أي هاتف تحديدًا: iPhone 17 أم Samsung S26؟",
        "unresolved_references": ["the second one"],
        "resolution_basis": "insufficient_evidence",
        "confidence_band": "low",
    }

    def mocked_completion(messages, **kwargs):
        assert "أنت محلل سياق حواري" in messages[0]["content"]
        return json.dumps(ambiguous, ensure_ascii=False)

    def forbidden_search(*args, **kwargs):
        pytest.fail("An unresolved referent must not start web research.")

    monkeypatch.setattr(agent, "_request_completion", mocked_completion)
    monkeypatch.setattr(agent, "_collect_research", forbidden_search)

    result = agent.answer("What about the second one?", history=history)

    assert result["kind"] == "clarification_needed"
    assert result["intent_route"] == "CLARIFY"
    assert "iPhone 17" in result["answer"]
    assert "Samsung S26" in result["answer"]
    assert result["dialogue_context"]["needs_clarification"] is True
    assert result["used_web_search"] is False

def test_semantic_probe_catches_implicit_context_without_keyword_trigger(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    agent = WebAgent()
    agent.api_key = "test-key"
    question = "في وضعي، أبدأ بإيه؟"
    history = [
        {
            "role": "user",
            "content": (
                "عندي امتحان كيمياء بكرة، وفاضلي ساعتين أراجع الاتزان الكيميائي "
                "ومش فاهمه كويس."
            ),
        },
        {
            "role": "assistant",
            "content": "نقدر نرتب الساعتين لمراجعة المفاهيم والتدريب على المسائل.",
        },
    ]
    assert not might_be_context_dependent(question)

    semantic_context = {
        "resolved_question": (
            "في ظل امتحان الكيمياء غدًا ووجود ساعتين لمراجعة الاتزان الكيميائي، "
            "بماذا أبدأ؟"
        ),
        "intent": "how_to",
        "topic": "خطة مراجعة الاتزان الكيميائي",
        "entities": ["امتحان الكيمياء", "الاتزان الكيميائي"],
        "slots": {
            "goal": "مراجعة امتحان الكيمياء",
            "time_range": "ساعتان",
            "topic": "الاتزان الكيميائي",
        },
        "changed_slots": ["goal"],
        "is_follow_up": True,
        "topic_shift": False,
        "needs_web": False,
        "research_depth": "standard",
        "needs_clarification": False,
        "clarification_question": "",
        "unresolved_references": [],
        "resolution_basis": "history_inferred",
        "confidence_band": "medium",
    }
    seen: dict[str, Any] = {"context_calls": 0}

    def mocked_completion(messages, **kwargs):
        assert "أنت محلل سياق حواري" in messages[0]["content"]
        seen["context_calls"] += 1
        return json.dumps(semantic_context, ensure_ascii=False)

    def answer_without_search(resolved_question, prior_history):
        seen["resolved_question"] = resolved_question
        return {
            "answer": "ابدأ بمراجعة أساسيات الاتزان ثم حل أمثلة قصيرة.",
            "question": resolved_question,
            "search_query": resolved_question,
            "search_queries": [],
            "research_plan": {
                "mode": "auto",
                "planning_method": "general_qa_without_web",
                "web_search_skipped": True,
            },
            "sources": [],
            "used_language_model": True,
            "used_web_search": False,
            "search_attempted": False,
            "used_social_search": False,
            "warnings": [],
            "kind": "general_answer",
            "research_quality": "not_applicable",
            "model_calls": [],
        }

    def forbidden_search(*args, **kwargs):
        pytest.fail("This contextual study-plan question must not start web search.")

    monkeypatch.setattr(agent, "_request_completion", mocked_completion)
    monkeypatch.setattr(agent, "_answer_without_search", answer_without_search)
    monkeypatch.setattr(agent, "_collect_research", forbidden_search)

    result = agent.answer(question, history=history)

    assert seen["context_calls"] == 1
    assert "الكيمياء" in seen["resolved_question"]
    assert "ساعتين" in seen["resolved_question"]
    assert "الاتزان الكيميائي" in seen["resolved_question"]
    assert result["question"] == question
    assert result["dialogue_context"]["is_follow_up"] is True
    assert result["used_web_search"] is False
    assert result["search_attempted"] is False

