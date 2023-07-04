""""
Program: EmpWeeklyPay.py
Author: Juan P. Ceballos
Last day modified: 11/1/2020

The purpose of this program is to calculate an employee's total weekly pay.
1. Significant constants.
 Overtime Value
2. The inputs are.
 Hourly wage.
 Regular hours.
 Overtime hours
3. Computations.
 Overtime = Overtime hours * Overtime Value * hourly wage
 Weekly pay = Hourly wage * regular hours + overtime
4. The output is.
 Weekly pay
"""

# Constant
OVERTIME_VALUE = 1.5

#Inputs
hourlyWage = float(input("Enter the hourly wage: "))
regularHours = float(input("Enter the number of regular hours: "))
overtimeHours = float(input("Enter the number of overtime hours: "))

#Compute
overtime = overtimeHours * OVERTIME_VALUE * hourlyWage
weeklyPay = hourlyWage * regularHours + overtime

#Output
print("The weekly pay is $" + str(weeklyPay))
