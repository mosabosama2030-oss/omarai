from __future__ import annotations

import json

import pytest

from agents.web_agent import WebAgent


class FakeResponse:
    def __init__(self, content: str, finish_reason: str | None = None, *, include_reason: bool = True):
        choice = {"message": {"content": content}}
        if include_reason:
            choice["finish_reason"] = finish_reason
        self.body = json.dumps({"choices": [choice]}).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self, limit: int) -> bytes:
        return self.body[:limit]


def test_missing_finish_reason_is_rejected_and_bounded_fallback_is_used(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    agent.fallback_model = "backup/model"
    calls: list[str] = []

    def fake_urlopen(request, timeout):
        model = json.loads(request.data.decode("utf-8"))["model"]
        calls.append(model)
        if model == "primary/model":
            return FakeResponse("possibly incomplete response", include_reason=False)
        return FakeResponse("إجابة مكتملة من النموذج الاحتياطي", "stop")

    monkeypatch.setattr("agents.web_agent.urllib.request.urlopen", fake_urlopen)

    answer = agent._request_completion(
        [{"role": "user", "content": "اختبار"}],
        model="primary/model",
    )

    assert answer == "إجابة مكتملة من النموذج الاحتياطي"
    assert calls == ["primary/model", "backup/model"]
    assert [item["status"] for item in agent.generation_diagnostics] == [
        "finish_reason_missing",
        "accepted",
    ]
    assert agent.generation_diagnostics[0]["attempted_model"] == "primary/model"
    assert agent.generation_diagnostics[1]["attempted_model"] == "backup/model"


def test_unknown_finish_reason_is_rejected_and_fallback_is_used(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    agent.fallback_model = "backup/model"
    calls: list[str] = []

    def fake_urlopen(request, timeout):
        model = json.loads(request.data.decode("utf-8"))["model"]
        calls.append(model)
        if model == "primary/model":
            return FakeResponse("response with unrecognized termination", "vendor_specific_done")
        return FakeResponse("إجابة مكتملة", "stop")

    monkeypatch.setattr("agents.web_agent.urllib.request.urlopen", fake_urlopen)

    answer = agent._request_completion(
        [{"role": "user", "content": "اختبار"}],
        model="primary/model",
    )

    assert answer == "إجابة مكتملة"
    assert calls == ["primary/model", "backup/model"]
    assert agent.generation_diagnostics[0]["status"] == "finish_reason_not_accepted"
    assert agent.generation_diagnostics[0]["finish_reason"] == "vendor_specific_done"


def test_missing_finish_reason_from_all_models_fails_closed(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    agent.fallback_model = ""
    calls: list[str] = []

    def fake_urlopen(request, timeout):
        calls.append(json.loads(request.data.decode("utf-8"))["model"])
        return FakeResponse("may be incomplete", include_reason=False)

    monkeypatch.setattr("agents.web_agent.urllib.request.urlopen", fake_urlopen)

    with pytest.raises(RuntimeError, match="سبب انتهاء واضحًا"):
        agent._request_completion(
            [{"role": "user", "content": "اختبار"}],
            model="primary/model",
        )

    assert calls == ["primary/model"]
    assert agent.model_usage == []
    assert agent.generation_diagnostics == [{
        "requested_model": "primary/model",
        "attempted_model": "primary/model",
        "status": "finish_reason_missing",
    }]


def test_capability_question_distinguishes_configuration_from_live_health(monkeypatch):
    agent = WebAgent()

    monkeypatch.setattr(
        agent,
        "_collect_research",
        lambda plan: pytest.fail("Capability questions must not run live search"),
    )

    result = agent.answer("هل تستطيع البحث على الانترنت؟")

    assert result["kind"] == "capability_answer"
    assert result["search_attempted"] is False
    assert result["used_web_search"] is False
    capability = result["capability_status"]["web_search"]
    assert capability["implemented"] is True
    assert capability["runtime_status"] == "not_tested_in_this_response"
    assert capability["local_dependencies_ready"] is True
    assert "لم أنفّذ اختبار اتصال حي" in result["answer"]
    assert "DuckDuckGo HTML" in result["answer"]


@pytest.mark.parametrize("mode", ["auto", "deep", "latest", "social"])
def test_current_request_search_status_is_not_confused_with_capability(monkeypatch, mode):
    agent = WebAgent()
    monkeypatch.setattr(
        agent,
        "_collect_research",
        lambda plan: pytest.fail("This asks about the current response, not a web lookup"),
    )

    result = agent.answer("هل بحثت في الانترنت للاجابة الحالية؟", mode=mode)

    assert result["kind"] == "capability_answer"
    assert result["request_execution_status"] == {
        "search_attempted": False,
        "search_outcome": "not_attempted",
        "semantics": "status_of_this_request_only",
    }
    assert "لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا" in result["answer"]
    assert result["capability_status"]["web_search"]["runtime_status"] == (
        "not_tested_in_this_response"
    )
    assert result["search_attempted"] is False
