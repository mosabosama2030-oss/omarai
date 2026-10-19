"""Unit tests for Omarai's per-request resource budget."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import pytest

from agents.request_budget import RequestBudget, RequestBudgetExceeded


class FakeClock:
    def __init__(self, value: float = 100.0) -> None:
        self.value = value

    def __call__(self) -> float:
        return self.value


def test_resource_reservations_are_bounded_and_thread_safe_in_snapshot():
    clock = FakeClock()
    budget = RequestBudget(
        timeout_seconds=10,
        limits={"search_calls": 1},
        clock=clock,
    )

    budget.reserve("search_calls")
    with pytest.raises(RequestBudgetExceeded, match="search_calls"):
        budget.reserve("search_calls")

    snapshot = budget.snapshot()
    assert snapshot["counts"]["search_calls"] == 1
    assert snapshot["limits"]["search_calls"] == 1
    assert snapshot["deadline_exceeded"] is False


def test_deadline_blocks_new_work_and_caps_outbound_timeout():
    clock = FakeClock()
    budget = RequestBudget(timeout_seconds=10, clock=clock)

    clock.value += 7
    assert budget.timeout_for(30) == pytest.approx(3)
    assert budget.timeout_for(1) == pytest.approx(1)

    clock.value += 4
    assert budget.remaining_seconds() == 0
    with pytest.raises(RequestBudgetExceeded, match="وقت الطلب"):
        budget.reserve("model_calls")
    with pytest.raises(RequestBudgetExceeded, match="وقت الطلب"):
        budget.timeout_for(3)


def test_environment_overrides_are_clamped(monkeypatch):
    monkeypatch.setenv("OMARAI_REQUEST_BUDGET_SECONDS", "999")
    monkeypatch.setenv("OMARAI_REQUEST_MAX_SEARCH_CALLS", "999")
    monkeypatch.setenv("OMARAI_REQUEST_MAX_MODEL_CALLS", "-1")
    monkeypatch.setenv("OMARAI_REQUEST_MAX_TOOL_CALLS", "-1")

    snapshot = RequestBudget.from_environment().snapshot()

    assert snapshot["timeout_seconds"] == 120
    assert snapshot["limits"]["search_calls"] == 40
    assert snapshot["limits"]["model_calls"] == 1
    assert snapshot["limits"]["tool_calls"] == 0


def test_web_agent_reserves_search_model_and_page_work_before_io(monkeypatch):
    from agents.web_agent import WebAgent

    agent = WebAgent()
    agent.api_key = "test-key"

    agent._request_budget = RequestBudget(limits={"search_queries": 0})
    with pytest.raises(RequestBudgetExceeded, match="search_queries"):
        agent._search_web("budget test")

    agent._request_budget = RequestBudget(limits={"model_calls": 0})
    monkeypatch.setattr(
        "agents.web_agent.urllib.request.urlopen",
        lambda *args, **kwargs: pytest.fail("model HTTP request must not start"),
    )
    with pytest.raises(RequestBudgetExceeded, match="model_calls"):
        agent._request_completion([{"role": "user", "content": "test"}])

    agent._request_budget = RequestBudget(limits={"page_fetches": 0})
    with pytest.raises(RequestBudgetExceeded, match="page_fetches"):
        agent._fetch_page("https://example.com/")


def test_social_provider_reserves_budget_before_network_io(monkeypatch):
    from agents.web_agent import WebAgent

    monkeypatch.setenv("REDDIT_CLIENT_ID", "test-client")
    monkeypatch.setenv("REDDIT_CLIENT_SECRET", "test-secret")
    agent = WebAgent()
    agent._request_budget = RequestBudget(limits={"search_calls": 0})

    monkeypatch.setattr(
        "httpx.post",
        lambda *args, **kwargs: pytest.fail("social HTTP request must not start"),
    )
    with pytest.raises(RequestBudgetExceeded, match="search_calls"):
        agent._search_social("budget test", ["reddit"])

def test_concurrent_reservations_never_exceed_resource_limit():
    """Concurrent provider workers cannot reserve more calls than the request cap."""
    limit = 5
    workers = 32
    budget = RequestBudget(
        timeout_seconds=30,
        limits={"search_calls": limit},
    )

    def attempt_reservation() -> bool:
        try:
            budget.reserve("search_calls")
            return True
        except RequestBudgetExceeded:
            return False

    with ThreadPoolExecutor(max_workers=workers) as pool:
        outcomes = list(pool.map(lambda _index: attempt_reservation(), range(workers)))

    snapshot = budget.snapshot()
    assert sum(outcomes) == limit
    assert snapshot["counts"]["search_calls"] == limit
    assert snapshot["limits"]["search_calls"] == limit

