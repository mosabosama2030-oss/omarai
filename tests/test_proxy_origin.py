"""Regression tests for the proxy-aware Origin check. OMARAI-PROXY-ORIGIN-PATCH"""
from __future__ import annotations
import http.client
import threading
from http.server import ThreadingHTTPServer
import pytest
from agents.omarai import LeadStore
from api.omarai import Handler

TOKEN = "t" * 40
PUBLIC_NAME = "app-1234.hosting.example"

@pytest.fixture
def port(tmp_path, monkeypatch):
    monkeypatch.setenv("OMARAI_PUBLIC_DEPLOYMENT", "1")
    monkeypatch.setenv("OMARAI_ACCESS_TOKEN", TOKEN)
    monkeypatch.delenv("OMARAI_ALLOWED_ORIGINS", raising=False)
    monkeypatch.setattr(Handler, "store", LeadStore(tmp_path / "origin-test.sqlite3"))
    monkeypatch.setattr(Handler, "RATE_LIMIT_REQUESTS", 10_000)
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_port
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)

def call(port, method, extra):
    body = b'{"question": "x"}' if method == "POST" else b""
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + TOKEN, **extra}
    connection = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
    connection.putrequest(method, "/api/ask", skip_host=True)
    for name, value in headers.items():
        connection.putheader(name, value)
    connection.putheader("Content-Length", str(len(body)))
    connection.endheaders()
    if body:
        connection.send(body)
    response = connection.getresponse()
    response.read()
    connection.close()
    return response.status

ALLOWED_SHAPES = {
    "proxy keeps Host, forwards https": {"Host": PUBLIC_NAME, "X-Forwarded-Proto": "https"},
    "proxy keeps Host, sends no proto header": {"Host": PUBLIC_NAME},
    "proxy forwards plain http": {"Host": PUBLIC_NAME, "X-Forwarded-Proto": "http"},
    "proxy rewrites Host, public name in X-Forwarded-Host": {
        "Host": "127.0.0.1:8000", "X-Forwarded-Host": PUBLIC_NAME, "X-Forwarded-Proto": "http"},
}

@pytest.mark.parametrize("shape", ALLOWED_SHAPES)
def test_own_origin_is_accepted_behind_a_proxy(port, shape):
    headers = {**ALLOWED_SHAPES[shape], "Origin": "https://" + PUBLIC_NAME}
    assert call(port, "POST", headers) == 200
    assert call(port, "OPTIONS", {k: v for k, v in headers.items() if k != "Authorization"}) == 204

@pytest.mark.parametrize("shape", ALLOWED_SHAPES)
def test_a_foreign_site_is_still_refused(port, shape):
    headers = {**ALLOWED_SHAPES[shape], "Origin": "https://evil.example"}
    assert call(port, "POST", headers) == 403
    assert call(port, "OPTIONS", headers) == 403

def test_configured_origin_still_works_without_any_proxy_headers(port, monkeypatch):
    monkeypatch.setenv("OMARAI_ALLOWED_ORIGINS", "https://frontend.example")
    headers = {"Host": "127.0.0.1:8000", "Origin": "https://frontend.example"}
    assert call(port, "POST", headers) == 200
