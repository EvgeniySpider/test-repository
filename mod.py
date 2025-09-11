

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
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return None


def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    print('Игра закончилась вничью!', "\U0001F602")
    return True


def check_cell_move(board, row, col, users_move):
    if 1 < users_move > 9:
        print('Ошибка: введите число от 1 до 9!')
        return True
    if board[row][col] != ' ':
        print('Эта ячейка уже занята, выберите другую!')
        return True


def play():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player_move = 'X'
    while True:

        print_board(board)
        try:
            player_input = int(
                input(f'Игрок {player_move}. Введите номер клетки 1-9: '))

            row = (player_input - 1) // 3
            col = (player_input - 1) % 3

            if check_cell_move(board, row, col, player_input):
                continue

            board[row][col] = player_move
            print_board(board)

            if check_winner(board):
                print_board(board)
                print(f'Игрок {player_move} победил!', "\U0001F60E")

            if check_draw(board):
                print('Игра закончилась вничью!')
                print_board(board)

            player_move = 'O' if player_move == 'X' else 'X'

            if check_draw(board) or check_winner(board):
                ask_replay = input('Хотите сыграть ещё раз? ').lower()
                if ask_replay not in ['да', 'yes', 'д', 'y']:
                    print('Хорошего дня', '\U0001F917')
                    return
                board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        except ValueError:
            print('Ошибка: введите число!')


play()
