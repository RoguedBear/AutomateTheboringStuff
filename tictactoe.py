board = {'1': '\x1b[2m1\x1b[0m', '2': '\x1b[2m2\x1b[0m', '3': '\x1b[2m3\x1b[0m',
         '4': '\x1b[2m4\x1b[0m', '5': '\x1b[2m5\x1b[0m', '6': '\x1b[2m6\x1b[0m',
         '7': '\x1b[2m7\x1b[0m', '8': '\x1b[2m8\x1b[0m', '9': '\x1b[2m9\x1b[0m'}

def printBoard(board):
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('-----------')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('-----------')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'])


turn = '\x1b[1;31mX\x1b[0m'
for i in range(9):
    printBoard(board)
    print("Turn for: " + turn + '. You would move on which space?')
    move = input('\x1b[0;;40m> ')
    print('\r\x1b[0m')
    board[move] = turn
    if turn == '\x1b[1;31mX\x1b[0m':
        turn = '\x1b[1;32mO\x1b[0m'
    else:
        turn = '\x1b[1;31mX\x1b[0m'

printBoard(board)
