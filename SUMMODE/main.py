def solve_problem(n, s):
    """"""
    n_0 = [0] + [s[:i].count("0") for i in range(1, n+1)]
    n_1 = [0] + [s[:i].count("1") for i in range(1, n+1)]

    m = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            sub_0 = n_0[j] - n_0[i-1]
            sub_1 = n_1[j] - n_1[i-1]
            m += (1 + (sub_0 == sub_1))

    return m


if __name__ == "__main__":

    # read number of problems
    T = int(input())

    for _ in range(T):
        # read problem
        n = int(input())
        s = input()

        # solve problem
        solution = solve_problem(n, s)

        # print solution
        print(solution)