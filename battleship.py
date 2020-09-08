


def init_board():
    board = [['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0']]
    
    return board

board = init_board()


def print_board(board):
    alpha = ["A","B","C","D","E"]
    line = '    ---+---+---+---+---'
    print("     1   2   3   4   5")
    print("                                     ")
    counter = 0
    n = 0
    for row in board:
        row_num1, row_num2, row_num3, row_num4, row_num5 = row
        print(f' {alpha[n]}   {row_num1} | {row_num2} | {row_num3} | {row_num4} | {row_num5}')
        n += 1
        if counter < 4:
            print(line)
            counter += 1

print_board(board)


def switch_player(player):
    if player == "Player 1":
        player = "Player 2"
    else:
        player = "Player 1"
    return player
