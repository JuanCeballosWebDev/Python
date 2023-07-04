"""
Program: JuanCeballosNewtonModify.py
Author: Juan P. Ceballos
Compute the square root of a number
1. Inputs:
        A number  
2. Computations
        Package Newton's methods for approximating square roots in a function named 'newton'
        This function will expect the input number as an argument and returns the estimate of its square root
        Use a main function that allows the user to compute square roots of inputs until she presses the enter/return key
3. Outputs:
        The program's estimate of the square root uses Newton's method of successive approximations and Python's estimate using math.sqrt
"""
import math

# Initialize the tolarence and estimate
tolerance = 0.000001
estimate = 1.0

# Perform the succesive approximations
def newton(number):
    number = float(number)
    root = number
    while abs(number - root * root) > tolerance:
        root = (root + number / root) / 2
    return root

# Receive the input number from the user to compute square roots of inputs until she presses the enter/return key
def main():
    while True:
        number= input("Enter a positive number: ")
        if number == "":
            print("Thank you for using the program, have a nice day")
            break
        else:
            print("The progrma's estimate: ", newton(number))
            print("Python's estimate:      ", math.sqrt(float(number)))


if __name__=="__main__":
    main()


