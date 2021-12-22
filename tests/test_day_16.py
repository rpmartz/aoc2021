import unittest

from day_16 import *


class DaySixteen(unittest.TestCase):

    def test_D2FE28(self):
        hex = 'D2FE28'
        expected = '110100101111111000101000'
        actual = hex_to_bin(hex)
        self.assertEqual(expected, actual)

    def test_38006F45291200(self):
        hex = '38006F45291200'
        expected = '00111000000000000110111101000101001010010001001000000000'
        actual = hex_to_bin(hex)
        self.assertEqual(expected, actual)

    def test_example_literal(self):
        hex = 'D2FE28'

        expected = Packet(version=6, type_id=4, literal_value=2021)
        actual = parse_packet(StringIO(hex_to_bin(hex)))

        self.assertEqual(expected, actual)
