#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 1 || ! $1 =~ ^[a-zA-Z0-9_.:%-]+$ || $1 == -* ]]; then
    printf 'Usage: %s IP_OR_HOSTNAME\n' "${0##*/}" >&2
    exit 2
fi
host=$1
if ! command -v ping >/dev/null 2>&1; then
    printf '%s\n' 'Команда ping не установлена.' >&2
    exit 2
fi
if ping -n -c 1 -W 2 -- "$host" >/dev/null 2>&1; then
    printf 'ICMP reply: %s\n' "$host"
else
    status=$?
    if [[ $status -eq 1 ]]; then
        printf 'No ICMP reply: %s\n' "$host"
        exit 1
    fi
    printf 'Probe failed: %s\n' "$host" >&2
    exit 2
fi
