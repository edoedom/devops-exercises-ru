#!/usr/bin/env bash
set -euo pipefail
printf 'First: %s\n' "${1-}"
printf 'Count: %s\n' "$#"
# "$@" preserves each argument, including empty strings, spaces and wildcards.
for argument in "$@"; do
    printf 'Arg: %s\n' "$argument"
done
