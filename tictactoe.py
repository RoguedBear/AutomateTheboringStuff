import copy
from os import system


board = {'1': '\x1b[2m1\x1b[0m', '2': '\x1b[2m2\x1b[0m', '3': '\x1b[2m3\x1b[0m',
         '4': '\x1b[2m4\x1b[0m', '5': '\x1b[2m5\x1b[0m', '6': '\x1b[2m6\x1b[0m',
         '7': '\x1b[2m7\x1b[0m', '8': '\x1b[2m8\x1b[0m', '9': '\x1b[2m9\x1b[0m'}

# Initializing environmental variables. Geez.
X = '\x1b[1;31mX\x1b[0m'
O = '\x1b[1;32mO\x1b[0m'
human = X
computer = O
turn = X

# Prints out the board in a nice sweet format
def printBoard(game_board):
    '''
    Prints the gameboard
    INPUT: game_board: takes the board data structure to print it out
    '''
    print('\t ' + game_board['1'] + ' | ' + game_board['2'] + ' | ' + game_board['3'])
    print('\t-----------')
    print('\t ' + game_board['4'] + ' | ' + game_board['5'] + ' | ' + game_board['6'])
    print('\t-----------')
    print('\t ' + game_board['7'] + ' | ' + game_board['8'] + ' | ' + game_board['9'])


# Checks the winning conditions function
def hasWon(game_board):
    '''
    Checks if the game board is in a winning state
    INPUT: the game board
    OUTPUT: winning Player
    '''

    # Check horizontals.
    # Column 1
    if game_board['1'] == game_board['4'] == game_board['7'] and game_board['1'] in [X, O]:
        return game_board['1']
    # Column 2
    if game_board['2'] == game_board['5'] == game_board['8'] and game_board['2'] in [X, O]:
        return game_board['2']
    # Column 3
    if game_board['3'] == game_board['6'] == game_board['9'] and game_board['3'] in [X, O]:
        return game_board['3']

    # Check verticals
    # Row 1
    if game_board['1'] == game_board['2'] == game_board['3'] and game_board['1'] in [X, O]:
        return game_board['1']
    # Row 2
    if game_board['4'] == game_board['5'] == game_board['6'] and game_board['4'] in [X, O]:
        return game_board['4']
    # Row 3
    if game_board['7'] == game_board['8'] == game_board['9'] and game_board['7'] in [X, O]:
        return game_board['7']

    # Check Diagonals
    # D1
    if game_board['1'] == game_board['5'] == game_board['9'] and game_board['1'] in [X, O]:
        return game_board['1']
    # D2
    if game_board['7'] == game_board['5'] == game_board['3'] and game_board['2'] in [X, O]:
        return game_board['7']
    else:
        return None


# Score each game
def Score(game_board):
    '''
    Returns the score of the board if it is in end stage
    human wins: -1
    computer wins: 1
    tie: 0
    INPUT: game_board
    OUTPUT: the score
    '''
    players = {X: 'human', O: 'computer'}
    result = hasWon(game_board)
    if result is not None:
        if players[result] == 'human':
            # Human will minimise the computer, so negative.
            return -1
        elif players[result] == 'computer':
            # Maximise computer, so positive
            return 1
    else:
        return 0

# MINmax
def minimax(game_board, depth, isMaximising):
    """
    Does the minimaxing here.
    INPUT: game_board: the game board being used
           depth: i think it was supposed to ensure recursion limit, but its not
                  used, and im not gonna remove this parameter for a little
                  while cuz im lazy.
           isMaximising: BOOLEAN; Are we maximising or minimising

    OUTPUT: bestScore: ∈ {-1, 0, 1}
    """
    # Check if game is in end state:

    board_evaluation = Score(game_board)
    if board_evaluation == 'FULL':
        return 0
    if board_evaluation != 0: # game is in terminal state
        return board_evaluation

    # The game is not in end state if execution reaches here.
    # Check available moves now.
    # Available moves
    available_moves = [i if game_board[i] not in [X, O] else 0 for i in game_board.keys()]
    while True:
        try:
            available_moves.remove(0)
        except ValueError:
            break
    # If we are Maximising
    if isMaximising:
        bestScore = float('-inf')
        for move in available_moves:
            board_ = copy.copy(game_board)
            board_[move] = O
            score = minimax(board_, depth + 1, False)
            bestScore = max(bestScore, score)
        else:
            return bestScore

    # If we are minimising
    else:
        bestScore = float('inf')
        for move in available_moves:
            board__ = copy.copy(game_board)
            board__[move] = X
            score = minimax(board__, depth + 1, True)
            bestScore = min(bestScore, score)
        else:
            return bestScore
    return bestScore



def computerPlays(game_board ):
    '''
    Computer will decide the best move using MINmax ::sunglasses::
    INPUT: game_board: the game board data structure being used
    OUTPUT: __optimal__ move
    '''

    # Available moves
    available_moves = [i if game_board[i] not in [X, O] else 0 for i in game_board.keys()]
    # Remove the zeroes. feels like, instead of list comprehension,
    # I should have done an if/else for available moves. Computional Waste
    while True:
        try:
            available_moves.remove(0)
        except ValueError:
            break

    # Best score for the computer is currently -infinity
    bestScore = float('-inf')

    # Final/Best Move to play
    bestMove = '1'

    # Iterate through each move
    for move in available_moves:
        # Copy the gameboard first, cuz we don't want making changes to the actual gamebaord
        copied_board = copy.copy(game_board)
        copied_board[move] = O
        score = minimax(copied_board, 0, False)

        if score > bestScore:
            bestScore = score
            bestMove = move
            print(f"COMPUTER: Best move acquired: {bestMove}\tWith bestScore: {score}")
    return bestMove




# MAin game
print ("Welcome to TicTacToe!")
print (f"You are the the first player {X}.")

for i in range(5):

    printBoard(board)

    # Update Gameboard
    ## Validates the move entered
    while True:
        print("Turn for: " + turn + '. You would move on which space?')
        move = input('\x1b[0;;40m> ')
        print('\r\x1b[0m')
        if move in '123456789':
            if board[move] not in [X, O, '']:
                board[move] = turn
                break
            else:
                print("Place Already taken cheater.")
                continue
        else:
            print("Not a valid move")
            continue

    # Check if game has ended.
    end_game = hasWon(board)
    if end_game is not None: #That means we have a victory
        # pdb.set_trace()
        if end_game == human:
            print("Human WINS!")
            break
        else:
            print("YOU LOSE!!")
            break



    # Computer plays its part
    board[computerPlays(board)] = O

    # Now check endstate after computer's move
    end_game = hasWon(board)
    if end_game is not None: #That means we have a victory
        if end_game == human:
            print("Human WINS!")
            break
        else:
            print("YOU LOSE!!")
            break

    # ASSUMING Linux, clearing screen
    system('clear')
else:
    # GAme is tie
    print("TIE!!")
# The final print of the board.
printBoard(board)
