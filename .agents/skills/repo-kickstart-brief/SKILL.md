---
name: repo-kickstart-brief
description: >-
  Create a quick onboarding brief for a code repository: detect stack, find run
  and test commands, summarize risks, and propose next steps. Use this skill
  when the user asks how to start in a repo, wants a project overview, or asks
  what to run first.
metadata:
  author: simontrembler
---

# repo-kickstart-brief

Build a concise, practical "start here" brief for any repository.

## Procedure

1. Run discovery scripts in `scripts/`.
2. Fill the report using `assets/brief-template.md`.
3. Validate the report structure with `scripts/validate_brief.py`.
4. If validation fails, fix and re-check.

## When to load references

- Unsure how to infer stack/test/build signals -> read `references/heuristics.md`.
- Unsure about common false positives -> read `references/gotchas.md`.

## Output contract

- Keep it short and actionable.
- Use only observed evidence from files/commands.
- Do not invent commands or frameworks.
- Include concrete repo paths in findings.
- Include a repository hierarchy section with emojis (`📁` for folders, `📄` for files).

## Commands

```bash
bash scripts/scan_repo.sh
python3 scripts/detect_stack.py
```

Use the outputs as source material, then format with `assets/brief-template.md`.
When possible, infer hierarchy from actual paths discovered by the scan.

## Validation loop

Write draft to `brief.md`, then:

```bash
python3 scripts/validate_brief.py brief.md
```

Only finalize once validation passes.
