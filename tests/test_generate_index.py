from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


INDEXER_PATH = Path(__file__).resolve().parents[1] / "docs" / "generate_index.py"
INDEXER_SPEC = importlib.util.spec_from_file_location(
    "omarai_generate_index_for_tests",
    INDEXER_PATH,
)
assert INDEXER_SPEC is not None
assert INDEXER_SPEC.loader is not None
INDEXER = importlib.util.module_from_spec(INDEXER_SPEC)
sys.modules[INDEXER_SPEC.name] = INDEXER
INDEXER_SPEC.loader.exec_module(INDEXER)

SEARCH_PATH = Path(__file__).resolve().parents[1] / "docs" / "search_code.py"
SEARCH_SPEC = importlib.util.spec_from_file_location(
    "omarai_search_code_for_tests",
    SEARCH_PATH,
)
assert SEARCH_SPEC is not None
assert SEARCH_SPEC.loader is not None
SEARCH = importlib.util.module_from_spec(SEARCH_SPEC)
sys.modules[SEARCH_SPEC.name] = SEARCH
SEARCH_SPEC.loader.exec_module(SEARCH)


def test_indexes_functions_classes_methods_and_docstring_status(tmp_path: Path) -> None:
    """The index includes qualified names and distinguishes documented from missing."""
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "sample.py").write_text(
        'class DocumentedClass:\n'
        '    """A documented class."""\n'
        '    def documented_method(self):\n'
        '        """Price | unit."""\n'
        '        return None\n\n'
        'class UndocumentedClass:\n'
        '    pass\n\n'
        'def documented_function():\n'
        '    """A documented function."""\n'
        '    return None\n\n'
        'def undocumented_function():\n'
        '    return None\n\n'
        'async def async_function():\n'
        '    """An asynchronous function."""\n'
        '    return None\n',
        encoding="utf-8",
    )

    symbols, files_scanned = INDEXER.scan_repository(tmp_path)
    by_name = {symbol.name: symbol for symbol in symbols}
    markdown, _stats = INDEXER.build_index(tmp_path)

    assert files_scanned == 1
    assert by_name["DocumentedClass"].documented is True
    assert by_name["DocumentedClass.documented_method"].documented is True
    assert by_name["UndocumentedClass"].documented is False
    assert by_name["documented_function"].documented is True
    assert by_name["undocumented_function"].documented is False
    assert by_name["async_function"].kind == "دالة غير متزامنة"
    assert "Price" in markdown and "unit." in markdown
    assert "| موثق |" in markdown
    assert "| ناقص |" in markdown


def test_skips_virtual_environments_and_generated_dependency_directories(
    tmp_path: Path,
) -> None:
    """The scan avoids vendored dependencies, build outputs, and virtual environments."""
    (tmp_path / "app.py").write_text(
        'def application_entry():\n    """Main entry point."""\n',
        encoding="utf-8",
    )
    excluded_files = (
        tmp_path / ".venv" / "lib" / "hidden.py",
        tmp_path / "node_modules" / "package" / "hidden.py",
        tmp_path / "build" / "generated.py",
    )
    for path in excluded_files:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("def should_not_be_indexed():\n    pass\n", encoding="utf-8")

    symbols, files_scanned = INDEXER.scan_repository(tmp_path)

    assert files_scanned == 1
    assert [symbol.name for symbol in symbols] == ["application_entry"]


def test_syntax_error_does_not_overwrite_the_previous_index(
    tmp_path: Path,
    capsys,
) -> None:
    """A failed parse leaves the prior index intact rather than publishing partial data."""
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    index_path = docs_dir / "MASTER_INDEX.md"
    index_path.write_text("previous index must survive", encoding="utf-8")
    (tmp_path / "broken.py").write_text(
        "def incomplete(:\n    pass\n",
        encoding="utf-8",
    )

    result = INDEXER.main(["--root", str(tmp_path)])

    assert result == 1
    assert index_path.read_text(encoding="utf-8") == "previous index must survive"
    assert "لم يُكتب MASTER_INDEX.md" in capsys.readouterr().err


def test_repeated_generation_is_deterministic_and_does_not_rewrite_unchanged_index(
    tmp_path: Path,
) -> None:
    """An unchanged scan produces identical Markdown and avoids an unnecessary write."""
    (tmp_path / "app.py").write_text(
        'def entry():\n    """Entry point."""\n',
        encoding="utf-8",
    )
    first_markdown, _ = INDEXER.build_index(tmp_path)
    second_markdown, _ = INDEXER.build_index(tmp_path)
    output_path = tmp_path / "docs" / "MASTER_INDEX.md"

    assert first_markdown == second_markdown
    assert INDEXER.write_if_changed(output_path, first_markdown) is True
    assert INDEXER.write_if_changed(output_path, second_markdown) is False


def test_extracts_api_routes_env_web_and_doc_symbols(tmp_path: Path) -> None:
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    (api_dir / "server.py").write_text(
        "class Handler:\n"
        "    def do_GET(self):\n"
        "        parsed = type('P', (), {})()\n"
        "        if parsed.path in {'/', '/agent'}:\n"
        "            return\n"
        "        if parsed.path == '/api/health':\n"
        "            return\n"
        "    def do_POST(self):\n"
        "        path = '/api/ask'\n"
        "        if path == '/api/ask':\n"
        "            return\n",
        encoding="utf-8",
    )
    (tmp_path / ".env.example").write_text(
        "OMARAI_ACCESS_TOKEN=replace-me\n# OPTIONAL_KEY=1\n",
        encoding="utf-8",
    )
    (tmp_path / "app.py").write_text(
        "import os\nTOKEN = os.environ.get('OMARAI_ACCESS_TOKEN')\ndef test_sample():\n    return TOKEN\n",
        encoding="utf-8",
    )
    web_dir = tmp_path / "web"
    web_dir.mkdir()
    (web_dir / "page.html").write_text(
        '<div id="status"></div>\n<script>\nfunction setStatus(text){ return text; }\n</script>\n',
        encoding="utf-8",
    )
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "guide.md").write_text("# Guide Title\n\n## Section One\n", encoding="utf-8")

    routes = INDEXER.scan_api_routes(tmp_path)
    envs = INDEXER.scan_env_settings(tmp_path)
    web = INDEXER.scan_web_symbols(tmp_path)
    headings = INDEXER.scan_doc_headings(tmp_path)
    markdown, stats = INDEXER.build_index(tmp_path)

    route_names = {route.name for route in routes}
    assert "/" in route_names and "/api/health" in route_names and "/api/ask" in route_names
    assert "OMARAI_ACCESS_TOKEN" in {item.name for item in envs}
    assert ("معرّف HTML", "status") in {(item.kind, item.name) for item in web}
    assert "Guide Title" in {item.name for item in headings}
    assert stats["api_routes"] >= 3
    assert "github.com/mosabosama2030-oss/omarai/blob/main/" in markdown


def test_secrets_and_env_files_are_not_catalogued(tmp_path: Path) -> None:
    (tmp_path / "safe.py").write_text("def ok():\n    return 1\n", encoding="utf-8")
    (tmp_path / ".env").write_text("SECRET=should-not-appear\n", encoding="utf-8")
    groups = INDEXER.catalog_files(tmp_path)
    flat = [path for files in groups.values() for path in files]
    assert ".env" not in flat
    assert any(path.endswith("safe.py") for path in flat)


def test_index_updates_when_function_added_or_removed(tmp_path: Path) -> None:
    app = tmp_path / "app.py"
    app.write_text("def first():\n    return 1\n", encoding="utf-8")
    assert [s.name for s in INDEXER.scan_repository(tmp_path)[0]] == ["first"]
    app.write_text("def first():\n    return 1\n\ndef second():\n    return 2\n", encoding="utf-8")
    assert [s.name for s in INDEXER.scan_repository(tmp_path)[0]] == ["first", "second"]
    app.write_text("def second():\n    return 2\n", encoding="utf-8")
    assert [s.name for s in INDEXER.scan_repository(tmp_path)[0]] == ["second"]


def test_github_links_use_expected_path_and_line() -> None:
    assert INDEXER.github_link("api/omarai.py", 350) == (
        "https://github.com/mosabosama2030-oss/omarai/blob/main/api/omarai.py#L350"
    )


def test_text_search_returns_file_line_and_link(tmp_path: Path) -> None:
    (tmp_path / "sample.py").write_text("alpha\nunique_marker_value = 42\nbeta\n", encoding="utf-8")
    (tmp_path / ".env").write_text("unique_marker_value=secret\n", encoding="utf-8")
    hits = SEARCH.search_repository(tmp_path, "unique_marker_value")
    assert len(hits) == 1
    assert hits[0].file == "sample.py" and hits[0].line == 2
    assert hits[0].link.endswith("sample.py#L2")


def test_text_search_skips_excluded_directories(tmp_path: Path) -> None:
    (tmp_path / "visible.py").write_text("find_me_token\n", encoding="utf-8")
    hidden = tmp_path / ".venv" / "lib"
    hidden.mkdir(parents=True)
    (hidden / "hidden.py").write_text("find_me_token\n", encoding="utf-8")
    hits = SEARCH.search_repository(tmp_path, "find_me_token")
    assert [hit.file for hit in hits] == ["visible.py"]
