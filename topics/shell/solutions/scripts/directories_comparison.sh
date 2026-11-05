#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 2 ]]; then
    printf 'Usage: %s DIRECTORY DIRECTORY\n' "${0##*/}" >&2
    exit 2
fi
if [[ ! -d $1 || ! -d $2 ]]; then
    printf '%s\n' 'Оба аргумента должны быть существующими каталогами.' >&2
    exit 2
fi
# GNU diff: 0 = equal, 1 = different, 2 = error. Compare symlinks as links.
diff --recursive --no-dereference -- "$1" "$2"
