#!/usr/bin/env bash
set -euo pipefail

workspace_dir="${1:-/workspaces/veda}"
lock_file="/tmp/veda-uv-sync-watcher.lock"

exec 9>"${lock_file}"
if ! flock -n 9; then
  # Another watcher is already active.
  exit 0
fi

cd "${workspace_dir}"

echo "[uv-sync-watcher] started at $(date -Is)"

run_sync() {
  echo "[uv-sync-watcher] running uv sync --all-packages at $(date -Is)"
  if ! uv sync --all-packages; then
    echo "[uv-sync-watcher] uv sync failed at $(date -Is)"
    return 1
  fi
  echo "[uv-sync-watcher] uv sync completed at $(date -Is)"
}

# Ensure dependencies are aligned when watcher starts.
run_sync || true

# Watch root and package pyproject files, plus lockfile updates.
while inotifywait \
  --quiet \
  --recursive \
  --event close_write,create,delete,move \
  --include '(.*/)?(pyproject\.toml|uv\.lock)$' \
  --exclude '(^|/)(\.git|\.venv|\.pytest_cache|\.ruff_cache|__pycache__)(/|$)' \
  "${workspace_dir}"; do
  run_sync || true
done
