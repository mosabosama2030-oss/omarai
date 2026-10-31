"""Regression tests for outbound SSRF address policy."""

import socket

import pytest

from agents.web_agent import _public_http_url, _public_ip_literals


@pytest.mark.parametrize(
    "url",
    [
        "http://127.0.0.1/admin",
        "http://10.1.2.3/private",
        "http://172.16.0.1/private",
        "http://192.168.1.2/private",
        "http://169.254.169.254/latest/meta-data/",
        "http://100.64.0.1/private",
        "http://0.0.0.0/",
        "http://[::1]/admin",
        "http://[fc00::1]/private",
        "http://[fe80::1]/private",
        "http://[::ffff:192.168.1.1]/private",
        "http://[2001:db8::1]/documentation",
    ],
)
def test_outbound_url_filter_rejects_non_global_ip_literals(url):
    assert _public_http_url(url) is None


@pytest.mark.parametrize(
    "host",
    ["localhost", "printer.local", "api.internal", "service.localhost"],
)
def test_outbound_url_filter_rejects_local_hostnames(host):
    assert _public_http_url(f"https://{host}/") is None


@pytest.mark.parametrize(
    "resolved_ip",
    [
        "127.0.0.1",
        "10.0.0.10",
        "172.20.0.10",
        "192.168.10.10",
        "169.254.169.254",
        "100.64.0.10",
        "::1",
        "fc00::10",
        "fe80::10",
        "::ffff:192.168.10.10",
    ],
)
def test_dns_resolution_rejects_any_non_global_address(monkeypatch, resolved_ip):
    family = socket.AF_INET6 if ":" in resolved_ip else socket.AF_INET
    sockaddr = (
        (resolved_ip, 0, 0, 0)
        if family == socket.AF_INET6
        else (resolved_ip, 0)
    )
    monkeypatch.setattr(
        socket,
        "getaddrinfo",
        lambda *_args, **_kwargs: [(family, socket.SOCK_STREAM, 6, "", sockaddr)],
    )
    assert _public_ip_literals("customer-controlled.example") is None


def test_dns_resolution_rejects_mixed_public_and_private_addresses(monkeypatch):
    public = (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 0))
    private = (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("192.168.1.10", 0))
    monkeypatch.setattr(
        socket, "getaddrinfo", lambda *_args, **_kwargs: [public, private]
    )
    assert _public_ip_literals("mixed.example") is None


def test_dns_resolution_keeps_only_verified_global_addresses(monkeypatch):
    public = (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 0))
    monkeypatch.setattr(
        socket, "getaddrinfo", lambda *_args, **_kwargs: [public, public]
    )
    assert _public_ip_literals("public.example") == ["93.184.216.34"]
