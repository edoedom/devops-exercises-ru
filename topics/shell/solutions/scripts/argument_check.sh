#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 1 ]]; then
    printf 'Usage: %s ARGUMENT\n' "${0##*/}" >&2
    exit 2
fi
if [[ $1 == pizza ]]; then
    printf '%s\n' 'with pineapple?'
else
    printf '%s\n' 'I want pizza!'
fi
