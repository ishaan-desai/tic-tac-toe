from main import render_board
from main import new_board

board = new_board()

def get_all_legal_moves(board):
    legal_moves = []
    for x, row in enumerate(board):
        for y, val in enumerate(row):
            if val is None:
                legal_moves.append((x, y))
    return legal_moves

moves = get_all_legal_moves(board)
