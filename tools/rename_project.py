# tools/rename_project.py
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".mypy_cache",
    ".ruff_cache",
    ".pytest_cache",
    "build",
    "dist",
}


def run(cmd: list[str]) -> None:
    subprocess.check_call(cmd)


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def replace_text_in_file(path: Path, old: str, new: str) -> bool:
    try:
        txt = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False

    new_txt = txt.replace(old, new)
    if new_txt != txt:
        path.write_text(new_txt, encoding="utf-8")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--old", required=True)
    parser.add_argument("--new", required=True)
    args = parser.parse_args()

    old = args.old.strip()
    new = args.new.strip()

    if not new:
        raise SystemExit("NEW_NAME boş olamaz.")

    src_old = Path("src") / old
    src_new = Path("src") / new

    if not src_old.is_dir():
        raise SystemExit(f"{src_old} bulunamadı.")
    if src_new.exists():
        raise SystemExit(f"{src_new} zaten var.")

    # 1) Move package dir (use git mv if possible)
    try:
        run(["git", "mv", str(src_old), str(src_new)])
    except Exception:
        src_old.rename(src_new)

    # 2) Update references
    candidates: list[Path] = []

    # Common config/docs
    for p in [
        Path("pyproject.toml"),
        Path("Dockerfile"),
        Path("docker-compose.yml"),
        Path("Makefile"),
        Path("README.md"),
        Path(f"{old}.code-workspace"),
        Path(".github/workflows/ci.yml"),
        Path(".pre-commit-config.yaml"),
    ]:
        if p.exists():
            candidates.append(p)

    # Scan text files
    exts = {".py", ".toml", ".yml", ".yaml", ".md", ".json", ".txt", ".ini", ".cfg", ".env", ".example"}
    for p in Path(".").rglob("*"):
        if not p.is_file():
            continue
        if should_skip(p):
            continue
        if p.suffix in exts:
            candidates.append(p)

    # Deduplicate
    uniq: list[Path] = []
    seen: set[Path] = set()
    for p in candidates:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            uniq.append(p)

    changed = 0
    for p in uniq:
        if p.exists() and replace_text_in_file(p, old, new):
            changed += 1

    # 3) Rename workspace file name if present
    old_ws = Path(f"{old}.code-workspace")
    new_ws = Path(f"{new}.code-workspace")
    if old_ws.exists():
        try:
            run(["git", "mv", str(old_ws), str(new_ws)])
        except Exception:
            old_ws.rename(new_ws)

    print(f"✅ Rename tamamlandı: {old} -> {new}")
    print(f"✅ Güncellenen dosya sayısı: {changed}")
    print("➡️  Kontrol: git diff")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
