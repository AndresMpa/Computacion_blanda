from tic_tac_toe import check_winner, is_full, print_board, find_best_move, game_over
from tkinter import messagebox
import tkinter as tk


def update_gui():
    # Función para actualizar la GUI
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                buttons[i][j].config(text='X', state=tk.DISABLED)
            elif board[i][j] == 'O':
                buttons[i][j].config(text='O', state=tk.DISABLED)
            else:
                buttons[i][j].config(text=' ', state=tk.NORMAL)


def on_click(row, col):
    # Función para el manejo de eventos en la GUI
    if board[row][col] == ' ' and not game_over(board):
        board[row][col] = 'O'
        update_gui()

        if check_winner(board, 'O'):
            messagebox.showinfo("¡Has ganado!", "¡Felicidades, ganaste!")
            reset_game()
            return

        if is_full(board):
            messagebox.showinfo("¡Empate!", "El juego ha terminado en empate.")
            reset_game()
            return

        computer_row, computer_col = find_best_move(board)
        board[computer_row][computer_col] = 'X'
        update_gui()

        if check_winner(board, 'X'):
            messagebox.showinfo("¡La computadora ha ganado!",
                                "La computadora ha ganado el juego.")
            reset_game()
            return

        if is_full(board):
            messagebox.showinfo("¡Empate!", "El juego ha terminado en empate.")
            reset_game()


def reset_game():
    global board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    update_gui()


# Configuración de la ventana de la GUI
root = tk.Tk()
root.title("Tres en Raya")

buttons = [[None, None, None] for _ in range(3)]

# Crear botones
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', width=10, height=3,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

reset_button = tk.Button(root, text="Reiniciar Juego", command=reset_game)
reset_button.grid(row=3, column=1)

# Iniciar el juego
board = [[' ' for _ in range(3)] for _ in range(3)]
update_gui()

root.mainloop()
