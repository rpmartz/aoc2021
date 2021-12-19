import unittest

from day_16 import *


class DaySixteen(unittest.TestCase):

    def test_D2FE28(self):
        hex = 'D2FE28'
        expected = '110100101111111000101000'
        actual = hex_to_bin(hex)
        self.assertEqual(expected, actual)
