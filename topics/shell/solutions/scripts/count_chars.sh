#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 0 ]]; then
    printf 'Usage: %s\n' "${0##*/}" >&2
    exit 2
fi
# UTF-8 character count depends on LC_CTYPE. NUL bytes are outside this text interface.
while IFS= read -r line || [[ -n $line ]]; do
    if [[ -z $line ]]; then break; fi
    printf '%s\n' "${#line}"
done
