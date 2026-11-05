#!/usr/bin/env bash
set -euo pipefail
apply=false
if [[ ${1-} == --apply ]]; then
    apply=true
    shift
fi
if [[ $# -ne 1 ]]; then
    printf 'Usage: %s [--apply] DIRECTORY\n' "${0##*/}" >&2
    exit 2
fi
# Sentinel preserves even trailing newlines in the directory name.
if ! directory=$(cd -P -- "$1" && printf '%s.' "$PWD"); then exit 2; fi
directory=${directory%.}
if [[ $directory == / ]]; then
    printf '%s\n' 'Корень файловой системы не является учебным каталогом.' >&2
    exit 2
fi
if [[ $apply == true ]]; then
    find -P "$directory" -type f -empty -delete -print0
else
    find -P "$directory" -type f -empty -print0
fi | while IFS= read -r -d '' file; do
    printf '%q\n' "$file"
done
