board = {'1': '\x1b[2m1\x1b[0m', '2': '\x1b[2m2\x1b[0m', '3': '\x1b[2m3\x1b[0m',
         '4': '\x1b[2m4\x1b[0m', '5': '\x1b[2m5\x1b[0m', '6': '\x1b[2m6\x1b[0m',
         '7': '\x1b[2m7\x1b[0m', '8': '\x1b[2m8\x1b[0m', '9': '\x1b[2m9\x1b[0m'}

X = '\x1b[1;31mX\x1b[0m'
O = '\x1b[1;32mO\x1b[0m'

def printBoard(board):
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('-----------')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('-----------')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

# TODO: Won
def hasWon(board):
    '''
    Checks if the game board is in a winning state
    INPUT: the game board
    OUTPUT: winning Player
    '''

    # Check horizontals.
    # Column 1
    if board['1'] == board['4'] == board['7'] and board['1'] in [X, O]:
        return board['1']
    # Column 2
    if board['2'] == board['5'] == board['8'] and board['2'] in [X, O]:
        return board['2']
    # Column 3
    if board['3'] == board['6'] == board['9'] and board['3'] in [X, O]:
        return board['3']

    # Check verticals
    # Row 1
    if board['1'] == board['2'] == board['3'] and board['1'] in [X, O]:
        return board['1']
    # Row 2
    if board['4'] == board['5'] == board['6'] and board['4'] in [X, O]:
        return board['4']
    # Row 3
    if board['7'] == board['8'] == board['9'] and board['7'] in [X, O]:
        return board['7']

    # Check Diagonals
    # D1
    if board['1'] == board['5'] == board['9'] and board['1'] in [X, O]:
        return board['1']
    # D2
    if board['7'] == board['5'] == board['3'] and board['2'] in [X, O]:
        return board['7']
    else:
        return None



# TODO: Score each game
def score(game_board, player):
    players = {X: 'human', O: 'computer'}
    result = hasWon(game_board)
    if result is not None:
        if players[result] == 'human':
            # Human will minimise the computer, so negative.
            return -1
        elif players[result] == 'computer':
            # Maximise computer, so positive
            return 1


# TODO: MINmax





human = X
computer = O
turn = X

# MAin game
print ("Welcome to TicTacToe!")
print (f"You are the the first player {X}.")

for i in range(9):

    printBoard(board)

    # Update Gameboard
    while True:
        print("Turn for: " + turn + '. You would move on which space?')
        move = input('\x1b[0;;40m> ')
        print('\r\x1b[0m')
        if move in '123456789':
            if board[move] not in [X, O]:
                board[move] = turn
                break
            else:
                print("Place Already taken cheater.")
                continue
        else:
            print("Not a valid move")
            continue
    # Switch Turns
    if turn == X:
        turn = O
    else:
        turn = X

    print(score(board, turn))
    # Check if game is over
    end_game = hasWon(board)
    if end_game is not None: #That means we have a victory
        if end_game == human:
            print("Human WINS!")
            break
        else:
            print("YOU LOSE!!")
            break

else:
    # GAme is tie
    print("TIE!!")
printBoard(board)
