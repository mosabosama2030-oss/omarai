"""Security regression tests for outbound search connector boundaries."""
from __future__ import annotations

import json
import socket
import urllib.request

import pytest

from agents import search_connectors
from agents.web_agent import _public_http_url, _public_ip_literals


class _FakeResponse:
    def __init__(self, body: bytes):
        self.body = body
        self.read_limit = None

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self, limit: int):
        self.read_limit = limit
        return self.body[:limit]


class _FakeOpener:
    def __init__(self, response):
        self.response = response
        self.request = None
        self.timeout = None

    def open(self, request, timeout):
        self.request = request
        self.timeout = timeout
        return self.response


def test_academic_connectors_do_not_follow_provider_redirects():
    handler = search_connectors._NoRedirectHandler()
    request = urllib.request.Request("https://api.openalex.org/works")
    assert handler.redirect_request(
        request, None, 302, "Found", {}, "http://127.0.0.1/admin"
    ) is None


def test_academic_json_connector_uses_no_redirect_handler_and_bounded_read(monkeypatch):
    body = json.dumps({"results": []}).encode()
    response = _FakeResponse(body)
    opener = _FakeOpener(response)
    captured = {}

    def build_opener(handler_class):
        captured["handler_class"] = handler_class
        return opener

    monkeypatch.setattr(search_connectors.urllib.request, "build_opener", build_opener)
    assert search_connectors._http_get_json("https://api.openalex.org/works") == {
        "results": []
    }
    assert captured["handler_class"] is search_connectors._NoRedirectHandler
    assert response.read_limit == search_connectors.MAX_CONNECTOR_RESPONSE_BYTES + 1
    assert opener.timeout == search_connectors.DEFAULT_TIMEOUT_SECONDS


def test_academic_text_connector_rejects_oversized_response(monkeypatch):
    response = _FakeResponse(b"x" * (search_connectors.MAX_CONNECTOR_RESPONSE_BYTES + 1))
    opener = _FakeOpener(response)
    monkeypatch.setattr(
        search_connectors.urllib.request,
        "build_opener",
        lambda handler_class: opener,
    )
    with pytest.raises(ValueError, match="size limit"):
        search_connectors._http_get_text("https://export.arxiv.org/api/query")


@pytest.mark.parametrize(
    "url",
    [
        "http://127.0.0.1/admin",
        "http://10.0.0.8/",
        "http://172.16.0.1/",
        "http://192.168.1.20/",
        "http://169.254.169.254/latest/meta-data",
        "http://0.0.0.0/",
        "http://[::1]/",
        "http://[fc00::1]/",
        "http://[fe80::1]/",
        "http://[::ffff:127.0.0.1]/",
        "http://localhost/",
        "http://router.local/",
        "http://service.internal/",
    ],
)
def test_public_url_filter_rejects_private_local_and_non_global_targets(url):
    assert _public_http_url(url) is None


@pytest.mark.parametrize(
    "address",
    [
        "127.0.0.1",
        "10.0.0.8",
        "169.254.169.254",
        "::1",
        "fc00::1",
        "fe80::1",
        "::ffff:127.0.0.1",
    ],
)
def test_dns_resolution_fails_closed_for_private_or_local_answers(monkeypatch, address):
    family = socket.AF_INET6 if ":" in address else socket.AF_INET
    answer = (family, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", (address, 443, 0, 0))
    monkeypatch.setattr(
        search_connectors.socket if hasattr(search_connectors, "socket") else __import__("socket"),
        "getaddrinfo",
        lambda *_args, **_kwargs: [answer],
    )
    assert _public_ip_literals("private-answer.example") is None


def test_public_url_filter_keeps_public_https_targets():
    assert _public_http_url("https://example.com/path") == "https://example.com/path"
