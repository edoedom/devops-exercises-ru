# Bash helper: signed decimal integer with 1-9 digits, leading zeroes allowed.
parse_decimal() {
    if [[ $# -ne 1 || ! $1 =~ ^([+-]?)([0-9]{1,9})$ ]]; then
        printf '%s\n' 'Ожидается целое десятичное число: знак и не более 9 цифр.' >&2
        return 2
    fi
    local sign=${BASH_REMATCH[1]} digits=${BASH_REMATCH[2]} value
    value=$((10#$digits))
    if [[ $sign == - ]]; then value=$((-value)); fi
    printf '%s\n' "$value"
}
