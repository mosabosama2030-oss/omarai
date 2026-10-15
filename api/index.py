"""Vercel serverless entry for Omarai.

Vercel Python runtime detects a BaseHTTPRequestHandler subclass named
``handler`` in files under /api. This module re-exports the existing
application Handler so the same auth, rate-limit, research, and UI routes
work on Hobby without duplicating business logic.

Local / Docker / Render / Railway continue to use ``python -m cli.omarai serve``
and the ThreadingHTTPServer path in api.omarai.
"""
from __future__ import annotations

# Re-export the production Handler under the name Vercel expects.
from api.omarai import Handler as handler

# Explicit alias keeps static checkers and Vercel detection happy.
__all__ = ["handler"]
