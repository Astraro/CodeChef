import unittest

from INVEQ.main import solve_problem

class TestINVEQ(unittest.TestCase):
    """Test cases for problem INVEQ"""

    def test_solve_problem(self):
        self.assertEqual(solve_problem(9, "101111000"), 2)
        self.assertEqual(solve_problem(4, "0110"), 1)
        self.assertEqual(solve_problem(1, "1"), 0)
