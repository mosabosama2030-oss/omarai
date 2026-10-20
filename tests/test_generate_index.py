from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


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


def test_check_mode_validates_all_generated_indexes(tmp_path: Path, capsys) -> None:
    """Check mode detects stale master, line, and coverage indexes."""

    (tmp_path / "app.py").write_text("VALUE = 1\n", encoding="utf-8")

    assert INDEXER.main(["--root", str(tmp_path)]) == 0
    master_path = tmp_path / INDEXER.INDEX_RELATIVE_PATH
    line_index_path = tmp_path / INDEXER.SOURCE_LINES_INDEX_RELATIVE_PATH
    coverage_path = tmp_path / INDEXER.COVERAGE_AUDIT_RELATIVE_PATH
    assert master_path.exists()
    assert line_index_path.exists()
    assert coverage_path.exists()
    assert INDEXER.main(["--root", str(tmp_path), "--check"]) == 0

    original_line_index = line_index_path.read_text(encoding="utf-8")
    line_index_path.write_text("stale line index", encoding="utf-8")
    assert INDEXER.main(["--root", str(tmp_path), "--check"]) == 1
    assert line_index_path.read_text(encoding="utf-8") == "stale line index"
    assert "فهرس الأسطر قديم" in capsys.readouterr().err

    line_index_path.write_text(original_line_index, encoding="utf-8")
    coverage_path.write_text("stale coverage audit", encoding="utf-8")
    assert INDEXER.main(["--root", str(tmp_path), "--check"]) == 1
    assert coverage_path.read_text(encoding="utf-8") == "stale coverage audit"
    assert "فهرس تغطية الفهرسة قديم" in capsys.readouterr().err



def test_source_line_coverage_validator_rejects_missing_or_duplicate_lines(tmp_path: Path) -> None:
    """A gap or duplicate in line IDs prevents the generator from claiming full coverage."""
    source_file = tmp_path / "src.py"
    source_file.write_text("FIRST = 1\nSECOND = 2\n", encoding="utf-8")
    inventory = INDEXER.build_file_inventory(tmp_path)
    lines = INDEXER.scan_source_lines(tmp_path, inventory)

    INDEXER.validate_source_line_coverage(inventory, lines)
    with pytest.raises(INDEXER.IndexGenerationError, match="اكتمال فهرسة السطور"):
        INDEXER.validate_source_line_coverage(inventory, lines[:-1])
    with pytest.raises(INDEXER.IndexGenerationError, match="معرّف SRC مكرر"):
        INDEXER.validate_source_line_coverage(inventory, lines + [lines[0]])


def test_coverage_audit_discloses_metadata_only_and_excluded_paths_without_secrets(
    tmp_path: Path,
) -> None:
    """Coverage report states exact skipped-file reasons without exposing secret contents."""
    (tmp_path / "source.py").write_text("VALUE = 7\n", encoding="utf-8")
    (tmp_path / ".env").write_text("PRIVATE_API_TOKEN=never-print-this-secret\n", encoding="utf-8")
    (tmp_path / "large.txt").write_bytes(b"x" * (INDEXER.MAX_INDEXED_TEXT_BYTES + 1))
    (tmp_path / ".venv" / "lib").mkdir(parents=True)
    (tmp_path / ".venv" / "lib" / "hidden.py").write_text("PRIVATE = True\n", encoding="utf-8")

    inventory = INDEXER.build_file_inventory(tmp_path)
    lines = INDEXER.scan_source_lines(tmp_path, inventory)
    INDEXER.validate_source_line_coverage(inventory, lines)
    exclusions = INDEXER.discover_excluded_paths(tmp_path)
    report = INDEXER.render_coverage_audit_markdown(tmp_path, inventory, lines, exclusions)

    assert "100.00%" in report
    assert "large.txt" in report
    assert f"يتجاوز حد الفهرسة ({INDEXER.MAX_INDEXED_TEXT_BYTES} بايت)" in report
    assert ".env" in report
    assert ".venv/" in report
    assert "لم تُقرأ محتوياته" in report
    assert "never-print-this-secret" not in report
    assert "PRIVATE_API_TOKEN" not in report
    assert "PRIVATE = True" not in report


def test_multiple_review_markers_on_one_line_each_get_a_unique_finding_code(
    tmp_path: Path,
) -> None:
    """Different and repeated review tags on a single line must not overwrite each other."""
    source_file = tmp_path / "module.py"
    source_file.write_text(
        "# BUG: first defect; FIXME: repair it; BUG: second defect\n",
        encoding="utf-8",
    )

    inventory = INDEXER.build_file_inventory(tmp_path)
    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)
    findings = INDEXER.scan_finding_annotations(source_lines)
    pages, _ = INDEXER.render_source_line_pages(source_lines, inventory, findings)

    assert len(findings) == 3
    assert {item.marker for item in findings} == {"BUG", "FIXME"}
    assert len({item.finding_id for item in findings}) == 3
    bug_ids = [item.finding_id for item in findings if item.marker == "BUG"]
    assert any(item.endswith("-M01") for item in bug_ids)
    assert any(item.endswith("-M02") for item in bug_ids)
    page_content = "\n".join(pages.values())
    assert all(item.finding_id in page_content for item in findings)


def test_finding_scan_ignores_incidental_words_but_finds_real_annotations(
    tmp_path: Path,
) -> None:
    """Only explicit comment or prose markers become findings, never syntax/URLs/strings."""
    (tmp_path / "sample.py").write_text(
        'framework_url = "https://example.org/risk-management-framework"\n'
        'error = "ordinary error variable"\n'
        'template = "# BUG: this is inside a string"\n'
        '# BUG: real Python defect\n',
        encoding="utf-8",
    )
    (tmp_path / "app.js").write_text(
        'const template = "// BUG: not a comment";\n'
        'const error = 1;\n'
        'const x = 2; // FIXME: actual JS issue\n'
        '/* SECURITY: actual CSS/JS comment issue */\n',
        encoding="utf-8",
    )
    (tmp_path / "styles.css").write_text(
        ".box{gap:8px;color:red}\n"
        "/* GAP: deliberate comment annotation */\n",
        encoding="utf-8",
    )
    (tmp_path / "page.html").write_text(
        '<!-- REVIEW: check the navigation landmark -->\n'
        '<script>const template = "<!-- BUG: not a markup comment -->";</script>\n',
        encoding="utf-8",
    )
    (tmp_path / "guide.md").write_text(
        "The risk-management framework reports an error.\n"
        "```text\n"
        "# BUG: this sample should be ignored\n"
        "```\n"
        "- DEFECT: this explicitly documented defect should be indexed\n",
        encoding="utf-8",
    )

    inventory = INDEXER.build_file_inventory(tmp_path)
    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)
    findings = INDEXER.scan_finding_annotations(source_lines)
    summarized = {(item.file, item.marker, item.description) for item in findings}

    assert {item.marker for item in findings} == {
        "BUG", "FIXME", "SECURITY", "GAP", "REVIEW", "DEFECT"
    }
    assert any(path == "sample.py" and marker == "BUG" and "real Python defect" in desc
               for path, marker, desc in summarized)
    assert any(path == "app.js" and marker == "FIXME" for path, marker, _ in summarized)
    assert any(path == "app.js" and marker == "SECURITY" for path, marker, _ in summarized)
    assert any(path == "styles.css" and marker == "GAP" for path, marker, _ in summarized)
    assert any(path == "page.html" and marker == "REVIEW" for path, marker, _ in summarized)
    assert any(path == "guide.md" and marker == "DEFECT" for path, marker, _ in summarized)
    assert not any("risk-management" in desc.lower() for _, _, desc in summarized)
    assert not any("ordinary error variable" in desc for _, _, desc in summarized)
    assert not any("inside a string" in desc for _, _, desc in summarized)
    assert not any("sample should be ignored" in desc for _, _, desc in summarized)
