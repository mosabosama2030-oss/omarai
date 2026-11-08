"""Research planning, domain targeting, and multi-query source ranking.

This module is deterministic by design: the language model may propose a plan,
but all queries, result counts and source records are validated before use.
"""
from __future__ import annotations

import ipaddress
import re
from datetime import UTC, datetime, timedelta
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import urlparse

import tldextract

from agents.aspect_planning import extract_aspects
from agents.intent_router import resolve_followup_query
from agents.search_meta_tail import SEARCH_META_TAIL_RE as _SEARCH_META_TAIL_RE
from agents.search_meta_tail import strip_trailing_conjunctions

MAX_PLAN_QUERIES = 8
MAX_QUERY_CHARS = 240
MAX_FUSED_RESULTS = 18
