#!/usr/bin/env bash
# Apply the META_TAIL no-punctuation fix to agents/research.py
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
patch -p1 -d "$ROOT" < "$ROOT/patches/meta_tail_nopunct.patch"
echo "Applied META_TAIL no-punctuation fix. Run: pytest tests/test_meta_tail_nopunct.py tests/test_research.py -q"
