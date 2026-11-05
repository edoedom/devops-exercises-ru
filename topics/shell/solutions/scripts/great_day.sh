#!/usr/bin/env bash
set -euo pipefail
case $# in
    0) printf '%s\n' 'Today is a great day!' ;;
    1) printf 'Today is %s\n' "$1" ;;
    *) printf 'Usage: %s [DAY]\n' "${0##*/}" >&2; exit 2 ;;
esac
