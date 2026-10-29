from __future__ import annotations

import json

from agents.web_agent import WebAgent, _normalized_provider_usage


def test_provider_usage_keeps_only_valid_numeric_fields_and_openrouter_usd_cost():
    usage = {
        "prompt_tokens": 18,
        "completion_tokens": 24,
        "total_tokens": 42,
        "cost": 0.00125,
        "provider_private_payload": "must not be retained",
        "prompt_tokens_text": "18",
    }
    normalized = _normalized_provider_usage(
        usage, provider_base_url="https://openrouter.ai/api/v1"
    )
    assert normalized == {
        "prompt_tokens": 18,
        "completion_tokens": 24,
        "total_tokens": 42,
        "cost_usd": 0.00125,
    }


def test_generic_provider_cost_is_not_assumed_to_be_usd():
    normalized = _normalized_provider_usage(
        {"prompt_tokens": 5, "cost": 0.05},
        provider_base_url="https://custom-provider.example/v1",
    )
    assert normalized == {"prompt_tokens": 5}


def test_nonfinite_or_negative_provider_cost_is_not_recorded():
    normalized = _normalized_provider_usage(
        {"prompt_tokens": 2, "cost": float("nan"), "total_cost": -1},
        provider_base_url="https://openrouter.ai/api/v1",
    )
    assert normalized == {"prompt_tokens": 2}


def test_completion_records_provider_usage_without_retaining_provider_body(monkeypatch):
    agent = WebAgent()
    agent.api_key = "unit-test-key"
    agent.base_url = "https://openrouter.ai/api/v1"
    agent.fallback_model = ""

    class FakeResponse:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, traceback):
            return False

        def read(self, limit):
            return json.dumps({
                "choices": [{
                    "message": {"content": "إجابة اختبارية"},
                    "finish_reason": "stop",
                }],
                "usage": {
                    "prompt_tokens": 10,
                    "completion_tokens": 7,
                    "total_tokens": 17,
                    "cost": 0.0004,
                    "debug_blob": "private-provider-details",
                },
            }).encode("utf-8")

    monkeypatch.setattr("agents.web_agent.urllib.request.urlopen", lambda request, timeout: FakeResponse())
    answer = agent._request_completion(
        [{"role": "user", "content": "اختبر"}],
        model="test/model",
    )
    assert answer == "إجابة اختبارية"
    assert agent.model_usage[0]["provider_usage"] == {
        "prompt_tokens": 10,
        "completion_tokens": 7,
        "total_tokens": 17,
        "cost_usd": 0.0004,
    }
    assert "debug_blob" not in str(agent.model_usage)
