import unittest

from CHANGEXY.main import solve_problem


class TestCHANGEXY(unittest.TestCase):
    """Test cases for problem CHANGEXY."""

    def test_solve_problem(self):
        self.assertEqual(solve_problem(1, 8, 2), 3)
        self.assertEqual(solve_problem(3, 8, 2), 2)
        self.assertEqual(solve_problem(3, 7, 2), 2)
        self.assertEqual(solve_problem(1, 1000000000, 900000000), 100000001)
