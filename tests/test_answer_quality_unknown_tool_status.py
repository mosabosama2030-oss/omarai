from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_answer_quality_benchmark.py"


def test_unknown_required_tool_status_is_not_complete():
    spec = importlib.util.spec_from_file_location("answer_quality_runner_status_test", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    metrics = module._response_metrics(
        {
            "task_understanding": {
                "tool_execution": {
                    "required_tools": ["web_search"],
                    "tool_status_matrix": [{
                        "tool": "web_search",
                        "required_by_task_spec": True,
                        "status": "completed_maybe",
                    }],
                },
            },
            "search_report": {"search_outcome": "attempted_with_usable_sources"},
            "sources": [{"url": "https://example.org"}],
        },
        expected_strategy="web_search",
        transport_ok=True,
    )
    assert metrics["required_tool_statuses"][0]["status_valid"] is False
    assert metrics["required_tool_matrix_complete"] is False
