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


def test_workspace_api_forwards_optional_abort_signal_to_fetch():
    body = function_source(inline_script("workspace.html"), "api")
    assert re.search(r"signal\s*:\s*opts\.signal", body)


def test_workspace_chat_uses_bounded_abort_and_restores_chat_state():
    body = function_source(inline_script("workspace.html"), "sendChat")
    assert "new AbortController()" in body
    assert re.search(r"signal\s*:\s*controller\.signal", body)
    assert re.search(r"window\.setTimeout\s*\(.*controller\.abort", body, re.DOTALL)
    assert "window.clearTimeout(timeoutId)" in body
    assert "انتهى وقت انتظار الواجهة بعد 135 ثانية" in body
    assert "قد يواصل الخادم إنهاء العملية" in body
    assert "if(chat.busy)return" in body
    assert "chat.busy=false" in body


def test_legacy_agent_search_uses_bounded_abort_and_restores_controls():
    body = function_source(inline_script("agent.html"), "ask")
    assert "new AbortController()" in body
    assert re.search(r"signal\s*:\s*controller\.signal", body)
    assert re.search(r"window\.setTimeout\s*\(.*controller\.abort", body, re.DOTALL)
    assert "window.clearTimeout(timeoutId)" in body
    assert "انتهى وقت انتظار الواجهة بعد 135 ثانية" in body
    assert "قد يواصل الخادم إنهاء العملية" in body
    assert "setBusy(false)" in body


def test_signal_inbox_refresh_surfaces_errors_and_restores_button():
    body = function_source(inline_script("workspace.html"), "renderSignals")
    assert "refresh.disabled=true" in body
    assert "تعذر تحديث إشارات الطلب" in body
    assert "البيانات المعروضة هي آخر نسخة تم تحميلها" in body
    assert "catch(error)" in body
    assert "refresh.disabled=false" in body


def test_manual_signal_save_distinguishes_saved_from_refresh_failure():
    body = function_source(inline_script("workspace.html"), "createSignalForm")
    assert "refreshWarning" in body
    assert "تم حفظ الإشارة، لكن تعذر تحديث صندوق الإشارات" in body


def test_product_profile_save_distinguishes_saved_from_refresh_failure():
    body = function_source(inline_script("workspace.html"), "renderProductProfile")
    assert "refreshWarning" in body
    assert "تم حفظ ملف المنتج والسوق، لكن تعذر تحديث قائمة الملفات المحفوظة" in body


def test_discovery_signal_save_distinguishes_saved_from_refresh_failure():
    body = function_source(inline_script("workspace.html"), "renderDiscoveryRun")
    assert "refreshWarning" in body
    assert "تم حفظ الإشارة، لكن تعذر تحديث صندوق الإشارات" in body


def test_discovery_history_refresh_failure_keeps_the_saved_run_visible():
    body = function_source(inline_script("workspace.html"), "renderDiscovery")
    assert "state.activeDiscovery=savedRun" in body
    assert "refreshWarning" in body
    assert "تعذر تحديث سجل العمليات" in body
