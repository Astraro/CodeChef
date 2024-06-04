import unittest

from SUMMODE.main import solve_problem


class TestSUMMODE(unittest.TestCase):
    """Test cases for problem SUMMODE"""
    def test_solve_problem(self):
        self.assertEqual(solve_problem(2, "01"), 4)
        self.assertEqual(solve_problem(4, "0011"), 12)
        self.assertEqual(solve_problem(5, "10101"), 21)
