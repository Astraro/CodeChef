def solve_problem(a, b, k):
    """First approach to solve the problem: We start from b.
       If it is possible to divide b by k without remainder,
       and the result is still at least as large as a,
       we divide b by k. Otherwise, we decrease b several times by 1.
    """
    n = 0
    i = 0
    while b > a:
        remainder = b % k
        # Case 1: b is divisible by k, and the result is at least as large as a
        if (remainder == 0) & (b/k >= a):
            b = b // k
            n += 1
        # Case 2: b is divisible by k, but the result is smaller than a
        elif remainder == 0:
            n += (b - a)
            break
        # Case 3: b is not divisible by k
        else:
            b -= remainder
            n += remainder

    return n


if __name__ == "__main__":
    # read number of problems
    T = int(input())

    for _ in range(T):
        a, b, k = [int(v) for v in input().split()]

        solution = solve_problem(a, b, k)

        print(solution)
