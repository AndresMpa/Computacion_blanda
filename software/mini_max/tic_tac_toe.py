def print_board(board):
    # Esta función imprime el tablero en la consola
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def game_over(board):
    # Verificar filas, columnas y diagonales
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    # Si no hay ganador pero el tablero está lleno, es un empate
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return True
    return False


def check_winner(board, player):
    # Esta función verifica si el jugador (X o O) ha ganado el juego
    # Verifica filas
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Verifica columnas
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Verifica diagonales
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    # Esta función verifica si el tablero está lleno (empate)
    return all(cell != ' ' for row in board for cell in row)


def minimax(board, depth, is_maximizing):
    # Esta función implementa el algoritmo Minimax para determinar la mejor jugada
    # Utiliza recursión para evaluar todas las posibles jugadas y sus resultados
    scores = {
        'X': 1,    # Puntuación para el jugador X
        'O': -1,   # Puntuación para el jugador O
        'Tie': 0   # Puntuación para empate
    }

    if check_winner(board, 'X'):
        return scores['X']
    if check_winner(board, 'O'):
        return scores['O']
    if is_full(board):
        return scores['Tie']

    if is_maximizing:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval


def find_best_move(board):
    # Esta función encuentra la mejor jugada para la computadora (jugador X)
    best_eval = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                eval = minimax(board, 0, False)
                board[row][col] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move
