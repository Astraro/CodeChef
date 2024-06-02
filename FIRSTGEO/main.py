def solve_problem(s):
    """We count the number of '1' in the input string.
       In case that number is equal to two we have to
       distinguish two cases: Moving left/right or up/down
       vs moving in a quadrant.

       For all other combinations you can simply count the
       number of reachable points.
    """

    n = s.count("1")

    # We can only move in one direction
    if n == 1:
        return 11
    elif n == 2:
        # We can only move forwards and backwards
        if (s[0:2] == "11") | (s[2:4] == "11"):
            return 21
        # We can move in one quadrant
        else:
            return 121
    elif n == 3:
        # We can move in quadrants
        return 231
    else:
        # We can reach every point in the grid
        return 441


if __name__ == "__main__":
    # read number of problem
    T = int(input())

    for _ in range(T):
        # read problem
        s = input()

        # solve problem
        solution = solve_problem(s)

        # print solution
        print(solution)
