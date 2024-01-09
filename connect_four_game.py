from collections import deque


def check_for_win(r, c, coordinates):
    for _ in range(3):
        r, c = r + coordinates[0], c + coordinates[1]

        if not (0 <= r < rows and 0 <= c < cols):
            break

        if board[r][c] != player_symbol:
            break
    else:
        [print(f"[ {', '.join(row)} ]") for row in board]
        print(f"The winner is player: {player_number}")
        raise SystemExit


player_one_symbol = "1"
player_two_symbol = "2"

rows, cols = 6, 7

turn = deque([[1, player_one_symbol], [2, player_two_symbol]])
board = [["0"] * cols for row in range(rows)]

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
)

while True:
    [print(f"[ {', '.join(row)} ]") for row in board]
    player_number, player_symbol = turn[0]

    try:
        player_col = int(input(f"\nPlayer {player_number}, please choose a column: ")) - 1
    except ValueError:
        print("Select a valid number")
        continue

    if not 0 <= player_col < cols:
        print(f"Select a valid number in the range({1} and {cols})")
        continue

    row = 0

    if board[row][player_col] != '0':
        print("No empty spaces on that row!")
        continue

    while True:
        if row == rows - 1 or board[row + 1][player_col] != "0":
            board[row][player_col] = player_symbol
            break

        row += 1

    for raw in range(rows):
        for col in range(cols):
            if board[row][col] != player_symbol:
                continue
            for coordinates in directions:
                check_for_win(row, col, coordinates)

    turn.append(turn.popleft())
