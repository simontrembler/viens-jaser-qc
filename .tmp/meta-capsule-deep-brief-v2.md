# Repo Kickstart Brief

## 0) Repository hierarchy (emoji map)
- 📁 repo-root/
- 📁 .agents/
- 📁 .agents/skills/
- 📁 scripts/
- 📄 README.md
- 📄 AGENTS.md
- 📄 scripts/sync-skills
- 📄 scripts/validate-skills

## 1) Stack at a glance
- Primary language(s): Markdown, Shell, Python (tooling scripts)
- Framework/runtime: Agent Skills repository structure
- Package manager / tooling: No app package manager manifest detected (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml` absent)

## 2) What to run first
- Install: None required for core skill usage
- Run app: No application runtime detected (tooling repository)
- Run tests: `scripts/validate-skills`
- Lint/format: No dedicated linter command detected at root

## 3) Evidence found
- `scripts/validate-skills`: executable validator for skill frontmatter and references.
- `scripts/sync-skills`: executable sync utility for `~/.agents/skills` and `~/.claude/skills`.
- `.agents/skills/repo-kickstart-brief/SKILL.md`: defines the scan/template/validation workflow used in this test.

## 4) Risks or unknowns
- The path `/home/simon-tremblay/github/meta-capsule` appears to resolve to the same content as `viens-jaser-qc`, so repo identity should be confirmed.
- No CI workflow was found under `.github/workflows/`; checks may be local-only.

## 5) Next 3 steps
1. Confirm the canonical filesystem path for `meta-capsule` vs `viens-jaser-qc` (possible symlink or duplicate mount).
2. Keep `scripts/validate-skills` as the quality gate after every skill edit.
3. Add a CI workflow that runs `scripts/validate-skills` on push.
