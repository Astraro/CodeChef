import unittest

from GRAPHCOST.main import (
    compute_distance,
    solve_problem,
    solve_problem_using_dijkstra
)


class TestGRAPHCOST(unittest.TestCase):
    """Test cases for problem GRAPHCOST"""

    def test_compute_distance(self):
        self.assertEqual(compute_distance(0, 1, [2, 1, 2, 1]), 2)
        self.assertEqual(compute_distance(1, 0, [2, 1, 2, 1]), 2)
        self.assertEqual(compute_distance(0, 3, [2, 1, 2, 1]), 6)
        self.assertEqual(compute_distance(2, 0, [2, 1, 2, 1]), 4)

    def test_solve_problem_using_dijkstra(self):
        self.assertEqual(solve_problem_using_dijkstra(4, [2, 1, 1, 1]), 4)
        self.assertEqual(solve_problem_using_dijkstra(3, [3, 2, 1]), 5)
        self.assertEqual(solve_problem_using_dijkstra(5, [2, 4, 5, 2, 3]), 9)
        self.assertEqual(solve_problem_using_dijkstra(
            10, [4, 3, 1, 1, 2, 4, 1, 2, 2, 3]), 18
        )
        self.assertEqual(solve_problem_using_dijkstra(7, [3, 2, 1, 1, 4, 5, 1]), 9)

    def test_solve_problem(self):
        self.assertEqual(solve_problem(4, [2, 1, 1, 1]), 4)
        self.assertEqual(solve_problem(3, [3, 2, 1]), 5)
        self.assertEqual(solve_problem(5, [2, 4, 5, 2, 3]), 9)
        self.assertEqual(solve_problem(10, [4, 3, 1, 1, 2, 4, 1, 2, 2, 3]), 18)
        self.assertEqual(solve_problem(7, [3, 2, 1, 1, 4, 5, 1]), 9)
