"""Generate Omarai's deterministic repository-wide file and source-symbol index."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import sys
import tempfile
import tokenize
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

EXCLUDED_DIRECTORIES = frozenset(
    {
        ".git",
        ".hg",
        ".svn",
        ".venv",
        "venv",
        "env",
        "virtualenv",
        "__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        ".mypy_cache",
        ".tox",
        ".nox",
        "node_modules",
        "site-packages",
        "build",
        "dist",
    }
)
SENSITIVE_FILENAMES = frozenset(
    {
        ".env",
        ".env.local",
        ".env.production",
        ".env.development",
        "id_rsa",
        "id_ed25519",
    }
)
EXCLUDED_SUFFIXES = frozenset(
    {
        ".pyc",
        ".pyo",
        ".sqlite",
        ".sqlite3",
        ".db",
        ".pem",
        ".key",
        ".p12",
        ".pfx",
    }
)
MAX_INDEXED_TEXT_BYTES = 2 * 1024 * 1024
MAX_DESCRIPTION_LENGTH = 240
INDEX_RELATIVE_PATH = "docs/MASTER_INDEX.md"
SOURCE_LINES_INDEX_RELATIVE_PATH = "docs/SOURCE_LINES_INDEX.md"
INDEX_OUTPUT_PATHS = frozenset({INDEX_RELATIVE_PATH, SOURCE_LINES_INDEX_RELATIVE_PATH})

PYTHON_EXTENSIONS = frozenset({".py"})
JAVASCRIPT_EXTENSIONS = frozenset({".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx"})
CSS_EXTENSIONS = frozenset({".css", ".scss"})
CONFIG_EXTENSIONS = frozenset({".yml", ".yaml", ".toml", ".json", ".ini", ".cfg"})
TEXT_SCAN_EXTENSIONS = (
    PYTHON_EXTENSIONS
    | JAVASCRIPT_EXTENSIONS
    | CSS_EXTENSIONS
    | CONFIG_EXTENSIONS
    | frozenset({".html", ".htm", ".sh", ".md", ".env.example", ".example"})
)

JS_IDENTIFIER = r"[A-Za-z_$][A-Za-z0-9_$]*"
JS_FUNCTION_RE = re.compile(
    rf"\b(?:async\s+)?function\s*\*?\s+({JS_IDENTIFIER})\s*\("
)
JS_CLASS_RE = re.compile(rf"\bclass\s+({JS_IDENTIFIER})\b")
JS_ARROW_ASSIGNMENT_RE = re.compile(
    rf"\b(?:const|let|var)\s+({JS_IDENTIFIER})\s*=\s*"
    rf"(?:async\s*)?(?:\([^;\n]*?\)|{JS_IDENTIFIER})\s*=>"
)
JS_FUNCTION_ASSIGNMENT_RE = re.compile(
    rf"\b(?:const|let|var)\s+({JS_IDENTIFIER})\s*=\s*(?:async\s*)?function\b"
)
JS_VARIABLE_RE = re.compile(rf"\b(?:const|let|var)\s+({JS_IDENTIFIER})\b")
HTML_ATTRIBUTE_RE = re.compile(
    r"""\b(id|name|data-testid)\s*=\s*(["'])(.*?)\2""",
    flags=re.IGNORECASE | re.DOTALL,
)
HTML_SCRIPT_RE = re.compile(r"<script\b[^>]*>(.*?)</script\s*>", re.IGNORECASE | re.DOTALL)
HTML_STYLE_RE = re.compile(r"<style\b[^>]*>(.*?)</style\s*>", re.IGNORECASE | re.DOTALL)
CSS_COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)
CSS_CUSTOM_PROPERTY_RE = re.compile(r"--([A-Za-z_][A-Za-z0-9_-]*)\s*:")
CSS_CLASS_RE = re.compile(r"(?<![\w.-])\.([A-Za-z_][A-Za-z0-9_-]*)")
CSS_ID_RE = re.compile(r"(?<![\w.#])#([A-Za-z_][A-Za-z0-9_-]*)")
SHELL_FUNCTION_RE = re.compile(
    r"^\s*(?:function\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*\(\s*\)\s*\{?",
    re.MULTILINE,
)
MARKDOWN_HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$", re.MULTILINE)
YAML_KEY_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_.-]*)\s*:", re.MULTILINE)
TOML_KEY_RE = re.compile(r"^\s*([A-Za-z0-9_.-]+)\s*=", re.MULTILINE)
TOML_SECTION_RE = re.compile(r"^\s*\[([^\]]+)\]\s*$", re.MULTILINE)
JSON_KEY_RE = re.compile(r'"([^"]+)"\s*:')
INI_SECTION_RE = re.compile(r"^\s*\[([^\]]+)\]\s*$", re.MULTILINE)
INI_KEY_RE = re.compile(r"^\s*([A-Za-z0-9_.-]+)\s*=", re.MULTILINE)
UPPER_SNAKE_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b")
API_PATH_RE = re.compile(r"""["'](/(?:api|leads)(?:/[A-Za-z0-9_{}./-]+)*)["']""")
FINDING_MARKER_RE = re.compile(r"\b(TODO|FIXME|BUG|HACK|XXX|REVIEW|SECURITY|DEPRECATED)\b(?:\s*[:#-]?\s*(.*))?", re.IGNORECASE)


@dataclass(frozen=True, slots=True)
class IndexedSymbol:
    """Represent a Python definition or module/class assignment."""

    file: str
    name: str
    kind: str
    line: int
    description: str
    documented: bool | None


@dataclass(frozen=True, slots=True)
class IndexedFile:
    """Represent a repository file with stable identifiers and navigation metadata."""

    file: str
    file_type: str
    size_bytes: int
    line_count: int | None
    indexing_scope: str
    file_id: str
    category: str


@dataclass(frozen=True, slots=True)
class IndexedMarker:
    """Represent a statically discovered symbol outside the Python AST index."""

    file: str
    name: str
    kind: str
    line: int


@dataclass(frozen=True, slots=True)
class IndexedLine:
    """Represent one exact logical line from an eligible readable repository text file."""

    file: str
    file_id: str
    line_id: str
    category: str
    line: int
    content: str


@dataclass(frozen=True, slots=True)
class IndexedFinding:
    """Represent a source annotation that explicitly requests attention."""

    finding_id: str
    file: str
    line_id: str
    marker: str
    description: str


class IndexGenerationError(RuntimeError):
    """Signal that a complete Python AST index could not be generated."""


class SymbolVisitor(ast.NodeVisitor):
    """Collect Python classes, functions, methods and module/class assignments."""

    def __init__(self, relative_file: str) -> None:
        """Initialize the visitor for one repository-relative Python file."""
        self.relative_file = relative_file
        self.symbols: list[IndexedSymbol] = []
        self.scope: list[str] = []
        self.function_depth = 0

    @staticmethod
    def _description(node: ast.AST) -> tuple[str, bool]:
        """Return a compact first-paragraph summary and its documentation state."""
        docstring = ast.get_docstring(node, clean=True)
        if not docstring or not docstring.strip():
            return "لا توجد Docstring.", False

        first_paragraph = docstring.strip().split("\n\n", maxsplit=1)[0]
        summary = " ".join(first_paragraph.split())
        if len(summary) > MAX_DESCRIPTION_LENGTH:
            summary = summary[: MAX_DESCRIPTION_LENGTH - 3].rstrip() + "..."
        return summary, True

    def _record_definition(
        self,
        node: ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef,
        kind: str,
    ) -> None:
        """Record one class/function definition while preserving its qualified scope."""
        description, documented = self._description(node)
        qualified_name = ".".join((*self.scope, node.name))
        self.symbols.append(
            IndexedSymbol(
                file=self.relative_file,
                name=qualified_name,
                kind=kind,
                line=node.lineno,
                description=description,
                documented=documented,
            )
        )

    def _record_assignment_target(self, node: ast.AST, line: int) -> None:
        """Record declared names from a module-level or class-level assignment."""
        if isinstance(node, ast.Name):
            qualified_name = ".".join((*self.scope, node.id))
            self.symbols.append(
                IndexedSymbol(
                    file=self.relative_file,
                    name=qualified_name,
                    kind="متغير/ثابت Python",
                    line=line,
                    description="تعريف على مستوى الوحدة أو الكلاس.",
                    documented=None,
                )
            )
        elif isinstance(node, (ast.Tuple, ast.List)):
            for element in node.elts:
                self._record_assignment_target(element, line)

    def visit_Assign(self, node: ast.Assign) -> None:
        """Index module/class assignment names but avoid flooding the index with locals."""
        if self.function_depth == 0:
            for target in node.targets:
                self._record_assignment_target(target, node.lineno)
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        """Index annotated module/class assignments without counting local variables."""
        if self.function_depth == 0:
            self._record_assignment_target(node.target, node.lineno)
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Record a class and recursively inspect its body."""
        self._record_definition(node, "كلاس")
        self.scope.append(node.name)
        try:
            self.generic_visit(node)
        finally:
            self.scope.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Record a synchronous function or method and nested definitions."""
        self._record_definition(node, "دالة")
        self.scope.append(node.name)
        self.function_depth += 1
        try:
            self.generic_visit(node)
        finally:
            self.function_depth -= 1
            self.scope.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        """Record an asynchronous function or method and nested definitions."""
        self._record_definition(node, "دالة غير متزامنة")
        self.scope.append(node.name)
        self.function_depth += 1
        try:
            self.generic_visit(node)
        finally:
            self.function_depth -= 1
            self.scope.pop()


def _is_sensitive_or_runtime_path(path: Path) -> bool:
    """Exclude known local secrets, runtime databases, keys and generated bytecode."""
    name = path.name.lower()
    if name in SENSITIVE_FILENAMES:
        return True
    if name.startswith(".env") and name != ".env.example":
        return True
    return path.suffix.lower() in EXCLUDED_SUFFIXES


def discover_repository_files(root: Path) -> list[Path]:
    """Return the stable file inventory, excluding the generated index and runtime data."""
    discovered: list[Path] = []
    for current_directory, directory_names, file_names in os.walk(
        root,
        topdown=True,
        followlinks=False,
    ):
        directory_names[:] = sorted(
            name
            for name in directory_names
            if name not in EXCLUDED_DIRECTORIES
            and not (Path(current_directory) / name).is_symlink()
        )
        for file_name in sorted(file_names):
            candidate = Path(current_directory) / file_name
            if candidate.is_symlink() or _is_sensitive_or_runtime_path(candidate):
                continue
            relative_file = candidate.relative_to(root).as_posix()
            if relative_file == INDEX_RELATIVE_PATH:
                # Exclude the output to avoid a self-referential size/line-count loop.
                continue
            discovered.append(candidate)

    return sorted(
        discovered,
        key=lambda path: path.relative_to(root).as_posix().casefold(),
    )


def _read_text_bounded(path: Path) -> str | None:
    """Read supported UTF-8 text files only when they are within the scan-size bound."""
    try:
        if path.stat().st_size > MAX_INDEXED_TEXT_BYTES:
            return None
        if path.suffix.lower() == ".py":
            with tokenize.open(str(path)) as source_stream:
                text = source_stream.read()
        else:
            text = path.read_text(encoding="utf-8")
        if "\x00" in text:
            return None
        return text
    except (OSError, UnicodeError, LookupError, tokenize.TokenError):
        return None


def _count_lines(text: str) -> int:
    """Count source lines without adding an extra line for a trailing newline."""
    if not text:
        return 0
    return text.count("\n") + (not text.endswith("\n"))


def _file_type(path: Path) -> str:
    """Return a readable file type based on a known filename or extension."""
    name = path.name.lower()
    if name in {"dockerfile", "makefile", "procfile"}:
        return name.capitalize()
    suffix = path.suffix.lower()
    labels = {
        ".py": "Python",
        ".html": "HTML",
        ".htm": "HTML",
        ".js": "JavaScript",
        ".mjs": "JavaScript module",
        ".cjs": "CommonJS",
        ".jsx": "React JSX",
        ".ts": "TypeScript",
        ".tsx": "TypeScript JSX",
        ".css": "CSS",
        ".scss": "SCSS",
        ".md": "Markdown",
        ".yml": "YAML",
        ".yaml": "YAML",
        ".json": "JSON",
        ".toml": "TOML",
        ".sh": "Shell",
        ".sql": "SQL",
        ".txt": "Text",
        ".svg": "SVG",
        ".png": "PNG image",
        ".jpg": "JPEG image",
        ".jpeg": "JPEG image",
        ".webp": "WebP image",
    }
    return labels.get(suffix, suffix[1:].upper() if suffix else "بدون امتداد")


def _indexing_scope(path: Path, text: str | None) -> str:
    """Describe precisely whether a file receives symbol extraction or path inventory only."""
    if text is None:
        return "جرد المسار والحجم فقط (ثنائي/غير مقروء/أكبر من حد الفحص)"
    suffix = path.suffix.lower()
    if suffix in PYTHON_EXTENSIONS:
        return "جرد الملف + AST Python"
    if suffix in JAVASCRIPT_EXTENSIONS:
        return "جرد الملف + رموز JavaScript/TypeScript ساكنة"
    if suffix in CSS_EXTENSIONS:
        return "جرد الملف + محددات CSS والمتغيرات المخصصة"
    if suffix in {".html", ".htm"}:
        return "جرد الملف + معرفات HTML والرموز داخل script/style"
    if suffix == ".md":
        return "جرد الملف + عناوين Markdown"
    if suffix in CONFIG_EXTENSIONS:
        return "جرد الملف + مفاتيح إعداد ساكنة"
    if suffix == ".sh":
        return "جرد الملف + دوال Shell"
    if path.name.lower() in {"dockerfile", "makefile", "procfile"}:
        return "جرد الملف + أسماء إعدادات عامة إن وجدت"
    if path.name.lower() == ".env.example" or suffix == ".example":
        return "جرد الملف + أسماء إعدادات عامة إن وجدت"
    return "جرد ملف نصي فقط"


def build_file_inventory(root: Path) -> list[IndexedFile]:
    """Inventory repository files and record whether static symbol scanning was possible."""
    inventory: list[IndexedFile] = []
    for path in discover_repository_files(root):
        text = _read_text_bounded(path)
        inventory.append(
            IndexedFile(
                file=path.relative_to(root).as_posix(),
                file_type=_file_type(path),
                size_bytes=path.stat().st_size,
                line_count=_count_lines(text) if text is not None else None,
                indexing_scope=_indexing_scope(path, text),
            )
        )
    return inventory


def discover_python_files(root: Path) -> list[Path]:
    """Return sorted Python files from the eligible repository inventory."""
    return [
        path
        for path in discover_repository_files(root)
        if path.suffix.lower() == ".py"
    ]


def scan_repository(root: Path) -> tuple[list[IndexedSymbol], int]:
    """Parse every eligible Python file or fail without producing a partial index."""
    python_files = discover_python_files(root)
    all_symbols: list[IndexedSymbol] = []
    failures: list[str] = []

    for source_path in python_files:
        relative_file = source_path.relative_to(root).as_posix()
        try:
            with tokenize.open(str(source_path)) as source_stream:
                source = source_stream.read()
            syntax_tree = ast.parse(source, filename=relative_file)
        except SyntaxError as exc:
            location = f"السطر {exc.lineno}: {exc.msg}" if exc.lineno else exc.msg
            failures.append(f"{relative_file}: {location}")
            continue
        except (OSError, UnicodeError, LookupError, tokenize.TokenError) as exc:
            failures.append(f"{relative_file}: {type(exc).__name__}: {exc}")
            continue

        visitor = SymbolVisitor(relative_file)
        visitor.visit(syntax_tree)
        all_symbols.extend(visitor.symbols)

    if failures:
        detail = "\n".join(f"- {failure}" for failure in failures)
        raise IndexGenerationError(
            "تعذر إنشاء فهرس Python كامل؛ لم يُكتب MASTER_INDEX.md. "
            "أصلح الملفات التالية ثم أعد التشغيل:\n" + detail
        )

    all_symbols.sort(
        key=lambda symbol: (
            symbol.file.casefold(),
            symbol.line,
            symbol.name.casefold(),
            symbol.kind,
        )
    )
    return all_symbols, len(python_files)


def _line_at(source: str, offset: int, base_line: int = 1) -> int:
    """Return a 1-based line number for a match in the supplied source fragment."""
    return base_line + source.count("\n", 0, offset)


def _add_marker(
    markers: list[IndexedMarker],
    seen: set[tuple[str, str, str]],
    relative_file: str,
    name: str,
    kind: str,
    line: int,
) -> None:
    """Add the first occurrence of a symbol category within one file."""
    clean_name = " ".join(name.strip().split())
    if not clean_name:
        return
    key = (relative_file, clean_name, kind)
    if key in seen:
        return
    seen.add(key)
    markers.append(
        IndexedMarker(
            file=relative_file,
            name=clean_name,
            kind=kind,
            line=max(line, 1),
        )
    )


def _scan_javascript(
    source: str,
    relative_file: str,
    markers: list[IndexedMarker],
    seen: set[tuple[str, str, str]],
    base_line: int = 1,
) -> None:
    """Extract navigational JS/TS declarations using bounded regular-expression heuristics."""
    for pattern, kind in (
        (JS_FUNCTION_RE, "دالة JavaScript/TypeScript"),
        (JS_CLASS_RE, "كلاس JavaScript/TypeScript"),
    ):
        for match in pattern.finditer(source):
            _add_marker(
                markers,
                seen,
                relative_file,
                match.group(1),
                kind,
                _line_at(source, match.start(), base_line),
            )

    function_variable_locations: set[tuple[str, int]] = set()
    for pattern in (JS_ARROW_ASSIGNMENT_RE, JS_FUNCTION_ASSIGNMENT_RE):
        for match in pattern.finditer(source):
            line = _line_at(source, match.start(), base_line)
            name = match.group(1)
            function_variable_locations.add((name, line))
            _add_marker(
                markers,
                seen,
                relative_file,
                name,
                "دالة JavaScript/TypeScript",
                line,
            )

    for match in JS_VARIABLE_RE.finditer(source):
        line = _line_at(source, match.start(), base_line)
        name = match.group(1)
        if (name, line) in function_variable_locations:
            continue
        _add_marker(
            markers,
            seen,
            relative_file,
            name,
            "متغير JavaScript/TypeScript",
            line,
        )


def _scan_css(
    source: str,
    relative_file: str,
    markers: list[IndexedMarker],
    seen: set[tuple[str, str, str]],
    base_line: int = 1,
) -> None:
    """Extract CSS class/id selectors and custom properties; this is not a full CSS parser."""
    cleaned = CSS_COMMENT_RE.sub(
        lambda match: "".join("\n" if char == "\n" else " " for char in match.group(0)),
        source,
    )
    patterns = (
        (CSS_CUSTOM_PROPERTY_RE, "متغير CSS مخصص"),
        (CSS_CLASS_RE, "محدد class في CSS"),
        (CSS_ID_RE, "محدد id في CSS"),
    )
    for pattern, kind in patterns:
        for match in pattern.finditer(cleaned):
            _add_marker(
                markers,
                seen,
                relative_file,
                match.group(1),
                kind,
                _line_at(cleaned, match.start(), base_line),
            )


def _scan_html(
    source: str,
    relative_file: str,
    markers: list[IndexedMarker],
    seen: set[tuple[str, str, str]],
) -> None:
    """Extract HTML navigation attributes plus embedded JS and CSS declarations."""
    for match in HTML_ATTRIBUTE_RE.finditer(source):
        attribute = match.group(1).lower()
        raw_value = match.group(3).strip()
        for value in raw_value.split() if attribute == "data-testid" else [raw_value]:
            _add_marker(
                markers,
                seen,
                relative_file,
                value,
                f"قيمة سمة HTML ({attribute})",
                _line_at(source, match.start()),
            )

    for match in HTML_SCRIPT_RE.finditer(source):
        script = match.group(1)
        base_line = _line_at(source, match.start(1))
        _scan_javascript(script, relative_file, markers, seen, base_line)
    for match in HTML_STYLE_RE.finditer(source):
        style = match.group(1)
        base_line = _line_at(source, match.start(1))
        _scan_css(style, relative_file, markers, seen, base_line)


def _scan_config_keys(
    source: str,
    suffix: str,
    relative_file: str,
    markers: list[IndexedMarker],
    seen: set[tuple[str, str, str]],
) -> None:
    """Extract configuration keys/sections without evaluating or loading configuration."""
    if suffix in {".yml", ".yaml"}:
        patterns = ((YAML_KEY_RE, "مفتاح إعداد YAML"),)
    elif suffix == ".toml":
        patterns = (
            (TOML_SECTION_RE, "قسم TOML"),
            (TOML_KEY_RE, "مفتاح إعداد TOML"),
        )
    elif suffix == ".json":
        patterns = ((JSON_KEY_RE, "مفتاح JSON"),)
    elif suffix in {".ini", ".cfg"}:
        patterns = (
            (INI_SECTION_RE, "قسم إعداد"),
            (INI_KEY_RE, "مفتاح إعداد"),
        )
    else:
        patterns = ()
    for pattern, kind in patterns:
        for match in pattern.finditer(source):
            _add_marker(
                markers,
                seen,
                relative_file,
                match.group(1),
                kind,
                _line_at(source, match.start()),
            )


def scan_static_symbols(root: Path, inventory: list[IndexedFile]) -> list[IndexedMarker]:
    """Extract supplementary navigational symbols from frontend, docs, config and scripts."""
    markers: list[IndexedMarker] = []
    seen: set[tuple[str, str, str]] = set()
    for indexed_file in inventory:
        path = root / indexed_file.file
        suffix = path.suffix.lower()
        file_name = path.name.lower()
        is_example_env = file_name == ".env.example"
        if suffix not in TEXT_SCAN_EXTENSIONS and not is_example_env and file_name not in {
            "dockerfile",
            "makefile",
            "procfile",
        }:
            continue

        source = _read_text_bounded(path)
        if source is None:
            continue

        if suffix in JAVASCRIPT_EXTENSIONS:
            _scan_javascript(source, indexed_file.file, markers, seen)
        elif suffix in CSS_EXTENSIONS:
            _scan_css(source, indexed_file.file, markers, seen)
        elif suffix in {".html", ".htm"}:
            _scan_html(source, indexed_file.file, markers, seen)
        elif suffix == ".md":
            for match in MARKDOWN_HEADING_RE.finditer(source):
                heading = match.group(2).strip()
                _add_marker(
                    markers,
                    seen,
                    indexed_file.file,
                    heading,
                    f"عنوان Markdown (H{len(match.group(1))})",
                    _line_at(source, match.start()),
                )
        elif suffix == ".sh":
            for match in SHELL_FUNCTION_RE.finditer(source):
                _add_marker(
                    markers,
                    seen,
                    indexed_file.file,
                    match.group(1),
                    "دالة Shell",
                    _line_at(source, match.start()),
                )
        elif suffix in CONFIG_EXTENSIONS:
            _scan_config_keys(source, suffix, indexed_file.file, markers, seen)

        if suffix in TEXT_SCAN_EXTENSIONS or is_example_env or file_name in {
            "dockerfile",
            "makefile",
            "procfile",
        }:
            for match in UPPER_SNAKE_RE.finditer(source):
                _add_marker(
                    markers,
                    seen,
                    indexed_file.file,
                    match.group(0),
                    "اسم ثابت/إعداد بصيغة UPPER_SNAKE_CASE",
                    _line_at(source, match.start()),
                )

        if suffix in PYTHON_EXTENSIONS | JAVASCRIPT_EXTENSIONS | {".html", ".htm"}:
            for match in API_PATH_RE.finditer(source):
                _add_marker(
                    markers,
                    seen,
                    indexed_file.file,
                    match.group(1),
                    "مسار API/واجهة محتمل",
                    _line_at(source, match.start()),
                )

    markers.sort(
        key=lambda marker: (
            marker.file.casefold(),
            marker.line,
            marker.kind.casefold(),
            marker.name.casefold(),
        )
    )
    return markers


def _markdown_cell(value: str) -> str:
    """Normalize text and escape Markdown table delimiters."""
    return " ".join(value.replace("\r", " ").replace("\n", " ").split()).replace(
        "|", r"\|"
    )


def render_markdown(
    symbols: list[IndexedSymbol],
    files_scanned: int,
    inventory: list[IndexedFile] | None = None,
    static_symbols: list[IndexedMarker] | None = None,
) -> str:
    """Render the repository inventory and source-symbol index deterministically."""
    file_inventory = inventory or []
    marker_inventory = static_symbols or []
    documented_count = sum(symbol.documented is True for symbol in symbols)
    missing_count = sum(symbol.documented is False for symbol in symbols)
    not_applicable_count = sum(symbol.documented is None for symbol in symbols)
    lines = [
        "# MASTER INDEX — Omarai",
        "",
        "<!-- هذا الملف مُولَّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->",
        "",
        "> هذا فهرس تنقّل ساكن للمستودع، وليس فهرسًا لكل كلمة أو دليلًا على صحة كل ملف.",
        "> يُفهرس Python عبر AST؛ أما JavaScript/TypeScript وHTML وCSS والإعدادات والعناوين",
        "> فتُلتقط رموزها بأساليب ساكنة محدودة، وقد تتضمن النتائج الرمزية بعض المطابقات التقريبية.",
        "",
        "## ملخص الفهرسة",
        "",
        f"- ملفات المستودع في الجرد: **{len(file_inventory)}**",
        f"- ملفات Python المحللة: **{files_scanned}**",
        f"- تعريفات Python المفهرسة: **{len(symbols)}**",
        f"- تعريفات Python موثقة بوجود Docstring: **{documented_count}**",
        f"- تعريفات Python بلا Docstring: **{missing_count}**",
        f"- تعريفات لا ينطبق عليها Docstring: **{not_applicable_count}**",
        f"- الرموز الساكنة الإضافية: **{len(marker_inventory)}**",
        "",
        "## جرد ملفات المستودع",
        "",
        ("يشمل الملفات المؤهلة من الشفرة والواجهة والاختبارات والوثائق والإعدادات وCI. "
        "يُستثنى ملف الفهرس المولّد نفسه لتجنب الحلقة الذاتية، كما تُستثنى المجلدات المولّدة "
        "والبيئات والملفات المحلية الحساسة وقواعد البيانات والمفاتيح المعروفة."),
        "",
        "| الملف | النوع | الحجم (بايت) | عدد الأسطر | نطاق الفهرسة |",
        "|---|---|---:|---:|---|",
    ]

    if file_inventory:
        for item in file_inventory:
            line_count = str(item.line_count) if item.line_count is not None else "غير متاح"
            lines.append(
                "| "
                + " | ".join(
                    (
                        _markdown_cell(item.file),
                        _markdown_cell(item.file_type),
                        str(item.size_bytes),
                        line_count,
                        _markdown_cell(item.indexing_scope),
                    )
                )
                + " |"
            )
    else:
        lines.append("| — | — | — | — | لم يُمرر جرد ملفات إلى المولّد. |")

    lines.extend(
        [
            "",
            "## تعريفات Python من AST",
            "",
            ("> تُحسب حالة Docstring للدوال والكلاسات فقط. المتغيرات والثوابت لا تُصنّف "
            "على أنها موثقة أو ناقصة Docstring."),
            "",
            "| الملف | النوع | الاسم المؤهل | الوصف | حالة Docstring | السطر |",
            "|---|---|---|---|---|---:|",
        ]
    )

    if not symbols:
        lines.append("| — | — | — | لا توجد تعريفات Python في الملفات المؤهلة. | — | — |")
    else:
        for symbol in symbols:
            if symbol.documented is True:
                status = "موثق"
            elif symbol.documented is False:
                status = "ناقص"
            else:
                status = "لا ينطبق"
            lines.append(
                "| "
                + " | ".join(
                    (
                        _markdown_cell(symbol.file),
                        _markdown_cell(symbol.kind),
                        _markdown_cell(symbol.name),
                        _markdown_cell(symbol.description),
                        status,
                        str(symbol.line),
                    )
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "## الرموز الساكنة الإضافية",
            "",
            ("هذا القسم للمساعدة في الوصول إلى الواجهة والإعدادات والوثائق؛ "
            "استخراج الرموز غير المحللة بـAST استدلالي وقد لا يساوي تحليلًا كاملًا للغة."),
            "",
            "| الملف | نوع الرمز | الاسم/القيمة | السطر |",
            "|---|---|---|---:|",
        ]
    )
    if marker_inventory:
        for marker in marker_inventory:
            lines.append(
                "| "
                + " | ".join(
                    (
                        _markdown_cell(marker.file),
                        _markdown_cell(marker.kind),
                        _markdown_cell(marker.name),
                        str(marker.line),
                    )
                )
                + " |"
            )
    else:
        lines.append("| — | — | — | لم تُكتشف رموز ساكنة إضافية. |")

    lines.extend(
        [
            "",
            "---",
            "",
            "## حدود الفهرسة",
            "",
            "- جرد الملفات لا يعني فهرسة محتوى كل ملف نصيًا؛ بعض الملفات مدرجة بالمسار والحجم فقط.",
            "- الملفات النصية الأكبر من 2 MiB أو غير القابلة للقراءة لا تُحلل رموزها.",
            "- لا تُفحص محتويات البيئة الافتراضية والاعتماديات والمجلدات المولدة.",
            "- لا تُقرأ ملفات البيئة المحلية وقواعد البيانات والمفاتيح المعروفة.",
            "- تحليل Python يرفض إنشاء فهرس جزئي عند وجود خطأ نحوي في أي ملف Python مؤهل.",
            ("- يُحدّث هذا الفهرس آليًا عبر GitHub Actions عند دفع تغيير إلى main؛ "
            "وتظل تغييرات المصدر قيد المراجعة حتى تُدمج وفق سياسة المستودع."),
            "",
        ]
    )
    return "\n".join(lines)


def write_if_changed(output_path: Path, content: str) -> bool:
    """Write atomically only when the generated index differs from the existing file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        if output_path.read_text(encoding="utf-8") == content:
            return False
    except FileNotFoundError:
        pass

    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=output_path.parent,
            prefix=f".{output_path.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary_file:
            temporary_file.write(content)
            temporary_path = Path(temporary_file.name)
        temporary_path.replace(output_path)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()
    return True


def _generate(root: Path) -> tuple[str, int, int, int, int, int]:
    """Create the complete in-memory index without writing files."""
    inventory = build_file_inventory(root)
    symbols, python_file_count = scan_repository(root)
    static_symbols = scan_static_symbols(root, inventory)
    markdown = render_markdown(symbols, python_file_count, inventory, static_symbols)
    return (
        markdown,
        python_file_count,
        len(inventory),
        len(symbols),
        sum(symbol.documented is True for symbol in symbols),
        sum(symbol.documented is False for symbol in symbols),
    )


def main(argv: Sequence[str] | None = None) -> int:
    """Generate the living repository index or check that the committed copy is current."""
    parser = argparse.ArgumentParser(
        description="إنشاء/فحص فهرس مستودع Omarai وملفات الشفرة والرموز الساكنة."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="مسار جذر المستودع (الافتراضي: جذر مشروع Omarai).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="لا تكتب أي ملف؛ أعد حالة فشل إذا كان MASTER_INDEX.md قديمًا أو مفقودًا.",
    )
    arguments = parser.parse_args(argv)

    try:
        root = arguments.root.resolve(strict=True)
        if not root.is_dir():
            raise ValueError(f"المسار المحدد ليس مجلدًا: {root}")
        (
            markdown,
            python_file_count,
            repository_file_count,
            symbol_count,
            documented_count,
            missing_count,
        ) = _generate(root)
        output_path = root / INDEX_RELATIVE_PATH

        if arguments.check:
            try:
                current = output_path.read_text(encoding="utf-8")
            except FileNotFoundError:
                print(
                    f"الفهرس غير موجود: {output_path}. شغّل المولّد دون --check.",
                    file=sys.stderr,
                )
                return 1
            if current != markdown:
                print(
                    f"الفهرس قديم: {output_path}. شغّل python docs/generate_index.py.",
                    file=sys.stderr,
                )
                return 1
            changed = False
        else:
            changed = write_if_changed(output_path, markdown)
    except (IndexGenerationError, OSError, ValueError) as exc:
        print(f"خطأ في إنشاء فهرس Omarai: {exc}", file=sys.stderr)
        return 1

    if arguments.check:
        action = "الفهرس محدث والتحقق ناجح"
    else:
        action = "تم تحديث" if changed else "الفهرس محدث بالفعل"
    print(
        f"{action}: {output_path} | "
        f"ملفات المستودع: {repository_file_count} | "
        f"ملفات Python: {python_file_count} | "
        f"تعريفات Python: {symbol_count} | "
        f"موثق: {documented_count} | "
        f"ناقص Docstring: {missing_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
