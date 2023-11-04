
#To-do: Add appropriate header information.
#Credit to Eric Pogue

import sys

print("\nNumbering Systems with Python")
numberOfArgs = len(sys.argv)
print("Total arguments passed: " + str(numberOfArgs))
print("Argument 1: " + sys.argv[0])

#To-do: Check for on argumnets or more than to arguments and provide a meaningful error message.

if numberOfArgs == 2:
    print("Argument 2: " + sys.argv[1])
    numberAsAString = sys.argv[1]
    numberAsAnInt = int(numberAsAString, base=10)
    numberAsHex = hex(numberAsAnInt)
    numberAsOct = oct(numberAsAnInt)
    numberAsBin = bin(numberAsAnInt)

    print("Input:  " + numberAsAString)
    print("Number: " + str(numberAsAnInt))
    print("Hex:    " + numberAsHex)
    print("Oct:    " + numberAsOct)
    print("Bin:    " + numberAsBin)


print("")

