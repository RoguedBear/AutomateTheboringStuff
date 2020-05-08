import copy
from sys import setrecursionlimit
import pdb
#setrecursionlimit(10**6)
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
def Score(game_board):
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
        # CHeck if gameboard is filled since, minmax.
        for boardState in game_board.values():
            if boardState not in [X, O]:
                break
        else:
            return 'FULL'
        return 0

# TODO: MINmax
def minimax(board, depth, isMaximising):
    """
    Does the minimaxing here.
    """
    # Check if game is in end state:
    board_evaluation = Score(board)
    if board_evaluation == 'FULL':
        return 0
    if board_evaluation != 0: # game is in terminal state
        return board_evaluation

    # The game is not in end state if execution reaches here.
    # Check available moves now.
    board_ = copy.copy(board)
    # Available moves
    available_moves = [i if board_[i] not in [X, O] else 0 for i in board_.keys()]
    while True:
        try:
            available_moves.remove(0)
        except ValueError:
            break
    if isMaximising:
        bestScore = float('-inf')
        for move in available_moves:
            board__ = copy.copy(board_)
            board__[move] = O
            score = minimax(board__, depth + 1, False)

            bestScore = max(bestScore, score)
        else:
            return bestScore

    else:
        bestScore = float('inf')
        for move in available_moves:
            board__ = copy.copy(board_)
            board__[move] = X
            score = minimax(board__, depth + 1, True)

            bestScore = min(bestScore, score)
        else:
            return bestScore
    return bestScore

def computerPlays(game_board ):
    '''
    Computer will decide the best move using MINmax ::sunglasses::
    '''
    # Copy the gameboard first, cuz we don't want making changes to the actual gamebaord
    board = copy.copy(game_board)

    # Available moves
    available_moves = [i if board[i] not in [X, O] else 0 for i in board.keys()]
    while True:
        try:
            available_moves.remove(0)
        except ValueError:
            break
    # Best score for the computer is currently -infinity
    bestScore = float('-inf')
    # Move to play
    bestMove = '1'

    for move in available_moves:
        copied_board = copy.copy(game_board)
        copied_board[move] = O
        score = minimax(copied_board, 0, False)
        print('OUTSIDE RECURSION')
        if score > bestScore:
            bestScore = score
            bestMove = move
            print(f"Best move acquired: {bestMove}\tWith bestScore: {score}")
    return bestMove

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
        # Check if game is over
        end_game = hasWon(board)
        if end_game is not None: #That means we have a victory
            if end_game == human:
                print("Human WINS!")
                break
            else:
                print("YOU LOSE!!")
                break

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
    # Switch Turns
    # if turn == X:
    #     # turn = O
    #
    # else:
    #     turn = X



    # COmputer plays its part
    board[computerPlays(board)] = O
else:
    # GAme is tie
    print("TIE!!")
printBoard(board)
