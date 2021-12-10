import unittest

from day10 import *


class DayTenTests(unittest.TestCase):

    def test_corrupted_samples(self):
        line = '{([(<{}[<>[]}>{[]{[(<()>'
        c = find_corruption(line)
        self.assertEqual(c, '}')

        line = '[[<[([]))<([[{}[[()]]]'
        c = find_corruption(line)
        self.assertEqual(c, ')')

        line = '[{[{({}]{}}([{[{{{}}([]'
        c = find_corruption(line)
        self.assertEqual(c, ']')

        line = '[<(<(<(<{}))><([]([]()'
        c = find_corruption(line)
        self.assertEqual(c, ')')

        line = '<{([([[(<>()){}]>(<<{{'
        c = find_corruption(line)
        self.assertEqual(c, '>')
