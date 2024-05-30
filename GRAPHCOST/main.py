import heapq


def compute_distance(i, j, a):
    return abs(i - j) * max(a[i], a[j])


def solve_problem_using_dijkstra(N, a):
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


def solve_problem(N, a):
    """It turned out that Dijkstra was too slow.
       The following strategy seems to work:
       - We process the nodes in increasing order starting from node 0.
         Everytime, we have a node with weight that is at most the weight
         of the predecessor we choose this node for our path.
       - Afterwards, we use the same strategy going backwards from node N-1.
    """

    distance = 0
    predecessor = 0

    for node_current in range(1, N):
        if a[node_current] <= a[predecessor]:
            distance += (node_current - predecessor) * max(a[predecessor], a[node_current])
            predecessor = node_current

    # In case that we already find a path to the final node, we can return the distance
    if predecessor == N-1:
        return distance

    # Otherwise, we use the same strategy going backwards from N-1
    end_point = predecessor
    predecessor = N-1
    node_current = N-2
    while node_current >= end_point:
        if a[node_current] <= a[predecessor]:
            distance += (predecessor - node_current) * max(a[predecessor], a[node_current])
            predecessor = node_current

        node_current -= 1

    return distance


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
