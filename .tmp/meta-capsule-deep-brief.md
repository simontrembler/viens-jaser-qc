# Repo Kickstart Brief

## 1) Stack at a glance
- Primary language(s): Markdown + shell + Python (skill toolkit repo)
- Framework/runtime: Agent Skills structure (`.agents/skills/*/SKILL.md`)
- Package manager / tooling: No app package manager manifest at root (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml` absent)

## 2) What to run first
- Install: None required for core usage (skills are markdown files + local scripts)
- Run app: Not an app runtime repo; primary workflow is skill sync/validation
- Run tests: `scripts/validate-skills`
- Lint/format: No dedicated linter command declared at root; use `scripts/validate-skills` as quality gate

## 3) Evidence found
- `scripts/validate-skills`: executable validation script for all `SKILL.md` files.
- `scripts/sync-skills`: executable sync script that links skills to `~/.agents/skills` and `~/.claude/skills`.
- `.agents/skills/repo-kickstart-brief/SKILL.md`: contains procedure for repo scanning, templating, and brief validation.

## 4) Risks or unknowns
- This repository appears to be a skills/tooling monorepo, not a deployable service; expecting app run commands would be misleading.
- No CI workflow under `.github/workflows/`; script checks may rely on local discipline unless CI is added later.

## 5) Next 3 steps
1. Run `scripts/validate-skills` after each skill edit to keep frontmatter/references clean.
2. Run `scripts/sync-skills` to propagate updated skills into user-level directories.
3. If you want stronger automation, add a CI job that executes `scripts/validate-skills` on every push.
