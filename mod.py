board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

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


def play(board = None):
    if board is None:
        raise 'Нужна таблица!'
    
    while True:
    
        print_board(board)
        player_x = int(input('Игрок №1 - X. Введите номер клетки 1-9: '))
        
        if player_x > 0 and player_x < 4:
            board[0][player_x - 1] = 'X'
        elif player_x < 7:
            board[1][player_x - 4] = 'X'
        elif player_x < 10:
            board[2][player_x - 7] = 'X'
        print_board(board)
        
        if check_winner(board):
            print_board(board)
            print('Игрок №1 победил!')
            break
        elif check_draw(board):
            print('Игра закончилась вничью!')
        
        player_o = int(input('Игрок №2 - O. Введите номер клетки 1-9: '))
        if player_o > 0 and player_o < 4:
            board[0][player_o - 1] = 'O'
        elif player_o < 7:
            board[1][player_o - 4] = 'O'
        elif player_o < 10:
            board[2][player_o - 7] = 'O'
        print_board(board)
        if check_winner(board):
            print_board(board)
            print('Игрок №2 победил!')
            break
        elif check_draw(board):
            print('Игра закончилась вничью!')

play(board)