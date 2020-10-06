"""
Steps to take when initiating the game
"""
# Initiatial stage

Board Representation - using coordinates
    0, 1, 2
0
1
2

#O, X - represents players
# Data structure to represents board
2-D grid, list , array
[
        ['X', None, 'O'],
        ['O', None, None],
        [None, 'X', 'X']
        ]

            
start_game(){
        player_1 turn
        player_2 turn

        current_player = ??
        render_board() - every turn
        send_move(x, y, player_id)        
        check_for_winner(board)
        if winner exits:
            print(winner)
            quit loop
        if board_is_full():
            print("Draw")
            break

        repeat till game is over



        }

