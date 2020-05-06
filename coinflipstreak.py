# Head Tails streak probability simulator (cuz i dont know methz)
import random

streakValue = 6
times = 10000

values = ['H', 'T']
numberOfStreaks = 0
for experimentNumber in range(times):
    streakCount = 0
    # Code that creates a list of 100 'heads' or 'tails' values.
    sample_space = [values[random.randint(0, 1)] for i in range(100)] # Should have random H T in the list
    # print(len(sample_space))
    # print(sample_space)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for index, outcome in enumerate(sample_space) :
        if index != 99:
            if outcome == sample_space[index + 1]: # Next outcome is also same

                streakCount += 1
                continue
            if streakCount == streakValue:
                numberOfStreaks += 1


            else:

                streakCount = 0


print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / times * 100))
print(f'Chance of streak: {(numberOfStreaks / times * 100 )}' )
