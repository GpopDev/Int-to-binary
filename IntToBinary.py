"""
Install better coments extension if u are on vscode
TODO: Convert a number to binary representation
# ? STATUS: Done
"""
follow = True

while follow is True:
    try:
        number = int(input("Insert a number to see its value in binary: "))
        print("The binary is: ", bin(number), "\n")
        act = input("Enter another number?: Y or N: " ) ; act = act.lower()
    
        if act == "y":
            pass
        elif act == "n":
            follow = False
        else:
            print("Invalid letter, use Y for yes or N for no")
    except ValueError:
        print("U need to enter a number")
    
