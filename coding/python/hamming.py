"""Even-parity Hamming: позиции считаются с 1 слева, parity bits — степени двойки."""


def validate(bits):
    if not isinstance(bits, str) or not bits or set(bits) - {'0', '1'}:
        raise ValueError('Нужна непустая строка из 0 и 1')


def encode_even(bits):
    validate(bits)
    parity_count = 0
    while (1 << parity_count) < len(bits) + parity_count + 1:
        parity_count += 1
    result = [0] * (len(bits) + parity_count + 1)
    data = iter(bits)
    for position in range(1, len(result)):
        if position & (position - 1):
            result[position] = int(next(data))
    for bit in range(parity_count):
        parity_position = 1 << bit
        result[parity_position] = sum(result[position] for position in range(1, len(result))
                                      if position & parity_position) % 2
    return ''.join(str(bit) for bit in result[1:])


def syndrome(bits):
    validate(bits)
    result = 0
    for position, bit in enumerate(bits, 1):
        if bit == '1':
            result ^= position
    return result
