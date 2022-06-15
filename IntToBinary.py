"""
TODO: Convert a number to binary representation
# ? STATUS: Done
"""

def get_number():
    number = int(input("Insert a number to see its value in binary: "))

number = int(input("Insert a number to see its value in binary: "))

if number > 1024:
    print("Too big number")
    get_number()
else:
    print("The binary value is: ", bin(number))
