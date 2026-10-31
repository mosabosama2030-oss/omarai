from __future__ import annotations

import httpx
import pytest

from agents.web_agent import (
    MAX_PROVIDER_RESPONSE_BYTES,
    WebAgent,
    _bounded_http_request,
)


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload
        self.status_code = 200

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


def test_brave_search_adapter_normalizes_real_api_response(monkeypatch):
    monkeypatch.setenv("BRAVE_SEARCH_API_KEY", "unit-test-secret")
    requested = {}

    def fake_get(url, **kwargs):
        requested["url"] = url
        requested.update(kwargs)
        return FakeResponse({
            "web": {
                "results": [{
                    "title": "Current research",
                    "url": "https://example.org/research",
                    "description": "A substantive search result.",
                    "page_age": "October 10, 2026",
                }]
            }
        })

    monkeypatch.setattr(
        "agents.web_agent._bounded_http_request",
        lambda method, url, **kwargs: fake_get(url, **kwargs),
    )
    rows = WebAgent()._search_brave("بحث حديث")
    assert requested["url"] == "https://api.search.brave.com/res/v1/web/search"
    assert requested["headers"]["X-Subscription-Token"] == "unit-test-secret"
    assert requested["params"]["country"] == "EG"
    assert rows[0]["provider"] == "brave_search_api"
    assert rows[0]["published_at"] == "October 10, 2026"
    assert "unit-test-secret" not in str(rows)


def test_tavily_search_adapter_normalizes_live_search_results(monkeypatch):
    monkeypatch.setenv("TAVILY_API_KEY", "unit-test-tavily-secret")
    requested = {}

    def fake_post(url, **kwargs):
        requested["url"] = url
        requested.update(kwargs)
        return FakeResponse({
            "results": [{
                "title": "Official report",
                "url": "https://example.org/report",
                "content": "A source excerpt from the search response.",
                "published_date": "2026-10-11",
            }]
        })

    monkeypatch.setattr(
        "agents.web_agent._bounded_http_request",
        lambda method, url, **kwargs: fake_post(url, **kwargs),
    )
    rows = WebAgent()._search_tavily("official sources report")
    assert requested["url"] == "https://api.tavily.com/search"
    assert requested["json"]["api_key"] == "unit-test-tavily-secret"
    assert requested["json"]["include_answer"] is False
    assert rows[0]["provider"] == "tavily_search_api"
    assert rows[0]["snippet"].startswith("A source excerpt")
    assert "unit-test-tavily-secret" not in str(rows)


def test_search_api_setup_status_reports_only_presence_not_secret_values(monkeypatch):
    monkeypatch.setenv("BRAVE_SEARCH_API_KEY", "brave-secret")
    monkeypatch.setenv("TAVILY_API_KEY", "tavily-secret")
    status = WebAgent.status()
    assert status["brave_search_api_configured"] is True
    assert status["tavily_search_api_configured"] is True
    assert "brave-secret" not in str(status)
    assert "tavily-secret" not in str(status)



def test_bounded_provider_transport_caps_streamed_bytes_even_when_length_lies(monkeypatch):
    chunks_read = []
    observed = {}

    class FakeResponse:
        status_code = 200

        def __init__(self):
            self.headers = {"content-length": "1"}
            self.request = httpx.Request("GET", "https://provider.example/search")

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def iter_bytes(self):
            for chunk in (
                b"A" * MAX_PROVIDER_RESPONSE_BYTES,
                b"B",
                b"C",
            ):
                chunks_read.append(len(chunk))
                yield chunk

    class FakeClient:
        def __init__(self, **kwargs):
            observed["client_options"] = kwargs

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def stream(self, method, url, **kwargs):
            observed["method"] = method
            observed["url"] = url
            observed["request_options"] = kwargs
            return FakeResponse()

    monkeypatch.setattr(httpx, "Client", FakeClient)
    with pytest.raises(ValueError, match="size limit"):
        _bounded_http_request(
            "GET",
            "https://provider.example/search",
            timeout=4.0,
            follow_redirects=True,
            params={"q": "test"},
        )

    assert observed["client_options"]["timeout"] == 4.0
    assert observed["client_options"]["follow_redirects"] is False
    assert observed["client_options"]["trust_env"] is False
    assert observed["method"] == "GET"
    assert observed["url"] == "https://provider.example/search"
    assert observed["request_options"] == {"params": {"q": "test"}}
    assert chunks_read == [MAX_PROVIDER_RESPONSE_BYTES, 1]


def test_bounded_provider_transport_returns_buffered_response(monkeypatch):
    payload = b'{"results":[{"title":"bounded"}]}'
    observed = {}

    class FakeResponse:
        status_code = 200

        def __init__(self):
            self.headers = {"content-type": "application/json"}
            self.request = httpx.Request("POST", "https://provider.example/search")

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def iter_bytes(self):
            yield payload[:10]
            yield payload[10:]

    class FakeClient:
        def __init__(self, **kwargs):
            observed["client_options"] = kwargs

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def stream(self, method, url, **kwargs):
            observed["method"] = method
            observed["request_options"] = kwargs
            return FakeResponse()

    monkeypatch.setattr(httpx, "Client", FakeClient)
    response = _bounded_http_request(
        "POST",
        "https://provider.example/search",
        timeout=3.0,
        json={"query": "test"},
    )

    assert response.status_code == 200
    assert response.json() == {"results": [{"title": "bounded"}]}
    assert observed["method"] == "POST"
    assert observed["request_options"] == {"json": {"query": "test"}}
    assert observed["client_options"]["follow_redirects"] is False
    assert observed["client_options"]["trust_env"] is False



def test_bounded_provider_transport_enforces_absolute_total_deadline(monkeypatch):
    chunks_read = []

    class FakeResponse:
        status_code = 200
        request = httpx.Request("GET", "https://provider.example/slow")
        headers = {}

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def iter_bytes(self):
            for chunk in (b"first", b"second"):
                chunks_read.append(chunk)
                yield chunk

    class FakeClient:
        def __init__(self, **kwargs):
            assert kwargs["timeout"] == 9.0
            assert kwargs["follow_redirects"] is False

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def stream(self, method, url, **kwargs):
            assert method == "GET"
            return FakeResponse()

    # Start at t=0; the first chunk arrives before the deadline.
    # The deadline expires before requesting the second chunk.
    clock = iter((0.0, 0.0, 2.0))
    monkeypatch.setattr("agents.web_agent.time.monotonic", lambda: next(clock))
    monkeypatch.setattr(httpx, "Client", FakeClient)

    with pytest.raises(TimeoutError, match="total request deadline"):
        _bounded_http_request(
            "GET",
            "https://provider.example/slow",
            timeout=9.0,
            total_timeout=1.5,
        )

    assert chunks_read == [b"first"]


@pytest.mark.parametrize("total_timeout", [0, -1, float("inf"), "not-a-number"])
def test_bounded_provider_transport_rejects_invalid_total_deadlines(total_timeout):
    with pytest.raises(ValueError, match="total_timeout"):
        _bounded_http_request(
            "GET",
            "https://provider.example/search",
            total_timeout=total_timeout,
        )
