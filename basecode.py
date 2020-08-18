board = [[' ', ' ', ' '], 
         [' ', ' ', ' '], 
         [' ', ' ', ' ']]

for row in board: #initial display of board
    print(row)

p1 = 'x'
p2 = 'o'

play = False #game is live
winner_p1 = False
winner_p2 = False

#check if break breaks both loops
def draw(board): #to check whether game can continue
    cont = False #cont means continue
    for row in board:
        for item in row:
            if item == ' ':
                cont = True
                break
    return cont

def p1_win(board):
    if ((board[0][0] == p1) and (board[0][1] == p1) and (board[0][2] == p1)) or \
        ((board[1][0] == p1) and (board[1][1] == p1) and (board[1][2] == p1)) or \
            ((board[2][0] == p1) and (board[2][1] == p1) and (board[2][2] == p1)) or \
                ((board[0][0] == p1) and (board[1][0] == p1) and (board[2][0] == p1)) or \
                    ((board[0][1] == p1) and (board[1][1] == p1) and (board[2][1] == p1)) or \
                        ((board[0][2] == p1) and (board[1][2] == p1) and (board[2][2] == p1)) or \
                            ((board[0][0] == p1) and (board[1][1] == p1) and (board[2][2] == p1)) or \
                                ((board[0][2] == p1) and (board[1][1] == p1) and (board[2][0] == p1)):
        return True
    else:
        return False

def p2_win(board):
    if ((board[0][0] == p2) and (board[0][1] == p2) and (board[0][2] == p2)) or \
        ((board[1][0] == p2) and (board[1][1] == p2) and (board[1][2] == p2)) or \
            ((board[2][0] == p2) and (board[2][1] == p2) and (board[2][2] == p2)) or \
                ((board[0][0] == p2) and (board[1][0] == p2) and (board[2][0] == p2)) or \
                    ((board[0][1] == p2) and (board[1][1] == p2) and (board[2][1] == p2)) or \
                        ((board[0][2] == p2) and (board[1][2] == p2) and (board[2][2] == p2)) or \
                            ((board[0][0] == p2) and (board[1][1] == p2) and (board[2][2] == p2)) or \
                                ((board[0][2] == p2) and (board[1][1] == p2) and (board[2][0] == p2)):
        return True
    else:
        return False

play = draw(board)
winner_p1 = p1_win(board)
winner_p2 = p2_win(board)

while play and (not winner_p1) and (not winner_p2):
    p1_entry = int(input('enter p1: '))
    if p1_entry == 1:
        board[0][0] = p1
    elif p1_entry == 2:
        board[0][1] = p1
    elif p1_entry == 3:
        board[0][2] = p1
    elif p1_entry == 4:
        board[1][0] = p1
    elif p1_entry == 5:
        board[1][1] = p1
    elif p1_entry == 6:
        board[1][2] = p1
    elif p1_entry == 7:
        board[2][0] = p1
    elif p1_entry == 8:
        board[2][1] = p1
    elif p1_entry == 9:
        board[2][2] = p1

    for row in board:
        print(row)

    play = draw(board)
    if not play:
        break

    winner_p1 = p1_win(board)
    if winner_p1:
        print("player 1 won!")
        break

    winner_p2 = p2_win(board)
    if winner_p2:
        print("player 2 won!")
        break

    p2_entry = int(input('enter p2: '))
    if p2_entry == 1:
        board[0][0] = p2
    elif p2_entry == 2:
        board[0][1] = p2
    elif p2_entry == 3:
        board[0][2] = p2
    elif p2_entry == 4:
        board[1][0] = p2
    elif p2_entry == 5:
        board[1][1] = p2
    elif p2_entry == 6:
        board[1][2] = p2
    elif p2_entry == 7:
        board[2][0] = p2
    elif p2_entry == 8:
        board[2][1] = p2
    elif p2_entry == 9:
        board[2][2] = p2

    for row in board:
        print(row)

    play = draw(board)

    winner_p1 = p1_win(board)
    if winner_p1:
        print("player 1 won!")
    winner_p2 = p2_win(board)
    if winner_p2:
        print("player 2 won!")

    continue

