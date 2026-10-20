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
    markdown = INDEXER.render_markdown(symbols, files_scanned)

    assert files_scanned == 1
    assert by_name["DocumentedClass"].documented is True
    assert by_name["DocumentedClass.documented_method"].documented is True
    assert by_name["UndocumentedClass"].documented is False
    assert by_name["documented_function"].documented is True
    assert by_name["undocumented_function"].documented is False
    assert by_name["async_function"].kind == "دالة غير متزامنة"
    assert "Price \\| unit." in markdown
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
    first_symbols, first_count = INDEXER.scan_repository(tmp_path)
    second_symbols, second_count = INDEXER.scan_repository(tmp_path)
    first_markdown = INDEXER.render_markdown(first_symbols, first_count)
    second_markdown = INDEXER.render_markdown(second_symbols, second_count)
    output_path = tmp_path / "docs" / "MASTER_INDEX.md"

    assert first_markdown == second_markdown
    assert INDEXER.write_if_changed(output_path, first_markdown) is True
    assert INDEXER.write_if_changed(output_path, second_markdown) is False
