
colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

color = {}

def is_safe(region, c):
    for neighbor in graph[region]:
        if neighbor in color and color[neighbor] == c:
            return False
    return True

def map_coloring(regions):
    if not regions:
        return True

    region = regions[0]

    for c in colors:
        if is_safe(region, c):
            color[region] = c

            if map_coloring(regions[1:]):
                return True

            del color[region]

    return False

regions = list(graph.keys())

if map_coloring(regions):
    print("Map Coloring Solution:")
    for region, c in color.items():
        print(region, ":", c)
else:
    print("No solution exists")
