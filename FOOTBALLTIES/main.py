def solve_problem(x, y):
    """To solve the problem we only have to at the number
       of points of the first team. The result is just
       the number of points mod 3.
    """
    return x % 3


if __name__ == "__main__":
    # read number of problems
    T = int(input())

    for _ in range(T):
        # read problem
        x, y = [int(v) for v in input().split()]

        # solve problem
        solution = solve_problem(x, y)

        # print solution
        print(solution)
