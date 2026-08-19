#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from typing import Iterable


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def is_ignored(path: Path) -> bool:
    ignored_parts = {".git", "node_modules", "dist", "build", ".venv", "venv"}
    return any(part in ignored_parts for part in path.parts)


def within_depth(path: Path, root: Path, max_depth: int) -> bool:
    rel_parts = path.relative_to(root).parts
    return len(rel_parts) <= max_depth + 1


def collect_files(root: Path, names: Iterable[str], max_depth: int) -> list[Path]:
    matches: list[Path] = []
    for name in names:
        for path in root.rglob(name):
            if not path.is_file():
                continue
            if is_ignored(path):
                continue
            if not within_depth(path, root, max_depth):
                continue
            matches.append(path)
    return sorted(set(matches))


def infer_manager(package_dir: Path, root: Path) -> str:
    if (package_dir / "pnpm-lock.yaml").exists() or (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (package_dir / "yarn.lock").exists() or (root / "yarn.lock").exists():
        return "yarn"
    return "npm"


def main() -> None:
    parser = argparse.ArgumentParser(description="Detect stack hints from repository files.")
    parser.add_argument("--root", default=".", help="Repository root path (default: .)")
    parser.add_argument(
        "--max-depth",
        type=int,
        default=5,
        help="Max recursive depth from root (default: 5)",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    max_depth = args.max_depth

    languages: set[str] = set()
    frameworks: set[str] = set()
    package_manager: set[str] = set()
    run_command = None
    test_command = None

    manifest_paths = collect_files(
        root,
        [
            "package.json",
            "pyproject.toml",
            "requirements.txt",
            "go.mod",
            "Cargo.toml",
            "pnpm-lock.yaml",
            "yarn.lock",
            "package-lock.json",
        ],
        max_depth,
    )

    package_files = [p for p in manifest_paths if p.name == "package.json"]
    pyproject_files = [p for p in manifest_paths if p.name == "pyproject.toml"]
    requirements_files = [p for p in manifest_paths if p.name == "requirements.txt"]
    go_mod_files = [p for p in manifest_paths if p.name == "go.mod"]
    cargo_files = [p for p in manifest_paths if p.name == "Cargo.toml"]

    for p in manifest_paths:
        if p.name in {"pnpm-lock.yaml"}:
            package_manager.add("pnpm")
        if p.name in {"yarn.lock"}:
            package_manager.add("yarn")
        if p.name in {"package-lock.json"}:
            package_manager.add("npm")

    for package_json in package_files:
        languages.add("JavaScript/TypeScript")
        manager = infer_manager(package_json.parent, root)
        package_manager.add(manager)

        try:
            parsed = json.loads(read_text(package_json))
        except json.JSONDecodeError:
            parsed = {}

        scripts = parsed.get("scripts", {}) if isinstance(parsed, dict) else {}
        deps = {}
        if isinstance(parsed, dict):
            deps.update(parsed.get("dependencies", {}) or {})
            deps.update(parsed.get("devDependencies", {}) or {})
        dep_keys = {str(k).lower() for k in deps.keys()}

        if "react" in dep_keys:
            frameworks.add("React")
        if "vite" in dep_keys:
            frameworks.add("Vite")
        if "next" in dep_keys:
            frameworks.add("Next.js")

        rel_dir = str(package_json.parent.relative_to(root))
        prefix = "" if rel_dir == "." else f"(cd {rel_dir} && "
        suffix = "" if rel_dir == "." else ")"

        if run_command is None:
            if "dev" in scripts:
                run_command = f"{prefix}{manager} {'run ' if manager == 'npm' else ''}dev{suffix}"
            elif "start" in scripts:
                run_command = f"{prefix}{manager} {'run ' if manager == 'npm' else ''}start{suffix}"

        if test_command is None and "test" in scripts:
            test_command = f"{prefix}{manager} {'run ' if manager == 'npm' else ''}test{suffix}"

    if pyproject_files or requirements_files:
        languages.add("Python")
        pyproject_text = "\n".join(read_text(p) for p in pyproject_files)
        requirements_text = "\n".join(read_text(p) for p in requirements_files)
        if "pytest" in pyproject_text or "pytest" in requirements_text:
            if test_command is None:
                test_command = "pytest"
        elif (root / "tests").exists() and test_command is None:
            test_command = "python -m unittest"

        if (root / "src/main.py").exists() and run_command is None:
            run_command = "python3 src/main.py"
        elif (root / "main.py").exists() and run_command is None:
            run_command = "python3 main.py"

    if go_mod_files:
        languages.add("Go")
        if test_command is None:
            test_command = "go test ./..."
    if cargo_files:
        languages.add("Rust")
        if test_command is None:
            test_command = "cargo test"

    vite_configs = collect_files(root, ["vite.config.ts", "vite.config.js", "vite.config.mjs"], max_depth)
    next_configs = collect_files(root, ["next.config.js", "next.config.mjs"], max_depth)
    if vite_configs:
        frameworks.add("Vite")
    if next_configs:
        frameworks.add("Next.js")
    if collect_files(root, ["manage.py"], max_depth):
        frameworks.add("Django")
    if collect_files(root, ["app.py"], max_depth) and "Python" in languages:
        frameworks.add("Flask/FastAPI candidate")

    payload = {
        "root": str(root),
        "max_depth": max_depth,
        "languages": sorted(languages),
        "frameworks": sorted(frameworks),
        "package_managers": sorted(package_manager),
        "run_command": run_command,
        "test_command": test_command,
        "ci_present": (root / ".github/workflows").exists(),
        "manifest_paths": [str(p.relative_to(root)) for p in manifest_paths],
    }

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
