# Heuristics

Use these checks to infer the project setup quickly.

## Stack signals

- Node: `package.json`, `pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`
- Python: `pyproject.toml`, `requirements.txt`, `poetry.lock`
- Rust: `Cargo.toml`
- Go: `go.mod`

## Test command signals

- Node:
  - `npm test` if `scripts.test` exists
  - `pnpm test` if `pnpm-lock.yaml` exists
  - `yarn test` if `yarn.lock` exists
- Python:
  - `pytest` if `pytest` appears in `pyproject.toml` or `requirements.txt`
  - `python -m unittest` as fallback if `tests/` exists

## Run command signals

- Node:
  - Prefer `npm run dev` when `scripts.dev` exists
  - Else prefer `npm start` when `scripts.start` exists
- Python:
  - If `src/main.py` exists: `python3 src/main.py`
  - Else if `main.py` exists: `python3 main.py`

## CI / quality signals

- GitHub Actions workflows under `.github/workflows/`
- Lint configs (`.eslintrc*`, `ruff.toml`, `pyproject.toml`, `.prettierrc*`)
- Formatting tools in scripts (`lint`, `format`, `check`)
