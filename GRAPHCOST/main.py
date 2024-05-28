import heapq


def compute_distance(i, j, a):
    return abs(i - j) * max(a[i], a[j])


def solve_problem(N, a):
    """We use the Dijkstra-algorithm to solve the problem."""
    # Introduces an array, which stores the information,
    # which vertices are already visited
    nodes_visited = [i == 0 for i in range(N)]

    # A priority queue
    q = []

    # Initialize priority queue with distances from starting node
    for i in range(N):
        heapq.heappush(q, (compute_distance(0, i, a), i))

    # While the final node is not visited
    while not nodes_visited[N-1]:
        # Select the node with the smallest node from the queue
        distance_node_current, node_current = heapq.heappop(q)
        # If selected node is the last node we can stop the search
        if node_current == N-1:
            return distance_node_current
        # Otherwise, we proceed from the new node
        elif not nodes_visited[node_current]:
            nodes_visited[node_current] = True
            for i in range(N):
                if not nodes_visited[i]:
                    heapq.heappush(q, (distance_node_current + compute_distance(node_current, i, a), i))


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
