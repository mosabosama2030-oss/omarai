from pathlib import Path


def test_discovery_ui_keeps_completed_result_when_history_refresh_fails():
    source = (Path(__file__).parents[1] / "web" / "workspace.html").read_text(
        encoding="utf-8"
    )
    handler_start = source.index('const run=action("بدء اكتشاف الطلب"')
    handler_end = source.index('  run.disabled=!canWrite();', handler_start)
    handler = source[handler_start:handler_end]

    # A completed discovery is authoritative even if the secondary history
    # refresh fails. Keep the result in state and render it for the user.
    assert handler.index("state.activeDiscovery=completed;") < handler.index(
        "try{await loadDiscoveryRuns()}catch(error){historyError=error}"
    )
    assert "renderDiscovery();" in handler
    assert "اكتمل الاكتشاف وحُفظت نتيجته" in handler


def test_discovery_ui_replaces_loading_state_on_failure_and_offers_retry():
    source = (Path(__file__).parents[1] / "web" / "workspace.html").read_text(
        encoding="utf-8"
    )
    handler_start = source.index('const run=action("بدء اكتشاف الطلب"')
    handler_end = source.index('  run.disabled=!canWrite();', handler_start)
    handler = source[handler_start:handler_end]

    assert 'root.replaceChildren(controls,status);' in handler
    assert 'status.replaceWith(emptyState("تعذر إكمال الاكتشاف"' in handler
    assert 'action("إعادة المحاولة","primary",()=>run.click())' in handler
    assert "finally{run.disabled=false}" in handler
