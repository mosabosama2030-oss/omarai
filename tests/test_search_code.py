from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

SEARCH_PATH = Path(__file__).resolve().parents[1] / "docs" / "search_code.py"
SEARCH_SPEC = importlib.util.spec_from_file_location("omarai_search_code_for_tests", SEARCH_PATH)
assert SEARCH_SPEC is not None
assert SEARCH_SPEC.loader is not None
SEARCH = importlib.util.module_from_spec(SEARCH_SPEC)
sys.modules[SEARCH_SPEC.name] = SEARCH
SEARCH_SPEC.loader.exec_module(SEARCH)


def test_search_returns_stable_file_line_and_source_link(tmp_path: Path) -> None:
    """Text search returns the exact file and 1-based line without network access."""
    source = tmp_path / "app.py"
    source.write_text("first = 1\nneedle = 2\nlast = 3\n", encoding="utf-8")

    hits = SEARCH.search_repository(tmp_path, "needle")

    assert len(hits) == 1
    assert hits[0].file == "app.py"
    assert hits[0].line == 2
    assert "needle = 2" in hits[0].text
    assert hits[0].link.endswith("/app.py#L2")


def test_search_supports_multiline_context_and_regex(tmp_path: Path) -> None:
    """The context argument returns the requested number of adjacent lines."""
    source = tmp_path / "app.py"
    source.write_text("before one\nbefore two\nVALUE_42 = 7\nafter one\nafter two\n", encoding="utf-8")

    hits = SEARCH.search_repository(
        tmp_path, r"VALUE_\d+", use_regex=True, context=2
    )

    assert len(hits) == 1
    assert hits[0].context_before.splitlines() == ["before one", "before two"]
    assert hits[0].context_after.splitlines() == ["after one", "after two"]


def test_search_excludes_common_secret_files_and_runtime_directories(tmp_path: Path) -> None:
    """Local searches skip common secret paths and binary/runtime data."""
    (tmp_path / "app.py").write_text("safe_value = 1\n", encoding="utf-8")
    (tmp_path / ".env").write_text("TOKEN=private-value\n", encoding="utf-8")
    (tmp_path / "credentials.json").write_text('{"token":"private-value"}\n', encoding="utf-8")
    aws_dir = tmp_path / ".aws"
    aws_dir.mkdir()
    (aws_dir / "credentials").write_text("token=private-value\n", encoding="utf-8")
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    (data_dir / "records.sqlite3").write_bytes(b"database-token")
    (tmp_path / "credentials.example").write_text("TOKEN=replace-me\n", encoding="utf-8")

    hits = SEARCH.search_repository(tmp_path, "private-value")
    safe_example = SEARCH.search_repository(tmp_path, "replace-me")

    assert hits == []
    assert len(safe_example) == 1
    assert safe_example[0].file == "credentials.example"


def test_search_validates_query_limits_and_reports_invalid_regex(tmp_path: Path) -> None:
    """Invalid search controls fail clearly instead of silently returning confusing results."""
    try:
        SEARCH.search_repository(tmp_path, "")
    except ValueError as exc:
        assert "فارغ" in str(exc)
    else:
        raise AssertionError("An empty search query should be rejected.")

    for kwargs in ({"max_results": 0}, {"context": -1}):
        try:
            SEARCH.search_repository(tmp_path, "needle", **kwargs)
        except ValueError:
            continue
        raise AssertionError(f"Invalid search limits should be rejected: {kwargs}")

    try:
        SEARCH.search_repository(tmp_path, "(", use_regex=True)
    except re.error:
        pass
    else:
        raise AssertionError("An invalid regular expression should be rejected.")

def test_search_links_use_the_requested_revision_not_main(tmp_path: Path) -> None:
    source = tmp_path / "app.py"
    source.write_text("needle = 1\n", encoding="utf-8")

    hits = SEARCH.search_repository(
        tmp_path, "needle", repository_ref="fix/review-branch"
    )

    assert len(hits) == 1
    assert hits[0].link == (
        "https://github.com/mosabosama2030-oss/omarai/"
        "blob/fix/review-branch/app.py#L1"
    )


def test_default_repository_ref_prefers_explicit_environment_override(
    monkeypatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("OMARAI_GITHUB_REF", "feature/current-review")
    monkeypatch.setenv("GITHUB_SHA", "a" * 40)

    assert SEARCH.default_repository_ref(tmp_path) == "feature/current-review"


def test_default_repository_ref_uses_valid_ci_sha(
    monkeypatch, tmp_path: Path
) -> None:
    monkeypatch.delenv("OMARAI_GITHUB_REF", raising=False)
    monkeypatch.setenv("GITHUB_SHA", "B" * 40)

    assert SEARCH.default_repository_ref(tmp_path) == "b" * 40

