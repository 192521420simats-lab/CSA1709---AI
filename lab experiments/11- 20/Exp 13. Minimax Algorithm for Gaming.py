
def minimax(depth, node, maximizing, values):
    if depth == 3:
        return values[node]

    if maximizing:
        best = float('-inf')

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i,
                            False, values)
            best = max(best, value)

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i,
                            True, values)
            best = min(best, value)

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = minimax(0, 0, True, values)

print("Best Value:", result)
