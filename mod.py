

board = [[' ', ' ', 'x'], [' ', 'x', ' '], ['x', ' ', ' ']]


def print_board(board):
    print("\n   |   |   ")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("   |   |   \n")


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return board[0][column]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[1][1]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[1][1]

    return None
