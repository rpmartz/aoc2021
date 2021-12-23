from unittest import TestCase

from day_17 import process_step, build_target_grid


class Test(TestCase):

    def test_process_step_positive_x_start(self):
        v = (6, 3)
        expected_1 = (5, 2)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_1, v)

        expected_2 = (4, 1)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_2, v)

        expected_3 = (3, 0)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_3, v)

        expected_4 = (2, -1)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_4, v)

        expected_5 = (1, -2)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_5, v)

        expected_6 = (0, -3)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_6, v)

        expected_7 = (0, -4)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_7, v)

    def test_process_step_negative_x_start(self):
        v = (-3, 3)
        expected_1 = (-2, 2)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_1, v)

        expected_2 = (-1, 1)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_2, v)

        expected_3 = (0, 0)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_3, v)

        expected_4 = (0, -1)
        v = process_step(v[0], v[1])
        self.assertEqual(expected_4, v)

    def test_build_target_grid(self):
        target_grid = build_target_grid(150, 171, -70, -129)

        corners = {(150, -70), (150, -129), (171, -129), (171, -129)}
        self.assertTrue(all([point in target_grid for point in corners]))
