from decimal import Decimal
import importlib.util
from pathlib import Path
import random
import unittest

ROOT = Path(__file__).resolve().parent.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


budget = load('budget_lab', 'topics/sre/exercises/error_budget/budget.py')
binary = load('binary_example', 'coding/python/binary_search.py')
merge = load('merge_example', 'coding/python/merge_sort.py')


class BudgetTests(unittest.TestCase):
    def test_exact_threshold_and_overspend(self):
        self.assertEqual(budget.evaluate(1000, 999)['status'], 'met')
        result = budget.evaluate(1000, 998)
        self.assertEqual(result['status'], 'missed')
        self.assertEqual(Decimal(result['remaining_bad']), Decimal(-1))
        self.assertEqual(Decimal(result['budget_consumed']), Decimal(2))

    def test_no_data_is_not_success(self):
        result = budget.evaluate(0, 0)
        self.assertEqual(result['status'], 'no_data')
        self.assertIsNone(result['sli'])
        self.assertIsNone(result['burn_rate'])

    def test_invalid_counts_and_targets(self):
        for counts in [(-1, 0), (1, 2), (1, -1), (1.5, 1), (True, 0)]:
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                budget.evaluate(*counts)
        for slo in ['NaN', 'Infinity', '0', '1', '-0.5', '99.9', 'no']:
            with self.subTest(slo=slo), self.assertRaises(ValueError):
                budget.evaluate(10, 10, slo)

    def test_weighted_sli_and_fixture(self):
        import json
        windows = json.loads((ROOT / 'topics/sre/exercises/error_budget/requests.json').read_text())
        total = sum(w['total'] for w in windows)
        good = sum(w['good'] for w in windows)
        result = budget.evaluate(total, good)
        self.assertEqual(Decimal(result['sli']), Decimal('0.9982'))
        self.assertEqual(Decimal(result['remaining_bad']), Decimal(-8))


class Algorithms(unittest.TestCase):
    def test_merge_sort_does_not_mutate_and_preserves_duplicates(self):
        rng = random.Random(42)
        for size in range(60):
            values = [rng.randrange(-10, 11) for _ in range(size)]
            before = values.copy()
            self.assertEqual(merge.merge_sort(values), sorted(values))
            self.assertEqual(values, before)

    def test_binary_search_empty_missing_boundaries_and_duplicates(self):
        rng = random.Random(7)
        for size in range(40):
            values = sorted(rng.randrange(-10, 11) for _ in range(size))
            for target in range(-12, 13):
                index = binary.find_target_in_list(target, values)
                if target in values:
                    self.assertTrue(0 <= index < len(values))
                    self.assertEqual(values[index], target)
                else:
                    self.assertEqual(index, -1)
