def main():
    # tutaj docelowo będą wywoływane wszystkie (albo prawie) funkcje odpowiedzialne
    # za działanie gry
    ship = "X"
    board = init_board()
    print_board(board)
    moove = move(board)
    mark(board, moove[0], moove[1], ship)
    print_board(board)


def init_board():
    board = [['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0']]
    
    return board




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






def move(board):
    x = True
    while x:
        position = input("Enter coordinates for your ship: ").upper()

        if "1" in position:
            col = 0
        elif "2" in position:
            col = 1
        elif "3" in position:
            col = 2
        elif "4" in position:
            col = 3
        elif "5" in position:
            col = 4
        else:
            col = "not valid"

        if "A" in position:
            row = 0
        elif "B" in position:
            row = 1
        elif "C" in position:
            row = 2
        elif "D" in position:
            row = 3
        elif "E" in position:
            row = 4
        else:
            row = "not valid"

        if len(position) > 2:
            row = "not valid"
        
        if row or col == "not valid":
            print_board(board)
            print("\n Enter a valid coordinates!")
        elif board[col][row] != "0":
            print_board(board)
            print("\nYou have a ship here, already.")
        else:
            x = False

    return col, row


def mark(board, row, col, ship):
    board[row][col] = ship
    return board







def switch_player(player):
    if player == "Player 1":
        player = "Player 2"
    else:
        player = "Player 1"
    return player



main()
