"""
    imported render_board that creates the tic-tac-toe board
    imported sys for sys.exit()
"""
import sys
#  from main import render_board
"""
        DIAGONAL  co-ordinates:
        D1 - (0, 0), (1, 1), (2, 2)
        D2 - (0, 2), (1, 1), (2, 0)
"""

#  creating a function to check for winner
"""
        Write Unit Tests for checking:
        - rows: current
        - columns
        - diagonals

        Approach:
        Divide into three functions:
        All three take input = board
        - check_rows:
            extract rows check for winner
        - check-cols:
            extract cols and check for winner
        - check-diagonals
            extract diagonals and check for winner
"""
winner = False


def check_rows(board):
    """
        check for winner in rows
    """
    global winner
    for row in board:
        count_X = 0
        count_O = 0
        for sq in row:
            if sq == 'X':
                count_X += 1
            elif sq == 'O':
                count_O += 1
            if count_X == 3:
                print("winner is X!")
                winner = True
            elif count_O == 3:
                print("Winner is O!")
                winner = True

def check_cols(board):
    #  Extracting cols
    global winner
    cols = []
    col_0 = []
    col_1 = []
    col_2 = []
    for row in board:
        col_0.append(row[0])
        col_1.append(row[1])
        col_2.append(row[2])

    cols.append(col_0)
    cols.append(col_1)
    cols.append(col_2)

    #  Check for winner
    for i in cols:
        count_X = 0
        count_O = 0
        for sq in i:
            if sq == "X":
                count_X += 1
            elif sq == 'O':
                count_O += 1
            if count_X == 3:
                print('winner is X!')
                winner = True
            elif count_O == 3:
                print('winner is O!')
                winner = True


def check_diagonals(board):
    #  Extracting diagonals
    """
        DIAGONAL  co-ordinates:
        D1 - (0, 0), (1, 1), (2, 2)
        D2 - (0, 2), (1, 1), (2, 0)
        To get D2, flip the rows and 
        then extract prime diagonal
    """
    global winner
    diags = []
    diag_1 = [board[i][i] for i in range(len(board))]
    flip_board = []
    for row in board:
        flip_row = row[::-1]
        flip_board.append(flip_row)
    #  print(diag_1)
    diag_2 = [flip_board[i][i] for i in range(len(flip_board))]
    diags.append(diag_1)
    diags.append(diag_2)

    #  CHECK WINNER
    for d in diags:
        count_x = 0
        count_o = 0
        for sq in d:
            if sq == 'X':
                count_x += 1
            elif sq == 'O':
                count_o += 1
            if count_x == 3:
                print("Winner is X!")
                winner = True
            elif count_o == 3:
                print("winner is O!")
                winner = True


def get_winner(board):
    """
        CHECK FOR WINNER
    """
    check_rows(board)
    check_cols(board)
    check_diagonals(board)
    if winner == True:
        sys.exit()



"""
BOARD_R = [['X', 'O', 'X'], ['O', 'O', 'O'], ['O', 'X', 'X']]
BOARD_C = [['X', 'O', 'X'], ['O', 'O', 'X'], ['O', 'X', 'X']]
BOARD_D = [['O', 'O', 'X'], ['O', 'O', 'X'], ['X', 'X', 'O']]

get_winner(BOARD_D)
#  check_cols(board_c)
#  check_diagonals(board_d)

"""
