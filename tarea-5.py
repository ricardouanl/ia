import math


def minimax(board, maximizing):
    result = check_game_over(board)
    if ( result ):
        return {'X': 1, 'O': -1, 'T': 0}[result]

    if (maximizing):
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '-'):
                    board[i][j] = 'X'
                    score = minimax(board, False)
                    board[i][j] = '-'
                    best_score = max(score, best_score)
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '-'):
                    board[i][j] = 'O'
                    score = minimax(board, True)
                    board[i][j] = '-'
                    best_score = min(score, best_score)

    return best_score

def ia(board):
    best_score = math.inf
    move = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '-'):
                board[i][j] = 'O'
                score = minimax(board, True)
                board[i][j] = '-'
                if (score < best_score):
                    best_score = score
                    move = [i,j]
    return move

def check_game_over(board):
    game_over = False

    # horizontal
    for i in range(3):
        if (board[i][0] != '-' and board[i][0] == board[i][1] == board[i][2]):
            game_over = board[i][0]

    # vertical
    for i in range(3):
        if (board[0][i] != '-' and board[0][i] == board[1][i] == board[2][i]):
            game_over = board[0][i]

    # diagonal
    if (board[0][0] != '-' and board[0][0] == board[1][1] == board[2][2]):
        game_over = board[0][0]

    if (board[2][0] != '-' and board[2][0] == board[1][1] == board[0][2]):
        game_over = board[2][0]

    open_spots = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '-'):
                open_spots += 1

    if (game_over == False and open_spots == 0):
        return 'T'

    return game_over


def print_board(board):
    for i in range(3):
        print(board[i])


# MAIN

board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

print_board(board)
move = []

while(True):
    print("Seleccione una casilla:")
    print("Fila (1 a 3):")
    row = int(input()) - 1
    print("Columna (1 a 3):")
    column = int(input()) - 1

    if (board[row][column] != '-'):
        print('Movimiento no valido. Intente de nuevo')
        continue

    board[row][column] = 'X'

    print_board(board)
    if ( check_game_over(board) ):
        break

    move = ia(board)
    board[ move[0] ][ move[1] ] = 'O'

    print()
    print_board(board)
    if ( check_game_over(board) ):
        break


