import unittest
from RCBCSK.main import solve_problem


class TestRCBCSK(unittest.TestCase):
    """Test cases for problem RCBCSK"""

    def test_solve_problem(self):
        self.assertEqual(solve_problem(20, 0), "RCB")
        self.assertEqual(solve_problem(20, 3), "CSK")
        self.assertEqual(solve_problem(78, 50), "RCB")
