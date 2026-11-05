#!/usr/bin/env bash
set -euo pipefail
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
source "$script_dir/lib/decimal.sh"
if [[ $# -ne 1 ]]; then
    printf 'Usage: %s INTEGER\n' "${0##*/}" >&2
    exit 2
fi
if ! number=$(parse_decimal "$1"); then exit 2; fi
if (( number % 3 == 0 )); then
    printf '%s\n' 'one factor...actually two!'
elif (( number % 2 == 0 )); then
    printf '%s\n' 'one factor'
else
    printf '%s\n' "$number"
fi
