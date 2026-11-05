"""Учебный request-based SLO. Все счётчики — за одно и то же окно."""
import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path


def evaluate(total, good, slo=Decimal('0.999')):
    if type(total) is not int or type(good) is not int or not 0 <= good <= total:
        raise ValueError('Нужны целые счётчики: 0 <= good <= total')
    try:
        target = Decimal(str(slo))
    except InvalidOperation as exc:
        raise ValueError('Некорректный SLO') from exc
    if not target.is_finite() or not Decimal(0) < target < Decimal(1):
        raise ValueError('В этой лаборатории SLO задаётся долей строго между 0 и 1')
    bad = total - good
    if total == 0:
        return {'total': 0, 'good': 0, 'bad': 0, 'status': 'no_data',
                'sli': None, 'allowed_bad': None, 'remaining_bad': None,
                'budget_consumed': None, 'burn_rate': None}
    allowed = Decimal(total) * (1 - target)
    error_ratio = Decimal(bad) / total
    return {'total': total, 'good': good, 'bad': bad,
            'status': 'met' if Decimal(bad) <= allowed else 'missed',
            'sli': str(Decimal(good) / total), 'allowed_bad': str(allowed),
            'remaining_bad': str(allowed - bad),
            'budget_consumed': str(Decimal(bad) / allowed),
            'burn_rate': str(error_ratio / (1 - target))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--slo', default='0.999')
    args = parser.parse_args()
    try:
        windows = json.loads(args.input.read_text(encoding='utf-8'))
        if not isinstance(windows, list) or not windows:
            raise ValueError('Нужен непустой JSON-массив непересекающихся интервалов')
        for window in windows:
            evaluate(window['total'], window['good'], args.slo)
        result = evaluate(sum(w['total'] for w in windows), sum(w['good'] for w in windows), args.slo)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
