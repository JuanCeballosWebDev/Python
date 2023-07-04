"""
Program: JuanCeballosLuckySevens.py
Author: Juan P. Ceballos
Lucky Sevens Game.
1. The input is
	amount of money player wants to put into the pot
2. Computations
        two separate operations to represent two dice
        each dice should give a random number
        if the sum of the results of both dice is 7, control adds 4 to the pot
        otherwise pot -1
        game is played until the pot is empty
3. Outputs:
        number of rolls to break the player
        the maximum amount of money in the pot

"""
# the user enters the amount of money he or she wants to put into the pot
pot = int(input("Enter the amount of money in dollars, do not include cents, you want to put into the pot: "))

# import module random
import random

# variable to keep count
amountRolls = 0

# this while loop allows control to keep going until the pot is empty
while True:

# these two variables represent the two dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # the amount of rolls increase
    amountRolls += 1

    # here, the values of the two dice get summed
    roll = dice1 + dice2

    # if the roll is 7, $4 is added to the pot
    if roll == 7:
        pot += 4

    # if the roll is not equal to 7, $1 is substrated from to the pot
    else:
        pot -= 1

    # if pot is empty, control leave the loop
    if pot == 0:
        break

# control outputs the number of rolls to break the player
print ("You lost your money in: " + str(amountRolls) + " rolls")

# money in the pot
print ("The amount of money in the pot is : " + str(pot))
    
        
        






