def solve_problem(a, b, k):
    """First approach to solve the problem: We start from b.
       If it is possible to divide b by k without remainder,
       and the result is still at least as large as a,
       we divide b by k. Otherwise, we decrease b by 1.
    """
    n = 0
    while b > a:
        if (b % k == 0) & (b/k >= a):
            b /= k
        else:
            b -= 1
        n += 1

    return n


if __name__ == "__main__":
    # read number of problems
    T = int(input())

    for _ in range(T):
        a, b, k = [int(v) for v in input().split()]

        solution = solve_problem(a, b, k)

        print(solution)
