"""
Btw install the better comments extension if u are on vscode!
TODO: Convert a number to binary representation
# ? STATUS: Done
"""

# We wil use this func if the user type a big number
def get_number():
    number = int(input("Insert a number to see its value in binary: "))

number = int(input("Insert a number to see its value in binary: ")) # Variable for use if anythings doesnt go wrong

if number > 1024:
    print("Too big number")
    get_number() # Request again the number, a cool loop
else:
    print("The binary value is: ", bin(number))
