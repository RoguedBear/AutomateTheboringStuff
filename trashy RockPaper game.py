# Write your code here :-)
import random, sys
from os import system
from time import sleep
# These variables keep track of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

maxScore = input("How many points should the game last?\n")

while wins + losses < int(maxScore): # The main game loop
    system('clear')
    if wins > losses:
        win_print = '\x1b[1;32m'+ str(wins) + " Wins" '\x1b[0m'
        losses_print =  str(losses) + " Losses" +'\x1b[0m'
        ties_print = '\x1b[0;34m'+ str(ties) + " Ties" + '\x1b[0m'

    elif wins < losses:
        win_print =  str(wins) + " Wins" + '\x1b[0m'
        losses_print = '\x1b[1;31m'+ str(losses) + " Losses" + '\x1b[0m'
        ties_print = '\x1b[0;34m'+ str(ties) + " Ties" + '\x1b[0m'
    else:
        win_print = str(wins) + " Wins"
        losses_print = str(losses) + " Losses"
        ties_print = str(ties) + " Ties"
    print('\x1b[1mScore:',f"{win_print}, {losses_print}, {ties_print}","\x1b[0m")
    while True: # The player input loop.
        print("\x1b[1;40;40mEnter your move: (r)ock, (p)aper, (s)cissors or (q)uit. \x1b[0m")
        playerMove = input("> ")
        if playerMove == 'q':
            sys.exit() # Quit the program
        if playerMove == 'r' or playerMove =='p' or playerMove == 's':
            break # Break out of the player input looop
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print("ROCK versus...", end='\t', flush=True)
    elif playerMove == 'p':
        print("PAPER versus...", end='\t', flush=True)
    elif playerMove == 's':
        print("SCISSORS versus...", end='\t', flush=True)

    sleep(0.4)

    # Display what the computer chose:
    computerMove = random.choice(['r','p','s'])
    if computerMove == 'r':
        print("ROCK")
    elif computerMove == 'p':
        print("PAPER ")
    elif computerMove == 's':
        print("SCISSORS")

    # Display and record the win/loss/ties:
    if playerMove == computerMove:
        print("\x1b[33;5m" + "It is a tie!"+ "\x1b[0m")
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('\x1b[33;5m'+'You win!'+'\x1b[0m')
        wins += 1

    elif playerMove == 'p' and computerMove == 'r':
        print('\x1b[33;5m'+'You Win!'+'\x1b[0m')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('\x1b[33;5m'+"YOu win!"+'\x1b[0m')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('\x1b[33;5m'+"You Lose!\x1b[0m")
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('\x1b[33;5m'+"You Lose!\x1b[0m")
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('\x1b[33;5m'+"You Lose!\x1b[0m")
        losses += 1


    input("\x1b[37;2mPress ENTER...\x1b[0m")

print("\n\nGAME OVER")
if wins > losses:
    print("YOU WIN!!!")
elif wins < losses:
    print("YOU lose :(:(:( ")
else:
    print("It is a tie. Pretty close one")
