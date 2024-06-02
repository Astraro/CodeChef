import unittest

from FOOTBALLTIES.main import solve_problem


class TestFOOTBALLTIES(unittest.TestCase):
    """Test cases for problem FOOTBALLTIES."""
    def test_solve_problem(self):
        self.assertEqual(solve_problem(1, 1), 1)
        self.assertEqual(solve_problem(3, 0), 0)
        self.assertEqual(solve_problem(11, 5), 2)
        self.assertEqual(solve_problem(9, 9), 0)
