"""
Program: JuanCeballosGuessingGameModify.py
Author: Juan P. Ceballos
Modified Guessing Game.
1. The inputs are
	smaller number
	larger number
	answer from the user
	question from program
2. Computations and outputs:
        the computer needs to guess what number the user is thinking using a logarithmic operation to calculate the number of guesses possible
        the program then calculates the middle number between the larger number and the smaller number until it guesses the number the user is thinking
        if the number of guesses is more than the logarithmic operation, the program alerts the user about providing misleading information
        the computer uses a while loop to update the variables: answer, count, question, middleNumber, and roundupNumber
        if the variable answer = 1, the program gives a final answer giving the number of tries
"""

# accept the inputs.
smaller = int(input("Enter the smaller integer number: "))
larger = int(input("Enter the larger integer number: "))

# this helps include the smaller and larger variables into the guessing game
finalSmaller = smaller - 1
finalLarger = larger + 1

# import module math.
import math

# calculate minimum number of guesses.
guesses = math.log2(abs(larger - smaller) + 1)
guessesNumber = math.ceil(guesses)
count = 0

# enters the loop if we have more guesses
while guessesNumber > 0:
    
    # make a guess
    # The computer starts guessing from the middle number. 
    middleNumber = (finalLarger + finalSmaller ) / 2
    roundupNumber = round(middleNumber)
    answer = int(input("Is the number " + str(roundupNumber) + "? If yes, enter '1'. If not, enter '0': "))
    count += 1

    # check the user's input
    # If the user enters the wrong information, the while loop will keep asking for the right answer.
    while answer != 1 and answer != 0:
        answer = int(input("Please enter '1' for yes or '0' for no ONLY: "))

    # user picked 1
    if answer == 1:
        print ("I guessed your number in " + str(count) + " tries!")
        break
   
    # guess value goes down   
    guessesNumber -= 1
          
    # user picked 0
    # is it higher than or lower than guess?
    question = int(input("Is the number bigger than " + str(roundupNumber) + "? if yes, enter 1 if not enter 0: "))
    
    # check user input 
    while question != 1 and question != 0:
        question = int(input("Please enter '1' for yes or '0' for no ONLY: "))

    # user picked 1
    if question == 1:
       finalSmaller = roundupNumber

    # user picked 0
    else:
       finalLarger = roundupNumber

# if guesses are not correct, it means the user entered wrong information
if guessesNumber <= 0:
    print("You enter misleading information")
    
        
        






