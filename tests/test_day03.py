import unittest

from day_03 import find_co2_scrubber_rating, build_index_to_bit_count_map

test_input = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
]

class Day3Tests(unittest.TestCase):

    def test_co2_scrubber(self):
        expected = '01010'
        actual = find_co2_scrubber_rating(test_input, build_index_to_bit_count_map(test_input))
        self.assertEqual(expected, actual)