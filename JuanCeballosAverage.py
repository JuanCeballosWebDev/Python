"""
Program: JuanCeballosAverage.py
Author: Juan P. Ceballos
Average
1. The input is
        Ask the user what file he wants to access to calculate the numbers’ average in the file.
2. Computations
        Read the file
        Use the data to calculate the average of the numbers
        Simplify the design by using two higher-order functions
3. Outputs:
        Output the average of the numbers as a string.
"""
# Here, the function reduce is imported from functools
from functools import reduce

#Here the input from the user is validated to ensure the file has only numbers
def validateInput(inText):
    digits = True
    for line in inText:
        testline = line.split(" ")
        for number in testline:
            if number.isdigit() == False:
                digits = False
            else:
                digits = True
    return digits

# Here the average gets calculated
def average(text):
    text = reduce(lambda x, y: x + " " + y.strip(), text)
    testline = text.split(" ")
    size = len(testline)
    testline = map(float, testline)
    return reduce(lambda x, y: x + y, testline)/size

# Here is were the program starts, where the input is received, the file gets read, where the user is akd to enter the correct file and where the output is given.
def main ():
    while True:
        fileName = input("Please enter the file's name: ")
        inputFile = open(fileName, "r")
        text = inputFile.readlines()
        if validateInput(text):
            break
        else:
    	    print("Your file should contain only numbers")
    print("The average of all the numbers in the file is: ", average(text))  

if __name__ == "__main__":
    main()



