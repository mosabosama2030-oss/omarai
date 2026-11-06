from __future__ import annotations

import pytest

from agents.omarai import LeadStore
from agents.web_agent import WebAgent


def product_profile(name="لوحة إنذار الحريق", aliases=None):
    return {
        "product": {
            "name": name,
            "aliases": aliases or ["FACP"],
            "category_path": ["السلامة", "إنذار الحريق"],
            "use_cases": ["حماية المباني"],
            "problems_solved": ["اكتشاف الحريق مبكرًا"],
            "facts": [],
        },
        "market": {
            "locations": ["القاهرة", "الجيزة"],
            "industries": ["المقاولات"],
            "customer_types": ["مقاولون", "ملاك مشروعات"],
            "decision_roles": ["مدير مشتريات"],
            "exclusions": [],
        },
        "locale": "ar",
    }


def discovery_run():
    return {
        "answer": "عُثر على إشارة طلب واحدة.",
        "search_queries": ['"مطلوب شراء" "لوحة إنذار الحريق"'],
        "search_report": {
            "lead_generation": {
                "status": "candidate_signals_found",
                "candidate_signal_count": 1,
                "related_results_reviewed": 2,
                "qualification_rule": "public_demand_signal_phrase_by_type",
                "identity_verified": False,
            },
            "pipeline_completion_status": "completed",
        },
        "sources": [
            {
                "title": "طلب توريد لوحة إنذار",
                "url": "https://example.org/public-request/1",
                "snippet": "نبحث عن مورد لتوريد لوحة إنذار حريق لمشروع في القاهرة.",
                "platform": "web",
                "published_at": None,
                "page_fetched": False,
                "lead_qualification": "public_demand_signal",
                "lead_intent_evidence": {
                    "phrase": "نبحث عن مورد",
                    "basis": "snippet",
                    "signal_type": "request_for_quotation",
                    "product_fit": "unassessed",
                },
            },
            {
                "title": "كتالوج لوحات إنذار",
                "url": "https://example.net/catalog",
                "snippet": "كتالوج تعريفي بلوحات إنذار الحريق.",
                "platform": "web",
                "published_at": None,
                "page_fetched": False,
                "lead_qualification": "related_result_not_lead",
                "lead_intent_evidence": None,
            },
        ],
    }


def test_product_profiles_and_discovery_runs_are_tenant_scoped(tmp_path):
    store = LeadStore(tmp_path / "workspace-discovery.sqlite3")
    tenant_a = store.create_tenant("Workspace A", "workspace-a")
    tenant_b = store.create_tenant("Workspace B", "workspace-b")

    saved_profile = store.save_product_profile(product_profile(), tenant_id=tenant_a)
    saved_run = store.save_discovery_run(
        saved_profile["id"], discovery_run(), tenant_id=tenant_a
    )

    assert [item["id"] for item in store.list_product_profiles(tenant_id=tenant_a)] == [
        saved_profile["id"]
    ]
    assert store.list_product_profiles(tenant_id=tenant_b) == []
    assert store.get_product_profile(saved_profile["id"], tenant_id=tenant_b) is None
    assert store.get_discovery_run(saved_run["id"], tenant_id=tenant_b) is None
    assert store.list_discovery_runs(tenant_id=tenant_b) == []


def test_duplicate_product_profile_name_updates_within_tenant(tmp_path):
    store = LeadStore(tmp_path / "workspace-profiles.sqlite3")
    tenant = store.create_tenant("Workspace", "workspace")
    first = store.save_product_profile(product_profile(), tenant_id=tenant)
    updated = store.save_product_profile(
        product_profile(aliases=["FACP", "لوحة إنذار"]), tenant_id=tenant
    )

    assert updated["id"] == first["id"]
    assert updated["profile"]["product"]["aliases"] == ["FACP", "لوحة إنذار"]
    assert len(store.list_product_profiles(tenant_id=tenant)) == 1


def test_discovery_signal_save_uses_server_stored_qualification_and_evidence(tmp_path):
    store = LeadStore(tmp_path / "workspace-signals.sqlite3")
    tenant = store.create_tenant("Workspace", "workspace")
    profile = store.save_product_profile(product_profile(), tenant_id=tenant)
    run = store.save_discovery_run(profile["id"], discovery_run(), tenant_id=tenant)

    assert store.save_discovery_signal(run["id"], 1, tenant_id=tenant) is None

    saved, created = store.save_discovery_signal(run["id"], 0, tenant_id=tenant)
    assert created is True
    assert saved["source_url"] == "https://example.org/public-request/1"
    assert "نبحث عن مورد" in saved["note"]
    assert "request_for_quotation" in saved["note"]
    assert store.save_discovery_signal(run["id"], 0, tenant_id=tenant)[1] is False


def test_discovery_signal_save_rejects_other_tenant_run(tmp_path):
    store = LeadStore(tmp_path / "workspace-run-isolation.sqlite3")
    tenant_a = store.create_tenant("Workspace A", "workspace-a")
    tenant_b = store.create_tenant("Workspace B", "workspace-b")
    profile = store.save_product_profile(product_profile(), tenant_id=tenant_a)
    run = store.save_discovery_run(profile["id"], discovery_run(), tenant_id=tenant_a)

    assert store.save_discovery_signal(run["id"], 0, tenant_id=tenant_b) is None


def test_web_agent_forwards_structured_buyer_queries(monkeypatch):
    agent = WebAgent()
    captured = {}

    def fake_answer_with_budget(question, history=None, mode="auto", *, buyer_queries=None):
        captured.update(question=question, history=history, mode=mode, buyer_queries=buyer_queries)
        return {"kind": "lead_discovery", "sources": []}

    monkeypatch.setattr(agent, "_answer_with_budget", fake_answer_with_budget)
    queries = ['"مطلوب شراء" "لوحة إنذار الحريق"', '"عايز اشتري" "FACP"']

    result = agent.answer(
        "اكتشف طلب شراء معلن للمنتج في القاهرة",
        buyer_queries=queries,
    )

    assert result["kind"] == "lead_discovery"
    assert captured["buyer_queries"] == queries


def test_web_agent_can_skip_optional_search_connectors_by_request(monkeypatch):
    monkeypatch.setenv("DEEPSEEK_SEARCH_API_KEY", "test-deepseek")
    monkeypatch.setenv("BRAVE_SEARCH_API_KEY", "test-brave")
    monkeypatch.setenv("TAVILY_API_KEY", "test-tavily")
    agent = WebAgent()
    agent.allow_optional_providers = False
    monkeypatch.setattr(agent, "_search_duckduckgo_html", lambda _query: [])
    monkeypatch.setattr(agent, "_search_bing_rss", lambda _query: [])

    with pytest.raises(RuntimeError, match="لم تُرجع موصلات البحث"):
        agent._search_web("لوحة إنذار الحريق")

    statuses = {item["provider"]: item["status"] for item in agent._provider_diagnostics}
    assert statuses["deepseek_search_api"] == "disabled_by_request"
    assert statuses["brave_search_api"] == "disabled_by_request"
    assert statuses["tavily_search_api"] == "disabled_by_request"


def test_discovery_without_optional_approval_skips_reddit_oauth_but_keeps_public_rss(
    monkeypatch,
):
    import agents.web_agent as web_agent_module

    monkeypatch.setenv("REDDIT_CLIENT_ID", "configured-client-id")
    monkeypatch.setenv("REDDIT_CLIENT_SECRET", "configured-client-secret")
    agent = WebAgent()
    agent.allow_optional_providers = False
    called_urls = []

    class FakeResponse:
        status_code = 200
        content = (
            "<rss><channel><item><title>طلب شراء لوحة إنذار</title>"
            "<link>https://www.reddit.com/r/example/comments/123/request</link>"
            "<description>نبحث عن مورد للوحة إنذار حريق.</description>"
            "<pubDate>Fri, 06 Nov 2026 08:00:00 GMT</pubDate>"
            "</item></channel></rss>"
        ).encode()

    def fake_request(method, url, **kwargs):
        called_urls.append(url)
        if url != "https://www.reddit.com/search.rss":
            raise AssertionError("quota-backed Reddit OAuth must stay disabled")
        return FakeResponse()

    monkeypatch.setattr(web_agent_module, "_bounded_http_request", fake_request)
    results, _warnings = agent._search_social("لوحة إنذار حريق", ["reddit"])

    assert called_urls == ["https://www.reddit.com/search.rss"]
    assert results and results[0]["provider"] == "reddit_public_rss"
