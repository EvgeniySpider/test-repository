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
            return row[0]
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return board[0][column]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[1][1]
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

        if check_draw(board):
            print('Ничья!')
            return
        print_board(board)
        players_1 = int(input('Игрок 1. Введите ряд 1-3: ')) -1
        players_2 = int(input('Игрок 1. Введите позицию 1-9: ')) -1
        
        board[players_1][players_2] = 'X'
        print_board(board)
        
        
        print_board(board)

        if check_winner(board):
            print_board(board)
            print('Игрок №1 = X победил!')
            break

        player_3 = int(input('Игрок 2. Введите ряд 1-3: ')) -1
        player_4 = int(input('Игрок 2. Введите позицию 1-9: ')) -1
        board[player_3][player_4] = 'Y'
       
        if check_winner(board):
            print_board(board)
            print('Игрок №2 = Y победил!')
            return

play(board)