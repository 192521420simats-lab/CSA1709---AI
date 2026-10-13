
from collections import deque

def water_jug():
    capacity1, capacity2 = 4, 3
    target = 2

    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        path = path + [(a, b)]

        if a == target or b == target:
            for state in path:
                print(state)
            print("Goal reached!")
            return

        states = [
            (capacity1, b),
            (a, capacity2),
            (0, b),
            (a, 0),
            (a - min(a, capacity2 - b),
             b + min(a, capacity2 - b)),
            (a + min(b, capacity1 - a),
             b - min(b, capacity1 - a))
        ]

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

water_jug()
