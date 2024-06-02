import unittest

from FIRSTGEO.main import solve_problem


class TestFIRSTGEO(unittest.TestCase):
    """Test cases for problem FIRSTGEO"""
    def test_solve_problem(self):
        self.assertEqual(solve_problem("0010"), 11)
        self.assertEqual(solve_problem("1100"), 21)
        self.assertEqual(solve_problem("0110"), 121)
        self.assertEqual(solve_problem("1110"), 231)
        self.assertEqual(solve_problem("1111"), 441)
