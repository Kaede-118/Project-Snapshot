import os
import sys
from pathlib import Path
FULL_MODE = any(
    arg.lower() == "full"
    for arg in sys.argv[1:]
)
def get_root() -> Path:

    args = sys.argv[1:]

    if args and args[-1].lower() == "full":
        args = args[:-1]

    if args:

        target = Path(args[0]).resolve()

        if not target.exists():
            print(f"Directory not found: {target}")
            sys.exit(1)

        if not target.is_dir():
            print(f"Not a directory: {target}")
            sys.exit(1)

        return target

    return Path.cwd()

OUTPUT_FILE = "_ProjectSnapshot.txt"

MAX_FILE_SIZE = (
    50 * 1024 * 1024
    if FULL_MODE
    else 5 * 1024 * 1024
)

MAX_LINES = (
    999999
    if FULL_MODE
    else 300
)

IGNORE_DIRS = {
    ".git",
    ".idea",
    ".vscode",

    "target",
    "build",
    "dist",
    ".mvn",
    "images",

    "node_modules",

    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",

    ".gradle",
    ".next",
    ".nuxt",

    ".cache",
    "tmp",
    "temp",

    "logs",
    "log"
}

IGNORE_FILES = {
    OUTPUT_FILE,
    "mvnw",
    "mvnw.cmd",
    "HELP.md",

    ".gitignore",
    ".gitattributes",

    "LICENSE",
    "LICENSE.txt",

    "package-lock.json",
    "yarn.lock"
}

IGNORE_EXTS = {
    ".class",
    ".jar",
    ".war",

    ".zip",
    ".7z",
    ".rar",

    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",

    ".mp4",
    ".mkv",
    ".avi",
    ".mov",

    ".mp3",
    ".wav",
    ".flac",

    ".exe",
    ".dll",
    ".so",

    ".pyc"
}


def is_binary(path: Path) -> bool:
    try:
        with open(path, "rb") as f:
            chunk = f.read(4096)
            return b"\0" in chunk
    except Exception:
        return True


def should_skip(path: Path) -> bool:
    name = path.name

    if name in IGNORE_FILES:
        return True

    if name in IGNORE_DIRS:
        return True

    if path.suffix.lower() in IGNORE_EXTS:
        return True

    return False


def build_tree(root: Path) -> str:
    lines = []

    def walk(current: Path, prefix=""):
        try:
            entries = sorted(
                current.iterdir(),
                key=lambda x: (x.is_file(), x.name.lower())
            )
        except PermissionError:
            return

        entries = [
            e for e in entries
            if not should_skip(e)
        ]

        for i, entry in enumerate(entries):
            last = i == len(entries) - 1

            connector = "└─ " if last else "├─ "

            lines.append(
                prefix +
                connector +
                entry.name +
                ("/" if entry.is_dir() else "")
            )

            if entry.is_dir():
                walk(
                    entry,
                    prefix + ("    " if last else "│   ")
                )

    walk(root)

    return "\n".join(lines)


def collect_files(root: Path):
    files = []

    for current_root, dirs, filenames in os.walk(root):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIRS
        ]

        for filename in filenames:

            path = Path(current_root) / filename

            if should_skip(path):
                continue

            files.append(path)

    return sorted(files)


def dump_file(path: Path) -> str:
    try:
        size = path.stat().st_size

        if size > MAX_FILE_SIZE:
            return (
                f"[Large file skipped: "
                f"{size / 1024 / 1024:.1f} MB]"
            )

        if is_binary(path):
            return "[Binary file skipped]"

        text = path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        lines = text.splitlines()

        if not FULL_MODE and len(lines) > MAX_LINES:
            remain = len(lines) - MAX_LINES

            return (
                    "\n".join(lines[:MAX_LINES]) +
                    f"\n\n[Truncated {remain} lines]"
            )

        return text

    except Exception as e:
        return f"[Read error: {e}]"




def main():
    root = get_root()

    print(f"Root: {root}")
    print(f"Mode: {'FULL' if FULL_MODE else f'HEAD({MAX_LINES})'}")
    print("Scanning...")

    tree = build_tree(root)
    files = collect_files(root)

    output = []

    output.append("PROJECT TREE")
    output.append("=" * 80)
    output.append(str(root))
    output.append("")
    output.append(tree)

    output.append("")
    output.append("FILES")
    output.append("=" * 80)

    for file in files:
        rel = file.relative_to(root)

        output.append("")
        output.append("-" * 80)
        output.append(str(rel))
        output.append("-" * 80)

        output.append(
            dump_file(file)
        )

    out_path = root / OUTPUT_FILE

    out_path.write_text(
        "\n".join(output),
        encoding="utf-8"
    )

    print()
    total_size = sum(
        f.stat().st_size
        for f in files
    )

    print(f"Files: {len(files)}")
    print(f"Size : {total_size / 1024 / 1024:.2f} MB")
    print(f"Output: {out_path}")
    print("Done.")


if __name__ == "__main__":
    main()