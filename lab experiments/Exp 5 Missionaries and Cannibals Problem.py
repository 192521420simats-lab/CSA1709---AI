
from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (m, c, boat), path = queue.popleft()

        if (m, c, boat) == goal:
            for state in path:
                print(state)
            print("Solution found!")
            return

        for dm, dc in moves:
            if boat == 1:
                nm, nc, nb = m-dm, c-dc, 0
            else:
                nm, nc, nb = m+dm, c+dc, 1

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            rm, rc = 3-nm, 3-nc

            if ((nm == 0 or nm >= nc) and
                (rm == 0 or rm >= rc)):
                state = (nm, nc, nb)

                if state not in visited:
                    visited.add(state)
                    queue.append((state, path + [state]))

    print("No solution found!")

solve()
