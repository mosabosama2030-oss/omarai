"""Text search across Omarai repository source files (no external AI required).

Examples:
  python docs/search_code.py "def analyze"
  python docs/search_code.py --regex "OMARAI_[A-Z_]+" --ext py
  python docs/search_code.py "access token" --max 20
  python docs/search_code.py --root /path/to/omarai "do_POST"
"""

from __future__ import annotations

import argparse
import os
import re
import sys
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
        ".tmp",
        ".idea",
        ".vscode",
        ".aws",
        ".secrets",
        ".ssh",
        "credentials",
        "secrets",
    }
)
SECRET_BASENAMES = frozenset(
    {
        ".env",
        ".env.local",
        ".env.production",
        ".env.staging",
        ".netrc",
        ".npmrc",
        ".pypirc",
        "authorized_keys",
        "client_secret.json",
        "client_secrets.json",
        "credentials",
        "credentials.json",
        "credentials.yaml",
        "credentials.yml",
        "id_dsa",
        "id_ecdsa",
        "id_ed25519",
        "id_rsa",
        "secrets.json",
        "secrets.yaml",
        "secrets.yml",
        "service-account.json",
        "token.json",
    }
)
SENSITIVE_NAME_RE = re.compile(
    r"(?:^|[._-])(?:secret|secrets|credential|credentials|password|passwords|token|tokens|private[_-]?key)(?:[._-]|$)",
    re.IGNORECASE,
)
SENSITIVE_CONFIG_SUFFIXES = frozenset(
    {".cfg", ".conf", ".ini", ".json", ".properties", ".toml", ".txt", ".xml", ".yaml", ".yml"}
)
MAX_SEARCH_FILE_BYTES = 2 * 1024 * 1024


def _is_sensitive_path(path: Path) -> bool:
    """Return whether a local path appears to contain credentials or private runtime data."""
    name = path.name.lower()
    parent_names = {part.lower() for part in path.parts[:-1]}
    if name in SECRET_BASENAMES or parent_names & EXCLUDED_DIRECTORIES:
        return True
    if name.startswith(".env") and name != ".env.example":
        return True
    if name.endswith((".example", ".sample", ".template")):
        return False
    if SENSITIVE_NAME_RE.search(name) and path.suffix.lower() in SENSITIVE_CONFIG_SUFFIXES:
        return True
    return path.suffix.lower() in {".db", ".sqlite", ".sqlite3", ".pem", ".key", ".p12", ".pfx"}
DEFAULT_EXTENSIONS = frozenset(
    {
        ".py",
        ".md",
        ".html",
        ".htm",
        ".js",
        ".css",
        ".json",
        ".yml",
        ".yaml",
        ".toml",
        ".txt",
        ".sh",
        ".example",
    }
)
GITHUB_BLOB_BASE = "https://github.com/mosabosama2030-oss/omarai/blob/main"


@dataclass(frozen=True, slots=True)
class SearchHit:
    file: str
    line: int
    text: str
    context_before: str
    context_after: str

    @property
    def link(self) -> str:
        return f"{GITHUB_BLOB_BASE}/{self.file}#L{self.line}"


def discover_text_files(root: Path, extensions: frozenset[str]) -> list[Path]:
    discovered: list[Path] = []
    for current_directory, directory_names, file_names in os.walk(
        root, topdown=True, followlinks=False
    ):
        directory_names[:] = sorted(
            name
            for name in directory_names
            if name not in EXCLUDED_DIRECTORIES
            and not (Path(current_directory) / name).is_symlink()
        )
        for file_name in sorted(file_names):
            candidate = Path(current_directory) / file_name
            if candidate.is_symlink() or _is_sensitive_path(candidate.relative_to(root)):
                continue
            suffix = candidate.suffix.lower()
            if suffix not in extensions and not file_name.endswith(".example"):
                if file_name not in {".gitignore", ".dockerignore", "Dockerfile", "LICENSE"}:
                    continue
            discovered.append(candidate)
    return sorted(discovered, key=lambda p: p.relative_to(root).as_posix().casefold())


def search_repository(
    root: Path,
    query: str,
    *,
    use_regex: bool = False,
    case_sensitive: bool = False,
    extensions: frozenset[str] = DEFAULT_EXTENSIONS,
    max_results: int = 50,
    context: int = 1,
) -> list[SearchHit]:
    """Return ordered text matches with short context."""
    if not query:
        raise ValueError("استعلام البحث فارغ.")
    if max_results < 1:
        raise ValueError("max_results يجب أن يكون 1 أو أكبر.")
    if context < 0:
        raise ValueError("context لا يمكن أن يكون سالبًا.")

    flags = 0 if case_sensitive else re.IGNORECASE
    if use_regex:
        pattern = re.compile(query, flags)
    else:
        pattern = re.compile(re.escape(query), flags)

    hits: list[SearchHit] = []
    for path in discover_text_files(root, extensions):
        relative = path.relative_to(root).as_posix()
        try:
            if path.stat().st_size > MAX_SEARCH_FILE_BYTES:
                continue
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        lines = text.splitlines()
        for index, line in enumerate(lines):
            if pattern.search(line):
                before = "\n".join(lines[max(0, index - context) : index]) if context else ""
                after = (
                    "\n".join(lines[index + 1 : min(len(lines), index + 1 + context)])
                    if context
                    else ""
                )
                hits.append(
                    SearchHit(
                        file=relative,
                        line=index + 1,
                        text=line.rstrip(),
                        context_before=before.rstrip(),
                        context_after=after.rstrip(),
                    )
                )
                if len(hits) >= max_results:
                    return hits
    return hits


def format_hits(hits: list[SearchHit]) -> str:
    if not hits:
        return "لا توجد نتائج."
    blocks: list[str] = []
    for hit in hits:
        blocks.append(
            f"{hit.file}:{hit.line}\n"
            f"  {hit.text}\n"
            f"  → {hit.link}"
        )
        if hit.context_before:
            blocks[-1] += "\n" + "\n".join(
                f"  · {line}" for line in hit.context_before.splitlines()
            )
        if hit.context_after:
            blocks[-1] += "\n" + "\n".join(
                f"  · {line}" for line in hit.context_after.splitlines()
            )
    return "\n\n".join(blocks)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="بحث نصي داخل ملفات مستودع Omarai (بدون خدمات خارجية)."
    )
    parser.add_argument("query", help="النص أو التعبير المنتظم للبحث.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="جذر المستودع.",
    )
    parser.add_argument("--regex", action="store_true", help="تفسير الاستعلام كتعبير منتظم.")
    parser.add_argument("--case-sensitive", action="store_true", help="مطابقة حساسة لحالة الأحرف.")
    parser.add_argument(
        "--ext",
        action="append",
        default=[],
        help="امتداد ملف للبحث (يمكن تكراره)، مثل: --ext py --ext html",
    )
    parser.add_argument("--max", type=int, default=50, help="أقصى عدد نتائج (افتراضي 50).")
    parser.add_argument(
        "--context",
        type=int,
        default=0,
        help="عدد أسطر السياق قبل/بعد.",
    )
    args = parser.parse_args(argv)

    try:
        root = args.root.resolve(strict=True)
        extensions = (
            frozenset(f".{ext.lstrip('.')}" for ext in args.ext)
            if args.ext
            else DEFAULT_EXTENSIONS
        )
        hits = search_repository(
            root,
            args.query,
            use_regex=args.regex,
            case_sensitive=args.case_sensitive,
            extensions=extensions,
            max_results=max(1, args.max),
            context=max(0, args.context),
        )
    except (OSError, ValueError, re.error) as exc:
        print(f"خطأ في البحث: {exc}", file=sys.stderr)
        return 1

    print(format_hits(hits))
    print(f"\n# عدد النتائج: {len(hits)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
