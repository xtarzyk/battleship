



def init_board():
    board = [['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0']]
    return board





def switch_player(player):
    if player == "Player 1":
        player = "Player 2"
    else:
        player = "Player 1"
    return player