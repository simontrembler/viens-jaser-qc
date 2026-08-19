# Gotchas

Keep these pitfalls in mind when building the brief.

- A `package.json` alone does not guarantee `dev` or `test` scripts exist.
- A `tests/` directory does not guarantee tests actually run.
- Monorepos may have commands in subpackages instead of repo root.
- Generated folders (`dist/`, `build/`) are not proof of current build steps.
- CI files may be stale; mention them as "present" rather than "authoritative."
- If no clear run/test command is detected, say so explicitly and propose how to confirm.
