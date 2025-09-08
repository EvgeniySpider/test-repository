


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
    # Проверяем, есть ли пустые клетки
    for row in board:
        if ' ' in row:
            return False  # Есть пустые клетки, игра продолжается
    return True  # Все клетки заполнены, возможна ничья


def play(board=None):
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    if board is None:
        raise TypeError('Нужна таблица!')

    while True:
        print_board(board)

        # Ход игрока X
        while True:
            try:
                player_x = int(
                    input('Игрок №1 - X. Введите номер клетки 1-9: '))

                if player_x < 1 or player_x > 9:
                    print('Ошибка: введите число от 1 до 9!')
                    continue

                row = (player_x - 1) // 3
                col = (player_x - 1) % 3

                if board[row][col] != ' ':
                    print('Эта ячейка уже занята, выберите другую!')
                    continue

                board[row][col] = 'X'
                break

            except ValueError:
                print('Ошибка: введите число!')

        print_board(board)

        if check_winner(board):
            print('Игрок №1 победил!')
            return

        if check_draw(board):
            print('Игра закончилась вничью!')
            return

        # Ход игрока O
        while True:
            try:
                player_o = int(
                    input('Игрок №2 - O. Введите номер клетки 1-9: '))

                if player_o < 1 or player_o > 9:
                    print('Ошибка: введите число от 1 до 9!')
                    continue

                row = (player_o - 1) // 3
                col = (player_o - 1) % 3

                if board[row][col] != ' ':
                    print('Эта ячейка уже занята, выберите другую!')
                    continue

                board[row][col] = 'O'
                break

            except ValueError:
                print('Ошибка: введите число!')

        if check_winner(board):
            print('Игрок №2 победил!')
            return

        if check_draw(board):
            print('Игра закончилась вничью!')
            return


play()
