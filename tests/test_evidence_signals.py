from __future__ import annotations

from datetime import UTC, datetime

from agents.research import _parse_publication_date, evidence_signal_report


def test_evidence_signal_report_uses_domain_provider_page_and_date_coverage():
    now = datetime(2026, 10, 12, 12, 0, tzinfo=UTC)
    sources = []
    domains = [
        "agency.gov.eg", "university.edu.eg", "reuters.com", "apnews.com",
        "example.org", "example.net", "bbc.com", "sample.com",
    ]
    classes = [
        "government", "academic", "news", "news",
        "general", "general", "news", "general",
    ]
    for index, (domain, source_class) in enumerate(zip(domains, classes)):
        sources.append({
            "url": f"https://{domain}/article-{index}",
            "domain": domain,
            "source_class": source_class,
            "providers": ["brave_search_api"] if index % 2 else ["bing_rss"],
            "page_fetched": index < 3,
            "published_at": "2026-10-10T09:00:00Z" if index < 6 else "",
        })

    report = evidence_signal_report(sources, freshness="current", now=now)

    assert report["unique_sources"] == 8
    assert report["unique_domains"] == 8
    assert report["providers_count"] == 2
    assert report["pages_read"] == 3
    assert report["primary_sources"] == 2
    assert report["dated_sources"] == 6
    assert report["recent_sources"] == 6
    assert report["coverage_level"] == "متعدد المصادر"
    assert "ليس احتمال صحة الإجابة" in report["score_meaning"]


def test_evidence_signal_report_warns_when_no_sources_are_available():
    report = evidence_signal_report([], freshness="current")
    assert report["coverage_level"] == "محدود"
    assert report["coverage_score"] == 0
    assert any("لا توجد مصادر" in warning for warning in report["warnings"])
    assert any("حداثة النتائج غير مؤكدة" in warning for warning in report["warnings"])


def test_publication_date_parser_handles_iso_rfc822_and_relative_dates():
    now = datetime(2026, 10, 12, 12, 0, tzinfo=UTC)
    assert _parse_publication_date("2026-10-10T09:00:00Z", now) == datetime(
        2026, 10, 10, 9, 0, tzinfo=UTC
    )
    assert _parse_publication_date("2 days ago", now) == datetime(
        2026, 10, 10, 12, 0, tzinfo=UTC
    )
    assert _parse_publication_date("date not supplied", now) is None
