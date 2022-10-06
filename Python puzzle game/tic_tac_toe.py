import random
DEFAULT='[ ]'

def display_board(board):
    print()
    for row in board:
        for col in row:
            print(col, end='') #col data
        print() #change the line

def toss(call):
    return call == random.choice(['heads', 'tails'])

def is_full(board):
    for row in board:
        for col in row:
            if col == DEFAULT:
                return False #board is not full

    return True #board is full

def validate_coords(board, r, c):
    if r < 0 or r > 2:
        return False
    elif c < 0 or c > 2:
        return False
    elif board[r][c] != DEFAULT:
        return False
    else:
        return True

def check_win(board, symbol):
    #rowwise
    for i in range(3):
        if board[i][0]== symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True

    #colwise
    for i in range(3):
        if board[0][i]== symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True

    #diagonal check
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return  True

    #reverse diagonal check
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    return False #no win

def tictactoe():
    #data structures
    #1)board : nested list
    board = [[DEFAULT, DEFAULT, DEFAULT],[DEFAULT, DEFAULT, DEFAULT],[DEFAULT, DEFAULT, DEFAULT]]

    #2)players: list
    players = [input('Enter name of player1: ').title(), input('Enter name of player2: ').title()]
    print(players)

    #3)symbols: list
    symbols = ['[X]','[O]'] #predecided

    print(players[0],' flips the coin and', players[1], 'makes a call (heads/tails)')
    call = input().lower()
    if toss(call):
        print(players[1], 'wins the toss and starts the game')
        current_player = 1
    else:
        print(players[1], 'loses the toss and', players[0],'starts the game')
        current_player = 0

    #4)game variables
    is_draw = True #flag

    #5)game
    while not is_full(board):
        display_board(board)

        print(players[current_player], symbols[current_player],'plays :')
        print('Enter row (0/1/2) ')
        r = int(input())
        print('Enter col (0/1/2) ')
        c = int(input())

        if validate_coords(board, r, c):
            #update the board
            board[r][c] = symbols[current_player]
            #is this a winning move
            if check_win(board, symbols[current_player]):
                is_draw = False
                display_board(board)
                print(players[current_player], symbols[current_player], 'WINS!!!')
                break #stop the game
            else:
                #change the player
                current_player = (current_player+1) % 2
        else:
            print('Invalid Move!!!')
            print('Play Again.')

    if is_draw:
        display_board(board)
        print('Game Draw!!!')

def main(): #Entry point
    tictactoe()

main() #invokation to main