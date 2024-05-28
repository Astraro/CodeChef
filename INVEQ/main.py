def solve_problem(N, S):
    n_changes = 0
    for i in range(1, N):
        n_changes += (S[i] != S[i - 1])

    solution = (n_changes + 1) // 2

    return solution


if __name__ == "__main__":
    # read number of problems
    T = int(input())

    for i in range(T):
        # read problem
        N = int(input())
        S = input()

        # solve problem
        solution = solve_problem(N, S)

        # print solution
        print(solution)
