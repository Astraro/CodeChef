def solve_problem(N, a):
    pass


if __name__ == "__main__":
    # read number of problems
    T = int(input())

    for i in range(T):
        # read problem
        N = int(input())
        a = [int(v) for v in input().split()]

        # solve problem
        solution = solve_problem(N, a)

        # print solution
        print(solution)
