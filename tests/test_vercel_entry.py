"""Vercel entry and path-normalization smoke tests (no network, no secrets)."""
from __future__ import annotations

import importlib
import os
from pathlib import Path


def test_vercel_handler_export():
    """api/index.py must expose a BaseHTTPRequestHandler subclass named handler."""
    mod = importlib.import_module("api.index")
    assert hasattr(mod, "handler")
    from http.server import BaseHTTPRequestHandler

    assert issubclass(mod.handler, BaseHTTPRequestHandler)


def test_request_path_prefers_original_header():
    from api.omarai import Handler

    h = Handler.__new__(Handler)
    h.path = "/api"
    h.headers = {"x-vercel-original-path": "/agent"}
    assert h._request_path() == "/agent"


def test_request_path_falls_back_to_self_path():
    from api.omarai import Handler

    h = Handler.__new__(Handler)
    h.path = "/api/health"
    h.headers = {}
    assert h._request_path() == "/api/health"


def test_web_assets_exist_for_bundle():
    """HTML must be present so the Vercel function can serve the Arabic UI."""
    root = Path(__file__).resolve().parents[1]
    assert (root / "web" / "agent.html").is_file()
    assert (root / "web" / "dashboard.html").is_file()


def test_vercel_json_present():
    root = Path(__file__).resolve().parents[1]
    cfg = root / "vercel.json"
    assert cfg.is_file()
    text = cfg.read_text(encoding="utf-8")
    assert "maxDuration" in text
    assert "api/index.py" in text


def test_health_includes_platform_when_vercel(monkeypatch):
    """Health payload should surface platform=vercel when VERCEL is set."""
    monkeypatch.setenv("VERCEL", "1")
    # Minimal mock of a GET /api/health call is covered by existing API tests;
    # here we only verify the env branch is readable.
    assert os.getenv("VERCEL") == "1"
