from __future__ import annotations

import json
from urllib.error import HTTPError

from agents.web_agent import WebAgent


class FakeCompletionResponse:
    def __init__(self, answer: str):
        self.answer = answer

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self, _limit):
        return json.dumps({
            "choices": [{
                "message": {"content": self.answer},
                "finish_reason": "stop",
            }]
        }).encode("utf-8")


def _clear_model_environment(monkeypatch):
    for name in (
        "OMARAI_LLM_API_KEY",
        "OPENROUTER_API_KEY",
        "OMARAI_LLM_BASE_URL",
        "OMARAI_LLM_MODEL",
        "OMARAI_ANSWER_MODEL",
        "OMARAI_PLANNER_MODEL",
        "OMARAI_REVIEW_MODEL",
        "OMARAI_VERIFIER_MODEL",
        "OMARAI_LLM_FALLBACK_MODEL",
        "GEMINI_API_KEY",
        "OMARAI_GEMINI_MODEL",
        "MISTRAL_API_KEY",
        "OMARAI_MISTRAL_MODEL",
        "OMARAI_OPENROUTER_WEB_SEARCH",
    ):
        monkeypatch.delenv(name, raising=False)


def test_model_provider_configuration_uses_documented_model_defaults(monkeypatch):
    _clear_model_environment(monkeypatch)
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-openrouter-secret")
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-secret")
    monkeypatch.setenv("MISTRAL_API_KEY", "test-mistral-secret")

    agent = WebAgent()
    status = WebAgent.status()

    assert [provider["name"] for provider in agent.model_providers] == [
        "openrouter", "gemini", "mistral"
    ]
    assert agent.model_providers[1]["model"] == "gemini-3.1-flash-lite"
    assert agent.model_providers[2]["model"] == "mistral-small-latest"
    assert [provider["name"] for provider in status["model_providers"]] == [
        "openrouter", "gemini", "mistral"
    ]
    assert "test-openrouter-secret" not in repr(status)
    assert "test-gemini-secret" not in repr(status)
    assert "test-mistral-secret" not in repr(status)


def test_gemini_only_configuration_uses_gemini_models_without_openrouter_fallback(monkeypatch):
    _clear_model_environment(monkeypatch)
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-secret")

    agent = WebAgent()
    status = WebAgent.status()

    assert agent.primary_provider == "gemini"
    assert agent.base_url == "https://generativelanguage.googleapis.com/v1beta/openai"
    assert agent.answer_model == "gemini-3.1-flash-lite"
    assert agent.planner_model == agent.answer_model
    assert agent.verifier_model == agent.answer_model
    assert agent.fallback_model == ""
    assert status["language_model_configured"] is True
    assert status["semantic_verifier_distinct_from_answer_model"] is False


def test_model_provider_failover_uses_gemini_after_primary_failure(monkeypatch):
    _clear_model_environment(monkeypatch)
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-openrouter-key")
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-key")
    agent = WebAgent()
    calls = []

    def fake_open(request, timeout):
        model = json.loads(request.data.decode("utf-8"))["model"]
        calls.append((request.full_url, model, request.get_header("Authorization")))
        if "openrouter.ai" in request.full_url:
            raise HTTPError(request.full_url, 503, "temporary", None, None)
        return FakeCompletionResponse("إجابة Gemini مكتملة")

    monkeypatch.setattr("agents.web_agent._open_model_request", fake_open)
    answer = agent._request_completion(
        [{"role": "user", "content": "اختبار"}], model=agent.answer_model
    )

    assert answer == "إجابة Gemini مكتملة"
    assert [call[1] for call in calls] == [
        "google/gemma-4-31b-it:free",
        "openrouter/free",
        "gemini-3.1-flash-lite",
    ]
    assert calls[-1][0] == (
        "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
    )
    assert calls[-1][2] == "Bearer test-gemini-key"
    assert agent.model_usage[-1]["used_model"] == "gemini-3.1-flash-lite"


def test_model_provider_failover_reaches_mistral_after_gemini_failure(monkeypatch):
    _clear_model_environment(monkeypatch)
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-openrouter-key")
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-key")
    monkeypatch.setenv("MISTRAL_API_KEY", "test-mistral-key")
    agent = WebAgent()
    calls = []

    def fake_open(request, timeout):
        model = json.loads(request.data.decode("utf-8"))["model"]
        calls.append((request.full_url, model, request.get_header("Authorization")))
        if "mistral.ai" not in request.full_url:
            raise HTTPError(request.full_url, 503, "temporary", None, None)
        return FakeCompletionResponse("إجابة Mistral مكتملة")

    monkeypatch.setattr("agents.web_agent._open_model_request", fake_open)
    answer = agent._request_completion(
        [{"role": "user", "content": "اختبار"}], model=agent.answer_model
    )

    assert answer == "إجابة Mistral مكتملة"
    assert [call[1] for call in calls] == [
        "google/gemma-4-31b-it:free",
        "openrouter/free",
        "gemini-3.1-flash-lite",
        "mistral-small-latest",
    ]
    assert calls[-1][0] == "https://api.mistral.ai/v1/chat/completions"
    assert calls[-1][2] == "Bearer test-mistral-key"
    assert agent.model_usage[-1]["used_model"] == "mistral-small-latest"


def test_semantic_verifier_request_does_not_fail_over_to_another_provider(monkeypatch):
    _clear_model_environment(monkeypatch)
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-openrouter-key")
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-key")
    agent = WebAgent()
    calls = []

    def fake_open(request, timeout):
        calls.append(request.full_url)
        raise HTTPError(request.full_url, 401, "unauthorized", None, None)

    monkeypatch.setattr("agents.web_agent._open_model_request", fake_open)
    try:
        agent._request_completion(
            [{"role": "user", "content": "claim verification"}],
            model=agent.verifier_model,
            allow_fallback=False,
        )
    except RuntimeError as exc:
        assert "HTTP 401" in str(exc)
    else:
        raise AssertionError("semantic verifier unexpectedly accepted a failed provider request")

    assert calls == ["https://openrouter.ai/api/v1/chat/completions"]


def test_openrouter_web_search_tool_is_not_sent_to_fallback_provider(monkeypatch):
    _clear_model_environment(monkeypatch)
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-openrouter-key")
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-key")
    monkeypatch.setenv("OMARAI_OPENROUTER_WEB_SEARCH", "1")
    agent = WebAgent()
    observed = []

    def fake_open(request, timeout):
        payload = json.loads(request.data.decode("utf-8"))
        observed.append((request.full_url, payload))
        if "openrouter.ai" in request.full_url:
            raise HTTPError(request.full_url, 503, "temporary", None, None)
        return FakeCompletionResponse("إجابة احتياطية")

    monkeypatch.setattr("agents.web_agent._open_model_request", fake_open)
    answer = agent._request_completion(
        [{"role": "user", "content": "ابحث"}],
        model=agent.answer_model,
        enable_web_search=True,
    )

    assert answer == "إجابة احتياطية"
    assert observed[0][0].startswith("https://openrouter.ai/")
    assert observed[0][1]["tools"][0]["type"] == "openrouter:web_search"
    assert observed[-1][0].startswith("https://generativelanguage.googleapis.com/")
    assert "tools" not in observed[-1][1]
