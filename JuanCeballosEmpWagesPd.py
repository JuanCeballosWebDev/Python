"""
Program: JuanCeballosEmpWagesPd.py
Author: Juan P. Ceballos
Employees' wage for each paid period
1. The input is
        Ask the user what file he wants to access to calculate the salaries for each employee.
2. Computations
        Input file name from user and print to terminal a report of wages.
        Report in a tabular format with a proper header.
        The table should include employees' last name, hours worked and wages paid for period.
3. Outputs:
        The table with employees' last name, hours worked and wages paid for period.
"""
# Input from user
fileName = input("Please enter the file's name: ")
 
# Here the document gets opened and the information gets stored in the variable 'inputFile'
inputFile = open(fileName, "r")

# Here the information is read and stored in the variable 'text'
text = inputFile.readlines()

# Here, the tabular format's header and the columns' subtitles last name, hourly wage, hours worked and wages paid are stored in the variables 'title' and 'columns.'
title = "Employees' wage for each paid period"
columns = "Last name  Hourly wage  Hours worked  Wage paid"

# We get the length of the string in the variable columns
size = len(columns)

# We center it with the string columns’ size and print the title and the columns
title = title.center(size) 
print (title)
print (columns)

# Here the wage is calculated and all the information is printed in a tabular format
for row in text:
    ourList = row.split(" ")
    lastName = ourList[0]
    payPerHour = round(float(ourList[1]))
    workedHours = round(float(ourList[2]))
    wage = payPerHour * workedHours
    print("%-10s%8d%13d%13d" % (lastName, payPerHour ,workedHours, wage))
    


