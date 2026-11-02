#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")"

command -v uv >/dev/null || {
    echo "uv is not installed" >&2
    exit 1
}

uv lock --check --offline --quiet || {
    echo "uv.lock is out of date with pyproject.toml" >&2
    exit 1
}