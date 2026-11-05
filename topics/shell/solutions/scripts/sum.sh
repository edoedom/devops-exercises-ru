#!/usr/bin/env bash
set -euo pipefail
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
source "$script_dir/lib/decimal.sh"
if [[ $# -ne 2 ]]; then
    printf 'Usage: %s INTEGER INTEGER\n' "${0##*/}" >&2
    exit 2
fi
if ! left=$(parse_decimal "$1"); then exit 2; fi
if ! right=$(parse_decimal "$2"); then exit 2; fi
sum() { printf '%s\n' "$(($1 + $2))"; }
sum "$left" "$right"
