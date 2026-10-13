
import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

def astar(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            print("Shortest Path:", path)
            print("Total Cost:", cost)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, distance in graph[node].items():
            if neighbor not in visited:
                new_cost = cost + distance
                new_f = new_cost + heuristic[neighbor]
                heapq.heappush(
                    queue,
                    (new_f, new_cost, neighbor,
                     path + [neighbor])
                )

    print("Path not found!")

astar('A', 'D')
