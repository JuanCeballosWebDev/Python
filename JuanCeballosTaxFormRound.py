""""
Program: TaxFormRound.py
Author: Juan P. Ceballos
Last day modified: 11/1/2020

The purpose of this program is to calculate a person’s income tax and randomize the output to two digits of precision.
1. Significant constants.
 Tax rate.
 Standard deduction.
 Deduction per dependent.
2. The inputs are.
 Gross income.
 The number of dependents.
3. Computations.
 Taxable income = Gross income - 10000 - (3000 * number of dependents).
 Income tax =  Taxable income * 0.20.
4. The outputs are.
 The income tax.
"""

# Constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

#Inputs
grossIncome = float(input("Enter the groos income: "))
numDependents = int(input("Enter the number of dependents: "))

#Compute
TaxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION  * numDependents
incomeTax = TaxableIncome * TAX_RATE

#Output
print("The income tax is $" + str(round(incomeTax, 2)))
