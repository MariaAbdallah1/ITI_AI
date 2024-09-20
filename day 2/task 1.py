from math import inf as infinity
from random import choice
import tkinter as tk
from tkinter import messagebox

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluate(state):
    if wins(state, COMP):
        return +1
    elif wins(state, HUMAN):
        return -1
    else:
        return 0

def wins(state, player):
    win_state = [ 
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state

def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP) or not empty_cells(state)

def empty_cells(state):
    return [[i, j] for i, row in enumerate(state) for j, cell in enumerate(row) if cell == 0]

def valid_move(x, y):
    return [x, y] in empty_cells(board)

def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    return False

def minimax(state, depth, player):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best

def ai_turn():
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    update_board()
    check_game_status()

def human_turn(x, y):
    if valid_move(x, y):
        set_move(x, y, HUMAN)
        update_board()
        check_game_status()
        if not game_over(board):
            root.after(500, ai_turn)

def update_board():
    for i in range(3):
        for j in range(3):
            if board[i][j] == COMP:
                buttons[i][j].config(text='O', state=tk.DISABLED)
            elif board[i][j] == HUMAN:
                buttons[i][j].config(text='X', state=tk.DISABLED)
            else:
                buttons[i][j].config(text='', state=tk.NORMAL)

def check_game_status():
    if wins(board, HUMAN):
        status_label.config(text="You win!")
        disable_buttons()
    elif wins(board, COMP):
        status_label.config(text="AI wins!")
        disable_buttons()
    elif not empty_cells(board):
        status_label.config(text="It's a draw!")
        disable_buttons()

def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state=tk.DISABLED)

def on_button_click(i, j):
    if set_move(i, j, HUMAN):
        update_board()
        check_game_status()
        if not game_over(board):
            root.after(500, ai_turn)

root = tk.Tk()
root.title("Tic Tac Toe")

# Status label
status_label = tk.Label(root, text="Your turn")
status_label.grid(row=3, column=0, columnspan=3)

# Create buttons for the board
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', width=5, height=2,
                                  command=lambda i=i, j=j: on_button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
