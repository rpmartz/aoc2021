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

    def test_versions(self):
        hex = 'D2FE28'
        expected_version = 6
        actual = get_packet_version(hex_to_bin(hex))
        self.assertEqual(expected_version, actual)

        hex = '38006F45291200'
        expected_version = 1
        actual = get_packet_version(hex_to_bin(hex))
        self.assertEqual(expected_version, actual)

    def test_type(self):
        hex = 'D2FE28'
        expected_type = 4
        actual = get_packet_type(hex_to_bin(hex))
        self.assertEqual(expected_type, actual)

        hex = '38006F45291200'
        expected_type = 6
        actual = get_packet_type(hex_to_bin(hex))
        self.assertEqual(expected_type, actual)
