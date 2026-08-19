# Repo Kickstart Brief

## 0) Repository hierarchy (emoji map)
- 📁 repo-root/
- 📄 package.json
- 📁 .github/workflows/
- 📄 .github/workflows/ci.yml
- 📄 README.md

## 1) Stack at a glance
- Primary language(s): TypeScript, Markdown
- Framework/runtime: Node.js
- Package manager / tooling: npm

## 2) What to run first
- Install: `npm install`
- Run app: `npm run dev`
- Run tests: `npm test`
- Lint/format: `npm run lint`

## 3) Evidence found
- `package.json`: contains scripts `dev`, `test`, `lint`
- `.github/workflows/ci.yml`: CI workflow is configured
- `README.md`: documents local setup commands

## 4) Risks or unknowns
- Commands are inferred from root-level scripts only; subpackages may differ.
- No explicit runtime version found in `.nvmrc` or `engines`.

## 5) Next 3 steps
1. Run install and test commands to validate assumptions.
2. Confirm required env vars from README or `.env.example`.
3. Open CI workflow to mirror local checks.
