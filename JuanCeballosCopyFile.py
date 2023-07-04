"""
Program: JuanCeballosCopyFile.py
Author: Juan P. Ceballos
Copy File
1. Inputs:
        The file names for the first document and second document.
        The first document should contain text.
        The second document should not exist; if it does, it will be overwritten.  
2. Computations
        Use the method 'open' to open the first document and the second document.
        Read data from the first document and store it in the variable text in memory.
        Use the method 'write' to write information to the second document from the variable text in memory. 
        Use the method 'close', so the information in the new document does not get lost. Yes! Very important. You don’t have to do this when you read from a file in Python.
3. Outputs:
        The second document created will be the output.
"""
# Inputs from user
inputFile= input("Please enter the name of the .txt document: ")
outputFile = input("Please enter the name of the .txt document where you want the information from first file to be copied: ")

# Here the input file gets opened and the information gets stored in the variable 'userInFile'
userInFile = open(inputFile, "r")

# Open input file and read data into text
text = userInFile.read()

# Here the second document entered by the user is opened or created
userOutFile = open(outputFile, "w")
    
# Here the second document gets written
userOutFile.write(text)

# Close the file
userOutFile.close()



    
        
        






