"""Generate Omarai's deterministic Python symbol and docstring inventory."""

from __future__ import annotations

import argparse
import ast
import os
import sys
import tempfile
import tokenize
from dataclasses import dataclass
from pathlib import Path
from collections.abc import Sequence


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
MAX_DESCRIPTION_LENGTH = 240


@dataclass(frozen=True, slots=True)
class IndexedSymbol:
    """Represent a class or function discovered in a Python source file."""

    file: str
    name: str
    kind: str
    line: int
    description: str
    documented: bool


class IndexGenerationError(RuntimeError):
    """Signal that a complete and trustworthy index could not be generated."""


class SymbolVisitor(ast.NodeVisitor):
    """Collect classes, functions, methods, and their docstring summaries."""

    def __init__(self, relative_file: str) -> None:
        """Initialize the visitor for one repository-relative Python file."""
        self.relative_file = relative_file
        self.symbols: list[IndexedSymbol] = []
        self.scope: list[str] = []

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

    def _record(
        self,
        node: ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef,
        kind: str,
    ) -> None:
        """Record one definition while preserving its qualified scope."""
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

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Record a class and recursively inspect its body."""
        self._record(node, "كلاس")
        self.scope.append(node.name)
        try:
            self.generic_visit(node)
        finally:
            self.scope.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Record a synchronous function or method and nested definitions."""
        self._record(node, "دالة")
        self.scope.append(node.name)
        try:
            self.generic_visit(node)
        finally:
            self.scope.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        """Record an asynchronous function or method and nested definitions."""
        self._record(node, "دالة غير متزامنة")
        self.scope.append(node.name)
        try:
            self.generic_visit(node)
        finally:
            self.scope.pop()


def discover_python_files(root: Path) -> list[Path]:
    """Return sorted repository-local Python files, excluding generated environments."""
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
            if not file_name.endswith(".py"):
                continue
            candidate = Path(current_directory) / file_name
            if candidate.is_symlink():
                continue
            discovered.append(candidate)

    return sorted(
        discovered,
        key=lambda path: path.relative_to(root).as_posix().casefold(),
    )


def scan_repository(root: Path) -> tuple[list[IndexedSymbol], int]:
    """Parse every eligible Python file or fail without producing a partial index."""
    python_files = discover_python_files(root)
    all_symbols: list[IndexedSymbol] = []
    failures: list[str] = []

    for source_path in python_files:
        relative_file = source_path.relative_to(root).as_posix()
        try:
            # tokenize.open honors Python source encoding declarations.
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
            "تعذر إنشاء فهرس كامل؛ لم يُكتب MASTER_INDEX.md. "
            "أصلح ملفات Python التالية ثم أعد التشغيل:\n" + detail
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


def _markdown_cell(value: str) -> str:
    """Normalize text and escape Markdown table delimiters."""
    return " ".join(value.replace("\r", " ").replace("\n", " ").split()).replace(
        "|", r"\|"
    )


def render_markdown(symbols: list[IndexedSymbol], files_scanned: int) -> str:
    """Render a stable Markdown index; documentation means a non-empty docstring exists."""
    documented_count = sum(symbol.documented for symbol in symbols)
    missing_count = len(symbols) - documented_count
    lines = [
        "# MASTER INDEX — Omarai",
        "",
        "<!-- هذا الملف مُولَّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->",
        "",
        "> حالة التوثيق هنا تعني وجود Docstring غير فارغة فقط؛ ولا تُقيّم دقتها أو كفايتها.",
        "> يعرض عمود الوصف أول فقرة من الـDocstring للمحافظة على سهولة قراءة الفهرس.",
        "",
        "## ملخص الفهرسة",
        "",
        f"- ملفات Python المفحوصة: **{files_scanned}**",
        f"- الدوال والكلاسات المفهرسة: **{len(symbols)}**",
        f"- موثق بوجود Docstring: **{documented_count}**",
        f"- ناقص Docstring: **{missing_count}**",
        "",
        "## سجل الدوال والكلاسات",
        "",
        "| الملف | النوع | اسم الدالة / الكلاس | الوصف | حالة التوثيق | السطر |",
        "|---|---|---|---|---|---:|",
    ]

    if not symbols:
        lines.append("| — | — | — | لم تُكتشف دوال أو كلاسات في ملفات Python المفحوصة. | — | — |")
    else:
        for symbol in symbols:
            status = "موثق" if symbol.documented else "ناقص"
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
            "---",
            "",
            (
                "أُنشئ هذا الفهرس بتحليل AST القياسي في Python. تُستثنى مجلدات البيئات الافتراضية "
                "والاعتماديات والملفات المولدة لتجنب فهرسة نواتج البناء أو نسخ المكتبات."
            ),
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


def main(argv: Sequence[str] | None = None) -> int:
    """Run indexing from the selected repository root and report changes clearly."""
    parser = argparse.ArgumentParser(
        description="إنشاء فهرس Markdown للدوال والكلاسات والـDocstrings في Omarai."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="مسار جذر المستودع (الافتراضي: جذر مشروع Omarai).",
    )
    arguments = parser.parse_args(argv)

    try:
        root = arguments.root.resolve(strict=True)
        if not root.is_dir():
            raise ValueError(f"المسار المحدد ليس مجلدًا: {root}")

        symbols, files_scanned = scan_repository(root)
        output_path = root / "docs" / "MASTER_INDEX.md"
        markdown = render_markdown(symbols, files_scanned)
        changed = write_if_changed(output_path, markdown)
    except (IndexGenerationError, OSError, ValueError) as exc:
        print(f"خطأ في إنشاء فهرس Omarai: {exc}", file=sys.stderr)
        return 1

    action = "تم تحديث" if changed else "الفهرس محدث بالفعل"
    print(
        f"{action}: {output_path} | "
        f"ملفات Python: {files_scanned} | "
        f"تعريفات: {len(symbols)} | "
        f"موثق: {sum(symbol.documented for symbol in symbols)} | "
        f"ناقص: {sum(not symbol.documented for symbol in symbols)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
