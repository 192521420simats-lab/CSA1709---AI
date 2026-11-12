
board = [' ' for i in range(9)]

def display():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

def check_winner():
    win = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in win:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

player = 'X'

while True:
    display()
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid position! Try again.")
        continue

    board[pos] = player

    if check_winner():
        display()
        print(player, "wins!")
        break

    if ' ' not in board:
        display()
        print("Game Draw!")
        break

    player = 'O' if player == 'X' else 'X'
