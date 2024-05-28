def solve_problem(x, y):
    if x >= y + 18:
        return "RCB"
    else:
        return "CSK"


if __name__ == "__main__":

    # read input
    x, y = [int(v) for v in input().split()]

    # solve problem
    solution = solve_problem(x, y)

    # print solution
    print(solution)
