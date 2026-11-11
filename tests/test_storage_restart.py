from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from agents.omarai import LeadStore


def test_sqlite_records_survive_a_new_python_process(tmp_path):
    database_path = tmp_path / "omarai.sqlite3"
    marker = "sqlite-restart-" + tmp_path.name
    store = LeadStore(database_path)
    tenant_id = store.create_tenant(f"SQLite restart {marker}", marker)
    user_id = store.create_user(f"{marker}@example.invalid", f"SQLite {marker}")
    store.add_membership(tenant_id, user_id, "owner")

    lead, created = store.add(
        f"نحتاج موردًا لنظام إنذار حريق {marker}",
        f"https://example.invalid/demand/{marker}",
        tenant_id=tenant_id,
    )
    assert created is True
    profile = store.save_product_profile(
        {
            "product": {"name": f"Fire alarm {marker}", "aliases": ["FACP"]},
            "market": {"locations": ["Cairo"], "industries": ["Manufacturing"]},
        },
        tenant_id=tenant_id,
    )
    run = store.save_discovery_run(
        profile["id"],
        {
            "answer": "تم حفظ عملية اكتشاف اختبارية.",
            "kind": "lead_discovery",
            "search_queries": ["نحتاج موردًا لنظام إنذار حريق"],
            "sources": [{
                "title": "طلب توريد اختباري",
                "url": f"https://example.invalid/source/{marker}",
                "snippet": "نحتاج موردًا لنظام إنذار حريق",
                "lead_qualification": "public_demand_signal",
                "lead_intent_evidence": {
                    "phrase": "نحتاج موردًا",
                    "basis": "source_text",
                    "signal_type": "direct_purchase_request",
                },
            }],
            "search_report": {"search_outcome": "results_found"},
        },
        tenant_id=tenant_id,
    )

    child_code = """
import json
import sys
from agents.omarai import LeadStore
store = LeadStore(sys.argv[1])
tenant_id = sys.argv[2]
print(json.dumps({
    "lead_ids": [row["id"] for row in store.list(tenant_id=tenant_id)],
    "profile_ids": [row["id"] for row in store.list_product_profiles(tenant_id=tenant_id)],
    "run_ids": [row["id"] for row in store.list_discovery_runs(tenant_id=tenant_id)],
}))
"""
    repository_root = Path(__file__).resolve().parents[1]
    completed = subprocess.run(
        [sys.executable, "-c", child_code, str(database_path), tenant_id],
        cwd=repository_root,
        check=True,
        capture_output=True,
        text=True,
    )
    persisted = json.loads(completed.stdout)

    assert persisted["lead_ids"] == [lead["id"]]
    assert persisted["profile_ids"] == [profile["id"]]
    assert persisted["run_ids"] == [run["id"]]
