"""
    Importing sys to use sys.exit() to quit game
    Importing check_winner functions to check for winner game
"""
import sys
import winner


def new_board():
    """
    correct way to create 2D lists in python
    2d = [[1 for i in range(3)] for j in range(3)]
    """
    board = [[None for i in range(3)] for j in range(3)]
    return board

rows = [0, 1, 2]
cols = [0, 1, 2]
board = new_board()
# board[1][0] = 'X'
# board[1][1] = 'O'
# print(board)

def render_board(board):
    print(*cols, sep=" ")
    print("_"*5)
    conv = lambda i:i or '_'
    for row in board:
        res = [conv(i) for i in row]
        print(*res, sep=" ")


# render_board(board)

#  Get player input
def get_move(player_id):
    print("Turn", player_id)
    x = int(input("What is your x-coordinates move ?: "))
    y = int(input("What is your y coordinates move ?: "))
    #  print("The x coordinate is: ", x)
    #  print("The y-coordinate value is: ", y)
    t = (x, y)
    return t


#  move_coords = get_move()
#  print(move_coords)

# Make Move
def make_move(board, move, player_id):
    """ returns a new board, as mutation is messy """
    player_id = player_id
    temp = board[:]
    x = move[0]
    y = move[1]
    if temp[x][y] == 'X' or temp[x][y] == 'O':
        raise Exception('Illegal Move!, Space already occupied')
    else:
        temp[x][y] = player_id
    return temp

# making a move
# new_board = make_move(board, move_coords, 'O')
# render_board(new_board)


def is_board_full(board):
    count = 0
    for row in board:
        for sq in row:
            if sq == "X" or sq == "O":
                count += 1
    if count == 9:
        print("the board is full")
        sys.exit()



if __name__ == '__main__':
    board = new_board()
    render_board(board)
    global x
    X = True
    #  register players
    player_x = input("Enter Player id: X\n")
    player_o = input("Enter Player id: O\n")

    print("X goes first")
    while X == True:
        # x move
        move_x = get_move(player_x)
        x_board = make_move(board, move_x, player_x)
        render_board(x_board)
        winner.get_winner(x_board)
        is_board_full(x_board)

        # o move
        move_o = get_move(player_o)
        o_board = make_move(x_board, move_o, player_o)
        render_board(o_board)
        winner.get_winner(o_board)
        is_board_full(o_board)




















