
from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
cities = range(1, n)
min_cost = float('inf')
best_path = []

for path in permutations(cities):
    route = (0,) + path + (0,)
    cost = 0

    for i in range(len(route) - 1):
        cost += graph[route[i]][route[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = route

print("Shortest Route:", best_path)
print("Minimum Distance:", min_cost)
