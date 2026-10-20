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
    """The Python AST index includes qualified names and documentation state."""
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


def test_indexes_module_and_class_assignments_but_not_function_locals(
    tmp_path: Path,
) -> None:
    """Module/class attributes are searchable without flooding the index with locals."""
    (tmp_path / "settings.py").write_text(
        'MODULE_SETTING = "enabled"\n'
        'class Settings:\n'
        '    CLASS_SETTING: str = "strict"\n'
        '    def method(self):\n'
        '        local_only = "do not index"\n'
        '        return local_only\n',
        encoding="utf-8",
    )

    symbols, _ = INDEXER.scan_repository(tmp_path)
    by_name = {symbol.name: symbol for symbol in symbols}

    assert by_name["MODULE_SETTING"].kind == "متغير/ثابت Python"
    assert by_name["MODULE_SETTING"].documented is None
    assert by_name["Settings.CLASS_SETTING"].kind == "متغير/ثابت Python"
    assert "local_only" not in by_name


def test_indexes_frontend_ids_javascript_symbols_css_and_documentation_headings(
    tmp_path: Path,
) -> None:
    """Frontend declarations and Markdown headings remain navigable without language parsers."""
    web_dir = tmp_path / "web"
    docs_dir = tmp_path / "docs"
    web_dir.mkdir()
    docs_dir.mkdir()
    (web_dir / "agent.html").write_text(
        '<div id="chat-panel" name="question-box" data-testid="send-button"></div>\n'
        "<style>\n"
        ".chat-panel { --accent-color: #fff; }\n"
        "#answer-panel { display: block; }\n"
        "</style>\n"
        "<script>\n"
        "function sendMessage() { return true; }\n"
        "class AgentCore {}\n"
        "const fetchAnswer = async (question) => question;\n"
        "const ACCESS_TOKEN = 'example';\n"
        "</script>\n",
        encoding="utf-8",
    )
    (docs_dir / "guide.md").write_text(
        "# User Guide\n## Troubleshooting\n",
        encoding="utf-8",
    )
    (tmp_path / "settings.yml").write_text(
        "OMARAI_ENABLED: true\nrequest-budget:\n  max-calls: 3\n",
        encoding="utf-8",
    )

    inventory = INDEXER.build_file_inventory(tmp_path)
    symbols = INDEXER.scan_static_symbols(tmp_path, inventory)
    names_by_kind = {(symbol.kind, symbol.name) for symbol in symbols}

    assert ("قيمة سمة HTML (id)", "chat-panel") in names_by_kind
    assert ("قيمة سمة HTML (name)", "question-box") in names_by_kind
    assert ("قيمة سمة HTML (data-testid)", "send-button") in names_by_kind
    assert ("دالة JavaScript/TypeScript", "sendMessage") in names_by_kind
    assert ("كلاس JavaScript/TypeScript", "AgentCore") in names_by_kind
    assert ("دالة JavaScript/TypeScript", "fetchAnswer") in names_by_kind
    assert ("متغير JavaScript/TypeScript", "ACCESS_TOKEN") in names_by_kind
    assert ("محدد class في CSS", "chat-panel") in names_by_kind
    assert ("محدد id في CSS", "answer-panel") in names_by_kind
    assert ("متغير CSS مخصص", "accent-color") in names_by_kind
    assert ("عنوان Markdown (H1)", "User Guide") in names_by_kind
    assert ("عنوان Markdown (H2)", "Troubleshooting") in names_by_kind
    assert ("مفتاح إعداد YAML", "OMARAI_ENABLED") in names_by_kind
    assert ("اسم ثابت/إعداد بصيغة UPPER_SNAKE_CASE", "OMARAI_ENABLED") in names_by_kind


def test_repository_inventory_covers_files_and_excludes_private_runtime_paths(
    tmp_path: Path,
) -> None:
    """The file inventory includes docs/config and excludes known local secret/runtime files."""
    (tmp_path / "app.py").write_text("VALUE = 1\n", encoding="utf-8")
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "guide.md").write_text("# Guide\n", encoding="utf-8")
    (tmp_path / ".env").write_text("OPENROUTER_API_KEY=private-value\n", encoding="utf-8")
    (tmp_path / ".env.example").write_text(
        "OPENROUTER_API_KEY=replace-me\n", encoding="utf-8"
    )
    (tmp_path / "local.sqlite3").write_bytes(b"not a real database")
    (tmp_path / "logo.bin").write_bytes(b"\x00\x01\x02")

    inventory = INDEXER.build_file_inventory(tmp_path)
    paths = {item.file for item in inventory}
    by_path = {item.file: item for item in inventory}

    assert "app.py" in paths
    assert "docs/guide.md" in paths
    assert ".env.example" in paths
    assert ".env" not in paths
    assert "local.sqlite3" not in paths
    assert "logo.bin" in paths
    assert by_path["logo.bin"].line_count is None



def test_excludes_credential_names_and_secret_directories(tmp_path: Path) -> None:
    """The repository index does not copy common local credential files into generated docs."""
    (tmp_path / "app.py").write_text("VALUE = 1\n", encoding="utf-8")
    (tmp_path / "credentials.json").write_text(
        '{"private_key":"do-not-index"}\n', encoding="utf-8"
    )
    (tmp_path / "client_secret.json").write_text(
        '{"client_secret":"do-not-index"}\n', encoding="utf-8"
    )
    aws_dir = tmp_path / ".aws"
    aws_dir.mkdir()
    (aws_dir / "credentials").write_text("aws_secret_access_key=do-not-index\n", encoding="utf-8")
    secrets_dir = tmp_path / "secrets"
    secrets_dir.mkdir()
    (secrets_dir / "runtime.txt").write_text("token=do-not-index\n", encoding="utf-8")
    examples_dir = tmp_path / "examples"
    examples_dir.mkdir()
    (examples_dir / "credentials.example").write_text(
        "TOKEN=replace-me\n", encoding="utf-8"
    )
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "credential-handling.md").write_text(
        "# Credential handling guide\n", encoding="utf-8"
    )

    inventory = INDEXER.build_file_inventory(tmp_path)
    paths = {item.file for item in inventory}
    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)
    indexed_text = "\n".join(item.content for item in source_lines)

    assert "app.py" in paths
    assert "examples/credentials.example" in paths
    assert "docs/credential-handling.md" in paths
    assert "credentials.json" not in paths
    assert "client_secret.json" not in paths
    assert ".aws/credentials" not in paths
    assert "secrets/runtime.txt" not in paths
    assert "do-not-index" not in indexed_text

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
        tmp_path / "omarai_agent.egg-info" / "PKG-INFO",
        tmp_path / "package.dist-info" / "METADATA",
    )
    for path in excluded_files:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("def should_not_be_indexed():\n    pass\n", encoding="utf-8")

    symbols, files_scanned = INDEXER.scan_repository(tmp_path)

    assert files_scanned == 1
    assert [symbol.name for symbol in symbols] == ["application_entry"]
    inventory_paths = {item.file for item in INDEXER.build_file_inventory(tmp_path)}
    assert not any(".egg-info/" in path for path in inventory_paths)
    assert not any(".dist-info/" in path for path in inventory_paths)


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
        'def entry():\n    """Entry point."""\n', encoding="utf-8"
    )
    first_symbols, first_count = INDEXER.scan_repository(tmp_path)
    second_symbols, second_count = INDEXER.scan_repository(tmp_path)
    first_inventory = INDEXER.build_file_inventory(tmp_path)
    second_inventory = INDEXER.build_file_inventory(tmp_path)
    first_static = INDEXER.scan_static_symbols(tmp_path, first_inventory)
    second_static = INDEXER.scan_static_symbols(tmp_path, second_inventory)
    first_markdown = INDEXER.render_markdown(
        first_symbols, first_count, first_inventory, first_static
    )
    second_markdown = INDEXER.render_markdown(
        second_symbols, second_count, second_inventory, second_static
    )
    output_path = tmp_path / "docs" / "MASTER_INDEX.md"

    assert first_markdown == second_markdown
    assert INDEXER.write_if_changed(output_path, first_markdown) is True
    assert INDEXER.write_if_changed(output_path, second_markdown) is False


def test_check_mode_detects_stale_index_without_modifying_it(tmp_path: Path, capsys) -> None:
    """Check mode fails on a stale index and leaves the existing file untouched."""
    (tmp_path / "app.py").write_text("VALUE = 1\n", encoding="utf-8")
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    index_path = docs_dir / "MASTER_INDEX.md"
    index_path.write_text("stale", encoding="utf-8")

    assert INDEXER.main(["--root", str(tmp_path), "--check"]) == 1
    assert index_path.read_text(encoding="utf-8") == "stale"
    assert "الفهرس قديم" in capsys.readouterr().err

    assert INDEXER.main(["--root", str(tmp_path)]) == 0
    assert INDEXER.main(["--root", str(tmp_path), "--check"]) == 0


def test_indexes_every_eligible_text_line_with_file_and_line_ids(tmp_path: Path) -> None:
    """All readable text lines, including blank lines and unfamiliar extensions, are searchable."""
    (tmp_path / "app.py").write_text(
        'VALUE = 1\n\n'
        'def greet():\n'
        '    return "hello"\n',
        encoding="utf-8",
    )
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "guide.txt").write_text(
        "First documented step.\nSecond documented step.\n",
        encoding="utf-8",
    )
    (tmp_path / ".env").write_text("PRIVATE_TOKEN=do-not-index\n", encoding="utf-8")
    (tmp_path / "payload.bin").write_bytes(b"\x00\x01\x02")

    inventory = INDEXER.build_file_inventory(tmp_path)
    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)
    findings = INDEXER.scan_finding_annotations(source_lines)
    line_by_file_and_number = {(line.file, line.line): line for line in source_lines}
    pages, pages_by_file = INDEXER.render_source_line_pages(source_lines, inventory, findings)
    lines_markdown = INDEXER.render_source_lines_markdown(
        source_lines, inventory, findings, pages_by_file, pages
    )
    all_page_content = "\n".join(pages.values())

    assert ("app.py", 1) in line_by_file_and_number
    assert ("app.py", 2) in line_by_file_and_number
    assert line_by_file_and_number[("app.py", 2)].content == ""
    assert line_by_file_and_number[("app.py", 4)].content == '    return "hello"'
    assert line_by_file_and_number[("docs/guide.txt", 2)].content == "Second documented step."
    assert line_by_file_and_number[("app.py", 1)].line_id.startswith("SRC-")
    assert line_by_file_and_number[("app.py", 1)].file_id.startswith("FILE-")
    assert line_by_file_and_number[("app.py", 1)].category == "ملفات أخرى"
    assert "PRIVATE_TOKEN" not in lines_markdown
    assert "payload.bin" not in {line.file for line in source_lines}
    assert "Second documented step." in all_page_content
    assert "SRC-" in all_page_content
    assert "SOURCE_LINES_001" in lines_markdown
    assert pages_by_file["app.py"]


def test_explicit_review_markers_have_unique_codes_and_source_line_links(
    tmp_path: Path,
) -> None:
    """TODO/FIXME/BUG-style annotations receive stable named IDs linked to their exact lines."""
    (tmp_path / "module.py").write_text(
        "# TODO: verify fallback\n"
        "value = 1  # FIXME: handle overflow\n"
        "# SECURITY: check token handling\n"
        "def ready():\n"
        "    return True\n",
        encoding="utf-8",
    )

    inventory = INDEXER.build_file_inventory(tmp_path)
    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)
    findings = INDEXER.scan_finding_annotations(source_lines)

    assert [item.marker for item in findings] == ["FIXME", "SECURITY", "TODO"]
    assert len({item.finding_id for item in findings}) == 3
    for finding in findings:
        assert finding.finding_id.startswith(f"FND-{finding.marker}-")
        assert finding.line_id.startswith("SRC-")
        assert finding.file == "module.py"


def test_check_mode_validates_both_generated_indexes(tmp_path: Path, capsys) -> None:
    """Check mode detects a missing or stale line index as well as a stale master index."""
    (tmp_path / "app.py").write_text("VALUE = 1\n", encoding="utf-8")

    assert INDEXER.main(["--root", str(tmp_path)]) == 0
    master_path = tmp_path / INDEXER.INDEX_RELATIVE_PATH
    line_index_path = tmp_path / INDEXER.SOURCE_LINES_INDEX_RELATIVE_PATH
    assert master_path.exists()
    assert line_index_path.exists()
    assert INDEXER.main(["--root", str(tmp_path), "--check"]) == 0

    line_index_path.write_text("stale line index", encoding="utf-8")
    assert INDEXER.main(["--root", str(tmp_path), "--check"]) == 1
    assert line_index_path.read_text(encoding="utf-8") == "stale line index"
    assert "فهرس الأسطر قديم" in capsys.readouterr().err
