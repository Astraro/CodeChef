import heapq


def compute_distance(i, j, a):
    return abs(i - j) * max(a[i], a[j])


def solve_problem(N, a):
    """We use the Dijkstra-algorithm to solve the problem."""
    # Introduces an array that contains the distances from node 0
    distances = [N**3 for _ in range(N)]
    visited = [False for _ in range(N)]

    # A priority queue
    q = []
    heapq.heappush(q, (0, 0))

    while True:
        # Select the node with the smallest distance from the queue
        distance_node_current, node_current = heapq.heappop(q)
        visited[node_current] = True

        if node_current == N-1:
            return distance_node_current

        for neighbour in range(N):
            if not visited[neighbour]:
                distance_current_neighbour = abs(node_current - neighbour)*max(a[node_current], a[neighbour])
                distance_start_current_neighbour = distance_node_current + distance_current_neighbour
                if distance_start_current_neighbour < distances[neighbour]:
                    distances[neighbour] = distance_start_current_neighbour
                    heapq.heappush(q, (distance_start_current_neighbour, neighbour))


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
