#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
MAX_DEPTH="${MAX_DEPTH:-5}"

echo "== Root =="
echo "$ROOT"
echo

echo "== Top-level entries =="
ls -la "$ROOT"
echo

echo "== Key files =="
for f in \
  "package.json" \
  "pnpm-lock.yaml" \
  "yarn.lock" \
  "pyproject.toml" \
  "requirements.txt" \
  "poetry.lock" \
  "Cargo.toml" \
  "go.mod" \
  "README.md"
do
  if [ -f "$ROOT/$f" ]; then
    echo "$f"
  fi
done
echo

echo "== Deep manifests (max depth: $MAX_DEPTH) =="
rg --files "$ROOT" \
  -g "**/package.json" \
  -g "**/pnpm-lock.yaml" \
  -g "**/yarn.lock" \
  -g "**/pyproject.toml" \
  -g "**/requirements.txt" \
  -g "**/poetry.lock" \
  -g "**/Cargo.toml" \
  -g "**/go.mod" \
  -g "!**/.git/**" \
  -g "!**/node_modules/**" \
  -g "!**/dist/**" \
  -g "!**/build/**" \
  | awk -v md="$MAX_DEPTH" -F'/' 'NF <= md+1 {print}' || true
echo

echo "== Deep framework hints =="
rg --files "$ROOT" \
  -g "**/vite.config.ts" \
  -g "**/vite.config.js" \
  -g "**/vite.config.mjs" \
  -g "**/next.config.js" \
  -g "**/next.config.mjs" \
  -g "!**/.git/**" \
  -g "!**/node_modules/**" \
  -g "!**/dist/**" \
  -g "!**/build/**" \
  | awk -v md="$MAX_DEPTH" -F'/' 'NF <= md+1 {print}' || true
echo

echo "== CI workflows =="
if [ -d "$ROOT/.github/workflows" ]; then
  ls -1 "$ROOT/.github/workflows"
else
  echo "(none)"
fi
