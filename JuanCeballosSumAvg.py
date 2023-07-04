"""
Program: JuanCeballosSumAvg.py
Author: Juan P. Ceballos
Average calculation.
1. The inputs are
	series of numbers
2. Computations
        average = sum of inputs / by number of inputs entered
3. Outputs:
        sum of inputs
        average of inputs
"""
# variable to help sum inputs
theSum = 0.0

# variable to keep count
count = 0

# data from user
while True:
    data = input("Enter a number or just 'enter' to quit: ")

    # if user presses enter, contol comes out of the loop
    if data == "":
        break

    # data is transformed from a string value to a float value
    numbers = float(data)

    # count increases
    count += 1

    # control sums the inputs from user
    theSum += numbers

# control calculates the average
average = theSum / count

# control outputs the sum of inputs
print ("The sum of the numbers entered is: " + str(theSum))

# control outputs the average
print ("The average is: " + str(average))
    
        
        






