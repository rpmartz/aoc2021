from unittest import TestCase

from day_22 import *


class Test(TestCase):
    def test_cuboid_from_line(self):
        line = 'on x=10..12,y=10..12,z=10..12'

        result = cuboid_from_line(line)

        self.assertEqual('on', result[0])
        points = result[1]
        self.assertEqual(27, len(points))
        self.assertTrue((10, 10, 10) in points)
        self.assertTrue((12, 12, 12) in points)

    def test_example(self):
        lines = [
            'on x=10..12,y=10..12,z=10..12',
            'on x=11..13,y=11..13,z=11..13',
            'off x=9..11,y=9..11,z=9..11',
            'on x=10..10,y=10..10,z=10..10'
        ]

        state = process(lines)
        self.assertEqual(39, len(state['on']))
