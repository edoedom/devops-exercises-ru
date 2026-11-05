#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 0 ]]; then
    printf 'Usage: %s\n' "${0##*/}" >&2
    exit 2
fi
message='Hello World'
printf '%s\n' "$message" > amazing_output.txt
