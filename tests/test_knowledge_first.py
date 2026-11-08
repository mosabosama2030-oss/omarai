"""Offline tests for the knowledge-first-then-evidence stage (no network, no API)."""
import os

from agents.web_agent import WebAgent
from agents.request_budget import RequestBudgetExceeded


def _agent(answer="إجابة من المعرفة"):
    os.environ["OMARAI_KNOWLEDGE_FIRST"] = "1"
    agent = WebAgent()
    agent.api_key = "test-key"
    agent.calls = 0

    def fake(question, history):
        agent.calls += 1
        if answer is None:
            return None
        return {"answer": answer}

    agent._answer_without_search = fake
    return agent


def _web_result(**extra):
    base = {
        "kind": "web_research",
        "intent_route": "WEB_SIMPLE",
        "research_quality": "good",
        "answer": "إجابة بالأدلة [المصدر 1]",
        "sources": [{"url": "https://example.org/a", "title": "A"}],
    }
    base.update(extra)
    return base


def test_knowledge_answer_added_beside_evidence_answer():
    agent = _agent()
    result = _web_result()
    agent._attach_knowledge_first("ما هو X؟", [], result)
    assert result["knowledge_answer"] == "إجابة من المعرفة"
    assert result["answer"] == "إجابة بالأدلة [المصدر 1]"
    check = result["knowledge_check"]
    assert check["status"] == "evidence_gathered"
    assert check["label"] == "model_knowledge_unverified"
    assert check["reconciliation"] == "not_machine_compared"


def test_insufficient_evidence_is_flagged():
    agent = _agent()
    result = _web_result(kind="insufficient_evidence", sources=[])
    agent._attach_knowledge_first("ما هو X؟", [], result)
    assert result["knowledge_check"]["status"] == "no_sufficient_evidence"


def test_skips_non_web_routes_and_kinds():
    agent = _agent()
    for result in (
        _web_result(intent_route="MODEL_ONLY"),
        _web_result(kind="general_answer"),
        _web_result(kind="clarification"),
    ):
        agent._attach_knowledge_first("سؤال", [], result)
        assert "knowledge_answer" not in result
    assert agent.calls == 0


def test_env_switch_disables_stage():
    agent = _agent()
    os.environ["OMARAI_KNOWLEDGE_FIRST"] = "0"
    try:
        result = _web_result()
        agent._attach_knowledge_first("سؤال", [], result)
    finally:
        os.environ["OMARAI_KNOWLEDGE_FIRST"] = "0"
    assert "knowledge_answer" not in result
    assert agent.calls == 0


def test_failure_leaves_evidence_result_intact():
    agent = _agent(answer=None)
    result = _web_result()
    agent._attach_knowledge_first("سؤال", [], result)
    assert "knowledge_answer" not in result
    assert result["knowledge_check"]["status"] == "knowledge_answer_unavailable"
    assert result["answer"] == "إجابة بالأدلة [المصدر 1]"


def test_budget_exhaustion_is_swallowed():
    os.environ["OMARAI_KNOWLEDGE_FIRST"] = "1"
    agent = WebAgent()

    def boom(question, history):
        raise RequestBudgetExceeded("budget")

    agent._answer_without_search = boom
    result = _web_result()
    agent._attach_knowledge_first("سؤال", [], result)
    assert "knowledge_answer" not in result


def test_failed_knowledge_call_does_not_pollute_generation_diagnostics():
    agent = _agent()
    agent.generation_diagnostics = [{"status": "ok"}]

    def noisy(question, history):
        agent.generation_diagnostics.append({"status": "failed"})
        return None

    agent._answer_without_search = noisy
    agent._attach_knowledge_first("سؤال", [], _web_result())
    assert agent.generation_diagnostics == [{"status": "ok"}]
