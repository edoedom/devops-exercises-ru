#!/usr/bin/env bash
set -euo pipefail
case $# in
    0) printf 'Usage: %s <argument>\n' "${0##*/}" >&2; exit 2 ;;
    1) printf 'Got it: %s\n' "$1" ;;
    *) printf '%s\n' 'hey hey...too many!' >&2; exit 2 ;;
esac
