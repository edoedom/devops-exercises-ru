import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


cidr = load('cidr_lab','topics/network/exercises/cidr/cidr.py')
hamming = load('hamming_lab','coding/python/hamming.py')


class CIDR(unittest.TestCase):
    def test_usual_subnet(self):
        result = cidr.describe('198.51.100.0/24')
        self.assertEqual(result['netmask'],'255.255.255.0')
        self.assertEqual(result['address_count'],256)
        self.assertEqual(result['host_count'],254)
        self.assertEqual((result['first_host'],result['last_host']),('198.51.100.1','198.51.100.254'))

    def test_point_to_point_and_host_routes_are_not_minus_two(self):
        for prefix,count,last in [('198.51.100.0/31',2,'198.51.100.1'),('198.51.100.42/32',1,'198.51.100.42')]:
            with self.subTest(prefix=prefix):
                result = cidr.describe(prefix)
                self.assertEqual(result['host_count'],count)
                self.assertEqual(result['last_host'],last)
                self.assertFalse(result['has_conventional_broadcast'])

    def test_invalid_input_and_noncanonical_network(self):
        for value in ['198.51.100.86/24','198.51.100.0/33','2001:db8::/64','not-cidr','198.51.100.0',None,True]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                cidr.describe(value)

    def test_longest_prefix_not_first_match(self):
        routes = ['0.0.0.0/0','198.51.100.0/24','198.51.100.128/25']
        self.assertEqual(cidr.route_for('198.51.100.200',routes),'198.51.100.128/25')
        self.assertEqual(cidr.route_for('198.51.100.20',list(reversed(routes))),'198.51.100.0/24')
        self.assertEqual(cidr.route_for('203.0.113.1',routes),'0.0.0.0/0')

    def test_no_matching_route(self):
        self.assertIsNone(cidr.route_for('203.0.113.1',['198.51.100.0/24']))
        self.assertIsNone(cidr.route_for('203.0.113.1',[]))


class Hamming(unittest.TestCase):
    def test_published_word_and_information_bits(self):
        data = '100111010001101'
        word = hamming.encode_even(data)
        self.assertEqual(word,'00110011110100011101')
        self.assertEqual(hamming.syndrome(word),0)
        extracted = ''.join(bit for position,bit in enumerate(word,1) if position & (position-1))
        self.assertEqual(extracted,data)
        self.assertIn(word,(ROOT/'README.md').read_text())

    def test_every_single_bit_flip_is_detected_at_its_position(self):
        word = hamming.encode_even('100111010001101')
        for index in range(len(word)):
            changed = word[:index]+('0' if word[index]=='1' else '1')+word[index+1:]
            self.assertEqual(hamming.syndrome(changed),index+1)

    def test_invalid_bits(self):
        for value in ['', '102','foo',None,1010]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                hamming.encode_even(value)
