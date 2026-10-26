from __future__ import annotations

import pytest

from agents.web_agent import WebAgent, _relevance_ratio


@pytest.mark.parametrize(
    ("question", "evidence"),
    [
        (
            "ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.",
            "Cairo is the capital city of Egypt.",
        ),
        (
            "حلّل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميّز بين الحقائق والاستنتاجات، واذكر روابط المصادر.",
            "Electric vehicles in Egypt face challenges around charging infrastructure, upfront costs, and driving range.",
        ),
        (
            "ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.",
            "Recent developments in AI agents include tool use, planning, and more autonomous workflows.",
        ),
        (
            "اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة. وضّح إذا كانت النتائج غير كافية لتمثيل آراء المستخدمين عمومًا.",
            "Egyptian electric-car users share experiences about charging access, ownership costs, and public charging infrastructure.",
        ),
    ],
)
def test_long_arabic_requests_match_relevant_english_search_results(question, evidence):
    # The output language/citation instructions must not outweigh the subject terms.
    assert _relevance_ratio(question, evidence) >= 0.20


def test_unrelated_search_result_remains_below_relevance_threshold():
    question = (
        "حلّل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين "
        "التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة."
    )
    evidence = "Latest football league table, match scores, and player transfers."
    assert _relevance_ratio(question, evidence) < 0.20


def test_generic_instruction_only_query_does_not_accept_arbitrary_evidence():
    assert _relevance_ratio("اذكر روابط المصادر وأجب بإيجاز", "Football match scores") == 0.0


def test_connector_summary_distinguishes_completed_filtering_from_usable_results():
    agent = WebAgent()
    summary = agent._connector_status_summary(
        [
            {
                "provider": "bing_rss",
                "query": "اختبار بحث",
                "status": "filtered_all",
                "result_count": 0,
                "rejected_count": 6,
                "error": "all candidates failed URL/domain/relevance checks",
            }
        ],
        [],
    )
    bing = next(item for item in summary["connectors"] if item["name"] == "bing_rss")

    # A provider response was processed, but it supplied no usable evidence.
    assert bing["attempted"] is True
    assert bing["available_for_this_request"] is True
    assert bing["verified_for_this_request"] is True
    assert bing["usable_results_for_this_request"] is False
    assert bing["candidate_count"] == 6
    assert bing["result_count"] == 0
    assert bing["rejected_count"] == 6


@pytest.mark.parametrize(
    ("question", "evidence"),
    [
        (
            "السيارات الكهربائية والشحن والتكلفة والبنية التحتية في مصر",
            "Electric vehicles in Egypt need charging infrastructure and affect ownership costs.",
        ),
        (
            "وكلاء الذكاء الاصطناعي والتطورات الجديدة",
            "Recent developments in AI agents include planning and tool use.",
        ),
        (
            "اراء وتجارب المستخدمين للسيارات الكهربائية في مصر",
            "Reviews from electric car users in Egypt discuss charging and ownership.",
        ),
    ],
)
def test_core_bilingual_topic_synonyms_are_matched(question, evidence):
    assert _relevance_ratio(question, evidence) >= 0.20
