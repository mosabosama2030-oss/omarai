"""Cooperative per-request resource budgets for Omarai's web-research pipeline.

The budget limits work that has not started yet and caps the timeout supplied to
each outbound operation by the remaining request window. Socket libraries may
still overrun a cooperative deadline slightly while unwinding an in-flight call;
this is not a hard real-time cancellation primitive.
"""
from __future__ import annotations

import os
import threading
import time
from collections.abc import Callable, Mapping
from typing import Any


class RequestBudgetExceeded(Exception):
    """Raised when a request cannot start more work within its resource budget."""


DEFAULT_TIMEOUT_SECONDS = 90
MAX_TIMEOUT_SECONDS = 120
RESOURCE_LIMITS = {
    "search_queries": (8, 8),
    "search_calls": (32, 40),
    "model_calls": (8, 12),
    "page_fetches": (8, 8),
    "tool_calls": (3, 3),
}


def _bounded_env_int(name: str, default: int, minimum: int, maximum: int) -> int:
    raw = os.getenv(name, "").strip()
    try:
        value = int(raw) if raw else default
    except (TypeError, ValueError):
        value = default
    return max(minimum, min(value, maximum))


class RequestBudget:
    """Thread-safe counters and a cooperative monotonic deadline for one answer."""

    def __init__(
        self,
        timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
        limits: Mapping[str, int] | None = None,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        self._clock = clock
        bounded_timeout = max(10, min(int(timeout_seconds), MAX_TIMEOUT_SECONDS))
        self.started_at = clock()
        self.deadline = self.started_at + bounded_timeout
        self._limits = {
            key: max(0, min(int(value), RESOURCE_LIMITS[key][1]))
            for key, (default, _maximum) in RESOURCE_LIMITS.items()
            for value in [limits[key] if limits and key in limits else default]
        }
        self._counts = {key: 0 for key in self._limits}
        self._lock = threading.Lock()

    @classmethod
    def from_environment(cls) -> "RequestBudget":
        timeout = _bounded_env_int(
            "OMARAI_REQUEST_BUDGET_SECONDS",
            DEFAULT_TIMEOUT_SECONDS,
            10,
            MAX_TIMEOUT_SECONDS,
        )
        limits = {
            key: _bounded_env_int(
                f"OMARAI_REQUEST_MAX_{key.upper()}",
                defaults[0],
                0 if key == "tool_calls" else 1,
                defaults[1],
            )
            for key, defaults in RESOURCE_LIMITS.items()
        }
        return cls(timeout_seconds=timeout, limits=limits)

    def remaining_seconds(self) -> float:
        return max(0.0, self.deadline - self._clock())

    def timeout_for(self, configured_seconds: float) -> float:
        """Cap one outbound timeout to time remaining; raise instead of starting at zero."""
        remaining = self.remaining_seconds()
        if remaining <= 0:
            raise RequestBudgetExceeded("انتهت ميزانية وقت الطلب.")
        return min(float(configured_seconds), remaining)

    def remaining_units(self, resource: str) -> int:
        """Return unused units for a resource; zero means disabled, exhausted, or expired."""
        if resource not in self._limits:
            raise ValueError(f"unknown request-budget resource: {resource}")
        if self.remaining_seconds() <= 0:
            return 0
        with self._lock:
            return max(0, self._limits[resource] - self._counts[resource])

    def reserve(self, resource: str, amount: int = 1) -> None:
        """Atomically reserve resource units before initiating external work."""
        if resource not in self._limits:
            raise ValueError(f"unknown request-budget resource: {resource}")
        if amount < 1:
            raise ValueError("reservation amount must be positive")
        with self._lock:
            if self.remaining_seconds() <= 0:
                raise RequestBudgetExceeded("انتهت ميزانية وقت الطلب.")
            limit = self._limits[resource]
            if self._counts[resource] + amount > limit:
                raise RequestBudgetExceeded(
                    f"تم بلوغ حد موارد الطلب: {resource}."
                )
            self._counts[resource] += amount

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            counts = dict(self._counts)
            limits = dict(self._limits)
        remaining = self.remaining_seconds()
        return {
            "policy": "cooperative_per_request_budget",
            "timeout_seconds": round(self.deadline - self.started_at, 3),
            "elapsed_seconds": round(max(0.0, self._clock() - self.started_at), 3),
            "remaining_seconds": round(remaining, 3),
            "deadline_exceeded": remaining <= 0,
            "counts": counts,
            "limits": limits,
            "resources_at_limit": [
                key for key, limit in limits.items() if limit > 0 and counts[key] >= limit
            ],
            "disabled_resources": [key for key, limit in limits.items() if limit == 0],
            "hard_cancellation_guaranteed": False,
        }
