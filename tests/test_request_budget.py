"""Unit tests for Omarai's per-request resource budget."""
from __future__ import annotations

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
