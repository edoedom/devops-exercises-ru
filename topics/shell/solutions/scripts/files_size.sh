#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 0 ]]; then
    printf 'Usage: %s\n' "${0##*/}" >&2
    exit 2
fi
shopt -s dotglob nullglob
for entry in ./*; do
    # Parse only the numeric prefix; retain the ORIGINAL pathname for display.
    record=$(du -sk "$entry")
    size=${record%%$'\t'*}
    printf '%s\t%q\n' "$size" "${entry#./}"
done
