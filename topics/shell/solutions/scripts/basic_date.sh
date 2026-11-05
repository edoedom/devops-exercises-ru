#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 0 ]]; then
    printf 'Usage: %s\n' "${0##*/}" >&2
    exit 2
fi
date +%F > the_date.txt
