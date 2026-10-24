from __future__ import annotations

import pytest

from agents.web_agent import WebAgent, _relevance_ratio


@pytest.mark.parametrize(
    ("question", "evidence"),
    [
        (
            "ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.",
            "Cairo is the capital of Egypt and one of the country's largest cities.",
        ),
        (
            "حلّل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميّز بين الحقائق والاستنتاجات، واذكر روابط المصادر.",
            "Electric cars in Egypt face challenges including high upfront costs, limited charging infrastructure, and gaps in public charging stations. The report compares costs and charger availability.",
        ),
        (
            "ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.",
            "AI agents are seeing rapid developments, new releases, deployments, and research updates this week.",
        ),
        (
            "اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة. وضّح إذا كانت النتائج غير كافية لتمثيل آراء المستخدمين عمومًا.",
            "In Egypt, electric-car owners and users share reviews, opinions, positive experiences, and complaints about charging and running costs.",
        ),
    ],
)
def test_realistic_arabic_questions_match_english_evidence_without_instruction_noise(
    question: str, evidence: str
):
    # Citation, formatting, and time-window instructions should not drown out the topic.
    assert _relevance_ratio(question, evidence) >= 0.20


def test_filtered_all_connector_diagnostics_do_not_claim_usable_evidence():
    agent = WebAgent()
    agent._record_provider_diagnostic(
        provider="bing_rss",
        query="ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟",
        status="filtered_all",
        result_count=0,
        rejected_count=6,
        error="all candidates failed URL/domain/relevance checks",
        candidate_count=6,
        rejection_reasons={"low_topical_relevance": 6},
    )

    summary = agent._connector_status_summary(list(agent._provider_diagnostics), [])
    bing = next(item for item in summary["connectors"] if item["name"] == "bing_rss")

    assert bing["attempted"] is True
    assert bing["response_received"] is True
    assert bing["available_for_this_request"] is True
    assert bing["verified_for_this_request"] is False
    assert bing["source_usable"] is False
    assert bing["quality_filter_exhausted"] is True
    assert bing["candidate_count"] == 6
    assert bing["result_count"] == 0
    assert bing["rejected_count"] == 6
    assert bing["rejection_reasons"] == {"low_topical_relevance": 6}
    assert bing["failure_observed"] is False


def test_provider_http_denials_are_not_reported_as_uncertain_generic_failures(monkeypatch):
    agent = WebAgent()
    monkeypatch.delenv("DEEPSEEK_SEARCH_API_KEY", raising=False)
    monkeypatch.delenv("BRAVE_SEARCH_API_KEY", raising=False)
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    monkeypatch.setattr(
        agent,
        "_search_duckduckgo_html",
        lambda _query: (_ for _ in ()).throw(RuntimeError("HTTP 403")),
    )
    monkeypatch.setattr(agent, "_search_bing_rss", lambda _query: [])
    with pytest.raises(RuntimeError):
        agent._search_web("Cairo capital Egypt")

    duck = next(
        item for item in agent._provider_diagnostics if item["provider"] == "duckduckgo_html"
    )
    # A direct HTTP response is a confirmed attempted request, even if access is denied.
    assert duck["status"] == "unauthorized"
