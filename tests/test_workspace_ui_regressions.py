from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "web"


def inline_script(name: str) -> str:
    html = (ROOT / name).read_text(encoding="utf-8")
    scripts = re.findall(r"<script[^>]*>([\s\S]*?)</script\s*>", html, re.IGNORECASE)
    assert scripts, f"{name} must contain its application script"
    return "\n".join(scripts)


def function_source(script: str, name: str) -> str:
    match = re.search(
        rf"(?:async\s+)?function\s+{re.escape(name)}\s*\([^)]*\)\s*\{{",
        script,
    )
    assert match, f"function {name} must exist"
    next_function = re.search(
        r"\n(?:async\s+)?function\s+[A-Za-z_$]", script[match.end():]
    )
    end = match.end() + next_function.start() if next_function else len(script)
    return script[match.start():end]


def test_discovery_progress_clears_on_failure_and_history_refresh_is_non_fatal():
    script = inline_script("workspace.html")
    body = function_source(script, "renderDiscovery")

    assert 'setAttribute("role","status")' in body
    assert "progress.replaceWith" in body or "progress.remove()" in body
    assert re.search(
        r"try\s*\{\s*await\s+loadDiscoveryRuns\(\)\s*\}\s*catch",
        body,
    ), "history refresh failure must be isolated from successful discovery creation"
    assert "تم حفظ نتيجة الاكتشاف" in body, (
        "the UI must distinguish a saved discovery from a failed history refresh"
    )


def test_general_search_uses_bounded_fetch_and_restores_controls_after_timeout():
    script = inline_script("agent.html")
    body = function_source(script, "ask")

    assert "new AbortController()" in body
    assert "signal: controller.signal" in body
    assert re.search(r"setTimeout\s*\(.*controller\.abort", body, re.DOTALL)
    assert re.search(r"clearTimeout\s*\(", body)
    assert "AbortError" in body, "timeouts must have a clear Arabic recovery message"
    assert "setBusy(false)" in body, "search controls must be restored in finally"


def test_signal_inbox_refresh_button_shows_errors_instead_of_rejecting_silently():
    script = inline_script("workspace.html")
    body = function_source(script, "renderSignals")

    assert "const refresh=action(" in body
    assert "refresh.disabled=true" in body
    assert "تعذر تحديث إشارات الطلب" in body
    assert "catch(error)" in body


def test_signal_persistence_is_not_reported_as_failed_when_list_refresh_fails():
    script = inline_script("workspace.html")
    discovery_body = function_source(script, "renderDiscoveryRun")
    manual_body = function_source(script, "createSignalForm")

    assert "refreshWarning" in discovery_body
    assert "تم حفظ الإشارة" in discovery_body
    assert "refreshWarning" in manual_body
    assert "تم حفظ الإشارة" in manual_body
