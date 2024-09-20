from math import inf as infinity
from random import choice
import tkinter as tk

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0
    return score

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
    return wins(state, HUMAN) or wins(state, COMP) or len(empty_cells(state)) == 0

def empty_cells(state):
    return [[i, j] for i, row in enumerate(state) for j, cell in enumerate(row) if cell == 0]

def valid_move(x, y):
    return [x, y] in empty_cells(board)

def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    return False

def alpha_beta(state, depth, alpha, beta, player):
    """
    Alpha-beta pruning implementation for Tic-Tac-Toe.
    :param state: current state of the board
    :param depth: depth of the node in the tree
    :param alpha: best value for maximizing player so far
    :param beta: best value for minimizing player so far
    :param player: the current player
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = alpha_beta(state, depth - 1, alpha, beta, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score
            alpha = max(alpha, best[2])
        else:
            if score[2] < best[2]:
                best = score
            beta = min(beta, best[2])

        if beta <= alpha:
            break

    return best

def ai_turn():
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = alpha_beta(board, depth, -infinity, infinity, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    update_board()
    if game_over(board):
        end_game()

def human_turn(x, y):
    if valid_move(x, y):
        set_move(x, y, HUMAN)
        update_board()
        if not game_over(board):
            ai_turn()

def update_board():
    for i in range(3):
        for j in range(3):
            value = board[i][j]
            if value == HUMAN:
                buttons[i][j].config(text='X', state=tk.DISABLED)
            elif value == COMP:
                buttons[i][j].config(text='O', state=tk.DISABLED)
    if game_over(board):
        end_game()

def end_game():
    if wins(board, HUMAN):
        status_label.config(text="YOU WIN!")
    elif wins(board, COMP):
        status_label.config(text="YOU LOSE!")
    else:
        status_label.config(text="DRAW!")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.DISABLED)

def on_button_click(x, y):
    if board[x][y] == 0:
        human_turn(x, y)

# GUI Setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

status_label = tk.Label(root, text="Choose your move")
status_label.grid(row=0, column=0, columnspan=3)  # Use grid for status_label

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', width=10, height=5, command=lambda x=i, y=j: on_button_click(x, y))
        buttons[i][j].grid(row=i + 1, column=j)  # Use grid for buttons

root.mainloop()