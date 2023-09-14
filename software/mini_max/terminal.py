from tic_tac_toe import check_winner, is_full, print_board, find_best_move

# Tic tac toe desde la terminal
if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("¡Bienvenido al juego de tres en raya!")
    print_board(board)

    while True:
        player_row, player_col = map(int, input(
            "Ingresa la fila y columna (ejemplo: 0 1): ").split())

        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = 'O'
            print_board(board)

            if check_winner(board, 'O'):
                print("¡Has ganado!")
                break

            if is_full(board):
                print("¡Es un empate!")
                break

            computer_row, computer_col = find_best_move(board)
            board[computer_row][computer_col] = 'X'
            print("La computadora jugó en la fila",
                  computer_row, "y columna", computer_col)
            print_board(board)

            if check_winner(board, 'X'):
                print("¡La computadora ha ganado!")
                break

            if is_full(board):
                print("¡Es un empate!")
                break
        else:
            print("Esa casilla ya está ocupada. Intenta de nuevo.")
