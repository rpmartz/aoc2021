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
